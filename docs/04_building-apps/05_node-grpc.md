# Node gRPC API

For services that need to process a large volume of blocks or transactions, the node's gRPC API is faster to consume than the REST API: it returns Protobuf-serialized binary messages instead of JSON, and supports server-streaming for large result sets. See [Node Extensions](../05_node-guide/02_node-extensions) for enabling it on your own node.

```{note}
Verified against `@decentralchain/node-api-grpc` v2.0.0 (monorepo `main`).
```

## Installing

```bash
npm install @decentralchain/node-api-grpc
```

> Requires **Node.js >= 24** and an ESM environment (`"type": "module"`).

## Connecting

```typescript
import { mkDefaultChannel, mkTransactionsApi } from '@decentralchain/node-api-grpc';

const channel = mkDefaultChannel('mainnet-node.decentralchain.io'); // defaults to port 6870
const txApi = mkTransactionsApi(channel);

for await (const tx of txApi.getTransactions({ sender: '3D...' })) {
  console.log(tx);
}
```

`mkDefaultChannel(host, options?)` accepts a bare hostname (defaults to port `6870`), a `host:port` pair, or a full `http(s)://` or `grpc(s)://` URL. Pass Connect transport options (TLS, interceptors, timeouts) as the second argument.

## APIs

| Client factory | Service | Methods |
|---|---|---|
| `mkAccountsApi(channel)` | AccountsApi | `getBalances`, `getScript`, `getActiveLeases`, `getDataEntries`, `resolveAlias` |
| `mkAssetsApi(channel)` | AssetsApi | `getInfo`, `getNFTList` |
| `mkBlockchainApi(channel)` | BlockchainApi | `getActivationStatus`, `getBaseTarget`, `getCumulativeScore` |
| `mkBlocksApi(channel)` | BlocksApi | `getBlock`, `getBlockRange` |
| `mkTransactionsApi(channel)` | TransactionsApi | `getTransactions`, `getTransactionSnapshots`, `getStateChanges`, `getStatuses`, `getUnconfirmed`, `sign`, `broadcast` |

Request and response types are re-exported from [`@decentralchain/protobuf-schemas`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/protobuf-schemas), so importing `@decentralchain/node-api-grpc` alone is enough — no separate import is needed.

## Blockchain Updates

The BlockchainUpdates API streams block-level events (appends, rollbacks, microblocks) in real time — useful for indexers and services that need to react to chain state as it happens, without polling. It runs on a **separate port, 6881**, from the rest of the gRPC API.

```typescript
import { mkDefaultBlockchainUpdatesChannel, mkBlockchainUpdatesApi } from '@decentralchain/node-api-grpc';

const channel = mkDefaultBlockchainUpdatesChannel('mainnet-node.decentralchain.io'); // defaults to port 6881
const updatesApi = mkBlockchainUpdatesApi(channel);

for await (const event of updatesApi.subscribe({ fromHeight: 1 })) {
  console.log(event);
}
```

| Method | Purpose |
|---|---|
| `getBlockUpdate` | Fetch the update for a single height |
| `getBlockUpdatesRange` | Fetch updates for a height range |
| `subscribe` | Server-streaming subscription to new updates as they happen |

See [Node Extensions](../05_node-guide/02_node-extensions) for enabling the gRPC server (and hence BlockchainUpdates) on a node you operate; a public node must expose both ports for this package to reach it.
