% The code on this page is included verbatim from docs/_samples/airdrop.ts,
% which CI typechecks against the pinned SDK versions.

# Airdrop a Token

An airdrop sends a token to a list of addresses. On DecentralChain you send it with {ref}`Mass Transfer transactions <02_decentralchain/03_transaction:Mass Transfer Transaction>`: one transaction pays up to 100 recipients and costs far less than 100 separate transfers.

```{note}
The sample is typechecked against `@decentralchain/transactions@5.0.1`. It has not been broadcast as part of this documentation pass.
```

## Before You Start

You need:

* Node.js 24 or later, with the script saved as an ES module (`"type": "module"` in `package.json`).
* A Testnet account that holds the token, and enough DCC for the fees. To issue a token first, see {ref}`Issuing a Token <04_building-apps/03_how-to-guides:Issuing a Token>`; its ID is the ID of the Issue transaction.
* The list of recipients, as addresses or aliases.

```bash
npm install @decentralchain/transactions@5.0.1
```

## Send the Airdrop

The script splits the recipient list into batches of 100 and sends one Mass Transfer transaction per batch:

```{literalinclude} ../../_samples/airdrop.ts
:language: typescript
:lines: 2-
```

* **`amount`** is in the token's smallest unit. For a token with 2 decimals, `1_000` is 10.00 tokens. Each transfer in the list can have its own amount.
* **`assetId: null`** airdrops DCC instead of a token.
* **`attachment`** is optional: up to 140 bytes, base58-encoded, that every recipient sees on the transaction.
* **The fee** is set by the builder: 0.001 DCC plus 0.0005 DCC per transfer, rounded up to the next 0.001 DCC. A full batch of 100 costs 0.051 DCC. For a {ref}`smart asset <02_decentralchain/02_token(asset):Smart Asset>`, or a sender with an account script, add 0.004 DCC by passing `fee` yourself.

## Check the Results

Each batch is one transaction, so it either reaches every recipient in it or none of them. The script waits for each batch to be in a block before it sends the next, so if it stops part-way, every batch it logged is done and you can restart from the next one.

To check a recipient, read their balance of the token with `node-api-js`, as in {ref}`Reading Blockchain Data <04_building-apps/03_how-to-guides:Reading Blockchain Data>` (`api.assets.fetchBalanceAddressAssetId(address, assetId)`).
