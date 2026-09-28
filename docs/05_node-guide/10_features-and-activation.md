# Features and Activation

```{note}
Verified against node-scala v1.7.0.
```

Protocol changes ship as numbered **blockchain features**. A feature is not active just because a node supports it: it must be activated on the network, either by a generator vote or because the network defaults pre-activate it.

## How activation works

1. Generators signal support for features they implement in the blocks they produce.
2. At the end of each voting period, a feature that reached the voting threshold is scheduled for activation.
3. After activation, the new rules apply to every node.

Inspect the current state at any time:

```bash
curl -s http://localhost:6869/activation/status
```

The response includes `height`, `votingInterval`, `votingThreshold`, `nextCheck` and a `features` list with each feature's status.

## Unsupported features

By default `dcc.features.auto-shutdown-on-unsupported-feature = yes`: if the network activates a feature your node does not know, the node shuts down rather than follow a chain it cannot validate. The fix is to [upgrade](07_upgrade). Generators can list the features they vote for in `dcc.features.supported`.

## Feature list in v1.7.0

| ID | Feature |
|---|---|
| 1 | Minimum generating balance of 1000 DCC |
| 2 | NG protocol |
| 3 | Mass Transfer transaction |
| 4 | Smart accounts |
| 5 | Data transaction |
| 6 | Burn any tokens |
| 7 | Fee sponsorship |
| 8 | Fair PoS |
| 9 | Smart assets |
| 10 | Smart account trading |
| 11 | Ride 4 dApps |
| 12 | Order version 3 |
| 13 | Reduced NFT fee |
| 14 | Block reward and community-driven monetary policy |
| 15 | Ride V4, VRF, Protobuf, failed transactions |
| 16 | Ride V5, dApp-to-dApp invocations |
| 17 | Ride V6, MetaMask support |
| 18 | Consensus and MetaMask updates |
| 19 | Block reward distribution |
| 20 | Capped buy-back and DAO amounts |
| 21 | Cease buy-back |
| 22 | Light node |
| 23 | Boost block reward |
| 24 | `ecrecover` fix |
| 25 | Deterministic finality and Ride V9 |
| 26 | Continuation transaction |
| 27 | Lease expiration |
| 28 | Modern Groth16 verifier |

Which of these are active on a given network is a runtime fact — read it from `/activation/status` rather than from this table.

## Finality and HotStuff

Finality in v1.7.0 is provided by **Deterministic Finality (feature 25)**. The release also contains an experimental HotStuff BFT fast-finality engine, controlled by `dcc.hotstuff.enabled`. It is **off by default**, its design documents describe rework still pending, and it is gated on an external audit before any Mainnet use. Do not enable it on a production node. When it is enabled, `/node/status` additionally reports `hotStuffFinalizedHeight`.
