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
The function tables and examples elsewhere in this reference were written for standard library version 5. This page lists everything versions 6 to 9 add on top of that — traced directly through the blockchain-functions, crypto, types and bindings context modules of the node-scala `lang` module, not carried over from any other documentation.
```

## What changed in each version

### Version 6

* **`addressFromPublicKey`** gets a native (compiler-builtin) implementation, replacing the library-defined one used in V1–V5. The signature and behaviour are unchanged; only the evaluation cost differs.
* **`take`, `drop`, `takeRight`, `dropRight`** on `ByteVector` and `String`, and **`makeString`**, switch from unchecked to complexity-checked variants — very large inputs that previously ran unmetered now count properly against a script's complexity budget. Existing scripts that stayed within reasonable sizes are unaffected.
* **`InvokeExpressionTransaction`** — a new transaction type becomes visible to Ride (fields `expression: ByteVector`, `feeAssetId: ByteVector|Unit`, plus the common transaction fields).
* From V6 onward, **every active transaction type's Ride constructor is hidden** (`hideConstructor = true`) — a script can pattern-match on `TransferTransaction`, `InvokeScriptTransaction` and so on, but can no longer construct new values of these types directly. This was not the case in V1–V5.

### Version 7

* **`BlockInfo`** gains a `rewards: List[(Address, Int)]` field — the block reward distribution (miner, XTN buy-back, DAO address, etc., depending on network configuration) for that block, matching blockchain feature 19 (Block Reward Distribution). No new functions.

### Version 8

* **`calculateDelay(generator: Address, balance: Int): Int`** — computes the FairPoS block-generation delay for a hypothetical generator and generating balance, without needing to read full chain state. Complexity cost 1. Added to support Light Node use (feature 22): a light client can estimate block timing from a header alone.
* **`Order`** gains an `attachment: ByteVector|Unit` field.

### Version 9

* **`p256Verify(message: ByteVector, signature: ByteVector, publicKey: ByteVector): Boolean`** — verifies a signature made with the NIST P-256 (secp256r1) curve. Complexity cost 43.
* **`validateCertificateChain(certificateChain: List[ByteVector], crls: List[ByteVector], timestamp: Int): ByteVector`** — validates an X.509 certificate chain (up to 5 certificates) against certificate revocation lists as of `timestamp`. Complexity cost 43.
* **Fixed-cost (1-complexity) encode/decode variants**: `toBase64String_1C`, `fromBase64String_1C`, `toBase16String_1C`, `fromBase16String_1C` — capped-input versions of the existing Base64/Base16 functions for scripts that need a predictable, minimal complexity cost regardless of the general-purpose function's usual cost curve.
* **`CommitToGenerationTransaction`** becomes visible to Ride for the first time — fields `endorserPublicKey: ByteVector`, `generationPeriodStart: Int`, `commitmentSignature: ByteVector`, plus the common transaction fields — matching {ref}`Deterministic Finality <02_decentralchain/09_protocol:Finality>` (feature 25). Like every transaction type since V6, its constructor is hidden; a script can pattern-match on it but not build one.

Everything else available in V5 — data types, control flow, `FOLD<N>`, `invoke`/`reentrantInvoke`, script and structure definitions — carries forward unchanged into V6 through V9 unless noted above.
