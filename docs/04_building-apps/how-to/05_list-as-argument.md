% The code on this page is included verbatim from docs/_samples/: CI typechecks
% list-argument.ts, and docs/scripts/check_ride_samples.py compiles
% ride/list-argument.ride.

# Pass a List to a dApp

A callable function can take a {ref}`list <03_ride-language/02_data-types:List as Function Argument>` as an argument, which lets one call handle many items: a batch of scores, a set of recipients, a basket of orders. This guide passes two lists, names and scores, and stores each pair.

```{note}
The script compiles on the public Testnet node (2026-10-25) with complexity 122. The TypeScript is typechecked against `@decentralchain/transactions@5.0.1`. It has not been broadcast as part of this documentation pass.
```

## Before You Start

You need Node.js 24 or later, the `compileRide` helper from {ref}`Compile a Script <04_building-apps/07_smart-contracts-overview:Compile a Script>`, and two Testnet accounts with DCC from the [faucet](https://testnet.decentralscan.com/faucet): one for the dApp, one to call it.

```bash
npm install @decentralchain/transactions@5.0.1
```

## Write the Script

Save this as `ride/list-argument.ride`:

```{literalinclude} ../../_samples/ride/list-argument.ride
:language: text
:lines: 2-
```

* **List parameters** are declared as `List[String]`, `List[Int]`, `List[Boolean]` or `List[ByteVector]`. A list argument can't hold another list.
* **Ride has no open-ended loops.** `FOLD<N>` (see {doc}`Iterations with FOLD <../../03_ride-language/06_iterations-with-fold>`) walks a list of at most `N` items, so the script rejects longer lists before it folds. A larger `N` allows more items per call but raises the complexity.
* **`size(entries)`** is the index of the current name, which is how `addEntry` finds the matching score.

## Deploy the Script

```{literalinclude} ../../_samples/list-argument.ts
:language: typescript
:lines: 2-16
```

## Pass Lists

A list argument is `{ type: 'list', value: [...] }`, and every item in it is typed in turn:

```{literalinclude} ../../_samples/list-argument.ts
:language: typescript
:lines: 18-
```

After the call, the dApp holds `score_alice`, `score_bob` and `score_carol`. If the lists have different lengths, or more than 10 items, the script throws and the call is rejected.
