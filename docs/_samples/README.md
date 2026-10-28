# Docs code samples

Runnable versions of the code shown in the How-To Guides and elsewhere,
kept here so they are validated in CI instead of drifting silently
out of date with the SDK.

```{note}
`package.json` pins the exact versions the docs tell readers to install
(see `docs/04_building-apps/sdk/01_typescript.md`). Several of
them are on the npm `next` tag because the `latest` release fails to
import on Node.js 24. `node-api-grpc` has no published release yet, so
its page is not sampled here.
```

## Validation tiers

1. **Static + runtime (every PR, `docs_checks.yml`):** `npm install`,
   `npm run typecheck`, then a dynamic `import()` of every dependency on
   Node.js 24. `docs/scripts/check_install_snippets.py` additionally runs
   every `npm install` line in the docs exactly as written and checks
   that every imported name exists. `docs/scripts/check_sdk_table.py`
   installs and imports every version in the SDK table. No network
   beyond npm, no funded account.
2. **Drift (weekly, `sdk_drift.yml`):** `check_sdk_table.py --drift`
   fails when an npm publish or dist-tag change makes the SDK table stale.
3. **Ride compile (local, not in CI):** `ride/*.ride` holds every Ride
   script the docs show. `docs/scripts/check_ride_samples.py` compiles
   each one with a node's `POST /utils/script/compileCode` (the public
   Testnet node by default, `--node` for another) and fails on any
   compile error. It needs network access to a node, so the PR checks
   don't run it; run it after changing a Ride sample.
4. **Live run on the Testnet (`samples_testnet.yml`):** on every pull
   request that changes `docs/_samples/**`, weekly, and on demand,
   `runner/run-samples.mjs` runs every sample, the Java ones included,
   against `https://testnet-node.decentralchain.io` and fails if any of
   them fails. It prints how many samples it found, ran, passed, failed
   and skipped, and why each skipped one was skipped.

   The runner signs with the docs CI account: the repo secret
   `DOCS_TESTNET_SEED`, address `31SzjQoKSvAeE22McdFAdbn69aWy4CHxsX7`.
   For each run it derives a fresh account for every
   `'<role> secret seed phrase here'` placeholder, funds it from the CI
   account, and sends what is left back afterwards. Seeds reach a sample
   only through environment variables; they are never written to disk,
   and the runner removes them from the output.

   A full run takes about 5 minutes and uses about 6.2 DCC: the 1 DCC fees for issuing tokens and
   setting an asset script, the 1 DCC pledged to a dApp that locks its
   own account, and transaction fees. When the CI account holds less than
   the largest sample needs, the runner claims 10 DCC from the Testnet
   faucet, which allows one claim per address every 24 hours. If that
   isn't enough, it fails with a "top up" error. The account is
   disposable: if the seed is lost, create a new account, fund it from
   the faucet, and replace the secret.

   Run it locally with your own funded Testnet account:

   ```bash
   cd docs/_samples && npm install
   DOCS_TESTNET_SEED='your Testnet seed' node runner/run-samples.mjs --no-java
   node runner/run-samples.mjs --read-only           # no account needed
   node runner/run-samples.mjs --only transfer.ts    # one or more samples
   ```

5. **Java compile (every PR, `docs_checks.yml`):** `java/` is a Maven
   project holding the Java SDK samples. CI runs `mvn -q compile` with
   JDK 25 against the published `io.decentralchain:java-sdk` release.

## Adding a sample

Each file's top comment names the doc page it illustrates. Write seeds as
`'<role> secret seed phrase here'` and send example transfers to
`31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9`: the Testnet runner then runs a new
sample without any setup, giving each role a fresh account with 1.5 DCC.
If it needs more DCC, a value from another sample or an account shared
with another sample, add it to `runner/manifest.mjs`. Java samples
go in `java/src/main/java/samples/`. Pin the same
exact version the page's `npm install` line uses. Samples that deploy a
script read it from `ride/` and compile it with `compileRide` from
`compile-ride.ts`.

The smart contract pages (`04_building-apps/07_` to `10_`) show their
samples with `{literalinclude}` (skipping the top comment with `:lines:`),
so the published code is exactly the code that is typechecked and
compiled. Prefer that over pasting a copy into a page.
