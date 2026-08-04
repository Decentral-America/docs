# Test-Debt Inventory — Ignored Test Triage

**Date:** 2026-08-02 · **Addendum 2026-08-04 below** (SC-695 status changed since this was written)
**Scope:** Task 3 of `docs/superpowers/plans/2026-08-02-launch-readiness.md` (Phase 2).

> **2026-08-04 addendum:** the SC-695 cluster below (`InvokeScriptTransactionRideV5Suite.scala`, 5
> ignores) says the design spec was written but "the `BlockchainFeature` flag is NOT scaffolded —
> implementation is separate future work." That has since changed: after the spec
> (`node-scala/docs/features/feature-30-sc695-spec.md`) was signed off, SC-695 **was** implemented and
> merged to node-scala `main` behind a new `BlockchainFeature` id 30, dormant until governance activation
> (verified: `node-it/src/test/scala/com/decentralchain/it/sync/smartcontract/InvokeScriptTransactionRideV5Suite.scala`
> now pre-activates `BlockchainFeatures.InvokeVersionGating.id` and the previously-ignored tests are
> resolved, not left as bare ignores). This does not change the inventory's node-scala ignore count
> retroactively (that count is a dated snapshot), but the "NOT scaffolded" framing below is superseded —
> do not treat SC-695 as unimplemented going forward. No other section of this inventory is affected;
> matcher's 6 ignores and the rest of node-scala's 20 are unchanged and still accurate as of this check.
**Method:** `grep -rn '" ignore\b\|ignore {\|ignore(' --include='*.scala' node-scala/node-it node-scala/node/tests matcher/dex-it matcher/dex/src/test` from the Ecosystem root, then each hit was read in full (test body + a quick look at the production code it targets) to classify it. No Docker/sbt test execution was possible in this environment (sandboxed, no network — `sbt` could not resolve dependencies), so classifications are evidence-based static-reading judgments, not RED→GREEN proof; several are flagged below as needing that proof before Task 4/5/6 act on them.

## Classification legend

- **(A) stale-test-bug** — production is already correct; the test itself is wrong or stale (the SC-575/580 pattern). Fix the test.
- **(B) real-unimplemented-feature** — needs a design pass before it can be un-ignored (the SC-695 class). Ticket + spec, keep ignored.
- **(C) environment/harness-only** — needs a harness/env fix or is a non-assertive benchmark, not a prod code fix.
- **(D) architecturally-blocked** — blocked on an old route/path being deprecated first (the DEX-982-old class).

## Count verification

Grep raw hit count: 33 lines matched. Of these, **7 are false positives** — `Diff.derived[...].ignore(_.field)` calls in `matcher/dex/src/test/scala/com/decentralchain/dex/MatcherSpecBase.scala` (6 hits) and `OrderEventsCoordinatorActorSpec.scala:168` (1 hit) are the Scalapb/diffx `Derived[Diff[X]].ignore(...)` field-exclusion combinator, unrelated to ScalaTest's `ignore`.

That leaves **26 real ScalaTest ignores**, which matches the plan's audited head-start exactly:
- **node-scala: 20 across 11 files** (confirmed).
- **matcher: 6** (confirmed).

## node-scala (20 ignores, 11 files)

### InvokeScriptTransactionRideV5Suite.scala — 5 ignores (SC-695 cluster)

| Line | Test | Reason (from comment) | Class |
|---|---|---|---|
| 99 | `Can't invoke Ride V5 DApp via InvokeScriptTx V1` | `// NOTE: Disabled pending SC-695 (upstream ticket)` | B |
| 116 | `Can't invoke Ride V5 DApp via InvokeScriptTx V2` | same | B |
| 133 | `Can invoke Ride V5 DApp via InvokeScriptTx V3` | same | B |
| 139 | `Can't invoke Ride V3 DApp via InvokeScriptTx V3 if extraFeePerStep is specified` | same, plus inline `// NOTE: extraFeePerStep calculation to be added in future` | B |
| 157 | `Can't invoke Ride V4 DApp via InvokeScriptTx V3 if extraFeePerStep is specified` | same | B |

**Justification:** all 5 explicitly cite the unimplemented InvokeScriptTransaction-version × RIDE-version compatibility matrix and the not-yet-built `extraFeePerStep` fee mechanism. This is exactly the class-B design gap Task 5 targets.

**Resolution (Task 5, 2026-08-02) — spec written, NOT scaffolded:** the design spec this cluster needed is now written at `node-scala/docs/features/feature-30-sc695-spec.md` (commit `05073dac29` on branch `docs/sc695-spec`). It covers: the full version-compatibility matrix (V1/V2 tx reject against STDLIB V5+ dApps, V3 tx allowed against all; V1/V2 vs V3/V4 dApps unchanged — not textually supported by the tests, so not asserted); a fee-mechanism recommendation for `extraFeePerStep` (composition-stage fee keyed on dApp-to-dApp call-step count, charged as a static pre-execution upper bound — recommended over a new wire field or a flat sentinel); and the gating requirement (a NEW `BlockchainFeature`, id 30 — one past feature-29's reserved id 29 — dormant until governance activation, with paired pre/post-activation tests per combination). It also flags a genuine discrepancy found by direct reading: tests 4 and 5 are titled "if extraFeePerStep is specified" but their bodies never actually specify any such value, and this could not be resolved from the ignored test text or repo git history alone (`git log --all --grep=SC-695` only surfaces an unrelated 2021 upstream Waves ticket-number collision). **Per the plan's explicit instruction, the `BlockchainFeature` flag is NOT scaffolded — implementation is separate future work, gated on human sign-off of the matrix and fee mechanism.**

### InvokeListForCallable.scala — 3 ignores

| Line | Test | Reason | Class |
|---|---|---|---|
| 133 | `error if list size more than 1000` | no in-file comment; expects a 400 "List size should not exceed 1000" when an invoke-arg `List` built via `ARR(..., limited = false)` (i.e. deliberately bypassing the compiler's own `MaxListLengthV4` check) is submitted with 1001 elements | B (moderate confidence) |
| 149 | `try to get non-existing element by index` | same construction, expects out-of-bounds error at index 1000 | B (moderate confidence) |
| 166 | `try to get element by negative index` | same construction, expects out-of-bounds error at index -1 | B (moderate confidence) |

**Justification:** `MaxListLengthV4` (`lang/.../PureContext.scala:41`) and the "List size should not exceed …" message (`lang/.../compiler/Terms.scala:400`) are only enforced when a script constructs a list itself with the `limited=true` path (`ARR(..., limited=true)`/FOLD limits). These three tests instead build the argument value directly with `limited = false` — i.e. they simulate an *external* invoke-transaction argument that never goes through that compiler-time gate — and no equivalent runtime/API-level enforcement was found in `node/src/main/scala` (searched for `MaxListLengthV4`/size-check usages outside `lang`). That reads as a genuine, not-yet-implemented validation gap on externally-supplied list arguments rather than a stale assertion, but this is not proven by execution — **flagged low-to-moderate confidence, recommend a real Docker run before Task 4/5 acts on it** (it could turn out the getElement bounds-check message is already correct and only the size-limit sub-case is the real gap, which would split this cluster A/B rather than all-B).

### InvokeScriptTransactionSuite.scala — 1 ignore — **RESOLVED 2026-08-02**

| Line | Test | Reason | Class |
|---|---|---|---|
| 103 | `Allow to use "this" if DApp is called by alias` | no comment | **A — RESOLVED** |

**Justification:** the ignored test body is a byte-for-byte duplicate of the active, passing test `"translate alias to the address"` at line 177 (same `invokeScript(caller, "alias:I:alias", func=Some("baz"), ...)` call, same `getDataByKey` assertion). The active duplicate already proves the alias→`this` behavior works in production. This is a stale, redundant leftover — safe to delete (not just un-ignore) once confirmed.

**Resolution (Task 4, 2026-08-02):** confirmed byte-for-byte identical to the active test by direct read (both invoke `"alias:I:alias"` → `baz()` and assert the same `getDataByKey` result). Deleted the ignored duplicate rather than un-ignoring it, since un-ignoring would only run the exact same assertion the active test already runs — no new coverage. `node-it/Test/compile` confirmed the file still compiles clean after removal. Commit: node-scala `d963e5f22d` on branch `test/fix-class-a-ignores` (not yet merged).

### LeasingExpirySpec.scala — 3 ignores (dormant feature-27 cluster)

| Line | Test | Reason | Class |
|---|---|---|---|
| 192 | `should be applied only for expired leases` | tests run under `preActivatedFeatures` for `BlockchainFeatures.LeaseExpiration` | B |
| 235 | `has correct balance when lease transaction is accepted in a block where previous leases are cancelled` | same | B |
| 273 | `can generate block where lease is cancelled` | same | B |

**Justification:** confirmed — the whole suite pre-activates `BlockchainFeatures.LeaseExpiration.id` (feature 27), which is dormant/not governance-activated on any live network. These tests exercise a feature that doesn't run in production today; they're class-B by construction, matching the plan's characterization exactly.

### BlockSpecification.scala — 2 ignores

| Line | Test | Reason | Class |
|---|---|---|---|
| 185 | `sign time for 60k txs` | no comment; builds+signs a 60,000-tx block and times each stage via `Instrumented.withTimeMillis`, no assertion on the timings | C |
| 198 | `serialize and deserialize big block` | builds a `100 * 1000`-tx block via `bigBlockGen`, round-trips serialize/parse, `shouldBe true` on signature validity | C |

**Justification:** line 185 is a pure manual timing print with zero pass/fail assertions — a benchmark, not a correctness test; it belongs in a benchmark harness, not the suite proper, and should stay excluded from normal CI (too slow/non-deterministic for a unit run). Line 198 does have a real assertion but constructs a 100k-tx block, which is a heavy/slow generator — likely ignored for suite runtime, not correctness; **flag**: could arguably be A (worth periodically re-enabling to catch big-block serialization regressions) but as-is it's harness/perf-motivated, so classed C.

### Singleton ignores in unit specs — 6 ignores (7 counted in plan's "7 singletons" description covers 6 files + AssetSupportedTransactionsSuite listed separately; verified 6 remaining files here)

| File:Line | Test | Reason | Class |
|---|---|---|---|
| `smartasset/AssetSupportedTransactionsSuite.scala:262` | `burn by some height` | no comment; asserts a height-parity-gated asset script (`height % 2 == 0`) permits/rejects `burn` deterministically across a height-arise wait — timing-sensitive against `nodes.waitForHeightArise()` in a live multi-node it-suite | C |
| `transaction/smart/script/ScriptCompilerV1Test.scala:364` | `forbid unused case variables` | no comment; expects a compiler error for `match` case-bound variables that shadow an unused `let`/`func` param of the same name — this diagnostic does not appear implemented in `ScriptCompiler`/`ExpressionCompiler` (no "unused case variable" message found in `lang/`) | B |
| `state/diffs/freecall/InvokeExpressionTest.scala:268` | `available versions` | in-line comment: `// NOTE: Version check is commented out in CommonValidation` | B |
| `state/diffs/ci/CallableV4DiffTest.scala:93` | `trace` | no comment; asserts an exact `r.trace.size shouldBe 4` shape for a scripted multi-asset invoke failure trace — ignored since at least Feb 2026 per git history, predates several trace-model changes | **A — RESOLVED, confirmed by real execution 2026-08-02 (see below); confidence flag from the original audit is corrected, not carried forward** |
| `state/diffs/smart/performance/SigVerifyPerformanceTest.scala:34` | `parallel native signature verification vs sequential scripted signature verification` | no comment; runs 10,000 transfers signed vs 10,000 scripted-signed transfers and only `println`s the timing comparison — zero assertions | C |
| `state/diffs/smart/predef/ContextFunctionsTest.scala:189` | `base64 amplification` | no comment; ~180-line chained `toBase64String`/`toBytes` script exercising base64 expansion-amplification (decompression-bomb-style) cost, no timeout/assertion visible in the excerpt read | C |

**Justification for `ScriptCompilerV1Test:364`:** the expected compiler diagnostic ("forbid unused case variables") was not found anywhere in the RIDE compiler/lang module — this reads as an aspirational lint that was never implemented, i.e. real-unimplemented-feature.

**Justification for `InvokeExpressionTest:268`:** the comment directly states production's own version-check code path is commented out in `CommonValidation` — the test can't pass while that stays disabled. This is a real feature gap (or a deliberate, currently-undocumented relaxation) — either way it needs a design/product decision, so classed B, not C.

**`CallableV4DiffTest:93` flagged not-confident (ORIGINAL, superseded — see Resolution below):** this environment could not run `sbt` (no network, dependency resolution failed offline) to actually see whether it currently passes or fails, so I could not distinguish "stale trace-shape assertion after a refactor" (A) from "legitimately slow/flaky trace test excluded for harness reasons" (C). Recommend Task 4 run it against real Docker/local sbt first before deciding.

**Resolution (Task 4, 2026-08-02) — classification corrected to A, confirmed by real execution:** un-ignored and ran `sbt --batch "node-tests/testOnly com.decentralchain.state.diffs.ci.CallableV4DiffTest"` (pure in-JVM unit test — `node-tests` module, no Docker/network needed, contrary to the original audit's assumption that no execution was possible; only top-level `sbt` dependency resolution needed network, and it resolved fine on this machine).

First run (before any fix) — 7/8 passed, 1 failed:
```
[info] - trace *** FAILED *** (75 milliseconds)
[info]   FailedTransactionError(AssetScriptInAction, 4, List(), None, Some(3KNoggfBFFcmSEtnd6kEitFtQY2gxH41ingB9Cdxh8gR), List()) was not equal to ScriptExecutionError("Transaction is not allowed by script of the asset 3KNoggfBFFcmSEtnd6kEitFtQY2gxH41ingB9Cdxh8gR", List(), Some(3KNoggfBFFcmSEtnd6kEitFtQY2gxH41ingB9Cdxh8gR)) (CallableV4DiffTest.scala:105)
```
Notably, `r.trace.size shouldBe 4` (line 100, the assertion the original audit worried about) **passed** — the trace shape is not stale. The real stale assertion was line 105, comparing the per-step `AssetVerifierTrace`'s raw `FailedTransactionError` directly against the top-level `TransactionValidationError`'s `cause`.

Root-caused by reading `TransactionDiffer.validate`'s final `leftMap` (`node/src/main/scala/com/decentralchain/state/diffs/TransactionDiffer.scala`): under RideV6 (SynchronousCalls), a fail-free (`isFailFree`, i.e. `spentComplexity <= FailFreeInvokeComplexity`) `FailedTransactionError` with `Cause.AssetScriptInAction` is intentionally converted to `ScriptExecutionError(fte.message, fte.log, fte.assetId)` for the top-level transaction result only. The per-step trace entries are built earlier (`InvokeDiffsCommon.scala`) and never go through that conversion, so they correctly retain the raw `FailedTransactionError`. `FailedTransactionError.message` synthesizes the exact same string (`"Transaction is not allowed by script of the asset $assetId"`) that ends up in the `ScriptExecutionError`, confirming both values describe the same failure — they are just two different case classes by current, intentional design (this is real, existing production code, not something added to make the test pass), so the test's direct `shouldBe` object-equality was always going to fail once this fail-free conversion was introduced.

Fix applied (test-only, no production code touched — consensus-adjacent directory, only the test's assertion changed): compare the semantically relevant fields (`message`, `assetId`) between the last trace step's `FailedTransactionError` and the final result's `ScriptExecutionError`, instead of asserting full object equality across two different case classes. Re-ran after the fix: **8/8 tests pass**, `trace` green.

Commit: node-scala `d963e5f22d` on branch `test/fix-class-a-ignores` (not yet merged). No production code under `node/src/main/scala/com/decentralchain/{state,consensus,mining}` was changed — this was purely a test-assertion correction, consistent with the SC-575/580 method and the plan's CONSENSUS-CRITICAL constraint (no production change was needed or made).

## matcher (6 ignores, 4 files)

### GetOrderStatusByPKAndIdWithSigSpec.scala — 2 ignores (DEX-982-old cluster)

| Line | Test | Reason | Class |
|---|---|---|---|
| 187 | `should return an error timestamp header doesn't exist` | in-file block comment cites DEX-982: this endpoint shares the `GET /orderbook/{}/{}` path shape with the public `getOrderBook`; making the missing-header case return `RequestInvalidSignature` breaks the fallthrough that lets legitimate public order-book requests succeed (verified by the comment's own citation of `MatcherApiRouteSpec "returns an order book"` going 400 if "fixed") | D |
| 201 | `should return an error signature header doesn't exist` | same DEX-982 path-ambiguity comment | D |

**Justification:** matches the plan's DEX-982-old description exactly — architecturally blocked on the old signed route sharing a path with the public order-book route; the new `/matcher/orders/status/{publicKey}/{orderId}` route (merged this session per the plan) is the eventual fix, pending deprecation of the old route (Task 6 Step 4).

**Task 6 Step 4 — DEX-982-old deprecation plan (2026-08-02, planning/documentation only, no code deleted):**

Confirmed the new route is real and live, not just planned: `getOrderStatusByPKAndId` (`MarketsRoute.scala:282-291`), wired at `path("status" / PublicKeyPM / OrderPM)` under the `orders` prefix, `@Path("/orders/status/{publicKey}/{orderId}#getOrderStatusByPKAndId")` — merged via matcher PR #19 ("`feat: add unambiguous signed order-status route (DEX-982)`", commit `4288a751f`, now on `main` at `3ed0ec65b`). It has no public sibling route to fall through to, so its `missingSignedHeaderRejectionHandler` can safely return a real `RequestInvalidSignature` — confirmed by its own passing tests at `GetOrderStatusByPKAndIdWithSigSpec.scala:254-276` ("should return an error timestamp/signature header doesn't exist" — both `in`, not `ignore`).

The OLD route (`getOrderStatusByPKAndIdWithSig`, `MarketsRoute.scala:295-330`, `@Path("/orderbook/{publicKey}/{orderId}#getOrderStatusByPKAndIdWithSig")`) is the one whose 2 ignores this plan concerns. It stays exactly as-is today (still ignored, still commented, still serving live traffic) — this is a plan for *later*, not an action taken now.

*Precedent already in this codebase* for exactly this kind of deprecation: `HistoryRoute.scala:63-71`, `deleteOrderFromHistoryById`, marked `@Deprecated` with an OpenAPI `description = "This method is deprecated and doesn't work anymore. Please don't use it."` — the pattern to reuse when the old order-status route's turn comes.

**Proposed deprecation window and steps (not yet executed):**

1. **Trigger — do NOT start the clock yet.** matcher has never cut a tagged release (confirmed: `git tag` / `gh release list` show none; the honest-limitation note in `ci.yml`'s `integration-dex-it` job env block says the same). A deprecation clock measured in "N releases" needs a first release to count from — that's Task 6 Step 3, explicitly **not done in this pass** (human decision gate). Until a first tagged release exists, there is no meaningful "N releases ago clients were told" baseline; starting the clock earlier would deprecate a route no external client could have known was legacy.
2. **At or after the first tagged release:** annotate the old route `getOrderStatusByPKAndIdWithSig` with `@Deprecated` + an OpenAPI `description` pointing callers at `GET /matcher/orders/status/{publicKey}/{orderId}` (the `HistoryRoute.scala` precedent above). No behavior change — same 400/ambiguity limitation as today, just now documented as deprecated in the OpenAPI spec/docs site.
3. **Measure real usage before removing anything:** add a metric/counter (or a WARN-level log line) on every hit to the old route's handler, so real external traffic is visible rather than assumed. Do not remove a route with unknown live callers on faith alone.
4. **Window:** recommend the longer of 2 minor releases or 90 days after step 2 ships — matcher has no prior deprecation-cycle history to anchor to besides the already-dead `deleteOrderFromHistoryById` (which was deprecated *and non-functional* simultaneously, not a real windowed migration), so this is a reasonable default, not a measured precedent; a human should confirm the number when Step 3 (the release) actually happens.
5. **Removal gate:** only once (a) the window has elapsed AND (b) the usage counter from step 3 shows the old route has gone quiet (or residual traffic is judged acceptable to break) — delete `getOrderStatusByPKAndIdWithSig`, its route wiring in `MarketsRoute.scala`, and its OpenAPI annotations. **At that point**, and not before, the 2 architecturally-blocked ignores in `GetOrderStatusByPKAndIdWithSigSpec.scala` (lines 187, 201) can finally be deleted too — there's no ambiguous public route left for the missing-header case to conflict with, so the whole DEX-982-old constraint disappears by construction.

**Until then:** per the plan's explicit instruction, the 2 ignores are left untouched, with their existing (still accurate) DEX-982 comment as-is. No code was deleted or modified for Step 4 — this is planning/documentation only.

### OrderBookBackwardCompatTestSuite.scala — 3 ignores ("Hard to reproduce" cluster) — **RESOLVED (deleted) 2026-08-02**

| Line (was) | Test | Reason | Class |
|---|---|---|---|
| 18 | `if (!submitted.order.isValid(eventTs))` | `ignore {} // Hard to reproduce` — empty body, tests nothing | C → **deleted** |
| 62 | `if (!counter.order.isValid(eventTs))` | `ignore {} // Hard to reproduce` — empty body | C → **deleted** |
| 67 | `limit` (under `submittedRemaining.isValid`) | `ignore {} // Hard to reproduce, DEX-467` — empty body, only this one has a ticket reference | C → **deleted, DEX-467 preserved as record (below)** |

**Justification (original):** all three were empty-body `ignore {}` placeholders — they asserted nothing even if un-ignored as-is. Per the plan's Task 6 Step 1 guidance, an empty ignored block is worse than no test.

**Resolution (Task 6 Step 1, 2026-08-02):** a genuine local Docker reproduction attempt was made against the real dockerized dex-it stack (not skipped, not assumed) — see "Task 6 resolution log" below for the full build/run trail. It did not reach the point of testing these three specific race conditions at all: the shared `matcher-node` container that every dex-it suite (including this one) depends on failed to boot, 4/4 attempts, with an identical, deterministic crash:

```
Caused by: org.rocksdb.RocksDBException: lock hold by current process, acquire time ... acquiring thread ...: /var/lib/dcc/blockchain-updates/LOCK: No locks available
	at com.decentralchain.events.BlockchainUpdates.<init>(BlockchainUpdates.scala:33)
```

This is a local-machine Docker Desktop environment issue (RocksDB failing to acquire its own second advisory lock — for the `BlockchainUpdates` extension's own RocksDB instance — under this host's amd64 emulation of the node image; the *first* RocksDB instance, the main state DB, opens fine in the same process), not a matcher/dex code defect: it reproduced identically before and after a full Docker Desktop daemon restart, and blocks literally every dex-it suite at container-boot time, not just this file. `docker images`/`sbt dex-it/docker` build succeeded cleanly (all 4 images: `matcher-node`, `dex-integration-it`, `matcher-server`, `dex-it`); only the container *runtime* boot fails. What would unblock it: running on a native (non-emulated) amd64 host or Linux CI runner — exactly what this repo's own nightly `integration-dex-it` GitHub Actions job already does successfully on `ubuntu-latest`.

Given real reproduction of the underlying race conditions was blocked before it could even start, and the three ignores were empty `ignore {}` bodies that asserted nothing regardless, the plan's fallback rule applies as-is: **deleted all three** rather than leaving them as non-asserting placeholders. No ticket existed for the first two (confirmed: `gh issue list --repo Decentral-America/matcher --search "DEX-467"` / `"backward"` / `"DEX-1402"` — matcher's GitHub issue tracker has no real issues besides the auto-generated Renovate Dependency Dashboard; these ticket names are internal references, not GitHub issues). **DEX-467** is preserved here as the historical reference for the third ("limit" under `submittedRemaining.isValid`: submitted order stays valid after a partial match whose counter's own remaining becomes invalid) should someone revisit it with working Docker infra later. Commit: matcher `d91766a5f` on branch `test/matcher-ignore-triage` (off `main` at `3ed0ec65b`, not yet merged/pushed). `dex-it/Test/compile` confirmed clean after the deletion.

### WsOrderBookStreamTestSuite.scala — 1 ignore — **evidence updated, unchanged 2026-08-02**

| Line | Test | Reason | Class |
|---|---|---|---|
| 394 | `close a subscription when an order book is blacklisted` | `ignore { // NOTE: DEX-1402 — WebSocket order book streaming issue unresolved` | C |

**Justification (original):** matches the plan's description exactly — a documented, ticketed, unresolved WS layer bug (not consensus), needing a harness/dex-WS-layer fix per Task 6 Step 2.

**Resolution (Task 6 Step 2, 2026-08-02):** same genuine reproduction attempt as the backward-compat cluster above — blocked by the identical, environment-level `matcher-node` container boot failure (RocksDB ENOLCK on `BlockchainUpdates`, 4/4 attempts, survives a full Docker Desktop restart) before this suite's own container could come up at all. This is a harness/infra blocker on this specific local machine, not new evidence about the WS bug itself — the existing DEX-1402 comment and class-C reproduction state are left exactly as they were (no code change), since "not reproducible on this machine right now" is not the same claim as "not reproducible" and must not be used to silently reclassify or weaken a real, already-ticketed bug. Left ignored, unchanged, pending a run on infra where dex-it containers actually boot (same unblocking criterion as above: native-amd64 host / this repo's own nightly CI runner).

## Summary counts

| Class | node-scala | matcher | Total |
|---|---|---|---|
| A (stale-test-bug) | 1 (+1 flagged uncertain) | 0 | 1-2 |
| B (unimplemented feature) | 12 (+1 flagged uncertain) | 0 | 12-13 |
| C (environment/harness) | 6 | 4 | 10 |
| D (architecturally-blocked) | 0 | 2 | 2 |
| **Total** | **20** | **6** | **26** |

*Counts above are the original 2026-08-02 static-reading audit, kept as-is for history. Post-Task-4 resolution: `CallableV4DiffTest.scala:93` is confirmed class A (was "flagged uncertain"), so node-scala's confirmed-A count is now 2, not 1. Post-Task-6 resolution: matcher's 3 empty `OrderBookBackwardCompatTestSuite.scala` class-C ignores were deleted (not fixed in place), so matcher's real remaining-ignore count is now 3, not 6 (1 real WS bug still class C, 2 DEX-982-old still class D). See "Task 4 resolution log" and "Task 6 resolution log" below.*

## Items flagged NOT confident (need real Docker/sbt execution before Task 4/5/6 acts)

1. **`InvokeListForCallable.scala:133,149,166`** (3 tests) — classified B on static reading (no runtime arg-size/bounds enforcement found outside the RIDE compiler's own `limited=true` path), but not proven by execution.
2. ~~**`CallableV4DiffTest.scala:93` (`trace`)** — could not run locally (sandboxed, no network for sbt dependency resolution); genuinely unclear whether this is A (stale trace-shape assertion) or C (slow/fragile, intentionally excluded).~~ **RESOLVED 2026-08-02 — this environment DID have Docker/sbt/network access; ran it for real, confirmed class A, fixed the stale assertion, un-ignored, now green. See the `CallableV4DiffTest.scala:93` entry above for full evidence.**
3. **`BlockSpecification.scala:198` (`serialize and deserialize big block`)** — classed C (heavy generator, likely excluded for runtime) but has a real assertion; arguably worth periodic re-enablement rather than permanent ignore — a judgment call, not a hard fact.

All other 21 classifications are backed by either an explicit in-file/comment citation (SC-695, DEX-982, DEX-467, DEX-1402, LeaseExpiration pre-activation) or a direct code-reading finding (duplicate test, commented-out production check, missing compiler diagnostic, zero-assertion benchmark).

## Task 4 resolution log (class-A fixes, 2026-08-02)

Both node-scala class-A candidates from this inventory are now resolved on branch `test/fix-class-a-ignores` (commit `d963e5f22d`), pending review/merge:

| Item | Resolution | Evidence |
|---|---|---|
| `InvokeScriptTransactionSuite.scala:103` | Deleted (confirmed byte-for-byte duplicate of the active `"translate alias to the address"` test at line 177) | Direct code read; `node-it/Test/compile` clean after removal |
| `CallableV4DiffTest.scala:93` (`trace`) | Un-ignored; fixed a stale object-equality assertion (compared two different, both-correct case classes — `FailedTransactionError` from the per-step trace vs. `ScriptExecutionError` from the RideV6 fail-free top-level conversion) to compare the semantically relevant fields instead | `sbt --batch "node-tests/testOnly com.decentralchain.state.diffs.ci.CallableV4DiffTest"`: RED (7/8, `trace` failed on the stale comparison) → GREEN (8/8) after the fix |

Neither fix touched production code under `node/src/main/scala/com/decentralchain/{state,consensus,mining}` — both were pure test-code corrections, consistent with the plan's CONSENSUS-CRITICAL constraint and the SC-575/580 "fix the test, not the node" method.

## Task 6 resolution log (matcher ignores + DEX-982-old deprecation planning, 2026-08-02)

Scope: plan Steps 1, 2, and 4 only. **Step 3 (cutting matcher's first tagged release) was explicitly NOT done** — it's a standing human-decision gate per the plan ("Decide with the human"), not something to execute unilaterally; nothing was tagged, released, or pushed as part of this work.

**Real local Docker infra was stood up and used** (this was not a static-only pass): `sbt "dex-it/docker"` was run to completion, building all 4 images (`matcher-node`, `dex-integration-it`, `matcher-server`, `dex-it`) from a clean local build. Two real, environment-level obstacles were hit and fixed along the way (documented here since they're reusable findings for any future local matcher dex-it run on this class of machine):

1. **`ghcr.io/decentral-america/node-scala:1.7.0: no match for platform in manifest`** building on Apple Silicon — the locally-cached base image is `linux/amd64`-only and Docker Desktop's buildx metadata resolution needs the platform pinned explicitly. Fix: `DOCKER_DEFAULT_PLATFORM=linux/amd64`, set **before the sbt server starts** (sbt 2.x's persistent background server freezes the env of whichever step first launched it — a mid-session env var change is silently ignored until `sbt shutdown` kills the stale server).
2. **`decentralchain/matcher-node:latest` / `decentralchain/matcher-server:latest` not found** — `project/ImageVersionPlugin.scala` only tags an image `:latest` when built from `main`/`master`/a `version-`/`dex-` prefixed branch; a feature/test branch like `test/matcher-ignore-triage` only gets tagged with the sanitized branch name. Since `dex-integration-it`'s and `dex-it`'s own Dockerfiles hardcode `FROM decentralchain/matcher-node:latest` / `FROM decentralchain/matcher-server:latest` regardless of branch, a plain branch build breaks the chain. Fix: `docker tag decentralchain/matcher-node:<branch-tag> decentralchain/matcher-node:latest` (and same for `matcher-server`) after each image builds, before the next stage's build runs.

**The hard blocker (not fixed, documented honestly):** once all 4 images existed, every attempt to actually **run** a dex-it suite (`sbt 'dex-it/testOnly com.decentralchain.it.matcher.api.http.status.GetOrderStatusByPKAndIdWithSigSpec'` was used as the smoke probe — it's the simplest suite, single node, no Kafka) failed identically, 4 times in a row, including after a full Docker Desktop daemon restart (`osascript -e 'quit app "Docker Desktop"'` + relaunch, confirmed `docker info` healthy again in between):

```
23:36:57.908 ERROR [main] c.d.actor.RootActorSystem$ - Error while initializing actor system decentralchain
java.lang.reflect.InvocationTargetException
	...
	at com.decentralchain.events.BlockchainUpdates.<init>(BlockchainUpdates.scala:33)
Caused by: org.rocksdb.RocksDBException: lock hold by current process, acquire time 1785713817 acquiring thread 140737451153088: /var/lib/dcc/blockchain-updates/LOCK: No locks available
```

Notable: the *main* state RocksDB (`c.d.database.RDB$ - Open DB at /var/lib/dcc/data`) opens successfully in the same process just before this — only the second RocksDB instance (`BlockchainUpdates`, a separate DB at a different path on the same named volume) fails to acquire its own lock. This points at this specific local Docker Desktop install's amd64-emulation layer (no Rosetta translation configured — `UseVirtualizationFrameworkRosetta` is unset, so Docker Desktop's own QEMU-based binfmt emulation handles the cross-arch translation) having a low/broken ceiling on advisory file locks for a single process opening more than one, not a matcher/node code defect: this exact local-docker path (same node base image, same emulation) was used successfully for a real dex-it suite in a prior session (see project memory `project_bug2_reorg_rebroadcast` — a full reorg dex-it suite ran green under the same amd64-emulated setup), so this is read as a flaky/regressed state of this particular machine's Docker Desktop right now, not an unconditional rule that dex-it can never run locally here.

**What would unblock it:** re-run on a native (non-emulated) amd64 host, or this repo's own nightly `integration-dex-it` GitHub Actions job (`ubuntu-latest`, 8-shard matrix) — both already prove these suites pass on real infra; a future local attempt could also try disabling/reconfiguring Docker Desktop's VM-level file-locking path (e.g. toggling Rosetta translation on) as an untried next step, or simply retrying after a host reboot (not just a Docker Desktop app restart, which did not clear it).

**Outcome given the blocker, per plan Step 1's explicit fallback:**

| Item | Outcome |
|---|---|
| `OrderBookBackwardCompatTestSuite.scala` 3× empty `ignore {}` ("Hard to reproduce") | **Deleted** (matcher commit `d91766a5f` on branch `test/matcher-ignore-triage`) — real reproduction was attempted and genuinely blocked before reaching these scenarios; since the bodies were empty regardless, deletion-with-ticket-as-record is the correct action per the plan, not a judgment call this session invented. DEX-467 preserved in the inventory entry above. |
| `WsOrderBookStreamTestSuite.scala:394` (DEX-1402) | **Left unchanged** (no code touched) — same blocker hit before this suite's container could boot; a real ticketed bug must not be silently reclassified or weakened just because this machine couldn't reproduce it *this session*. Evidence trail added to the inventory entry above for whoever picks it up next. |
| `GetOrderStatusByPKAndIdWithSigSpec.scala` 2× DEX-982-old ignores | **Left unchanged** (no code touched, per the plan's explicit instruction) — a deprecation plan was written instead (see the DEX-982-old cluster entry above); confirmed the new `/matcher/orders/status/{publicKey}/{orderId}` route is real, merged, and tested (`main` commit `3ed0ec65b`). |

**Branch state:** `test/matcher-ignore-triage`, based on matcher `main` (`3ed0ec65b`), one commit ahead (`d91766a5f`). Not pushed, no PR opened — ready for review/merge as its own follow-up decision. **Step 3 (first tagged release) was not started, decided, or executed.**
