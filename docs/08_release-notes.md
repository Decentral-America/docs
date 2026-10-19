# Release Notes

Full release history: [node-scala releases](https://github.com/Decentral-America/node-scala/releases) and the [SDK changelogs](https://github.com/Decentral-America/DecentralChain/tree/main/packages).

## Node v1.8.0 (2026-10-19)

The node version the public Testnet runs. Mainnet still runs an earlier release.

* **Block reward.** Feature 26, Adjusted Block Reward Distribution, is votable from this release (activated on the public Testnet). Continuation transaction and Lease expiration are renumbered to 27 and 28; see {doc}`Features and Activation <05_node-guide/10_features-and-activation>`.
* **Finality.** HotStuff can be made authoritative on a network that opts in (`dcc.hotstuff.authoritative`; the public Testnet does). Equivocating HotStuff voters forfeit their generation deposit from `functionality.hot-stuff-equivocation-penalty-height`. A lagging HotStuff replica re-anchors near the tip (`dcc.hotstuff.max-target-lag-fraction`), and finality hardening applies at a per-chain activation height.
* **Generators.** A generating node can commit itself to each generation period (`dcc.miner.self-commit-to-generation`), and recovers from peer-reconnection stalls on its own (`dcc.network.peer-stall-threshold`).
* **Transaction pool.** Transactions that depend on a prioritised parent are kept and re-broadcast across new blocks instead of being dropped, and network-received transactions rejected before their dependency arrived are retried.
* **Network defaults.** The built-in Testnet profile now uses port 6868 and the public Testnet node as its peer, and the Mainnet profile no longer ships third-party seed addresses. The built-in `testnet` chain type is still not the public Testnet chain.
* **Security.** Netty updated for CVE-2026-75595, plus ingress-robustness hardening.

Source: the [v1.8.0 tag](https://github.com/Decentral-America/node-scala/tree/v1.8.0).

## Node v1.7.0 (2026-07-25)

The first official GitHub release of node-scala (`v1.6.3` and earlier were git tags only).

* **Consensus safety fix.** The experimental HotStuff vote pool now checks quorum against every committee snapshot seen while a target's votes accumulate, closing a gap when committee membership changes mid-round. It also evicts stale votes from removed generators, bounds vote-pool memory, and verifies a quorum certificate locally before broadcasting it. HotStuff remains disabled by default (`dcc.hotstuff.enabled = false`); the public Testnet runs it enabled and authoritative. See {doc}`Features and Activation <05_node-guide/10_features-and-activation>`.
* **REST API.** `GET /node/status` now includes `generationPeriodLength`, a per-network constant that no endpoint exposed before.
* **Testing.** Expanded end-to-end testing: deterministic simulation, fault injection with network partitions, property-based fuzzing, and OpenAPI conformance checks in CI. No runtime behaviour change.

Source: the [v1.7.0 release page](https://github.com/Decentral-America/node-scala/releases/tag/v1.7.0).
