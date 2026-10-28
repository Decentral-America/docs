# Data Service API

For historical or aggregated queries — asset search, DEX exchange history, paginated transaction lists — a data service is faster than replaying a node's transaction history yourself. [`@decentralchain/data-service-client-js`](https://www.npmjs.com/package/@decentralchain/data-service-client-js) is the official TypeScript client for it.

```{note}
Verified against `@decentralchain/data-service-client-js` 4.2.0 on npm (installed and imported on Node.js 24 by the docs CI). The monorepo is renaming the package to `data-service-client`; that name is not published yet.
```

## Public endpoints

The package has no built-in URL: pass `rootUrl` for the network you use. For DEX queries, pass the address of that network's matcher.

| | Testnet | Mainnet |
|---|---|---|
| Data service `rootUrl` | `https://testnet-data-service.decentralchain.io/v0` | `https://data-service.decentralchain.io/v0` |
| Matcher API | `https://testnet-matcher.decentralchain.io/matcher` | no public Mainnet matcher yet |
| Matcher public key | `BEtB5b2kX8Yge4sb5RRbTUqd5Va8Ah8PhphowcW31z6Y` | — |
| Matcher address | `31VMNVAvVh67dPZ41nMnYZvhoZFW7wwPrmq` | — |

You can confirm the Testnet matcher's key at any time: `curl -s https://testnet-matcher.decentralchain.io/matcher` returns it as a JSON string.

## Installing

```bash
npm install @decentralchain/data-service-client-js@4.2.0
```

> Requires **Node.js >= 24** and an ESM environment (`"type": "module"`). Note the **default export** — this package doesn't use a named `{ DataServiceClient }` import.

## Connecting

```typescript
import DataServiceClient from '@decentralchain/data-service-client-js';

const client = new DataServiceClient({
  rootUrl: 'https://testnet-data-service.decentralchain.io/v0',
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

```{literalinclude} ../_samples/data-service-candles.ts
:language: typescript
:lines: 2-
```

```{warning}
`getCandles()` in `data-service-client-js` 4.2.0, the published release, throws `Invalid maxHeight: null` when any interval in the range has no trades: the data service returns those intervals with `null` prices and volumes, and the client rejects them. The example reads the candles endpoint (`GET /candles/{amountAsset}/{priceAsset}`) directly instead. The fix, which returns empty intervals as `null`, is in the monorepo but not yet published to npm.
```

## Matcher address

Several methods (`getPairs`, `getCandles`) take a matcher address as a parameter rather than assuming a single network-wide matcher. Use the Testnet matcher address `31VMNVAvVh67dPZ41nMnYZvhoZFW7wwPrmq` from [Public endpoints](#public-endpoints).
