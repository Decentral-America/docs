# Release Notes

Full release history: [node-scala releases](https://github.com/Decentral-America/node-scala/releases) and the [SDK changelogs](https://github.com/Decentral-America/DecentralChain/tree/main/packages).

## Node v1.7.0 (2026-07-25)

The first official GitHub release of node-scala (`v1.6.3` and earlier were git tags only).

* **Consensus safety fix.** The experimental HotStuff vote pool now checks quorum against every committee snapshot seen while a target's votes accumulate, closing a gap when committee membership changes mid-round. It also evicts stale votes from removed generators, bounds vote-pool memory, and verifies a quorum certificate locally before broadcasting it. HotStuff remains disabled by default (`dcc.hotstuff.enabled = false`); see {doc}`Features and Activation <05_node-guide/10_features-and-activation>`.
* **REST API.** `GET /node/status` now includes `generationPeriodLength`, a per-network constant that no endpoint exposed before.
* **Testing.** Expanded end-to-end testing: deterministic simulation, fault injection with network partitions, property-based fuzzing, and OpenAPI conformance checks in CI. No runtime behaviour change.

Source: the [v1.7.0 release page](https://github.com/Decentral-America/node-scala/releases/tag/v1.7.0).
