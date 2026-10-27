% The code on this page is included verbatim from docs/_samples/payments.ts,
% which CI typechecks against the pinned SDK versions.

# Accept Payments

To accept a payment in DCC or a token, a shop gives the customer an amount and a payment reference, the customer sends a {ref}`Transfer transaction <02_decentralchain/03_transaction:Transfer Transaction>` with that reference in its attachment, and the shop watches its own address for a matching transfer. No smart contract is involved.

```{note}
The sample is typechecked against `@decentralchain/transactions@5.0.1` and `@decentralchain/node-api-js@2.0.1`. It has not been broadcast as part of this documentation pass.
```

## Before You Start

You need Node.js 24 or later, a Testnet address for the shop and a funded Testnet account for the customer (see the [faucet](https://testnet.decentralscan.com/faucet)).

```bash
npm install @decentralchain/transactions@5.0.1 @decentralchain/node-api-js@2.0.1
```

## Pay an Invoice

In a real shop the customer signs in their own wallet, for example with {doc}`Cubensis Connect <../04_wallet-integration>`, and your page only fills in the recipient, the amount and the attachment. The sample signs with a seed phrase so that both sides fit in one script:

```{literalinclude} ../../_samples/payments.ts
:language: typescript
:lines: 2-21
```

The attachment carries the invoice ID as base58-encoded UTF-8 bytes, up to 140 bytes. It is public, like the rest of the transaction, so put a reference in it, never personal data.

## Check for Payment

The shop reads its latest transactions and looks for a transfer that matches the invoice:

```{literalinclude} ../../_samples/payments.ts
:language: typescript
:lines: 23-
```

What to check:

* **The type, recipient and token.** `type === 4` is a Transfer transaction. `assetId === null` means DCC; for a token payment, compare it with the token's ID.
* **The amount.** Amounts are integers in the smallest unit: 1 DCC is 100,000,000 Decentralites.
* **The attachment.** `fetchTransactions` returns it base58-encoded, so decode it before you compare.

`fetchTransactions(address, limit)` returns only transactions that are already in a block, newest first. A shop with more traffic pages back with its `after` argument (the ID of the last transaction already read), or keeps its own record of the transactions it has seen. To know a payment is in a block before you ship, rather than just accepted into a node's pool, wait for it with `waitForTx`, or with `waitForTxWithNConfirmations` to also wait for a number of blocks on top.
