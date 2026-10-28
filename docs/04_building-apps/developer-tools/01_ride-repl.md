% The code on this page is included verbatim from docs/_samples/ride-repl.ts,
% which CI typechecks; docs/scripts/check_install_snippets.py installs and
% imports the `npm install` line below.

# Ride REPL

The Ride REPL evaluates Ride one line at a time, so you can try out an expression, a function or a built-in without writing and deploying a whole script. Connected to a node, it also reads live chain state: heights, balances, account data and transactions.

The REPL is published as [`@decentralchain/ride-repl`](https://www.npmjs.com/package/@decentralchain/ride-repl), a JavaScript build of the Scala REPL in [`packages/ride/repl`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/ride/repl) of the DecentralChain monorepo. It has no command-line front end: you call it from a script, as below, or embed it in a web page.

```{note}
Verified on 2026-10-25 with `@decentralchain/ride-repl@1.6.2` on Node.js 24 and later, against the public Testnet node. The package ships no TypeScript declarations; the sample adds its own in `ride-repl-types.d.ts`.
```

## Install

```bash
npm install @decentralchain/ride-repl@1.6.2 @decentralchain/ts-lib-crypto@2.0.1
```

`ts-lib-crypto` provides the hash functions the REPL needs (see below).

## Run the REPL

```{literalinclude} ../../_samples/ride-repl.ts
:language: typescript
:lines: 2-
```

Output on the Testnet:

```text
> func double(n: Int) = n * 2
defined func double(n: Int): Int
> double(21)
res1: Int = 42
> sha256(toBytes("hello"))
res2: ByteVector = base58'42TEXg1vFAbcJ65y7qdYG9iCPvYfy3NDdVLd75akX2P5'
> height
res3: Int = 94609
> dccBalance(this).regular
res4: Int = 4696800003
> getString(this, "greeting")
res5: String|Unit = Unit
```

## How It Works

**Host functions.** The REPL doesn't hash or fetch anything itself. It calls functions that the host page or script defines as globals:

| Global | Needed for |
|---|---|
| `httpGet({ url })`, resolving to `{ status, body }` | Anything that reads the chain: `height`, `dccBalance`, `getString`, `transactionHeightById`… |
| `blake2b256`, `keccak256`, `sha256`, each `(ArrayBuffer) => ArrayBuffer` | The matching Ride hash functions |
| `curve25519verify`, `rsaVerify`, `merkleVerify` | `sigVerify`, `rsaVerify` and `checkMerkleProof`. The sample doesn't define them, so those calls fail with `ReferenceError` |

Pure expressions such as arithmetic, strings, lists and your own functions need none of them.

**Sessions.** `repl(settings)` starts a session. Its methods are:

* `evaluate(line)`, which resolves to `{ result }` or `{ error }`. A `let` or `func` stays defined for later lines.
* `info(name)` prints the declaration of a name you defined, and `totalInfo()` lists everything in scope.
* `clear()` forgets your definitions.
* `reconfigure(settings)` returns a session connected to another node or account.

**Connection settings.** `new NodeConnectionSettings(url, chainId, address)` takes the node URL, the chain ID as a number (`'!'.charCodeAt(0)`, 33, for the Testnet; `'?'`, 63, for Mainnet) and the address that `this` refers to. Call `repl()` without settings to work offline.

**Standard library.** The REPL compiles each line against the latest standard library version it supports. A script you deploy declares its own with `{-# STDLIB_VERSION ... #-}`. A built-in that works in the REPL can therefore be missing from an older script version.

## Limits

* Each line is one expression or one declaration. To try a whole dApp, or a function with `@Callable`, compile it with a node instead; see {ref}`Compile with a Node <04_building-apps/01_developer-tools:Compile with a Node>`.
* `FOLD<N>` is a compile-time macro, and the REPL can't parse it.
* The REPL only reads the chain. It never signs or broadcasts anything.
