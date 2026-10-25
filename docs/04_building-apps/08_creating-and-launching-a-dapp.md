% Every `npm install` line and every `import ... from '@decentralchain/...'`
% on this page is installed and imported on Node.js 24 by CI
% (docs/scripts/check_install_snippets.py). docs/_samples/deploy-dapp.ts and
% docs/_samples/invoke-dapp.ts typecheck the full examples, and
% docs/scripts/check_ride_samples.py compiles docs/_samples/ride/pledge-drive.ride.

# Creating and Launching a dApp

This walkthrough builds a small dApp on the Testnet, from the Ride source to a live call. The dApp runs a **pledge drive**. Backers pledge DCC before a deadline. If the pledges reach the goal by then, anyone can trigger the payout to a beneficiary. If they fall short, every backer can take their own pledge back. Nobody, the deployer included, can move the pledged DCC in any other way.

```{note}
Verified against node-scala v1.8.0 on 2026-10-24. The script compiles on the public Testnet node (`DecentralChain v1.8.0-dev-e6248f2408`) and the Mainnet node (`DCC v1.3.5`), and the fees below were confirmed with the Testnet node's `POST /transactions/calculateFee`. The TypeScript is typechecked against the published SDK; it has not been broadcast as part of this documentation pass.
```

## Before You Start

You need:

* Node.js 24 or later, with the scripts saved as ES modules (`"type": "module"` in `package.json`).
* Two Testnet accounts with DCC from the [faucet](https://testnet.decentralscan.com/faucet). The **campaign account** becomes the dApp and needs 0.003 DCC for its two setup transactions. The **backer account** needs the pledge plus 0.005 DCC for each call.
* The SDK and the `compileRide` helper from {ref}`Compile a Script <04_building-apps/07_smart-contracts-overview:Compile a Script>`:

```bash
npm install @decentralchain/transactions@5.0.1
```

Use a fresh account for the dApp. Once its script is set, this account can never send a transaction again.

## Write the Script

Save this as `pledge-drive.ride`:

```text
{-# STDLIB_VERSION 5 #-}
{-# CONTENT_TYPE DAPP #-}
{-# SCRIPT_TYPE ACCOUNT #-}

# Campaign settings. A Data transaction writes them before this script is set.
let beneficiary = addressFromStringValue(getStringValue(this, "beneficiary"))
let goal = getIntegerValue(this, "goal")
let deadline = getIntegerValue(this, "deadline")

func pledgeKey(backer: Address) = "pledge_" + toString(backer)
func pledgedBy(backer: Address) = getInteger(this, pledgeKey(backer)).valueOrElse(0)
func totalPledged() = getInteger(this, "total").valueOrElse(0)

@Callable(i)
func pledge() = {
  let payment = if (size(i.payments) == 1) then i.payments[0] else throw("Attach exactly one payment")
  if (height >= deadline) then throw("The campaign ended at height " + toString(deadline))
  else if (isDefined(payment.assetId)) then throw("Pledges are accepted in DCC only")
  else [
    IntegerEntry(pledgeKey(i.caller), pledgedBy(i.caller) + payment.amount),
    IntegerEntry("total", totalPledged() + payment.amount)
  ]
}

@Callable(i)
func refund() = {
  let amount = pledgedBy(i.caller)
  if (height < deadline) then throw("Refunds open at height " + toString(deadline))
  else if (totalPledged() >= goal) then throw("The goal was reached, so pledges are not refundable")
  else if (amount == 0) then throw("Nothing to refund")
  else [
    DeleteEntry(pledgeKey(i.caller)),
    ScriptTransfer(i.caller, amount, unit)
  ]
}

@Callable(i)
func payout() = {
  if (height < deadline) then throw("The payout opens at height " + toString(deadline))
  else if (totalPledged() < goal) then throw("The goal was not reached")
  else if (getBoolean(this, "paidOut").valueOrElse(false)) then throw("Already paid out")
  else [
    BooleanEntry("paidOut", true),
    ScriptTransfer(beneficiary, totalPledged(), unit)
  ]
}

# Nothing can be sent from the campaign account by its key, including a new script.
# The pledged DCC can only leave through refund() and payout().
@Verifier(tx)
func verify() = false
```

How it fits together:

* **State lives in the dApp's {ref}`account data storage <02_decentralchain/01_account:Account Data Storage>`.** `this` is the dApp's own address. The script reads its settings from there, and the callables record each backer's pledge under `pledge_<address>` and the running total under `total`.
* **Each `@Callable` function is an entry point.** `i` is the {ref}`Invocation <03_ride-language/05_structures:Invocation>`: `i.caller` is the address that sent the call and `i.payments` are the tokens attached to it. Attached payments reach the dApp's balance before the function runs, so `pledge()` only has to record them.
* **A function's result is a list of {ref}`script actions <03_ride-language/05_structures:Script Actions>`.** The node applies them after the function returns: `IntegerEntry`, `BooleanEntry` and `DeleteEntry` change data, and `ScriptTransfer` pays DCC out of the dApp's balance.
* **`throw()` aborts the call.** None of the actions apply and the attached payment stays with the caller.
* **`height`** is the current block height. On the Testnet a block arrives about every 30 seconds.
* **The verifier returns `false`,** so the campaign account can sign nothing at all: no transfers, no data changes, no new script. That is what makes the pledge drive trustworthy, and also why the settings must be written before the script.

## Check the Complexity

Compiling with `compileRide` prints the complexity. The Testnet node reports `pledge` 109, `refund` 113, `payout` 76 and a verifier complexity of 1. All three functions stay far below the 1,000 at which a failure starts to cost the caller a fee (see {ref}`Failed Transactions <04_building-apps/07_smart-contracts-overview:Failed Transactions>`). Every `throw()` in this dApp therefore rejects the call outright, and the backer pays nothing.

## Configure and Deploy

Deployment takes two transactions from the campaign account. The order matters: once the script is set, its verifier rejects everything the account sends, including Data transactions.

```typescript
import { readFile } from 'node:fs/promises';
import { data, setScript, broadcast, waitForTx, libs, nodeInteraction } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const campaignSeed = 'campaign account secret seed phrase here';
const beneficiary = '31ekkhvBGr91ygJf4st72hAEVU9BUBs3Ats'; // receives the DCC if the goal is met

// 1. Write the settings while the account still signs normally.
const deadline = (await nodeInteraction.currentHeight(nodeUrl)) + 2_880; // about one day of 30-second blocks
const settings = data(
  {
    data: [
      { key: 'beneficiary', type: 'string', value: beneficiary },
      { key: 'goal', type: 'integer', value: 500_000_000 }, // 5 DCC
      { key: 'deadline', type: 'integer', value: deadline },
    ],
    chainId: '!',
  },
  campaignSeed,
);
await broadcast(settings, nodeUrl);
await waitForTx(settings.id, { apiBase: nodeUrl, timeout: 120_000 });

// 2. Compile the dApp script and set it on the same account.
const script = await compileRide(await readFile('pledge-drive.ride', 'utf8'), nodeUrl);
const deploy = setScript({ script, chainId: '!' }, campaignSeed);
await broadcast(deploy, nodeUrl);
await waitForTx(deploy.id, { apiBase: nodeUrl, timeout: 120_000 });

console.log('dApp address:', libs.crypto.address(campaignSeed, '!'));
```

`waitForTx` waits until each transaction is in a block. The Set Script transaction must not reach the node before the settings are on chain, for the reason explained in {ref}`Sending a Transaction That Depends on Another <04_building-apps/03_how-to-guides:Sending a Transaction That Depends on Another>`.

The two transactions cost 0.001 DCC for the data and 0.002 DCC for the script (1,977 bytes, so two started kilobytes). Once the Set Script transaction is in a block, the account is a dApp. `GET /addresses/scriptInfo/{address}/meta` on any node lists its callable functions and their arguments.

## Call the dApp

A backer pledges 1 DCC by sending an Invoke Script transaction that names the function and attaches the payment:

```typescript
import { invokeScript, broadcast, waitForTx, nodeInteraction } from '@decentralchain/transactions';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const backerSeed = 'backer secret seed phrase here';
const dApp = '31fYMsRvDstHkCPfswAEvpEUVSReqwWVvjP'; // the campaign account from the deploy step

const pledge = invokeScript(
  {
    dApp,
    call: { function: 'pledge', args: [] },
    payment: [{ assetId: null, amount: 100_000_000 }], // 1 DCC
    chainId: '!',
  },
  backerSeed,
);
await broadcast(pledge, nodeUrl);
const info = await waitForTx(pledge.id, { apiBase: nodeUrl, timeout: 120_000 });
console.log('Application status:', info.applicationStatus);

// The callable's data entries are now in the dApp's account data storage.
const total = await nodeInteraction.accountDataByKey('total', dApp, nodeUrl);
console.log('Total pledged (Decentralites):', total?.value);
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
* Otherwise each backer sends `call: { function: 'refund', args: [] }` and gets their own pledge back.

Both calls are ordinary Invoke Script transactions and cost the sender 0.005 DCC.

## Changing a dApp Later

This dApp can never change, by design. If your dApp needs upgrades, write a `@Verifier` that approves Set Script transactions signed by a key you control, and only those. Your users then have to trust that key, because a new script can do anything with the funds the dApp holds. Tell them so. Use [Smart Accounts](09_smart-accounts) to require several signatures for an upgrade.

## Moving to Mainnet

The script already uses `STDLIB_VERSION 5`, the highest version Mainnet supports. Use a Mainnet node URL and `chainId: '?'`. Pass `fee: 1_000_000` to `setScript()`, because Mainnet charges a flat 0.01 DCC for Set Script and the SDK's default is the Testnet's per-kilobyte fee.
