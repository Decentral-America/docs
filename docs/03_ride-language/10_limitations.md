# Limitations

```{note}
Verified against node-scala commit [`104ddc70e8`](https://github.com/Decentral-America/node-scala/tree/104ddc70e8007175e0d1306b6db527ad37bb1b1f), the build the Testnet runs: `ContractLimits.scala` in the `lang` module and the node validators that enforce each value.
```

The node enforces every limit on this page. Some depend on the script's `STDLIB_VERSION`, and some on which {doc}`blockchain features <../05_node-guide/10_features-and-activation>` the network has activated. The Mainnet runs features up to 16 and so stops at version 5. The Testnet runs every feature, so all columns apply there. {doc}`Building Apps <../04_building-apps/07_smart-contracts-overview>` lists the values for each network.

## Complexity

Every function and operator has a complexity cost, listed per version in the {doc}`function reference <13_function-reference/index>`. The compiler adds up the costs along a script's most expensive path, and the node rejects a script whose total is over the limit for its kind.

| Limit | V1–V2 | V3–V4 | V5 | V6–V9 |
|---|---|---|---|---|
| Account script, or a dApp's `@Verifier` function | 2,000 | 2,000 | 2,000 | 2,000 |
| Asset script | 2,000 | 4,000 | 4,000 | 4,000 |
| One `@Callable` function | — | 4,000 | 10,000 | 52,000 |
| One invocation in total: the callable, every callable it reaches through dApp-to-dApp calls, and the asset scripts of every smart asset involved | — | 52,000 | 26,000 | 52,000 |
| dApp-to-dApp calls (`invoke`, `reentrantInvoke`) in one invocation | — | — | 100 | 100 |

The 2,000 limit on account scripts and verifiers applies once feature 15 is active, which is the case on both networks. Before that, account scripts had the asset-script limit. The V3–V4 total is 4,000 × 13: one callable plus the asset scripts of up to 2 payments and 10 script actions, each up to 4,000.

Two smaller thresholds also count complexity:

* **Failed-transaction threshold, 1,000.** If an Invoke Script transaction fails before its scripts have spent 1,000 complexity in total, the node rejects it and charges no fee. Past 1,000, the node saves it on the chain as failed and charges the fee. See {ref}`Transaction Fail <03_ride-language/07_dapp-to-app-invocation:Transaction Fail>`.
* **Free verifier, 200.** An account whose script or `@Verifier` costs more than 200 pays an extra 0.004 DCC on every transaction it sends.

## Script Size

| Script | Limit |
|---|---|
| Account script or asset script (`CONTENT_TYPE EXPRESSION`) | 8 KB (8,192 bytes) |
| dApp script (`CONTENT_TYPE DAPP`), before feature 17 | 32 KB (32,768 bytes) |
| dApp script (`CONTENT_TYPE DAPP`), from feature 17 | 160 KB (163,840 bytes) |
| Name of a function, variable or callable | 255 bytes |

The size limit applies to the compiled script, not the source. It depends on the network's features, not on `STDLIB_VERSION`, so a version 5 dApp can be up to 160 KB on the Testnet.

## Invocations and Script Actions

| Limit | V3 | V4 | V5 | V6–V9 |
|---|---|---|---|---|
| Arguments of a callable function | 22 | 22 | 22 | 22 |
| Payments attached to one invocation | 1 | 2 | 10 | 10 |
| `ScriptTransfer`, `Lease`, `LeaseCancel`, `Issue`, `Reissue`, `Burn` and `SponsorFee` actions | 10 | 10 | 30 | — |
| `ScriptTransfer`, `Lease` and `LeaseCancel` actions | — | — | — | 100 |
| `Issue`, `Reissue`, `Burn` and `SponsorFee` actions | — | — | — | 30 |
| Data entry actions (`BinaryEntry`, `BooleanEntry`, `IntegerEntry`, `StringEntry`, `DeleteEntry`) | 100 | 100 | 100 | 100 |
| Size of a data entry key | 100 bytes | 400 bytes | 400 bytes | 400 bytes |

Not every action type exists at every version. V3 has only `ScriptTransfer` and a single `DataEntry` type, returned in a `TransferSet`, a `WriteSet` or both in a `ScriptResult`. `Issue`, `Reissue`, `Burn`, `SponsorFee` and the typed data entries arrive in V4, and `Lease` and `LeaseCancel` in V5. See {doc}`Previous Versions <11_previous-versions>`.

How the action limits are counted:

* **Across the whole invocation.** The action counts are totals for every callable an invocation runs, including those reached through dApp-to-dApp calls.
* **By the outermost dApp's version, from feature 19.** Once feature 19 is active, a chain of dApp-to-dApp calls is held to the limits of the version of the dApp the transaction invoked. Before that, each dApp's own version applied.
* **Data size.** One callable's data entries can store at most 5 KB (5,120 bytes), and all callables in one invocation together at most 15 KB (15,360 bytes). From feature 17, this size is the key's UTF-8 bytes plus the value's bytes (8 for an integer, 1 for a boolean, nothing for a delete). Before that, it was each entry's serialized size.
* **Total payments, from feature 17.** Once feature 17 is active, an invocation and every dApp-to-dApp call it makes can attach at most 100 payments together.
* **Empty keys.** From version 4, a data entry key cannot be empty.

The Invoke Script transaction that starts an invocation can be at most 5 KB (5,120 bytes).

## Values

| Limit | Value |
|---|---|
| `String` | 32,767 bytes of UTF-8 |
| `ByteVector` | 32,767 bytes, except fields such as a transaction's `bodyBytes` |
| `N` in `FOLD<N>` | 1,000 |
| List built by `split`, `removeByIndex` or `replaceByIndex` | 1,000 elements |
| Tuple | 2 to 22 elements |
| Weight of any value | 344,764 |
| Weight of the lighter of two values compared with `==` or `!=` | 13,000 |

**Weight** approximates a value's size in bytes. A list weighs 20, plus 20 per element, plus its elements' weights. A tuple or structure weighs 40, plus 30 per field, plus its fields' weights. {ref}`Data Weight <03_ride-language/07_dapp-to-app-invocation:Data Weight>` has worked examples. The 344,764 limit is sized to hold the largest Data transaction a script can see: 2 × 165,947 bytes for its body and data, plus its header, sender, proofs and 100 data entries.
