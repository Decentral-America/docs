% The code on this page is included verbatim from docs/_samples/quick-start-account.ts
% and docs/_samples/quick-start-transfer.ts, which CI typechecks against the pinned
% SDK versions. Both were run on the public Testnet on 2026-10-27 (see the note below).

# Quick Start: Your First Transfer

This guide takes you from nothing to a confirmed transaction on the public Testnet in about ten minutes. You create an account, get free Testnet DCC from the faucet, send 1 DCC to another address and look the transaction up in the explorer.

Testnet DCC have no value, so nothing you do here can cost you money. Everything works the same way on Mainnet once you switch the node URL and chain ID (see {ref}`Moving to Mainnet <09_user-guides/01_quick-start:Moving to Mainnet>` at the end).

```{note}
Followed end to end on the public Testnet on 2026-10-27: the faucet paid 10 DCC in transaction `26UPUF6Psun5KyPQ2UiZinzo9qDuny8Nu9TziwaoLPVy`, and the transfer in step 4 is transaction `BVVmaKri16PUJJqHbLmDRnzcyc4SdYbr6GQZgDhhFPxx` (height 99,864).
```

## Step 1: Set Up a Project

You need [Node.js](https://nodejs.org/) 24 or later. Create a folder for the project, mark it as an ES module and install the transactions package:

```bash
mkdir dcc-quickstart && cd dcc-quickstart
npm init -y
npm pkg set type=module
npm install @decentralchain/transactions@5.0.1
```

Node.js 24 runs TypeScript files directly, so you can save the scripts below as `.ts` files and run them with `node <file>.ts`. To use plain JavaScript instead, save them as `.js` files; the code is the same.

## Step 2: Create a Testnet Account

An account is a key pair derived from a seed phrase: 15 random words. Save this script as `create-account.ts` and run it with `node create-account.ts`:

```{literalinclude} ../_samples/quick-start-account.ts
:language: typescript
:lines: 2-
```

It prints the seed phrase and the account's Testnet address, which starts with `31`. Write the seed phrase down and keep it private: anyone who has it controls the account, and it cannot be recovered if you lose it. For what the seed, keys and address are, see {ref}`Account <02_decentralchain/01_account:Account>`.

To manage the same account in a browser wallet, import the seed phrase into Cubensis Connect; see {doc}`Cubensis Connect User Guide <02_cubensis-connect>`.

## Step 3: Get Testnet DCC

The Testnet faucet sends 10 DCC to an address, once every 24 hours per address. Either open [testnet.decentralscan.com/faucet](https://testnet.decentralscan.com/faucet) and paste your address, or call the faucet's API:

```bash
curl -X POST https://testnet.decentralscan.com/api/faucet \
  -H 'Content-Type: application/json' \
  -d '{"address": "YOUR_TESTNET_ADDRESS"}'
```

A successful request returns the transfer's ID:

```json
{"amount": 10, "success": true, "txId": "26UPUF6Psun5KyPQ2UiZinzo9qDuny8Nu9TziwaoLPVy"}
```

The faucet answers `429` if the address already received DCC in the last 24 hours, and `400` for an address that is not a Testnet address.

Check that the DCC arrived. Balances are in Decentralites, the smallest unit: 1 DCC is 100,000,000 Decentralites.

```bash
curl https://testnet-node.decentralchain.io/addresses/balance/YOUR_TESTNET_ADDRESS
```

```json
{"address": "31gSFbvTohHJfF74ha1D5b2oJUYsp7UNRxt", "confirmations": 0, "balance": 1000000000}
```

## Step 4: Send Your First Transfer

Save this script as `send.ts`, put your seed phrase in `seed`, and run `node send.ts`. It sends 1 DCC to the address in `recipient`, which can be any Testnet address or alias:

```{literalinclude} ../_samples/quick-start-transfer.ts
:language: typescript
:lines: 2-
```

The output looks like this:

```text
Broadcast, transaction ID: BVVmaKri16PUJJqHbLmDRnzcyc4SdYbr6GQZgDhhFPxx
In block at height 99864
https://testnet.decentralscan.com/transaction?id=BVVmaKri16PUJJqHbLmDRnzcyc4SdYbr6GQZgDhhFPxx
```

The builder sets the minimum fee, 0.001 DCC, so the sender's balance drops by 1.001 DCC. Testnet blocks come about every 30 seconds, so `waitForTx` usually returns within a minute.

If the node rejects the transaction, `broadcast` throws with the node's error. The common ones are `negative dcc balance` (the faucet transfer is not in a block yet, or the balance is too low) and `Wrong chain-id` (the transaction was built for another network). See {ref}`Error Responses <05_node-guide/01_node-rest-api:Error Responses>` for the full list.

## Step 5: Look It Up in the Explorer

Open the link the script printed. DecentralScan shows the transaction's type, sender, recipient, amount, fee and the block it is in. Search for your address to see its balance and every transaction it took part in. {doc}`DecentralScan Guide <03_decentralscan>` explains each page.

## Moving to Mainnet

The same scripts work on Mainnet with three changes:

* Use the Mainnet node, `https://mainnet-node.decentralchain.io`.
* Pass `chainId: '?'`, and derive addresses with `libs.crypto.address(seed, '?')`. Mainnet addresses start with `3D`.
* Fund the account with real DCC, for example from [Decentral.Exchange](https://decentral.exchange/). There is no Mainnet faucet.

A seed phrase is not tied to a network: the same 15 words give a Testnet address and a different Mainnet address. Use a fresh seed for Mainnet rather than one you used in scripts or tests.

## Next Steps

* {doc}`Leasing <04_leasing>`: lease DCC to a generating node and share its rewards.
* {doc}`Sponsorship <05_sponsorship>`: let users pay fees in your token.
* {doc}`How-To Guides <../04_building-apps/03_how-to-guides>`: issue tokens, chain transactions and read chain data.
* {doc}`Wallet Integration <../04_building-apps/04_wallet-integration>`: let users sign in their own wallet instead of handling seed phrases in your code.
