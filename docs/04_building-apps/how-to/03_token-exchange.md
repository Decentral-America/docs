% The code on this page is included verbatim from docs/_samples/: CI typechecks
% token-exchange.ts, and docs/scripts/check_ride_samples.py compiles
% ride/token-exchange.ride.

# Exchange Tokens with a dApp

This guide builds a small exchange: a dApp that sells a token for DCC at a fixed price, and buys it back at the same price. A buyer calls the dApp with a DCC payment and receives the token in the same transaction. Nobody has to be online to fill the order.

For trading at market prices between any two tokens, use the DEX instead: its matcher pairs {doc}`orders <../../02_decentralchain/06_order>` and settles them with Exchange transactions.

```{note}
The script compiles on the public Testnet node (2026-10-25) with complexity 49 (`buy`) and 32 (`sell`). The TypeScript is typechecked against `@decentralchain/transactions@5.0.1`. It has not been broadcast as part of this documentation pass.
```

## Before You Start

You need:

* Node.js 24 or later, with the scripts saved as ES modules.
* Two Testnet accounts with DCC from the [faucet](https://testnet.decentralscan.com/faucet). The **exchange account** becomes the dApp and needs a little over 1 DCC: issuing the token costs 1 DCC. The **trader account** needs the purchase price plus 0.005 DCC for each call.
* The `compileRide` helper from {ref}`Compile a Script <04_building-apps/07_smart-contracts-overview:Compile a Script>`, saved as `compile-ride.ts`.

```bash
npm install @decentralchain/transactions@5.0.1
```

## Write the Script

Save this as `ride/token-exchange.ride`:

```{literalinclude} ../../_samples/ride/token-exchange.ride
:language: text
:lines: 2-
```

* **`price`** is in Decentralites per smallest unit of the token. For a token with 2 decimals, a price of `1_000_000` makes one whole token cost 1 DCC.
* **`buy()`** takes one DCC payment, sends back as many token units as it pays for, and returns the change.
* **`sell()`** takes one payment in the token and pays out DCC at the same price.
* **Payments reach the dApp before the function runs,** so `sell()` pays out from DCC that buyers brought in. If the dApp runs out of either asset, the call fails and the caller keeps their payment.

The exchange account keeps its normal signature check, so its owner can still restock, withdraw, or change the price with a Data transaction. Traders have to trust the owner on this. To make the price permanent, add a verifier that returns `false`, as the {doc}`pledge drive <../08_creating-and-launching-a-dapp>` does.

## Deploy the Exchange

```{literalinclude} ../../_samples/token-exchange.ts
:language: typescript
:lines: 2-45
```

The exchange account issues the token itself, so it holds the whole supply to sell. Each step waits for the previous one to be in a block, for the reason explained in {ref}`Sending a Transaction That Depends on Another <04_building-apps/03_how-to-guides:Sending a Transaction That Depends on Another>`.

## Trade

```{literalinclude} ../../_samples/token-exchange.ts
:language: typescript
:lines: 47-
```

The trader pays 5 DCC and gets 500 units, which is 5.00 tokens, then sells 200 units back for 2 DCC. `applicationStatus` is `succeeded` when the call went through. A call that fails one of the script's checks is rejected and costs the trader nothing.
