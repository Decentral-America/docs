# DecentralChain Docs — Expansion Plan

**Status:** Proposed · **Branch base:** `dev` · **Owner:** Docs / Developer Relations
**Goal:** Close the documentation gap identified against a reference blockchain documentation set by writing original, DecentralChain-native content for every missing section, with no dependency on any third-party project's text, branding, endpoints or tooling.

---

## 1. Current state (verified in this repo)

> **Correction (2026-09-26, found while starting WP0):** the pages listed below as "missing" for `02_decentralchain/` (01-10) and `03_ride-language/` (01-07) **already exist as `.rst` files** (~10k lines), so those toctree entries are not broken and the strict build had no dead refs. WP1/WP2 are therefore *review-and-verify against node-scala v1.7.0* (plus the v1.7.0 HotStuff/consensus content and feature-30), not greenfield writing. The independence grep already returns 0 hits. Real strict-build baseline was 9 warnings (duplicate autosectionlabels, `footer_items`), now fixed; CI guard added in `.github/workflows/docs_checks.yml`. Still genuinely missing: glossary, WP3 new pages, WP4 node pages, WP5.

| Area | Present | Gap |
|---|---|---|
| Introduction | `01_introduction.md` (187 lines) | none |
| DecentralChain (`02_decentralchain/`) | `index.md`, `11_tokenomics.md`, `12_cr-coin.md` | The toctree in `index.md` already lists **10 pages that do not exist**: `01_account`, `02_token(asset)`, `03_transaction`, `04_block`, `05_node`, `06_order`, `07_oracle`, `08_mainnet-testnet-stagenet`, `09_protocol`, `10_binary-format`. Existing pages already `{ref}` link to `02_decentralchain/05_node`, so these are **live broken cross-references**. |
| Ride (`03_ride-language/`) | `index.md` (32 lines) | The toctree lists **7 missing pages**: `01_syntax-basics` … `07_dapp-to-app-invocation`. |
| Building Apps | 5 thin pages | No dApp/smart account/smart asset guides, no per-language SDK pages, no data-service/gRPC/blockchain-updates pages, 3 how-tos only. |
| Node Guide | 4 pages | Single install path (source/DEB); no Docker/OS installs, sync/rollback, upgrade, logging, wallet, features/activation, troubleshooting. REST API page is 23 lines. |
| Cross-cutting | 11 locales (`.po`), Sphinx + pydata theme, GH Pages workflow | No glossary, no ecosystem-apps section, no release-notes/community section. |

**Key insight:** the information architecture is already decided in the toctrees. The work is to **write the missing files**, not to redesign navigation.

---

## 2. Guiding principles

1. **Source of truth is DecentralChain's own code, not any other docs site.** Every fact (fees, limits, IDs, byte layouts, function signatures, config keys) is verified against `Decentral-America/node-scala`, the SDK repos, or a running Testnet node. Third-party docs are never a source.
2. **Zero third-party dependencies in the published site.** No copied prose, diagrams, code samples, screenshots, links, package names (`@waves/*`, `waves-*`), hosts (`*.waves.*`), units (`WAVES`, `wavelet`), or product names (Keeper, Waves IDE, Surfboard-by-Waves). Enforced by CI (see §7).
3. **Original wording and original examples.** Structure may be conceptually similar (accounts → tokens → transactions is universal), but text, examples and diagrams are authored fresh from the DecentralChain implementation.
4. **Single naming vocabulary.** DCC (coin), CR Coin, Cubensis Connect (wallet), `@decentralchain/*` packages, `decentralchain-{network}.conf`, DecentralScan (explorer). Defined once in a glossary and terminology sheet (WP0).
5. **Every page is testable.** Code samples are executed against Testnet in CI where feasible; parameters tables are generated or cross-checked from node config.
6. **English first, translations follow.** New English pages merge first; `.po` regeneration is a separate, automated step so translators are never blocked.

---

## 3. Deliverables by work package

Priority: **P0** unblocks broken links / core developer path · **P1** completes the reference · **P2** polish and ecosystem.

### WP0 — Foundations (P0, ~2 days)
- `docs/_terminology.md` (internal, not published): canonical names, forbidden strings, unit conversions (DCC base unit, decimals — read from node config).
- Page templates (front matter, admonitions, "Related" footer, "Verified against node-scala vX.Y" stamp).
- Add `06_glossary.md` skeleton (grows with every WP).
- CI guard job (see §7) added **first**, so all later PRs are checked.
- Fix broken toctree entries by adding stub pages, or temporarily commenting them out, so the build is warning-free before content lands (`sphinx-build -W`).

### WP1 — DecentralChain fundamentals (P0, ~2–3 weeks) → fills the 10 missing toctree targets
| File | Content to author (from node-scala source) |
|---|---|
| `01_account.md` | Seed → key pair → address derivation, address format and chain-ID byte, account balance kinds (regular / available / generating / effective), account data storage (entry types, size limits), aliases (rules, length, charset), smart accounts and dApps overview |
| `02_token(asset).md` | Issuing tokens, decimals, reissuability, NFTs, smart assets, token ID derivation, DCC native coin, sponsored fee, asset info updates |
| `03_transaction.md` | Common fields, fee model and sponsored fee, signature and proofs, validation pipeline, lifecycle (UTX → block), **one section per transaction type** with field table + JSON example + fee formula + failure cases. Split into `03_transaction/` subpages if any type exceeds ~150 lines |
| `04_block.md` | Header fields, generation signature, base target, transactions root hash, genesis block, microblocks |
| `05_node.md` | Roles, leasing, generator income, block reward and voting, monetary policy (link to Tokenomics), generating-balance requirement. *Resolves the existing `{ref}` links from Node Guide.* |
| `06_order.md` | DEX order structure, matcher, order types, exchange transaction, fees (only if matcher is part of the public offering; otherwise remove from toctree) |
| `07_oracle.md` | Data-transaction-based oracle pattern with a worked example using DCC data entries |
| `08_mainnet-testnet-stagenet.md` | Mainnet and Testnet table (chain ID, address prefix, node URLs, explorer, faucet at testnet.decentralscan.com/faucet) sourced from `network-defaults.conf`; Stagenet noted as planned only |
| `09_protocol.md` | LPoS mechanics, NG/microblock protocol, cryptography primitives in use, blockchain data types, validation rules, feature activation |
| `10_binary-format.md` | Byte layouts for blocks, transactions (per type/version), network messages, generated from or cross-checked against the node's serializers |
| `06_glossary.md` | Filled from all of the above |

### WP2 — Ride language reference (P0/P1, ~3–4 weeks) → fills the 7 missing toctree targets
| File | Content |
|---|---|
| `01_syntax-basics.md` | Directives, definitions, expressions, variables, functions, exceptions, comments, imports |
| `02_data-types.md` | Int, BigInt, Boolean, ByteVector, String, Unit, List, Tuple, Union, Any, with limits |
| `03_functions.md` | Built-in variables and functions by category (account data, blockchain, bytes, conversion, dApp-to-dApp, decoding/encoding, exceptions, hashing, list, math, string, union, verification), operators, `match…case`. **Generate the signature tables from the node's `lang` module** (script, checked into `docs/scripts/`) so they cannot drift from the compiler |
| `04_script-types.md` | dApp script (annotations, `@Callable`, `@Verifier`), account script, asset script, stdlib versions and per-version differences |
| `05_structures.md` | Script actions, common structures, transaction structures |
| `06_iterations-with-fold.md` | `FOLD<N>`, limits, worked examples |
| `07_dapp-to-app-invocation.md` | `invoke` / `reentrantInvoke`, payments, state-change ordering, complexity accounting; **document the feature-30 (InvokeVersionGating) behaviour** already implemented in node-scala |
| Extra pages | `08_limitations.md` (complexity, data weight, per-version), `09_previous-versions.md`, `10_libraries-and-imports.md` |

### WP3 — Building Apps (P1, ~2–3 weeks)
- **New:** `05_smart-contracts-overview.md`, `06_creating-and-launching-a-dapp.md`, `07_smart-accounts.md` (incl. multisig and escrow walkthroughs, written as text + runnable code, not video), `08_smart-assets.md`.
- **New how-tos** appended to `03_how-to-guides.md` (or split into a `how-to/` folder): airdrop, payments, token exchange, simple voting, list-as-argument, creating and broadcasting transactions.
- **New API pages:** `09_data-service-api.md` (only if DecentralChain operates one; otherwise document the actual alternative), `10_node-grpc.md`, `11_blockchain-updates.md`.
- **Tooling:** extend `01_developer-tools.md` with editor tooling and a Ride REPL page only for tools that exist under `Decentral-America`.
- **SDKs:** split `02_client-libraries-and-sdk.md` into one page per published SDK (TypeScript packages first; add others only when an official package exists). Each page: install, minimal transfer, error handling, link to package repo.
- All code samples live under `docs/_samples/` and are executed in CI against Testnet.

### WP4 — Node Guide (P1, ~2 weeks)
New pages, each verified on a clean machine: `install-docker`, `install-ubuntu`, `install-macos`, `install-windows`, `sync-and-rollback` (import/export, snapshot download, rollback), `generate-blocks`, `upgrade`, `configuration` (reference table of keys generated from `reference.conf`), `logging`, `wallet`, `features-and-activation`, `troubleshooting` (incl. block-generation FAQ), and a fully expanded `01_node-rest-api.md` (API key, pagination, CORS, limits, error codes). Retain existing `custom-blockchain` and `extensions` pages and cross-link.

### WP5 — Ecosystem, community and release info (P2, ~1 week)
- `07_ecosystem-apps.md`: Wallet & Exchange, DecentralScan explorer, Testnet faucet (only if operated), Cubensis Connect.
- `08_release-notes.md`: seeded from node-scala GitHub releases (script-assisted).
- Extend `06_contributing.md` with community channels.

### WP6 — Localization and release (P2, ~1 week)
Regenerate `.pot`/`.po` (`sphinx-build -b gettext`, `sphinx-intl update`), push to Gitlocalize, spot-check RTL (`ar`) and CJK (`ja`, `zh`) rendering, enable `sphinx-build -W` as a required check, tag the release, update README badges.

---

## 4. Sequencing and estimate

```
WP0 ─┬─ WP1 ─┬─ WP2 ──┬─ WP6
     │       ├─ WP3   │
     │       └─ WP4 ──┘
     └──────────── WP5 (parallel, low risk)
```
WP1 is the critical path (Ride and Building Apps link into it). Realistic total: **~10–12 weeks for one full-time author**, or **~5–6 weeks with two** (one on WP1/WP4 protocol/node topics, one on WP2/WP3 developer topics). Every WP ships as its own PR train into `dev`, one section per PR (≤ ~600 changed lines) for reviewability.

---

## 5. Authoring workflow (per page)

1. **Research:** read the relevant node-scala source/tests and SDK code; reproduce behaviour on Testnet; record the commit SHA in the page footer.
2. **Draft** from the template; original prose and diagrams (Mermaid/SVG, no borrowed images).
3. **Samples:** add to `docs/_samples/`, run locally, add to CI.
4. **Self-review checklist:** forbidden-string scan clean · every number traced to source · links resolve · toctree updated · glossary terms added.
5. **Review:** one technical reviewer (node/SDK maintainer) + one editorial reviewer. Technical review must confirm claims against code, not against any external docs.
6. **Merge** to `dev`; promote to `main` at each WP boundary.

---

## 6. Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Node is a fork, so DecentralChain behaviour may silently differ from what an author assumes | High | Rule: facts only from node-scala source or Testnet. Reviewer signs off against code. Feature-flag-gated behaviour (e.g. feature 30) documented with activation state |
| Content unintentionally mirrors third-party wording | Medium | Write from source, not from reading other docs; CI similarity/forbidden-string scan; editorial review |
| Docs drift from code after release | High | Generate function tables and config references from source; "Verified against vX.Y" stamp; release-checklist item to re-run generators |
| Existing cross-refs/toctree break the build (`-W`) | High (already occurring) | Fix in WP0 before content work |
| Translation backlog explodes | Medium | Translate only after English stabilizes per WP; untranslated pages fall back to English |
| Features listed but not offered (matcher/orders, data service, faucet) | Medium | Confirm with product owners in WP0; drop the page and toctree entry rather than document something that doesn't exist |

---

## 7. Quality gates (CI)

1. `sphinx-build -W --keep-going` — warnings as errors (catches broken toctree/`{ref}`).
2. **Independence check:** grep-based job failing on `(?i)waves|wavelet|@waves/|keeper wallet|wavesplatform` outside an explicit allow-list (none expected), across `docs/**/*.md`, `*.rst`, samples and static assets.
3. Link checker (`sphinx-build -b linkcheck`).
4. Sample runner: executes `docs/_samples/*` against Testnet (nightly, non-blocking on PRs from forks).
5. Generator freshness check: regenerated Ride/config tables must produce no diff.
6. Spell-check / style lint (Vale) with the project vocabulary.

---

## 8. Definition of done

- Zero Sphinx warnings; zero forbidden-string hits; all links resolve.
- All toctree targets exist; every section in the comparison gap list is either published or explicitly dropped with a recorded reason.
- Every code sample executes on Testnet; every numeric parameter traced to source.
- Glossary complete; English published; translation catalogs regenerated.
- README and contributing guide updated with the authoring workflow above.

## 9. Decisions (resolved 2026-09-25)

| # | Question | Decision | Effect on plan |
|---|---|---|---|
| 1 | Matcher/DEX and data service? | **Matcher is public.** A data-service client (`@decentralchain/data-service-client`) is published, so a data service exists. | Keep `06_order`; keep the data-service API page. **Action:** get the production data-service base URL and API surface confirmed by the service owner before writing. |
| 2 | Testnet faucet / Stagenet? | Faucet live at `https://testnet.decentralscan.com/faucet`. **Stagenet does not exist yet.** | `08_mainnet-testnet-stagenet` becomes **Mainnet & Testnet**, with a short "Stagenet: planned" note. Do not publish stagenet parameters. Samples run against Testnet using the faucet. |
| 3 | Official SDKs beyond TypeScript? | Monorepo `Decentral-America/DecentralChain`: TS packages (`types`, `crypto`, `ts-lib-crypto`, `transactions`, `node-api`, `data-service-client`, `signer`, `ledger`, `cubensis-connect-provider`, `marshall`, `bignumber`, `parse-json-bignumber`), Ride tooling (`ride-lang`, `ride-repl`), JVM (`io.decentralchain:java-sdk`, `transactions`, `curve25519`). | WP3 SDK pages: one per TS package group, plus **Java SDK**, plus Ride tooling. No pages for C#/PHP/Swift/Python/Rust/Go. `@decentralchain/ledger` gets a hardware-wallet how-to. |
| 4 | Baseline node version? | **node-scala v1.7.0** | All pages stamped "Verified against node-scala v1.7.0". Generators pinned to tag `v1.7.0`. |
| 5 | Resourcing | Not yet stated | Default to the one-author plan (10-12 weeks) until confirmed. |

### Consequences of the v1.7.0 baseline (added after reading its release notes)
- v1.7.0 describes **HotStuff committee/quorum-certificate consensus safety** work. WP1 `09_protocol.md` and `05_node.md` must document the consensus **as implemented in v1.7.0**, not only LPoS and NG. Confirm with the node maintainers how LPoS, NG and HotStuff relate in this release before drafting.
- `/node/status` exposes `generationPeriodLength`; include it in the REST API page and the network parameters table.
- Only the release's own claims were checked (via its GitHub release page); the actual source at tag `v1.7.0` is still the authority for every page.

## 10. Immediate next steps
1. Approve this plan.
2. Start WP0 (CI guards and broken-toctree fix) on a `docs/expansion-wp0` branch off `dev`.
3. In parallel, request from owners: data-service base URL/API docs, matcher API base URL, mainnet/testnet chain IDs and node URLs (or confirm they should be read from `network-defaults.conf` at v1.7.0).

## 11. Execution log (2026-09-26)

Baseline verified against node-scala **v1.7.0** and the SDK monorepo `main`.

**Done:** CI guard + strict build (0 warnings); Node Guide pages (Docker, configuration, sync/import/export/rollback, upgrade, wallet, logging, features/activation, troubleshooting, expanded REST API); SDK page rebuilt from the monorepo (+ Java SDK, Ledger how-to); glossary, ecosystem, release notes, community; Ride stdlib-versions page; Commit To Generation transaction + fee row; Finality section; `_terminology.md`.

**Errors found in existing pages and fixed from source:** chain IDs (Mainnet `?`/63, Testnet `!`/33, not W/T/S) and address prefixes (`3D`/`31`); all 77 example addresses regenerated with the DCC chain byte and valid checksums; `chainId` values in JSON examples; minimum fee in protocol validation (0.001 DCC per unit, not 1 DCC); block time drift (100 ms); UTX pool size (100000); generating balance with feature 1 (1000 DCC); node-scala links (`master` -> `main`); package names (`node-api`, not `node-api-js`).

**Not done / needs input:** Ride function tables for stdlib V6-V9 (needs a generator over `lang`; the reference is V5-level); per-language install pages for macOS/Windows/Ubuntu DEB (not verified on clean machines); data-service page (URL/API surface unconfirmed); matcher API base URL; public node/faucet URL liveness (unreachable from the authoring sandbox); `.po` regeneration and Gitlocalize sync (WP6); Vale and sample-runner CI jobs; "feature 30" does not exist in v1.7.0 (features end at 28), so that item is dropped.

## 12. Audit (2026-09-27)

Re-verified the whole PR against a fresh `origin/dev` and against source, independently of the work that produced it.

**Found and fixed:**
- The branch had been cut from a stale `dev`; `dev` had since gained a Sphinx 9 upgrade, a `pr_check_workflow.yml` (duplicating this PR's build/link CI), and other changes. Rebased; dropped the now-redundant `conf.py` duplicate-label/footer fixes (upstream already made them) and reduced the added workflow to just the independence-grep job so it doesn't duplicate the existing build/link jobs.
- `conf.py` called `repo.active_branch.name`, which raises on a detached HEAD — exactly what every GitHub Actions PR checkout is. This broke `pr_check_workflow.yml`'s build job for **every** PR against this repo, confirmed by reproducing it locally on a detached checkout before and after the fix. Not something this work introduced, but it blocked this PR's own CI signal, so fixed with a fallback to the commit SHA.
- `POST /transactions/calculateFee` requires the node's API key (confirmed against `openapi.yaml`); the REST API page had listed it as an unauthenticated endpoint.
- The Commit To Generation Transaction section omitted the 100 DCC generation deposit (`CommitToGenerationTransaction.DepositInDcclets`) it locks in addition to the fee.
- 9 binary-format CSV tables (address, alias, burn, invoke script, issue, lease cancel, reissue, set asset script, set script) still had the old chain-ID byte values (87/84/83) — the first pass fixed the `.rst` prose and JSON examples but missed these tables.
- `06_contributing.md` linked to GitHub Discussions on the SDK repo; confirmed via `gh api …has_discussions` that no Decentral-America repository has Discussions enabled. Replaced with a pointer to per-repo issues.

**Checked and found correct:** the from-scratch Base58/Keccak/Blake2b address-checksum conversion (cross-verified against `pycryptodome`, 71 addresses, 0 checksum failures); the Docker `DCC_LOG_LEVEL` default (Dockerfile's `INFO` is authoritative over a stale `DEBUG` in `docker/README.md`); the Commit To Generation transaction type ID (19) and fee (0.01 DCC); the full 28-entry feature list; the stdlib-version-to-feature mapping; every other REST endpoint's auth requirement against `openapi.yaml`.

**Judgment call, not a bug:** the ~20 example addresses that originally used the fork's Testnet/Stagenet prefixes (3M/3N) were all normalized to the DecentralChain Mainnet chain ID, since none of them were in a context that specifically called for Testnet — no evidence the original mixture was meaningful rather than cosmetic.

**Still unverified, unchanged from §11:** live node/faucet/matcher/data-service URLs, Docker registry (ghcr.io vs. the v1.7.0 release notes' "Docker Hub" mention), install pages for macOS/Windows/Ubuntu, Ride stdlib V6-V9 function tables, `.po` regeneration.

## 13. Completing the remaining plan items (2026-09-27, continued)

Went back through §11/§12's "still needed" list and completed everything resolvable from source in this environment.

**Completed:**
- **Node gRPC API** (`04_building-apps/05_node-grpc.md`): full client API (Accounts/Assets/Blockchain/Blocks/Transactions), traced to `node-api-grpc`'s source (no README existed, read the TS source directly) and cross-checked the ports (6870, 6881) against `grpc-server/src/main/resources/application.conf` server-side — both match.
- **Data Service API** (`04_building-apps/06_data-service-api.md`): full client API from `data-service-client`'s README. Resolved the "needs a base URL from the owner" blocker differently than expected — the client takes `rootUrl` and the matcher address as required caller-supplied parameters; neither is hardcoded in source, so the page documents this honestly instead of guessing a production URL.
- **`05_node-guide/02_node-extensions.md`** expanded with the real gRPC config keys and defaults from `grpc-server/src/main/resources/application.conf`, and confirmed via `build.sbt` that `grpc-server` is packaged as its own separate deployable artifact.
- **Ride stdlib V6–V9**: added a real, source-verified "what's new per version" section to `08_stdlib-versions.md`, tracing every version-gated addition in `PureContext.scala`, `CryptoContext.scala`, the blockchain-functions/types/bindings context modules, and adding the missing `rewards` (V7) and `attachment` (V8) fields to the `BlockInfo`/`Order` structures in `05_structures.rst` and their CSV tables. This is not the exhaustive per-function-signature reference WP2 originally scoped (that still needs the compiler-driven generator script), but it is complete and correct for every actual behavioural difference from V5 in v1.7.0.
- **Install pages** for Linux (with DEB packaging), macOS and Windows, sourced from node-scala's own `README.md` and `build.sbt`. Each carries the same "not run on a clean machine" caveat as the Docker page, since no clean VM was available.
- **Translation tooling** (`docs/scripts/update_translations.sh`): built and end-to-end tested (gettext extraction + `sphinx-intl update` against all 11 languages) on a clean git checkout of this branch — confirmed it only adds/obsoletes msgids and never drops an existing translated `msgstr` (translated-string count went up, not down, from gettext's fuzzy-matching). Deliberately **not run against the committed `.po` files** in this PR: regenerating now would produce an ~11-language diff with no translator available to review it, and the plan itself scopes this as a separate step after English stabilizes.
- The independence-check CI caught a real self-violation while writing the stdlib-versions page: a sentence cited the node-scala fork's literal (un-renamed) internal filename for one of its `lang` module files, containing the forbidden string. Fixed before commit — direct evidence the CI guard from WP0 works.

**Still not done, and now believed not completable from this environment at all:**
- Exhaustive Ride function-signature tables for V6–V9 in the same per-function format as the V5 tables (needs the generator script, not just a "what's new" reading).
- Live verification of any public URL (node, faucet, matcher, data service) — no network egress from this sandbox reaches them.
- Actual translations (vs. the tooling to regenerate the catalog skeleton) — needs human translators or Gitlocalize.
- Docker registry ambiguity (ghcr.io vs. the v1.7.0 release notes' "Docker Hub") — needs a maintainer to say which is authoritative; found no third source in-repo to resolve it.
- Confirmed production data-service and matcher URLs — genuinely not published in source, not something more repo reading will produce.
- Vale spell-check and a sample-runner CI job — not attempted; both need product decisions (a house vocabulary list for Vale; actual runnable samples under `docs/_samples/` for the runner) that are separate scoped work, not blocked facts.

## 14. Completing the remaining list, with a major correction found along the way (2026-09-28)

Went through every row of the "still needed" table from §13 and pushed each as far as real evidence allowed.

**Docker registry (resolved):** Queried GHCR's anonymous registry API directly (not README text) — `ghcr.io/v2/decentral-america/node-scala/tags/list` returns `mainnet-latest`, `testnet-latest`, `stagenet-latest`, `1.7.0` and per-commit `sha-*` tags, live today. Checked Docker Hub under every plausible name (`decentral-america/node-scala`, `decentralamerica/*`, `decentralchain/*`) — none exist. ghcr.io is confirmed authoritative; the v1.7.0 release notes' "Docker Hub" mention was just imprecise wording.

**Live URLs (confirmed genuinely unreachable, not a sandbox limitation):** Retested from network that successfully reaches `github.com`, `ghcr.io`, `npmjs.org` and Maven Central — `decentralchain.io` and every subdomain checked (nodes, decentralscan.com, testnet faucet, data-service, matcher) fail DNS resolution outright (`curl: (6) Could not resolve host`). This matches the real GitHub Actions linkcheck job's own failures on the same domains from a completely different network. These domains do not currently exist on the public internet — this is a finding about the project, not a limitation of this environment.

**Ride V6-V9 function tables (partially completed with a real generator):** Wrote `docs/scripts/extract_ride_complexity.py`, which parses `NativeFunction("name", Map(V.. -> N, ...), ...)` calls directly out of node-scala's `lang` module — no guessing, every row is a function name taken verbatim from source. Found 33 functions/overloads whose complexity cost changes at V6 or later; published as `03_ride-language/09_complexity-changes.md`. This is not the exhaustive per-signature reference WP2 originally wanted (costs set through a helper function rather than a literal, such as the BigInt arithmetic operators, aren't captured — documented as a known gap on the page itself), but every row is mechanically extracted and re-runnable, not hand-transcribed.

**Translations:** Built and ran `docs/scripts/update_translations.sh` for real against the actual committed `.po` files (not just the earlier clean-checkout test) to see the true diff size. Result: ~86,000 lines changed across 40 files, because so much English content changed since the catalogs were last regenerated. Net effect on translated content: 838 existing translated strings orphaned (their English source changed, so gettext correctly falls back to English) against only 46 newly matched by fuzzy-merge. This is the tool working exactly as intended, not a bug — but it produces a diff far too large for this PR to carry responsibly with no translator to review it. **Reverted** (`git checkout -- docs/locales && git clean -fd docs/locales`); the tooling stays, tested and ready, for a maintainer to run deliberately.

**Vale + sample runner (both completed for real, not scaffolded):**
- `.vale.ini` + `.vale/styles/DecentralChain/*.yml`, operationalizing `docs/_terminology.md` into two enforceable rules. Installed Vale (v3.23.0) and docutils locally, ran it against a deliberately-bad test file to confirm the rules actually fire (they do, with the right messages), then ran it against the full 53-file docs tree — zero false positives, matching the CI grep exactly. Wired into `docs_checks.yml` with the release asset resolved dynamically via the GitHub API (the naive `.../latest/download/vale_Linux_64-bit.tar.gz` URL 404s — the real asset name is versioned — caught by testing the exact curl command before committing it).
- `docs/_samples/`: real runnable samples for transfer, issue, read-balance and data-service-candles, each typechecked against the actually-installed, actually-published npm packages (not assumed from source). Added a CI job (`samples_typecheck`) that installs and runs `tsc --noEmit` — static-only, no live broadcast, documented honestly as such in the samples' own README.

**Major correction found while building the sample runner, propagated everywhere:** installing the real npm packages to typecheck against turned up that **this session had gotten several package names backwards**. Earlier in this work, "verifying against the monorepo `main` branch" was treated as equivalent to "what you can `npm install` today" — it isn't. `main` is ahead of what's released, several packages are being renamed there, and the *pre-existing* docs content (before this session touched it) had the currently-correct, live npm names the whole time:

| What this session wrongly changed it to | What's actually live on npm today |
|---|---|
| `@decentralchain/node-api` | `@decentralchain/node-api-js` (v2.0.0) |
| `@decentralchain/data-service-client` | `@decentralchain/data-service-client-js` (v4.2.0) — **and** the import is a default export (`import DataServiceClient from '...'`), not the named `{ DataServiceClient }` the monorepo source uses |
| `@decentralchain/types` | `@decentralchain/ts-types` (v2.0.0) |
| `@decentralchain/protobuf-schemas` | `@decentralchain/protobuf-serialization` (v2.0.0) |

`@decentralchain/node-api-grpc` is the one package confirmed to have no published release under any name — genuinely new, not a rename. Every one of these findings was confirmed by actually running `npm install <name>` and reading the installed package's real `package.json`/`.d.ts`/README, not by re-reading source. Fixed across every page that named these packages: `02_client-libraries-and-sdk.md` (full rewrite of the package tables, now with an explicit "monorepo name, if renamed" column), `03_how-to-guides.md`, `05_node-grpc.md`, `06_data-service-api.md`, `01_node-rest-api.md`, `02_node-extensions.md`, and the sample files themselves.

**Lesson for future work on this repo:** "verified against the monorepo `main` branch" is a claim about API shape and source-of-truth correctness, not about npm installability. State both separately from now on, and check the registry directly (`npm install`, not just reading a README) before telling a reader to run a command.
