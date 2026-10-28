% Node entries are sourced from the node-scala GitHub releases and the commits
% between their tags; SDK entries from the DecentralChain monorepo's release tags
% and package CHANGELOG.md files, and from the npm registry. Checked 2026-10-27.

# Release Notes

Full release history: [node-scala releases](https://github.com/Decentral-America/node-scala/releases) and the [SDK changelogs](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk) (one `CHANGELOG.md` per package).

## Which Version Runs Where

| Network | Node version | Check it with |
|---|---|---|
| Public Testnet | node-scala v1.8.1 | `GET https://testnet-node.decentralchain.io/node/version` |
| Mainnet | An earlier release (the public node reports `DCC v1.3.5`) | `GET https://mainnet-node.decentralchain.io/node/version` |

Node images are published to `ghcr.io/decentral-america/node-scala` with one tag per release (`1.8.1`, `1.8.0`) and per network (`testnet-latest`, `mainnet-latest`). See {doc}`Install with Docker <05_node-guide/04_install-docker>` and {doc}`Upgrade <05_node-guide/07_upgrade>`.

## Node v1.8.1 (2026-10-24)

A maintenance release with no change to consensus, the REST API or Ride. The public Testnet runs it.

* **Dependencies.** groth16 0.2.1.2 and curve25519 1.0.1, both sha256-pinned.
* **Licensing.** A third-party notice for the GPL-3.0 dependency.
* **Blockchain Updates.** The gRPC bind address of the Blockchain Updates extension is configurable.
* README and comment fixes.

Source: the [v1.8.1 release](https://github.com/Decentral-America/node-scala/releases/tag/v1.8.1).

## Node v1.8.0 (2026-10-19)

The first release after v1.7.0: consensus and build hardening, plus the work merged since July. Every node on a chain must run it before the chain reaches its `finality-hardening-height`. On the public Testnet that was height 90,000, already passed.

* **Block reward.** Feature 26, Adjusted Block Reward Distribution, is votable from this release (activated on the public Testnet). Continuation transaction and Lease expiration are renumbered to 27 and 28; see {doc}`Features and Activation <05_node-guide/10_features-and-activation>`.
* **Finality.** HotStuff can be made authoritative on a network that opts in (`dcc.hotstuff.authoritative`; the public Testnet does). Equivocating HotStuff voters forfeit their generation deposit from `functionality.hot-stuff-equivocation-penalty-height`. A lagging HotStuff replica re-anchors near the tip (`dcc.hotstuff.max-target-lag-fraction`).
* **Finality hardening** (consensus change, from `finality-hardening-height`). HotStuff quorum weight comes from generating balance, and proven equivocators weigh 0. A voter can't be both a valid endorser and a proven equivocator. Blocks signed with the legacy BLS domain separation tag are no longer accepted.
* **HotStuff and P2P hardening** (no consensus change). A proposal gets a vote only after the expected leader's own signed vote for it, proposal views are bounded, and gossip is validated before it is relayed. Endorser indexes are validated when a block is decoded.
* **Generators.** A generating node can commit itself to each generation period (`dcc.miner.self-commit-to-generation`), and recovers from peer-reconnection stalls on its own (`dcc.network.peer-stall-threshold`). A failed initial snapshot is retried instead of forging without a state hash.
* **Transaction pool.** Transactions that depend on a prioritised parent are kept and re-broadcast across new blocks instead of being dropped, and network-received transactions rejected before their dependency arrived are retried.
* **REST API.** `GET /addresses/seq/*` and `GET /utils/seed*` now require the API key; see {ref}`Authentication <05_node-guide/01_node-rest-api:Authentication>`.
* **Settings.** On a chain with history, consensus heights are pinned by the genesis signature. An unknown consensus key stops the node from starting; unknown REST, HotStuff and miner keys log a warning.
* **Network defaults.** The built-in Testnet profile now uses port 6868 and the public Testnet node as its peer, and the Mainnet profile no longer ships third-party seed addresses. The built-in `testnet` chain type is still not the public Testnet chain.
* **Security.** Netty updated for CVE-2026-75595, plus ingress-robustness hardening.
* **Build.** Native libraries come from Maven Central with pinned checksums. Each release image is smoke-tested and scanned before it is tagged, and carries a build-provenance attestation.

The v1.8.0 image reports its version as `DecentralChain v1.8.0-dev-1a1221cdd8`: it was built just before the tag, from a tree that differs only in a CI workflow. The binary is the released one.

Source: the [v1.8.0 release](https://github.com/Decentral-America/node-scala/releases/tag/v1.8.0).

## Node v1.7.0 (2026-07-25)

The first official GitHub release of node-scala (`v1.6.3` and earlier were git tags only).

* **Consensus safety fix.** The experimental HotStuff vote pool now checks quorum against every committee snapshot seen while a target's votes accumulate, closing a gap when committee membership changes mid-round. It also evicts stale votes from removed generators, bounds vote-pool memory, and verifies a quorum certificate locally before broadcasting it. HotStuff remains disabled by default (`dcc.hotstuff.enabled = false`); the public Testnet runs it enabled and authoritative. See {doc}`Features and Activation <05_node-guide/10_features-and-activation>`.
* **REST API.** `GET /node/status` now includes `generationPeriodLength`, a per-network constant that no endpoint exposed before.
* **Testing.** Expanded end-to-end testing: deterministic simulation, fault injection with network partitions, property-based fuzzing, and OpenAPI conformance checks in CI. No runtime behaviour change.

Source: the [v1.7.0 release page](https://github.com/Decentral-America/node-scala/releases/tag/v1.7.0).

## SDK Release of 2026-06-23 (Not on npm Yet)

A monorepo release commit of 2026-06-23 versions every SDK package for the 2.0 modernization: the packages moved from `packages/ts` to `packages/sdk`, gained a groth16 v2 verifier and a blst 0.3.16 rebuild, and many took a major version. The release tags were pushed on 2026-10-19:

| Package | Version | Package | Version |
|---|---|---|---|
| `transactions` | 6.0.0 | `signer` | 3.0.0 |
| `node-api` (was `node-api-js`) | 3.0.0 | `cubensis-connect-provider` | 2.0.0 |
| `ts-lib-crypto` | 3.0.0 | `cubensis-connect-types` | 2.0.0 |
| `types` | 3.0.0 | `data-service-client` | 5.0.0 |
| `marshall` | 2.0.0 | `ledger` | 6.0.0 |
| `protobuf-schemas` | 3.1.0 | `oracle-data` | 2.0.0 |

None of these versions is published to npm: the registry's newest `transactions` is still 5.0.1. These docs keep pinning the published versions listed in the {doc}`TypeScript SDK <04_building-apps/sdk/01_typescript>` page, and will move to the new majors once they are on npm.

## Ride REPL v1.6.2 (2026-06-06)

`@decentralchain/ride-repl` 1.6.2 is published to npm (tag `ride-v1.6.2`). It fixes the build of the JavaScript Ride compiler it bundles. See {doc}`Ride REPL <04_building-apps/developer-tools/01_ride-repl>`.

## DecentralScan v2.1.0 (2026-06-13)

The explorer gained the Testnet faucet: the `/faucet` page and the `POST /api/faucet` endpoint, paid from a dedicated wallet. v1.3.2 (2026-06-15) fixed the peer list, so **All Peers** shows the connected nodes. See {doc}`DecentralScan Guide <09_user-guides/03_decentralscan>`.
