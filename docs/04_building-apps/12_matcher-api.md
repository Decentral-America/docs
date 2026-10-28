% Endpoints from the matcher's routes (Decentral-America/matcher,
% dex/src/main/scala/com/decentralchain/dex/api/http/routes) at c7e1f3b05, the
% commit the Testnet matcher reports as its version. The samples,
% docs/_samples/matcher-order.ts and matcher-history.ts, were run against the
% Testnet matcher on 2026-10-27.

# Matcher API

The matcher is the order-matching service behind Decentral.Exchange. You send it signed orders; it keeps the order books, matches a buy against a sell, and settles each match on the chain as an {ref}`Exchange transaction <02_decentralchain/03_transaction:Exchange Transaction>`. It never holds your funds: they stay in your account until a trade settles, and the matcher only reserves the amount your open orders need. For the structure of an order, see {ref}`Order <02_decentralchain/06_order:Order>`.

| Network | Matcher | Public key |
|---|---|---|
| Testnet | `https://testnet-matcher.decentralchain.io` | `BEtB5b2kX8Yge4sb5RRbTUqd5Va8Ah8PhphowcW31z6Y` |
| Mainnet | No public matcher yet | |

The matcher serves its own OpenAPI reference at [`/api-docs/index.html`](https://testnet-matcher.decentralchain.io/api-docs/index.html). This page covers the endpoints a trading app or bot needs.

## Matcher Settings

| Endpoint | Returns |
|---|---|
| `GET /matcher` | The matcher's public key, as a JSON string. Every order names it. |
| `GET /matcher/settings` | `matcherPublicKey`, `networkByte`, accepted `orderVersions`, `orderFee` and the fee `rates` |
| `GET /matcher/settings/rates` | How much of each asset pays a fee worth 1 DCC, for example `{"DCC": 1}` |

The Testnet matcher accepts order versions 1, 2 and 3 and charges a fee of 0.003 DCC per order (`"orderFee": {"dynamic": {"baseFee": 300000}}`). The fee is taken in proportion to how much of the order fills.

## Markets and Order Books

| Endpoint | Returns |
|---|---|
| `GET /matcher/orderbook` | Every market: amount and price asset, their names and decimals, and the `tickSize` |
| `GET /matcher/orderbook/{amountAsset}/{priceAsset}` | The order book: `bids` and `asks` as `amount`/`price` levels. `?depth=N` limits the levels. |
| `GET /matcher/orderbook/{amountAsset}/{priceAsset}/status` | The last trade's price, amount and side |
| `GET /matcher/orderbook/{amountAsset}/{priceAsset}/info` | The pair's matching rules (`tickSize`) |

Assets are given by ID, with `DCC` for DCC. A pair has a fixed order: on the Testnet, `DCCCANARY/DCC` is `Hs5y6vFumpwVp6my7rVEmJEQQD3wiQ29qJhnixNqPit5/DCC`. The reversed pair is not a market.

## Prices and Amounts

`amount` is always in the amount asset's smallest unit. `price` is how much of the price asset one whole amount-asset unit costs, and for order versions 1 to 3 it is scaled by 10^(8 + price asset decimals − amount asset decimals). For DCCCANARY/DCC, both with 8 decimals, the factor is 10^8: a price of 0.001 DCC is `100000`. For a token with 2 decimals priced in DCC, the factor is 10^14.

## Place and Cancel an Order

`POST /matcher/orderbook` takes a signed limit order; `POST /matcher/orderbook/market` takes a market order. `@decentralchain/transactions` builds and signs orders with `order()`, sends them with `submitOrder()`, and cancels them with `cancelOrder()` and `cancelSubmittedOrder()`:

```bash
npm install @decentralchain/transactions@5.0.1
```

```{literalinclude} ../_samples/matcher-order.ts
:language: typescript
:lines: 2-
```

Run on the Testnet, the matcher answered `OrderAccepted`, the status was `Accepted`, and the cancel answered `OrderCanceled`. An order's `expiration` can be at most 30 days after its `timestamp`; `order()` sets 29 days by default.

The matcher checks an order before it accepts it: the signature, the matcher public key, the pair, the version, the fee, the price against the tick size, and that the account's tradable balance covers the order and the fee.

## Order Status

`GET /matcher/orderbook/{amountAsset}/{priceAsset}/{orderId}` is public:

```json
{"status": "Cancelled", "filledAmount": 0, "filledFee": 0}
```

| Status | Meaning |
|---|---|
| `Accepted` | In the order book, nothing filled yet |
| `PartiallyFilled` | Part of it has traded; the rest is still in the book |
| `Filled` | Fully traded |
| `Cancelled` | Cancelled by its owner, or by the matcher (expired, or the balance no longer covers it) |
| `NotFound` | The matcher doesn't know the order |

`GET /matcher/transactions/{orderId}` lists the Exchange transactions that filled an order.

## Requests Signed with Your Key

Your order history and reserved balance are private. These endpoints need two headers: `Timestamp`, the current time in milliseconds, and `Signature`, the base58 signature of your public key's bytes followed by the timestamp as an 8-byte big-endian number.

| Endpoint | Returns |
|---|---|
| `GET /matcher/orderbook/{publicKey}` | Your orders in every pair. `?activeOnly=true` or `?closedOnly=true` filters them. |
| `GET /matcher/orderbook/{amountAsset}/{priceAsset}/publicKey/{publicKey}` | Your orders in one pair |
| `GET /matcher/balance/reserved/{publicKey}` | What your open orders reserve, per asset |

```{literalinclude} ../_samples/matcher-history.ts
:language: typescript
:lines: 2-
```

A wrong signature returns `400` with `"status": "InvalidSignature"`.

To cancel every open order at once, `POST /matcher/orderbook/cancel` takes `{"sender": <public key>, "timestamp": <ms>, "signature": <signature of the public key bytes and the big-endian timestamp>}`.

`GET /matcher/orderbook/{amountAsset}/{priceAsset}/tradableBalance/{address}` is public: it returns how much of each asset of the pair the address can still put into new orders.

## Errors

A rejected request returns a JSON object with `"success": false`, a `status`, a numeric `error` code and a `message`, for example:

```json
{"success": false, "status": "InvalidSignature", "error": 1051904, "message": "The request has an invalid signature"}
```

Endpoints under `/matcher/debug`, `GET /matcher/orders/{address}`, the fee-rate updates and order book deletion are for the matcher's operator: they need the operator's `X-Api-Key`.
