// Illustrates: docs/04_building-apps/developer-tools/01_ride-repl.md, "Run the REPL"
import { blake2b, keccak, sha256 } from '@decentralchain/ts-lib-crypto';
import { repl, NodeConnectionSettings } from '@decentralchain/ride-repl';

// The REPL calls host functions for hashing and for reading chain state: provide them as globals
const hash = (fn: (bytes: Uint8Array) => Uint8Array) => (message: ArrayBuffer) =>
  fn(new Uint8Array(message)).slice().buffer;
globalThis.blake2b256 = hash(blake2b);
globalThis.keccak256 = hash(keccak);
globalThis.sha256 = hash(sha256);
globalThis.httpGet = async ({ url }) => {
  const response = await fetch(url);
  return { status: response.status, body: await response.text() };
};

// Connect to the Testnet node (chain ID '!'), with `this` bound to an account
const session = repl(
  new NodeConnectionSettings('https://testnet-node.decentralchain.io', '!'.charCodeAt(0), '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9'),
);

for (const line of [
  'func double(n: Int) = n * 2',
  'double(21)',
  'sha256(toBytes("hello"))',
  'height',
  'dccBalance(this).regular',
  'getString(this, "greeting")',
]) {
  const { result, error } = await session.evaluate(line);
  console.log(`> ${line}\n${result ?? `error: ${error}`}`);
}
