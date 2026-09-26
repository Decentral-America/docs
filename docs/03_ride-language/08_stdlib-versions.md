# Standard Library Versions

```{note}
Verified against node-scala v1.7.0 (`StdLibVersion.scala` and `RideVersionProvider.scala`).
```

The `{-# STDLIB_VERSION n #-}` directive selects the version of the Ride standard library a script is compiled against. The compiler in node v1.7.0 supports versions 1 to 9; the default when the directive is omitted is 3.

A script can only use a version once the network has activated the matching {doc}`blockchain feature <../05_node-guide/10_features-and-activation>`:

| Stdlib version | Enabled by feature |
|---|---|
| 3 | 11 — Ride 4 dApps |
| 4 | 15 — Ride V4, VRF, Protobuf, failed transactions |
| 5 | 16 — Ride V5, dApp-to-dApp invocations |
| 6 | 17 — Ride V6, MetaMask support |
| 7 | 19 — Block reward distribution |
| 8 | 22 — Light node |
| 9 | 25 — Deterministic finality and Ride V9 |

The node treats the highest version whose feature is active as the network's current Ride version.

Check which features are active on a network with the node's `/activation/status` endpoint before compiling for a new version.

```{important}
The function tables and examples in this reference were written for standard library version 5. Functions and behaviour added in versions 6 to 9 are not yet documented here; consult the `lang` module of node-scala for the authoritative list until this reference is extended.
```
