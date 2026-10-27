% The code on this page is included verbatim from docs/_samples/: CI typechecks
% voting.ts, and docs/scripts/check_ride_samples.py compiles ride/voting.ride.

# Run a Simple Vote

This guide builds a poll as a dApp. Each address can vote once, for one of a fixed set of options, until a deadline. Votes and counts are stored in the dApp's {ref}`account data storage <02_decentralchain/01_account:Account Data Storage>`, so anyone can count them. Once deployed, nobody can change them, not even the account that created the poll.

```{note}
The script compiles on the public Testnet node (2026-10-25) with complexity 54 for `vote` and 1 for the verifier. The TypeScript is typechecked against `@decentralchain/transactions@5.0.1`. It has not been broadcast as part of this documentation pass.
```

## Before You Start

You need Node.js 24 or later, the `compileRide` helper from {ref}`Compile a Script <04_building-apps/07_smart-contracts-overview:Compile a Script>`, and two Testnet accounts with DCC from the [faucet](https://testnet.decentralscan.com/faucet). Use a fresh **poll account**: once its script is set, it can never send a transaction again. The **voter account** needs 0.005 DCC for each vote.

```bash
npm install @decentralchain/transactions@5.0.1
```

## Write the Script

Save this as `ride/voting.ride`:

```{literalinclude} ../../_samples/ride/voting.ride
:language: text
:lines: 2-
```

* **`i.caller`** is the address that sent the call, so `vote_<address>` records one vote per address. A second call from the same address is rejected.
* **`count_<option>`** keeps a running total, so reading the result takes one lookup per option.
* **The verifier returns `false`.** The poll account can't sign anything after the script is set, so it can't rewrite the data either. That is also why the deadline has to be written before the script.

One address is one vote. If a voter can create addresses freely, so can a cheater. To weight votes by stake instead, make `vote` require a payment in a token, or read the voter's token balance with `assetBalance(i.caller, assetId)`.

## Deploy the Poll

```{literalinclude} ../../_samples/voting.ts
:language: typescript
:lines: 2-22
```

## Vote

```{literalinclude} ../../_samples/voting.ts
:language: typescript
:lines: 24-34
```

Each argument of a call is an object with a `type` (`string`, `integer`, `boolean`, `binary` or `list`) and a `value`. The types must match the parameters of the callable function.

## Count the Votes

```{literalinclude} ../../_samples/voting.ts
:language: typescript
:lines: 36-
```

Anyone can read the counts without a transaction, from any node. To list every vote, read the dApp's data entries whose keys start with `vote_`.
