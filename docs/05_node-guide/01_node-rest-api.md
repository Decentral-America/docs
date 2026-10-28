# Node REST API

Every DecentralChain node exposes an HTTP REST API, compatible in shape with the Dcc node API it was forked from. It's how wallets, explorers, and SDKs read chain state (balances, blocks, transactions) and broadcast signed transactions, without needing their own indexer.

You normally don't call this API with raw HTTP requests — use [`@decentralchain/node-api-js`](https://www.npmjs.com/package/@decentralchain/node-api-js), the typed JavaScript/TypeScript client (soon to be renamed `node-api` in the monorepo, but install it under its current published name for now — see [Client Libraries and SDK](../04_building-apps/02_client-libraries-and-sdk)), as shown in [How-To Guides](../04_building-apps/03_how-to-guides). Its namespaces map directly onto the REST API's resource areas:

| Namespace | Covers |
|---|---|
| `addresses` | Address info, {ref}`balances <02_decentralchain/01_account:Account Balance>`, on-chain data entries |
| `alias` | {ref}`Alias <02_decentralchain/01_account:Alias>` lookup by address or name |
| `assets` | {ref}`Asset <02_decentralchain/02_token(asset):Token (Asset)>` details, distributions, balances |
| `blocks` | {ref}`Block <02_decentralchain/04_block:Block>` headers, height, sequences |
| `consensus` | Consensus algorithm parameters, generating balance |
| `leasing` | Active leases, {ref}`lease <02_decentralchain/05_node:Leased Proof of Stake>` info |
| `transactions` | Broadcast, transaction info, status, unconfirmed pool |
| `rewards` | {ref}`Block reward <02_decentralchain/05_node:Block Reward>` — current size and voting state |
| `node` | Node status and version |
| `peers` | Connected, known, and blacklisted peers |
| `eth` | Ethereum-compatibility endpoints |
| `activation` | Feature activation status |
| `utils` | Hashing, seed generation, script compilation |

If you're running your own node, point the client at its own host and port instead of a public endpoint like `https://testnet-node.decentralchain.io` — check your node's configuration file for the REST API port it's bound to.

## Base URL, port and interactive docs

A node listens on port `6869` (`dcc.rest-api.port`) and, by default, only on `127.0.0.1`. The node bundles an OpenAPI description (`openapi.yaml`) and Swagger UI; open the node's API root in a browser to explore every endpoint.

```{note}
Verified against node-scala v1.8.1, the version the public Testnet runs, on 2026-10-27.
```

## Authentication

Most read-only endpoints are public. Privileged ones — wallet and address management (`GET/POST /addresses`, `GET /wallet/seed`), transaction signing on behalf of the node wallet (`POST /transactions/sign`), `/debug/*`, `GET /addresses/seq/*` and `GET /utils/seed*` (since v1.8.0), all `/peers/*` endpoints (including the read-only `GET /peers/all`, `/peers/connected`, `/peers/blacklisted` and `/peers/suspended`, plus `/peers/connect` and `/peers/clearblacklist`) and `/node/stop` — require an `X-Api-Key` header matching the hash in `dcc.rest-api.api-key-hash`. See [Configuration](05_configuration). Requests with a wrong key get `403`. Fee estimation (`POST /transactions/calculateFee`) does not need a key.

The public Testnet gateway (`https://testnet-node.decentralchain.io`) deliberately exposes the read-only `GET /peers/*` lists without a key; on your own node they require `X-Api-Key`. The gateway does not route the write endpoints (`POST /peers/connect` returns `404`).

### Set Up an API Key

The node stores only a hash of the key, never the key itself:

1. Choose a long random key, for example with `openssl rand -hex 32` or a password manager.
2. Hash it with your own node's `POST /utils/hash/secure`, which needs no key:

   ```bash
   curl -X POST http://127.0.0.1:6869/utils/hash/secure -H 'Content-Type: text/plain' -d 'my-secret-key'
   ```

   ```json
   {"message": "my-secret-key", "hash": "GVCi432WRgAN3rAVeQ6ra8Kr6YFsdwY6Pxj8XDvUap6f"}
   ```

   Run this against your own node rather than a public one, so the key never leaves your machine.
3. Put the `hash` value in the configuration as `dcc.rest-api.api-key-hash` and restart the node.
4. Send the key itself, not the hash, in the `X-Api-Key` header:

   ```bash
   curl http://127.0.0.1:6869/peers/connected -H 'X-Api-Key: my-secret-key'
   ```

The node compares the hash of the header value with `api-key-hash`. While `api-key-hash` is empty (the default), every protected endpoint answers `403` with error `2`, whatever key is sent. The legacy header name `api_key` is still accepted, but use `X-Api-Key`.

Anyone with the key can sign transactions with the node's wallet and stop the node. Keep the REST API bound to `127.0.0.1`, or put it behind a reverse proxy that blocks the protected paths, before you expose a node to the internet.

## Commonly used endpoints

| Endpoint | Purpose |
|---|---|
| `GET /node/status` | Blockchain height, state height, update time and `generationPeriodLength` |
| `GET /node/version` | Node version |
| `GET /blocks/height`, `/blocks/last` | Current height and last block |
| `GET /blocks/height/finalized`, `/blocks/headers/finalized` | Finalized height and header |
| `GET /addresses/balance/{address}` | Address balance |
| `GET /assets/details` | Asset information |
| `GET /transactions/info/{id}`, `/transactions/status` | Transaction lookup and confirmation status |
| `POST /transactions/broadcast` | Submit a signed transaction |
| `POST /transactions/calculateFee` | Fee estimate for an unsigned transaction |
| `GET /transactions/unconfirmed` | Unconfirmed pool |
| `GET /blockchain/rewards` | Block reward state |
| `GET /activation/status` | [Feature activation](10_features-and-activation) |
| `GET /peers/all`, `/peers/connected` | Peer lists (require `X-Api-Key` on a node) |
| `POST /utils/script/compileCode` | Compile Ride source |
| `POST /utils/hash/secure`, `/utils/hash/fast` | Hashing helpers |
| `GET /utils/time` | Node time |

## Limits

Several endpoints cap result sizes through settings such as `transactions-by-address-limit` (1000), `blocks-request-limit` (100), `asset-details-limit` (100) and `data-keys-request-limit` (1000). A request above a limit is rejected with error `10`, `Too big sequence requested`; page through the results instead.

## Pagination

List endpoints page with a cursor rather than a page number: pass the last item you received as `after` to get the next page.

| Endpoint | Page size limit | Cursor |
|---|---|---|
| `GET /transactions/address/{address}/limit/{limit}` | `transactions-by-address-limit` (1000) | `?after={transaction ID}` |
| `GET /assets/nft/{address}/limit/{limit}` | `transactions-by-address-limit` (1000) | `?after={asset ID}` |
| `GET /assets/{assetId}/distribution/{height}/limit/{limit}` | `distribution-address-limit` (1000) | `?after={address}` |
| `GET /blocks/seq/{from}/{to}`, `/blocks/headers/seq/{from}/{to}` | `blocks-request-limit` (100 blocks) | Next height range |

`/transactions/address` returns the newest transactions first, wrapped in an outer array: `[[tx, tx, ...]]`. To read an address's full history, request a page, then pass the ID of the last transaction in it as `after`, and stop when a page comes back shorter than `limit`:

```bash
curl 'https://testnet-node.decentralchain.io/transactions/address/31VMNVAvVh67dPZ41nMnYZvhoZFW7wwPrmq/limit/100'
curl 'https://testnet-node.decentralchain.io/transactions/address/31VMNVAvVh67dPZ41nMnYZvhoZFW7wwPrmq/limit/100?after=<ID of the last transaction above>'
```

The distribution endpoint returns `{"hasNext": true, "lastItem": "<address>", "items": {"<address>": <balance>, ...}}`: pass `lastItem` as `after` while `hasNext` is `true`. `{height}` must be at most the current height minus one; a later height returns error `199`.

`GET /addresses/data/{address}` has no pages. It returns every data entry of the address unless you filter with `?key=` (repeatable) or `?matches=<regular expression>` (at most 200 characters).

## Error Responses

An error comes back with an HTTP status and a JSON body holding a numeric `error` code and a `message`:

```json
{"error": 102, "message": "invalid address"}
```

Match on `error` rather than on `message`: messages often include details such as the transaction or the balance.

| `error` | HTTP | Meaning |
|---|---|---|
| `0` | 500 | Unknown error |
| `1` | 400 | The JSON body is malformed or misses fields; `validationErrors` lists them |
| `2` | 403 | API key missing or wrong (see {ref}`Authentication <05_node-guide/01_node-rest-api:Authentication>`) |
| `10` | 400 | Too big sequence requested: a limit was exceeded |
| `101` | 400 | Invalid signature |
| `102` | 400 | Invalid address |
| `107` | 400 | The request or transaction is too big |
| `108` | 400 | Invalid public key |
| `111` | 400 | Invalid name, or a negative amount |
| `112` | 400 | Insufficient fee, or the transaction failed a state check such as `negative dcc balance` |
| `113` | 400 | Overflow error |
| `114` | 400 | A transaction to yourself, or a negative fee |
| `115` | 400 | A non-positive amount, or the node wallet has no key for the sender |
| `116` | 400 | The request contains invalid IDs |
| `117` | 400 | Invalid decimals |
| `199` | 400 | Other validation error; the message says what is wrong |
| `301` | 404 | Block does not exist |
| `302` | 404 | Alias does not exist |
| `303` | 400 | The transaction's timestamp is too far from the node's time |
| `304` | 404 | No data for this key |
| `305` | 400 | Ride compilation error |
| `306` | 400 | A script failed while executing (account script, asset script or dApp) |
| `307`, `308` | 400 | The transaction is not allowed by the account's or the asset's script |
| `311` | 404 | Transaction does not exist |
| `312` | 501 | Transaction type not supported |
| `400` | 400 | The transaction is already in the state at the given height |
| `402` | 400 | Account balance errors |
| `403` | 400 | Order validation error |
| `404` | 400 | Wrong chain ID: the transaction was built for another network |
| `405` | 400 | Invalid proofs (too many, or too big) |
| `406` | 404 | Not finalized |
| `4001`, `4002`, `4007` | 400 | Invalid transaction ID, block ID or asset ID |
| `4008`, `4009` | 400 | A required key or asset ID was not given |
| `5031` | 503 | The node did not respond in time; retry later |

A successful `200` from `POST /transactions/broadcast` only means the node accepted the transaction into its pool. Check `GET /transactions/status?id=<id>` (or use `waitForTx` in the SDK) to see when it is in a block.

## CORS

`access-control-allow-origin` is empty by default, so browsers on other origins are blocked. Set it to your application's origin rather than echoing every origin.
