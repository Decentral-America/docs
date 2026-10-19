% Every `npm install` line and every `import ... from '@decentralchain/...'`
% on this page is installed and imported on Node.js 24 by CI
% (docs/scripts/check_install_snippets.py), and docs/_samples/*.ts typecheck
% the full examples against the same pinned versions.

# How-To Guides

Practical examples for the most common tasks when building on DecentralChain. These use the [`transactions`](https://www.npmjs.com/package/@decentralchain/transactions) and [`node-api-js`](https://www.npmjs.com/package/@decentralchain/node-api-js) packages — see [Client Libraries and SDK](02_client-libraries-and-sdk) for the full package list and the exact version of each to install.

Both packages are ESM-only and require Node.js 24+.

All examples on this page target the public Testnet: node `https://testnet-node.decentralchain.io`, chain ID `!` (passed as `chainId: '!'` to the transaction builders) and Testnet addresses starting with `31`. For Mainnet, use a Mainnet node and `chainId: '?'`.

## Build, Sign, and Broadcast a Transaction

This example builds a {ref}`Transfer transaction <02_decentralchain/03_transaction:Transfer Transaction>`, signs it with a seed phrase, and broadcasts it. `broadcast()` is exported by `@decentralchain/transactions` itself — you don't need `node-api` just to send a transaction.

```bash
npm install @decentralchain/transactions@5.0.1
```

```typescript
import { transfer, broadcast } from '@decentralchain/transactions';

const seed = 'your secret seed phrase here';

// Build and sign a Transfer transaction
const signedTx = transfer(
  {
    recipient: '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9', // recipient address or alias (Testnet)
    amount: 100_000_000,                               // 1 DCC (8 decimals, i.e. 10^8 Decentralites)
    chainId: '!',                                      // Testnet chain ID
  },
  seed,
);

// Broadcast it
const result = await broadcast(signedTx, 'https://testnet-node.decentralchain.io');
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
    chainId: '!', // Testnet chain ID
  },
  seed,
);

await broadcast(signedTx, 'https://testnet-node.decentralchain.io');
```

See {doc}`Token (Asset) <../02_decentralchain/02_token(asset)>` for the full meaning of each issue parameter.

## Sending a Transaction That Depends on Another

A node checks each new transaction against the state of the chain's blocks (including the current microblock), **not** against other transactions still waiting in its unconfirmed pool. If transaction B spends funds that transaction A delivers, broadcast B only after A is in a block. Broadcasting B while A is still unconfirmed fails with HTTP 400 and a `negative dcc balance` (or `negative asset balance`) error. A `200` response to A's broadcast only means the node accepted A into its pool. It does not mean A is in a block yet.

`waitForTx` from `@decentralchain/transactions` polls the node until the transaction is in a block (on the Testnet this usually takes 1 to 4 seconds):

```typescript
import { transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const funderSeed = 'funder secret seed phrase here';
const newAccountSeed = 'new account secret seed phrase here';
const newAccountAddress = libs.crypto.address(newAccountSeed, '!');

// Parent: fund a new, empty account
const parent = transfer(
  { recipient: newAccountAddress, amount: 200_000_000, chainId: '!' },
  funderSeed,
);
await broadcast(parent, nodeUrl);

// Wait until the parent is in a block before spending what it delivered
await waitForTx(parent.id, { apiBase: nodeUrl, timeout: 120_000 });

// Child: spends the funds the parent delivered
const child = transfer(
  { recipient: '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9', amount: 100_000_000, chainId: '!' },
  newAccountSeed,
);
await broadcast(child, nodeUrl);
```

## Reading Blockchain Data

Use `node-api-js` to query {ref}`account <02_decentralchain/01_account:Account>` balances and other node state without running your own indexer. `create(nodeUrl)` returns a client namespaced by API area (`addresses`, `assets`, `blocks`, `transactions`, `leasing`, and more):

```bash
npm install @decentralchain/node-api-js@2.0.1
```

```typescript
import { create } from '@decentralchain/node-api-js';

const api = create('https://testnet-node.decentralchain.io');

const { balance } = await api.addresses.fetchBalance('31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9');
console.log('DCC balance (in Decentralites):', balance);

const { height } = await api.blocks.fetchHeight();
console.log('Current height:', height);
```

```{note}
The monorepo is renaming this package to `@decentralchain/node-api`, but that name isn't published yet — install `node-api-js` (above) until it is.
```

For richer historical queries (asset search, DEX order history, aggregated transaction data) use [`data-service-client-js`](https://www.npmjs.com/package/@decentralchain/data-service-client-js) against the data service API instead of querying a node directly — see [Data Service API](06_data-service-api).

## Signing with a Ledger Hardware Wallet

[`@decentralchain/ledger`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/ledger) talks to a Ledger Nano S or X running the DCC application. It derives public keys and signs on the device, so the private key never leaves the hardware. It supports WebUSB, Web Bluetooth and Node HID transports, and you install a Ledger transport package alongside it:

```bash
npm install @decentralchain/ledger@5.1.0 @ledgerhq/hw-transport-webusb@6.35.0
```

The package README documents the current `DCCLedger` API for connecting, reading the user's address and signing a transaction; start from its Quick Start.
