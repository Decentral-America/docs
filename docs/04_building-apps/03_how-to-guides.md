% Code samples verified directly against the current READMEs of
% @decentralchain/transactions, @decentralchain/node-api and @decentralchain/signer
% (2026-08) — do not copy older samples that reference `nodeInteraction.broadcast`
% from node-api, that function has moved into the `transactions` package itself.

# How-To Guides

Practical examples for the most common tasks when building on DecentralChain. These use the [`transactions`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/transactions) and [`node-api`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/node-api) packages — see [Client Libraries and SDK](02_client-libraries-and-sdk) for the full package list.

Both packages are ESM-only and require Node.js 24+.

## Build, Sign, and Broadcast a Transaction

This example builds a {ref}`Transfer transaction <02_decentralchain/03_transaction:Transfer Transaction>`, signs it with a seed phrase, and broadcasts it. `broadcast()` is exported by `@decentralchain/transactions` itself — you don't need `node-api` just to send a transaction.

```bash
npm install @decentralchain/transactions
```

```typescript
import { transfer, broadcast } from '@decentralchain/transactions';

const seed = 'your secret seed phrase here';

// Build and sign a Transfer transaction
const signedTx = transfer(
  {
    recipient: '3DQAabT4dnFEpVf6jabNisvugEyFCGQZ9MF', // recipient address or alias
    amount: 100_000_000,                               // 1 DCC (8 decimals, i.e. 10^8 Decentralites)
  },
  seed,
);

// Broadcast it
const result = await broadcast(signedTx, 'https://nodes.decentralchain.io');
console.log('Transaction ID:', result.id);
```

A raw seed phrase should only ever be used server-side, or in scripts/tests you control. Never ask a user for their seed phrase in a dApp — see [Wallet Integration](04_wallet-integration) for the browser-safe flow.

Every other {ref}`transaction type <02_decentralchain/03_transaction:Transaction>` has a matching builder exported from `@decentralchain/transactions`: `issue()`, `reissue()`, `burn()`, `lease()`, `cancelLease()`, `massTransfer()`, `data()`, `setScript()`, `setAssetScript()`, `invokeScript()`, `exchange()`.

## Issuing a Token

To issue a new {ref}`token <02_decentralchain/02_token(asset):Token (Asset)>`, use `issue()` the same way:

```typescript
import { issue, broadcast } from '@decentralchain/transactions';

const seed = 'your secret seed phrase here';

const signedTx = issue(
  {
    name: 'MyToken',
    description: 'A token issued on DecentralChain',
    quantity: 1_000_000,
    decimals: 2,
    reissuable: true,
  },
  seed,
);

await broadcast(signedTx, 'https://nodes.decentralchain.io');
```

See {doc}`Token (Asset) <../02_decentralchain/02_token(asset)>` for the full meaning of each issue parameter.

## Reading Blockchain Data

Use `node-api` to query {ref}`account <02_decentralchain/01_account:Account>` balances and other node state without running your own indexer. `create(nodeUrl)` returns a client namespaced by API area (`addresses`, `assets`, `blocks`, `transactions`, `leasing`, and more):

```bash
npm install @decentralchain/node-api
```

```typescript
import { create } from '@decentralchain/node-api';

const api = create('https://nodes.decentralchain.io');

const { balance } = await api.addresses.fetchBalance('3DQAabT4dnFEpVf6jabNisvugEyFCGQZ9MF');
console.log('DCC balance (in Decentralites):', balance);

const { height } = await api.blocks.fetchHeight();
console.log('Current height:', height);
```

For richer historical queries (asset search, DEX order history, aggregated transaction data) use [`data-service-client`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/data-service-client) against the data service API instead of querying a node directly.

## Signing with a Ledger Hardware Wallet

[`@decentralchain/ledger`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/ledger) talks to a Ledger Nano S or X running the DCC application. It derives public keys and signs on the device, so the private key never leaves the hardware. It supports WebUSB, Web Bluetooth and Node HID transports, and you install a Ledger transport package alongside it:

```bash
npm install @decentralchain/ledger @ledgerhq/hw-transport-webusb
```

The package README documents the current `DCCLedger` API for connecting, reading the user's address and signing a transaction; start from its Quick Start.
