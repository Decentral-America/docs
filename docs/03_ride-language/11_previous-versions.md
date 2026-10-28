# Previous Versions

```{note}
Verified against node-scala commit [`104ddc70e8`](https://github.com/Decentral-America/node-scala/tree/104ddc70e8007175e0d1306b6db527ad37bb1b1f). The functions, types and variables each version adds or removes come from the dump the {doc}`function reference <13_function-reference/index>` is generated from. Every compile error quoted below was reproduced on the Testnet node's `POST /utils/script/compileCode`.
```

The {doc}`function reference <13_function-reference/index>` covers versions 6 to 9, and the hand-written function and structure pages describe version 5. This page covers versions 1 to 5: which of them a network still accepts, what each one added, and what breaks when you move a script to a newer version.

## Which Versions a Network Accepts

A script always runs with the standard library version it was compiled for. A node upgrade or a feature activation never changes how an existing script evaluates. To use a newer version, recompile the script and set it again.

A new script is checked when a Set Script, Set Asset Script or Issue transaction carries it:

* **Versions 3 and later** need the blockchain feature listed under {doc}`Standard Library Versions <08_stdlib-versions>`.
* **Versions 1 and 2** need no feature of their own.
* **From feature 22 (Light Node), versions 1 to 3 are rejected.** The node refuses any new script below version 4 with `Script version below V4 is not allowed after Light Node feature activation`. Scripts already on the chain keep running.

| Network | Highest active feature | Versions accepted for a new script |
|---|---|---|
| Testnet | 26 | 4 to 9 |
| Mainnet | 16 | 1 to 5 |

Always write the `STDLIB_VERSION` directive. Without it, the compiler library assumes version 3, while the node's `/utils/script/compileCode` endpoint assumes version 5 on both networks, because feature 16 is active on both. The same source can therefore compile to two different scripts.

## What Each Version Added

Limits that change between versions, such as complexity, payments and script actions, are on {doc}`Limitations <10_limitations>`.

### Version 1

Account scripts and asset scripts, both `CONTENT_TYPE EXPRESSION`: a Boolean expression that allows or denies a transaction. There are no dApps. The library has 62 functions and operators: arithmetic and comparison, `sigVerify` and the `sha256`, `keccak256` and `blake2b256` hashes, Base58 and Base64 conversion, account data reads (`getInteger(address, key)` and the like), `dccBalance`, `assetBalance`, `transactionById` and `extract`. The global variables are `tx`, `height`, `unit` and the rounding modes `CEILING`, `DOWN`, `FLOOR`, `HALFDOWN`, `HALFEVEN`, `HALFUP` and `UP`.

### Version 2

The same functions and types as version 1, plus the `Buy` and `Sell` order-direction variables.

### Version 3

* **dApps.** `CONTENT_TYPE DAPP` scripts with `@Callable` and `@Verifier` functions. A callable returns a `WriteSet` of `DataEntry` values, a `TransferSet` of `ScriptTransfer` values, or both in a `ScriptResult`. It receives at most one payment, as `i.payment`. Callable arguments can be `Int`, `String`, `ByteVector` or `Boolean`.
* **New variables:** `this`, `lastBlock`, `nil`, and the RSA digest algorithms `NOALG`, `MD5`, `SHA1`, `SHA224`, `SHA256`, `SHA384`, `SHA512`, `SHA3224`, `SHA3256`, `SHA3384` and `SHA3512`.
* **New types:** `Invocation`, `AttachedPayment`, `BlockInfo`, `Asset` and `InvokeScriptTransaction`.
* **New functions:** `addressFromStringValue`, `assetInfo`, `blockInfoByHeight`, `checkMerkleProof`, `cons`, `fromBase16String`, `toBase16String`, `getBinaryValue`, `getBooleanValue`, `getIntegerValue`, `getStringValue`, `indexOf`, `lastIndexOf`, `split`, `parseInt`, `parseIntValue`, `toInt`, `toUtf8String`, `log`, `pow`, `rsaVerify`, `transferTransactionById`, `value` and `valueOrErrorMessage`.
* **Removed:** `transactionById`. Use `transferTransactionById`, which reads only Transfer transactions.

### Version 4

* **Callables return a list of actions** instead of `WriteSet`, `TransferSet` or `ScriptResult`, which are removed together with `DataEntry`. The actions are `BinaryEntry`, `BooleanEntry`, `IntegerEntry`, `StringEntry`, `DeleteEntry`, `ScriptTransfer`, `Issue`, `Reissue`, `Burn` and `SponsorFee`.
* **Payments and arguments.** An invocation carries up to 2 payments, as the list `i.payments`. Callable arguments can also be lists of the four primitive types.
* **New types:** `BalanceDetails` and `UpdateAssetInfoTransaction`.
* **New list functions:** the `++` and `:+` operators, `containsElement`, `indexOf` and `lastIndexOf` on lists, `max`, `min`, `median`, `removeByIndex` and `makeString`.
* **New verification functions:** `createMerkleRoot`, `ecrecover`, and `groth16Verify` and `bn256Groth16Verify`, each with `_1inputs` to `_15inputs` variants. Size-capped variants of the hashes and verifiers, such as `sha256_16Kb` and `sigVerify_8Kb`, cost less than the uncapped ones.
* **Other new functions:** `contains`, `valueOrElse`, `calculateAssetId` and `transferTransactionFromProto`. The `getInteger(data, key)` family that reads a list of data entries now takes the typed entries instead of `DataEntry`.
* **Removed:** `extract` (use `value`) and `checkMerkleProof` (use `createMerkleRoot`).
* **Data keys** can be up to 400 bytes instead of 100, and can no longer be empty.

### Version 5

* **dApp-to-dApp invocations** with `invoke` and `reentrantInvoke`, available in dApp scripts only. See {doc}`dApp-to-App Invocation <07_dapp-to-app-invocation>`. A callable can return a tuple of its actions and a value for the caller.
* **`BigInt`.** The type, `toBigInt`, `parseBigInt` and `parseBigIntValue`, and `BigInt` overloads of the arithmetic operators and of `fraction`, `pow`, `log`, `median`, `min`, `max`, `toBytes`, `toInt` and `toString`.
* **Leasing actions** `Lease` and `LeaseCancel`, with `calculateLeaseId`.
* **Own-account data reads.** `getInteger(key)`, `getString(key)` and the rest of that family read the script's own account without an address. They aren't available in asset scripts.
* **Other new functions:** `isDataStorageUntouched` and `scriptHash`.
* **Payments:** up to 10 per invocation.
* **Removed:** the `HALFDOWN` and `UP` rounding modes. `CEILING`, `DOWN`, `FLOOR`, `HALFEVEN` and `HALFUP` remain.

## Upgrading a Script

The compiler rejects these constructs once you raise `STDLIB_VERSION` past the version shown. Each row has been compiled on both sides of the boundary.

| From | To | What breaks | Compile error | Fix |
|---|---|---|---|---|
| 1–2 | 3 | `transactionById` | `Can't find a function 'transactionById'(ByteVector)` | `transferTransactionById` |
| 3 | 4 | `WriteSet`, `TransferSet`, `ScriptResult`, `DataEntry` | `Can't find a function 'WriteSet'(List[])` | Return a list of actions; use `IntegerEntry`, `StringEntry` and the other typed entries |
| 3 | 4 | `i.payment` | ``Undefined field `payment` of variable of type `Invocation` `` | `i.payments`, a list |
| 3 | 4 | `extract(x)` | `Can't find a function 'extract'(Int\|Unit)` | `value(x)` |
| 3 | 4 | `checkMerkleProof` | `Can't find a function 'checkMerkleProof'(ByteVector, ByteVector, ByteVector)` | `createMerkleRoot` |
| 4 | 5 | `HALFDOWN`, `UP` | `A definition of 'HALFDOWN' is not found` | Another rounding mode |
| 5 | 6 | A union type as a `@Callable` argument, such as `x: Int\|String` | `Union type is not allowed for callable function arguments` | One argument per type, or a `String` you parse |
| 7 | 8 | `FOLD` or `base16` as a variable or function name | `Parse error` | Rename; both are keywords from version 8 |
| 7 | 8 | An object pattern with no fields, such as `case AttachedPayment() =>` | `Parse error` | Match on the type: `case p: AttachedPayment =>` |
| 7 | 8 | A non-constant field pattern, such as `case AttachedPayment(amount = 2 + 3) =>` | `Only constant value could be matched with object field` | Bind the field and compare it in the case body |

Version 3 could not take a list as a callable argument: `List[Int]` fails with `Unexpected callable func arg type: List[Int]`. That is a restriction lifted by version 4, not a break.

Raising the version can also change costs without changing any code. Some functions get cheaper (`split` goes from 75 to 1 at version 6), and a few get more expensive (`pow` on `BigInt` goes from 200 to 270). Check the script's new total against {doc}`Complexity Changes by Version <09_complexity-changes>`.
