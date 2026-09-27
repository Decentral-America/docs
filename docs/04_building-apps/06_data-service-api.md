# Data Service API

For historical or aggregated queries — asset search, DEX exchange history, paginated transaction lists — a data service is faster than replaying a node's transaction history yourself. [`@decentralchain/data-service-client`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/data-service-client) is the official TypeScript client for it.

```{note}
Verified against `@decentralchain/data-service-client` v5.0.0 (monorepo `main`).
```

```{important}
The package does not hardcode a production data-service URL — `rootUrl` is a required constructor option, and the matcher address is likewise supplied by the caller for DEX queries. This page does not state a specific production `rootUrl` or matcher address, since neither is published in the SDK or node-scala source; confirm the current values with whoever operates your target network's data service and matcher before using the examples below.
```

## Installing

```bash
npm install @decentralchain/data-service-client
```

> Requires **Node.js >= 24** and an ESM environment (`"type": "module"`).

## Connecting

```typescript
import { DataServiceClient } from '@decentralchain/data-service-client';

const client = new DataServiceClient({
  rootUrl: 'https://<your-data-service-host>/v0',
});
```

| Option | Required | Purpose |
|---|---|---|
| `rootUrl` | Yes | Base URL of the data service API |
| `fetch` | No | Custom `fetch` implementation |
| `parse` | No | Custom JSON parser |
| `transform` | No | Custom response transformer |

## Methods

| Method | Purpose |
|---|---|
| `getAssets(...ids)` | Fetch one or more assets by ID |
| `getAssetsByTicker(ticker)` | Fetch assets by ticker symbol (`'*'` for all) |
| `getCandles(amountAsset, priceAsset, opts)` | OHLCV candles for a trading pair |
| `getPairs(matcherAddress)` | Returns a function to fetch pair data for a given matcher |
| `getExchangeTxs(opts?)` | Exchange (DEX trade) transactions, by ID or filtered/paginated |
| `getTransferTxs(opts?)` | Transfer transactions |
| `getMassTransferTxs(opts?)` | Mass transfer transactions |
| `aliases.getById(id)` / `getByIdList(ids)` / `getByAddress(address, opts?)` | Alias lookups |

All methods return `Promise<{ data: T; fetchMore?: (count: number) => Promise }>` — call `fetchMore` to page through a result set without re-specifying filters.

## Example: exchange history for a pair

```typescript
const { data: candles } = await client.getCandles(amountAssetId, priceAssetId, {
  timeStart: '2026-01-01',
  timeEnd: '2026-12-31',
  interval: '1d',
  matcher: matcherAddress,
});

const result = await client.getExchangeTxs({ limit: 10, sort: 'desc' });
console.log(result.data);
if (result.fetchMore) {
  const next = await result.fetchMore(10);
}
```

## Matcher address

Several methods (`getPairs`, `getCandles`) take a matcher address as a parameter rather than assuming a single network-wide matcher — DecentralChain's DEX matcher is operated as its own service, and its base URL and address are not published in node-scala or the SDK source. Obtain the current matcher address and API base URL from its operator before building against it.
