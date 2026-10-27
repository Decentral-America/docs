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
4. **Live broadcast (not set up):** broadcasting to the Testnet needs a
   funded Testnet account held as a CI secret. The samples target
   `https://testnet-node.decentralchain.io` with chain ID `!`.

5. **Java compile (every PR, `docs_checks.yml`):** `java/` is a Maven
   project holding the Java SDK samples. CI runs `mvn -q compile` with
   JDK 25 against the published `io.decentralchain:java-sdk` release.

## Adding a sample

Each file's top comment names the doc page it illustrates. Java samples
go in `java/src/main/java/samples/`. Pin the same
exact version the page's `npm install` line uses. Samples that deploy a
script read it from `ride/` and compile it with `compileRide` from
`compile-ride.ts`.

The smart contract pages (`04_building-apps/07_` to `10_`) show their
samples with `{literalinclude}` (skipping the top comment with `:lines:`),
so the published code is exactly the code that is typechecked and
compiled. Prefer that over pasting a copy into a page.
