# Wallet Integration

In a browser dApp, never ask a user for their seed phrase or private key. Instead, let the user sign transactions with their own wallet through [Cubensis Connect](https://github.com/Decentral-America/cubensis-connect), DecentralChain's browser extension wallet. There are two ways to integrate it.

## Recommended: Signer + Provider

[`@decentralchain/signer`](https://github.com/Decentral-America/signer) is a transaction-signing orchestrator: your dApp calls Signer, Signer delegates the actual signing to a **Provider**, and the Provider is the only piece that ever touches the user's key material. [`@decentralchain/cubensis-connect-provider`](https://github.com/Decentral-America/cubensis-connect-provider) implements that Provider interface for the Cubensis Connect extension, so your dApp code never sees a seed phrase or private key.

```bash
npm install @decentralchain/signer @decentralchain/cubensis-connect-provider
```

```typescript
import Signer from '@decentralchain/signer';
import { ProviderCubensis } from '@decentralchain/cubensis-connect-provider';

const signer = new Signer({ NODE_URL: 'https://nodes.decentralchain.io' });
signer.setProvider(new ProviderCubensis());

// Prompt the user to connect and authenticate via the Cubensis Connect extension
const user = await signer.login();
console.log('Logged in as:', user.address);

// Build, sign (via the extension) and broadcast a Transfer
const [broadcastedTx] = await signer
  .transfer({
    recipient: '3P4H4E4DYpaMr84SpAfNNWwSZM5RqQNbmgN',
    amount: 100_000_000, // 1 DCC
  })
  .broadcast();

console.log('Transaction ID:', broadcastedTx.id);
```

Because Signer only talks to the `Provider` interface, swapping `ProviderCubensis` for a different provider (e.g. a Ledger provider) later requires no changes to the rest of your dApp code. Signer supports every transaction type except Update Asset Info.

## Direct: the `CubensisConnect` browser API

On any page served over `http`/`https` with the extension installed, a global `CubensisConnect` object is injected into the page. This is what Signer's provider uses internally — you can also call it directly if you don't need Signer's abstraction:

| Method | Description |
|---|---|
| `publicState()` | Current account, network, and balance info, if the site is trusted |
| `auth(data)` | Authenticate the user, returning a signed proof of account ownership |
| `signTransaction(tx)` | Sign a transaction without broadcasting |
| `signAndPublishTransaction(tx)` | Sign and broadcast a transaction |
| `signOrder(order)` / `signAndPublishOrder(order)` | Sign (and optionally broadcast) a DEX order |
| `signCancelOrder(order)` / `signAndPublishCancelOrder(order)` | Sign (and optionally broadcast) an order cancellation |
| `encryptMessage(msg, publicKey)` / `decryptMessage(msg, publicKey)` | Encrypt/decrypt a message for a given public key |
| `on(event, callback)` | Subscribe to wallet events (account/network changes) |

The extension asks the user to explicitly trust a new site the first time it calls any method other than `on`. Until trusted, all other calls reject with `{message: "Api rejected by user", code: 12}`. See the [Cubensis Connect repository](https://github.com/Decentral-America/cubensis-connect#cubensis-connect-api) for the complete method list and response shapes, and [`cubensis-connect-types`](https://github.com/Decentral-America/cubensis-connect-types) for TypeScript definitions.

```typescript
if (window.CubensisConnect) {
  const authData = await window.CubensisConnect.auth({ data: 'My dApp Login' });
  console.log('Authenticated address:', authData.address);
}
```
