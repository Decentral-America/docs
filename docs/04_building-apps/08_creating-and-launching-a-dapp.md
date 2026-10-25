% The code on this page is included verbatim from docs/_samples/: CI typechecks
% deploy-dapp.ts and invoke-dapp.ts, docs/scripts/check_ride_samples.py compiles
% ride/pledge-drive.ride, and docs/scripts/check_install_snippets.py installs and
% imports the `npm install` line below.

# Creating and Launching a dApp

This walkthrough builds a small dApp on the Testnet, from the Ride source to a live call. The dApp runs a **pledge drive**. Backers pledge DCC before a deadline. If the pledges reach the goal by then, anyone can trigger the payout to a beneficiary. If they fall short, every backer can take their own pledge back. Nobody, the deployer included, can move the pledged DCC in any other way.

```{note}
Verified against node-scala v1.8.0 on 2026-10-25. The script compiles on the public Testnet node (`DecentralChain v1.8.0-dev-e6248f2408`) and the Mainnet node (`DCC v1.3.5`), and the fees below were confirmed with the Testnet node's `POST /transactions/calculateFee`. The TypeScript is typechecked against the published SDK; it has not been broadcast as part of this documentation pass.
```

## Before You Start

You need:

* Node.js 24 or later, with the scripts saved as ES modules (`"type": "module"` in `package.json`).
* Two Testnet accounts with DCC from the [faucet](https://testnet.decentralscan.com/faucet). The **campaign account** becomes the dApp and needs 0.004 DCC for its two setup transactions. The **backer account** needs the pledge plus 0.005 DCC for each call.
* The SDK and the `compileRide` helper from {ref}`Compile a Script <04_building-apps/07_smart-contracts-overview:Compile a Script>`, saved as `compile-ride.ts` next to your scripts:

```bash
npm install @decentralchain/transactions@5.0.1
```

Use a fresh account for the dApp. Once its script is set, this account can never send a transaction again. The addresses in the examples belong to throwaway example accounts; replace them with your own.

## Write the Script

Save this as `ride/pledge-drive.ride`, in a `ride` folder next to your scripts:

```{literalinclude} ../_samples/ride/pledge-drive.ride
:language: text
:lines: 2-
```

How it fits together:

* **State lives in the dApp's {ref}`account data storage <02_decentralchain/01_account:Account Data Storage>`.** `this` is the dApp's own address. The script reads its settings from there, and the callables record each backer's pledge under `pledge_<address>` and the amount the dApp currently holds in pledges under `total`.
* **Each `@Callable` function is an entry point.** `i` is the {ref}`Invocation <03_ride-language/05_structures:Invocation>`: `i.caller` is the address that sent the call and `i.payments` are the tokens attached to it. Attached payments reach the dApp's balance before the function runs, so `pledge()` only has to record them.
* **A function's result is a list of {ref}`script actions <03_ride-language/05_structures:Script Actions>`.** The node applies them after the function returns: `IntegerEntry`, `BooleanEntry` and `DeleteEntry` change data, and `ScriptTransfer` pays DCC out of the dApp's balance.
* **`throw()` aborts the call.** None of the actions apply and the attached payment stays with the caller.
* **`height`** is the current block height. On the Testnet a block arrives about every 30 seconds.
* **The verifier returns `false`,** so the campaign account can sign nothing at all: no transfers, no data changes, no new script. That is what makes the pledge drive trustworthy, and also why the settings must be written before the script.

## Check the Complexity

Compiling with `compileRide` prints the complexity. The Testnet node reports `pledge` 109, `refund` 129, `payout` 76 and a verifier complexity of 1. All three functions stay far below the 1,000 at which a failure starts to cost the caller a fee (see {ref}`Failed Transactions <04_building-apps/07_smart-contracts-overview:Failed Transactions>`). Every `throw()` in this dApp therefore rejects the call outright, and the backer pays nothing.

## Configure and Deploy

Deployment takes two transactions from the campaign account. The order matters: once the script is set, its verifier rejects everything the account sends, including Data transactions.

```{literalinclude} ../_samples/deploy-dapp.ts
:language: typescript
:lines: 2-
```

`waitForTx` waits until each transaction is in a block. The Set Script transaction must not reach the node before the settings are on chain, for the reason explained in {ref}`Sending a Transaction That Depends on Another <04_building-apps/03_how-to-guides:Sending a Transaction That Depends on Another>`.

The two transactions cost 0.001 DCC for the data and 0.003 DCC for the script (2,058 bytes, so three started kilobytes). Once the Set Script transaction is in a block, the account is a dApp. `GET /addresses/scriptInfo/{address}/meta` on any node lists its callable functions and their arguments.

## Call the dApp

A backer pledges 1 DCC by sending an Invoke Script transaction that names the function and attaches the payment:

```{literalinclude} ../_samples/invoke-dapp.ts
:language: typescript
:lines: 2-
```

The backer pays the 0.005 DCC fee; the dApp pays nothing for its own actions. Pass function arguments in `args` as typed values, for example `{ type: 'integer', value: 5 }` or `{ type: 'string', value: 'abc' }`.

If the function throws, `broadcast()` rejects with the node's error, whose message starts with `Error while executing dApp:` and ends with the text passed to `throw()`.

## Read the dApp's State

Everything the dApp records is public. Any node returns it:

* `GET /addresses/data/{dApp address}` lists every entry. Add `?matches=pledge_.*` to filter keys with a regular expression.
* `GET /addresses/data/{dApp address}/total` returns one entry.
* `GET /transactions/info/{transaction ID}` returns an Invoke Script transaction with its `applicationStatus`, its `spentComplexity` and a `stateChanges` object listing every action the call produced.

## Finish the Campaign

After the deadline height, exactly one of the two exits opens:

* If `total` reached `goal`, anyone sends `call: { function: 'payout', args: [] }` with no payment, and the dApp transfers the total to the beneficiary once.
* Otherwise each backer sends `call: { function: 'refund', args: [] }`, gets their own pledge back, and `total` goes down by that amount.

Both calls are ordinary Invoke Script transactions and cost the sender 0.005 DCC.

## Changing a dApp Later

This dApp can never change, by design. If your dApp needs upgrades, write a `@Verifier` that approves Set Script transactions signed by a key you control, and only those. Your users then have to trust that key, because a new script can do anything with the funds the dApp holds. Tell them so. Use [Smart Accounts](09_smart-accounts) to require several signatures for an upgrade.

## Moving to Mainnet

The script already uses `STDLIB_VERSION 5`, the highest version Mainnet supports. Use a Mainnet node URL and `chainId: '?'`. Pass `fee: 1_000_000` to `setScript()`, because Mainnet charges a flat 0.01 DCC for Set Script and the SDK's default is the Testnet's per-kilobyte fee.
