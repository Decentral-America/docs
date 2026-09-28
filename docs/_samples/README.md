# Docs code samples

Runnable versions of the code shown in the How-To Guides and elsewhere,
kept here so they can be validated in CI instead of drifting silently
out of date with the SDK.

```{note}
All three samples typecheck against packages actually published to npm
today (checked 2026-09-28), not just against the monorepo's source —
see the rename table in `docs/04_building-apps/02_client-libraries-and-sdk.md`
before assuming a package name from the monorepo is installable; several
are mid-rename (`node-api-js` → `node-api`,
`data-service-client-js` → `data-service-client`) and one,
`node-api-grpc`, has no published release under any name yet.
```

## Two validation tiers

1. **Static (this CI job, every PR):** `npm install && npm run typecheck`.
   Confirms every sample still compiles against the SDK's current
   published types — catches renamed exports, changed signatures, and
   the "verified against README X" comments going stale. No network,
   no funded account, safe to run on every PR.
2. **Live (not set up yet):** actually broadcasting to Testnet needs a
   funded Testnet account held as a CI secret, and this environment had
   no route to `nodes.decentralchain.io` or the Testnet faucet while
   writing these samples (see PLAN-docs-expansion.md — the domain
   itself doesn't currently resolve on the public internet, confirmed
   from a network that reaches github.com, npmjs.org and Maven Central
   fine). Wiring up broadcast-level validation is separate follow-up
   work, blocked on that changing.

## Adding a sample

Each file's top comment names the doc page it illustrates. Install
whichever package name is actually live on npm today (check
`npm view @decentralchain/<name> version`), even where the monorepo
source uses a different, in-progress name — see the note above.
