# Node gRPC API

For services that need to process a large volume of blocks or transactions, the node's gRPC API is faster to consume than the REST API: it returns Protobuf-serialized binary messages instead of JSON, and supports server-streaming for large result sets.

```{important}
**There is no public gRPC endpoint.** The public nodes `mainnet-node.decentralchain.io` and `testnet-node.decentralchain.io` expose only the REST API over HTTPS; the gRPC ports (`6870`, `6877`) and the BlockchainUpdates port (`6881`) are not reachable from the internet (checked 2026-10-18). To use gRPC, run your own node with the gRPC extension enabled (see [Node Extensions](../05_node-guide/02_node-extensions)) and connect to it. For the Testnet, see [Join the Public Testnet](../05_node-guide/15_join-testnet).
```

```{warning}
The TypeScript client `@decentralchain/node-api-grpc` is **not published to npm** yet (`npm view @decentralchain/node-api-grpc` returns `E404`, checked 2026-10-18). This page describes the API in its source (monorepo `packages/sdk/node-api-grpc`, v2.0.0) so you can see what it will offer. The examples below do not run until it is published.
```

## Installing (once published)

% snippet-check: skip
```bash
npm install @decentralchain/node-api-grpc
```

> Requires **Node.js >= 24** and an ESM environment (`"type": "module"`).

## Connecting

Point the client at a node you run yourself. `localhost` below is that node.

% snippet-check: skip
```typescript
import { mkDefaultChannel, mkTransactionsApi } from '@decentralchain/node-api-grpc';

const channel = mkDefaultChannel('localhost'); // defaults to port 6870
const txApi = mkTransactionsApi(channel);

for await (const tx of txApi.getTransactions({ sender: '31...' })) {
  console.log(tx);
}
```

`mkDefaultChannel(host, options?)` accepts a bare hostname (defaults to port `6870`), a `host:port` pair, or a full `http(s)://` or `grpc(s)://` URL. Pass Connect transport options (TLS, interceptors, timeouts) as the second argument. If your node's `dcc.grpc.port` is not `6870` (the public Testnet's own nodes use `6877`), pass `host:port`.

## APIs

| Client factory | Service | Methods |
|---|---|---|
| `mkAccountsApi(channel)` | AccountsApi | `getBalances`, `getScript`, `getActiveLeases`, `getDataEntries`, `resolveAlias` |
| `mkAssetsApi(channel)` | AssetsApi | `getInfo`, `getNFTList` |
| `mkBlockchainApi(channel)` | BlockchainApi | `getActivationStatus`, `getBaseTarget`, `getCumulativeScore` |
| `mkBlocksApi(channel)` | BlocksApi | `getBlock`, `getBlockRange` |
| `mkTransactionsApi(channel)` | TransactionsApi | `getTransactions`, `getTransactionSnapshots`, `getStateChanges`, `getStatuses`, `getUnconfirmed`, `sign`, `broadcast` |

Request and response types are re-exported from the protobuf schema package (published today as `@decentralchain/protobuf-serialization`; the monorepo is renaming it to `protobuf-schemas`), so importing `@decentralchain/node-api-grpc` alone is enough.

## Blockchain Updates

The BlockchainUpdates API streams block-level events (appends, rollbacks, microblocks) in real time — useful for indexers and services that need to react to chain state as it happens, without polling. It runs on a **separate port, 6881**, from the rest of the gRPC API.

% snippet-check: skip
```typescript
import { mkDefaultBlockchainUpdatesChannel, mkBlockchainUpdatesApi } from '@decentralchain/node-api-grpc';

const channel = mkDefaultBlockchainUpdatesChannel('localhost'); // defaults to port 6881
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

See [Node Extensions](../05_node-guide/02_node-extensions) for enabling the gRPC server (and hence BlockchainUpdates) on a node you operate.
