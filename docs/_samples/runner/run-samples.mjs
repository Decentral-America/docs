#!/usr/bin/env node
// Runs every docs sample against the public Testnet and fails if any of them fails.
//
//   DOCS_TESTNET_SEED='...' node docs/_samples/runner/run-samples.mjs [--only a.ts,b.ts] [--read-only] [--no-java]
//
// Each run derives fresh accounts from DOCS_TESTNET_SEED (the "CI account") and
// the run ID, one per seed placeholder, funds them from the CI account, runs the
// sample with the placeholders replaced, and sends what is left back to the CI
// account. Seeds reach a sample only through environment variables: they are
// never written to disk, and every seed is removed from the output before it is
// printed. See manifest.mjs for how each sample is set up, and
// docs/_samples/README.md for the CI job.
//
// Needs `npm install` in docs/_samples first, and for the Java samples, JDK 25
// and Maven on the PATH.

import { spawn } from 'node:child_process';
import { cp, mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { broadcast, libs, massTransfer, transfer, waitForTx } from '@decentralchain/transactions';
import { DEFAULT_FUND_DCC, EXAMPLE_RECIPIENT, javaSamples, samples } from './manifest.mjs';

const NODE_URL = 'https://testnet-node.decentralchain.io';
const FAUCET_URL = 'https://testnet.decentralscan.com/api/faucet';
const CHAIN_ID = '!';
const DCC = 100_000_000;
const SAMPLE_TIMEOUT_MS = 10 * 60_000;
const SAMPLES_DIR = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const WORK_DIR = path.join(SAMPLES_DIR, '.run');
const PLACEHOLDER = /'([^'\n]*?) secret seed phrase here'/g;
const JAVA_PLACEHOLDER = /"([^"\n]*?) secret seed phrase here"/g;

const args = process.argv.slice(2);
const only = args.includes('--only') ? args[args.indexOf('--only') + 1].split(',') : null;
const readOnlyRun = args.includes('--read-only');
const withJava = !args.includes('--no-java');

const mainSeed = process.env.DOCS_TESTNET_SEED ?? '';
if (!mainSeed && !readOnlyRun) {
  console.error('::error::DOCS_TESTNET_SEED is not set. Set it, or pass --read-only to run only the read-only samples.');
  process.exit(2);
}
const runId = process.env.GITHUB_RUN_ID ? `${process.env.GITHUB_RUN_ID}.${process.env.GITHUB_RUN_ATTEMPT ?? 1}` : String(Date.now());
const ciAddress = mainSeed ? libs.crypto.address(mainSeed, CHAIN_ID) : '';
const secrets = new Set(mainSeed ? [mainSeed] : []);

// --- helpers ---------------------------------------------------------------

const envName = (kind, name) => `DOCS_${kind}_${name.replace(/[^A-Za-z0-9]/g, '_').toUpperCase()}`;
const dcc = (amount) => (amount / DCC).toFixed(8).replace(/\.?0+$/, '');
const redact = (text) => [...secrets].reduce((out, s) => out.split(s).join('***'), text);
const getJson = async (url, init) => {
  const response = await fetch(url, init);
  const body = await response.json().catch(() => null);
  return { status: response.status, body };
};

const roleSeeds = new Map(); // run-wide role name -> seed
function roleSeed(role) {
  if (!roleSeeds.has(role)) {
    const seed = `${mainSeed} docs-samples run ${runId} ${role}`;
    roleSeeds.set(role, seed);
    secrets.add(seed);
  }
  return roleSeeds.get(role);
}
const roleAddress = (role) => libs.crypto.address(roleSeed(role), CHAIN_ID);

async function balanceOf(address) {
  const { body } = await getJson(`${NODE_URL}/addresses/balance/${address}`);
  return body?.balance ?? 0;
}

async function waitForEmptyPool(address) {
  for (let i = 0; i < 60; i++) {
    const { body } = await getJson(`${NODE_URL}/transactions/unconfirmed`);
    if (!Array.isArray(body) || !body.some((tx) => tx.sender === address)) return;
    await new Promise((resolve) => setTimeout(resolve, 3_000));
  }
}

// Sends what a role account holds back to the CI account. Accounts locked by a
// script that doesn't accept the role's signature keep their balance.
async function sweep(role) {
  const seed = roleSeed(role);
  const address = roleAddress(role);
  await waitForEmptyPool(address);
  const { body: script } = await getJson(`${NODE_URL}/addresses/scriptInfo/${address}`);
  const fee = 100_000 + (script?.script ? 400_000 : 0);
  const balance = await balanceOf(address);
  if (balance <= fee) return 0;
  try {
    const tx = transfer({ recipient: ciAddress, amount: balance - fee, fee, chainId: CHAIN_ID }, seed);
    await broadcast(tx, NODE_URL);
    await waitForTx(tx.id, { apiBase: NODE_URL, timeout: 120_000 });
    return balance - fee;
  } catch {
    return 0;
  }
}

function run(command, commandArgs, options) {
  return new Promise((resolve) => {
    const child = spawn(command, commandArgs, { ...options, stdio: ['ignore', 'pipe', 'pipe'] });
    let output = '';
    const timer = setTimeout(() => child.kill('SIGKILL'), options.timeout ?? SAMPLE_TIMEOUT_MS);
    child.stdout.on('data', (chunk) => { output += chunk; });
    child.stderr.on('data', (chunk) => { output += chunk; });
    child.on('error', (error) => {
      clearTimeout(timer);
      resolve({ code: `not started (${error.code})`, output: `${command}: ${error.message}` });
    });
    child.on('close', (code, signal) => {
      clearTimeout(timer);
      resolve({ code: signal ? `killed (${signal})` : code, output: redact(output) });
    });
  });
}

// Plans a sample: its accounts, funding and source replacements.
function plan(file, config, placeholderPattern, quote) {
  const roles = new Map(); // placeholder role -> run-wide role
  return (source) => {
    let out = source.replace(placeholderPattern, (_, role) => {
      const runRole = config.roles?.[role] ?? `${file}:${role}`;
      roles.set(role, runRole);
      return quote === "'" ? `(process.env.${envName('ROLE', runRole)} as string)` : `System.getenv("${envName('ROLE', runRole)}")`;
    });
    // Without a CI account (--read-only) the example recipient stays as it is.
    const replacements = { ...(ciAddress ? { [EXAMPLE_RECIPIENT.replaceAll("'", quote)]: 'ci' } : {}), ...config.replace };
    for (const [from, to] of Object.entries(replacements)) {
      if (to === 'ci' && !ciAddress) continue;
      let value = to;
      if (to === 'ci') value = `${quote}${ciAddress}${quote}`;
      else if (to.startsWith('address:')) value = quote === "'" ? `(process.env.${envName('ADDRESS', to.slice(8))} as string)` : `System.getenv("${envName('ADDRESS', to.slice(8))}")`;
      else if (to.startsWith('capture:')) value = quote === "'" ? `(process.env.${envName('CAPTURE', to.slice(8))} as string)` : `System.getenv("${envName('CAPTURE', to.slice(8))}")`;
      out = out.split(from).join(value);
    }
    return { source: out, roles };
  };
}

// --- main ------------------------------------------------------------------

const files = (await readdir(SAMPLES_DIR)).filter((f) => f.endsWith('.ts')).sort();
const javaDir = path.join(SAMPLES_DIR, 'java', 'src', 'main', 'java', 'samples');
const javaFiles = (await readdir(javaDir).catch(() => [])).filter((f) => f.endsWith('.java')).sort();
const listed = Object.keys(samples);
const order = [...listed.filter((f) => files.includes(f)), ...files.filter((f) => !listed.includes(f))];
// Every sample is prepared and compiled (they import each other's helpers); --only picks what runs.
const allEntries = [
  ...order.map((file) => ({ file, lang: 'ts', config: samples[file] ?? {} })),
  ...(withJava ? javaFiles : []).map((file) => ({ file, lang: 'java', config: javaSamples[file] ?? {} })),
];
const entries = allEntries.filter(({ file }) => !only || only.includes(file));

// Prepare the work dir: substituted copies, compiled with the samples' tsconfig.
await rm(WORK_DIR, { recursive: true, force: true });
await mkdir(path.join(WORK_DIR, 'out'), { recursive: true });
await cp(path.join(SAMPLES_DIR, 'ride'), path.join(WORK_DIR, 'out', 'ride'), { recursive: true });
const planned = new Map();
for (const entry of allEntries) {
  const { file, lang, config } = entry;
  if (lang !== 'ts' || config.skip) continue;
  const source = await readFile(path.join(SAMPLES_DIR, file), 'utf8');
  const result = plan(file, config, PLACEHOLDER, "'")(source);
  planned.set(file, result.roles);
  await writeFile(path.join(WORK_DIR, file), result.source);
}
await writeFile(
  path.join(WORK_DIR, 'tsconfig.json'),
  JSON.stringify({ extends: '../tsconfig.json', compilerOptions: { noEmit: false, outDir: 'out', rootDir: '.' }, include: ['*.ts'] }),
);
if (allEntries.some((e) => e.lang === 'ts')) {
  const tsc = await run(path.join(SAMPLES_DIR, 'node_modules', '.bin', 'tsc'), ['-p', WORK_DIR], { cwd: WORK_DIR });
  if (tsc.code !== 0) {
    console.error(`::error::The samples don't compile after their placeholders are replaced:\n${tsc.output}`);
    process.exit(1);
  }
}
if (allEntries.some((e) => e.lang === 'java' && !e.config.skip)) {
  await cp(path.join(SAMPLES_DIR, 'java'), path.join(WORK_DIR, 'java'), { recursive: true, filter: (src) => !src.includes(`${path.sep}target`) });
  for (const entry of allEntries.filter((e) => e.lang === 'java' && !e.config.skip)) {
    const target = path.join(WORK_DIR, 'java', 'src', 'main', 'java', 'samples', entry.file);
    const result = plan(entry.file, entry.config, JAVA_PLACEHOLDER, '"')(await readFile(target, 'utf8'));
    planned.set(entry.file, result.roles);
    await writeFile(target, result.source);
  }
  const mvn = await run('mvn', ['-q', '-f', path.join(WORK_DIR, 'java', 'pom.xml'), 'compile'], { cwd: WORK_DIR, timeout: 15 * 60_000 });
  if (mvn.code !== 0) {
    console.error(`::error::The Java samples don't compile after their placeholders are replaced:\n${mvn.output}`);
    process.exit(1);
  }
}

// Funding each sample needs, and the CI account's balance check.
const fundingOf = (entry) => {
  const roles = planned.get(entry.file) ?? new Map();
  return [...roles.keys()].map((role) => ({ role: roles.get(role), amount: Math.round((entry.config.fund?.[role] ?? DEFAULT_FUND_DCC) * DCC) }));
};
const runnable = entries.filter((e) => !e.config.skip && !e.config.helper && !(readOnlyRun && !e.config.readOnly));
if (!readOnlyRun) {
  const need = Math.max(0, ...runnable.map((e) => fundingOf(e).reduce((sum, f) => sum + f.amount, 0))) + DCC / 2;
  let balance = await balanceOf(ciAddress);
  console.log(`CI account ${ciAddress}: ${dcc(balance)} DCC; the largest sample needs ${dcc(need)} DCC at once.`);
  if (balance < need) {
    const claim = await getJson(FAUCET_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ address: ciAddress }) });
    console.log(`Balance too low; faucet claim: HTTP ${claim.status} ${JSON.stringify(claim.body)}`);
    if (claim.body?.txId) {
      await waitForTx(claim.body.txId, { apiBase: NODE_URL, timeout: 180_000 }).catch(() => {});
      balance = await balanceOf(ciAddress);
    }
  }
  if (balance < need) {
    console.error(`::error::The CI account ${ciAddress} holds ${dcc(balance)} DCC and needs at least ${dcc(need)}. Top it up from the faucet (https://testnet.decentralscan.com/faucet, 10 DCC per 24 hours) and run the job again.`);
    process.exit(1);
  }
}

// Run the samples in order.
const results = [];
const captures = {};
const started = Date.now();
for (const entry of entries) {
  const { file, lang, config } = entry;
  if (config.helper) { results.push({ file, status: 'helper', note: config.helper }); continue; }
  if (config.skip) { results.push({ file, status: 'skipped', note: config.skip }); continue; }
  if (readOnlyRun && !config.readOnly) { results.push({ file, status: 'skipped', note: '--read-only run' }); continue; }

  console.log(`\n::group::${file}`);
  const t0 = Date.now();
  const env = { ...process.env, DOCS_TESTNET_SEED: '' };
  try {
    const funding = fundingOf(entry);
    for (const { role } of funding) env[envName('ROLE', role)] = roleSeed(role);
    for (const [name, value] of Object.entries(captures)) env[envName('CAPTURE', name)] = value;
    for (const role of roleSeeds.keys()) env[envName('ADDRESS', role)] = roleAddress(role);

    // Scripts that name example accounts by public key get this run's keys.
    for (const [rideFile, replacements] of Object.entries(config.ride ?? {})) {
      let script = await readFile(path.join(SAMPLES_DIR, 'ride', rideFile), 'utf8');
      for (const [from, to] of Object.entries(replacements)) {
        const key = to === 'publicKey:ci' ? libs.crypto.publicKey(mainSeed) : libs.crypto.publicKey(roleSeed(to.replace(/^publicKey:/, '')));
        script = script.split(from).join(`base58'${key}'`);
      }
      await writeFile(path.join(WORK_DIR, 'out', 'ride', rideFile), script);
    }

    const transfers = funding.filter((f) => f.amount > 0).map((f) => ({ recipient: roleAddress(f.role), amount: f.amount }));
    if (transfers.length) {
      const tx = massTransfer({ transfers, chainId: CHAIN_ID }, mainSeed);
      await broadcast(tx, NODE_URL);
      await waitForTx(tx.id, { apiBase: NODE_URL, timeout: 180_000 });
      console.log(`Funded ${transfers.length} account(s) with ${dcc(transfers.reduce((s, t) => s + t.amount, 0))} DCC in ${tx.id}`);
    }

    const outFile = file.replace(/\.ts$/, '.js');
    const result = lang === 'ts'
      ? await run(process.execPath, [path.join(WORK_DIR, 'out', outFile)], { cwd: path.join(WORK_DIR, 'out'), env })
      : await run('mvn', ['-q', '-f', path.join(WORK_DIR, 'java', 'pom.xml'), 'org.codehaus.mojo:exec-maven-plugin:3.5.0:java', `-Dexec.mainClass=samples.${file.replace(/\.java$/, '')}`], { cwd: WORK_DIR, env });
    console.log(result.output.trimEnd());

    let failure = null;
    if (result.code !== 0) failure = `exit status ${result.code}`;
    else if (config.expect && !config.expect.test(result.output)) failure = `output doesn't match ${config.expect}`;
    for (const [name, pattern] of Object.entries(config.capture ?? {})) {
      const match = result.output.match(pattern);
      if (match) captures[name] = match[1];
      else failure ??= `nothing in the output matches ${pattern}`;
    }

    let swept = 0;
    for (const { role } of funding) swept += await sweep(role);
    if (swept) console.log(`Returned ${dcc(swept)} DCC to the CI account`);
    results.push({ file, status: failure ? 'failed' : 'passed', note: failure ?? '', seconds: Math.round((Date.now() - t0) / 1000) });
  } catch (error) {
    results.push({ file, status: 'failed', note: redact(String(error?.message ?? error)), seconds: Math.round((Date.now() - t0) / 1000) });
    console.log(redact(String(error?.stack ?? error)));
  }
  console.log('::endgroup::');
  const last = results.at(-1);
  console.log(`${last.status === 'passed' ? 'ok  ' : 'FAIL'} ${file} (${last.seconds}s)${last.note ? `: ${last.note}` : ''}`);
}

// Summary
const count = (status) => results.filter((r) => r.status === status).length;
console.log(`\nSamples: ${results.length - count('helper')} found, ${count('passed') + count('failed')} run, ${count('passed')} passed, ${count('failed')} failed, ${count('skipped')} skipped (${Math.round((Date.now() - started) / 1000)}s)`);
for (const r of results.filter((r) => r.status === 'failed')) console.log(`::error::${r.file} failed: ${r.note}`);
for (const r of results.filter((r) => r.status === 'skipped')) console.log(`skipped ${r.file}: ${r.note}`);
if (!readOnlyRun) console.log(`CI account ${ciAddress} now holds ${dcc(await balanceOf(ciAddress))} DCC`);
await rm(WORK_DIR, { recursive: true, force: true });
process.exit(count('failed') ? 1 : 0);
