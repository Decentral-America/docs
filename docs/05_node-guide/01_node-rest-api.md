# Node REST API

Every DecentralChain node exposes an HTTP REST API, compatible in shape with the Dcc node API it was forked from. It's how wallets, explorers, and SDKs read chain state (balances, blocks, transactions) and broadcast signed transactions, without needing their own indexer.

You normally don't call this API with raw HTTP requests — use [`@decentralchain/node-api`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/node-api), the typed JavaScript/TypeScript client, as shown in [How-To Guides](../04_building-apps/03_how-to-guides). Its namespaces map directly onto the REST API's resource areas:

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

If you're running your own node, point the client at its own host and port instead of a public endpoint like `https://nodes.decentralchain.io` — check your node's configuration file for the REST API port it's bound to.

## Base URL, port and interactive docs

A node listens on port `6869` (`dcc.rest-api.port`) and, by default, only on `127.0.0.1`. The node bundles an OpenAPI description (`openapi.yaml`) and Swagger UI; open the node's API root in a browser to explore every endpoint.

```{note}
Verified against node-scala v1.7.0.
```

## Authentication

Most read-only endpoints are public. Privileged ones — wallet and address management (`GET/POST /addresses`, `GET /wallet/seed`), transaction signing on behalf of the node wallet and fee estimation (`POST /transactions/sign`, `POST /transactions/calculateFee`), `/debug/*`, `/peers/connect`, `/peers/clearblacklist` and `/node/stop` — require an `X-Api-Key` header matching the hash in `dcc.rest-api.api-key-hash`. See [Configuration](05_configuration). Requests with a wrong key get `403`.

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
| `GET /peers/all`, `/peers/connected` | Peer lists |
| `POST /utils/script/compileCode` | Compile Ride source |
| `POST /utils/hash/secure`, `/utils/hash/fast` | Hashing helpers |
| `GET /utils/seed`, `/utils/time` | Random seed, node time |

## Limits

Several endpoints cap result sizes through settings such as `transactions-by-address-limit` (1000), `blocks-request-limit` (100), `asset-details-limit` (100) and `data-keys-request-limit` (1000). Requests above a limit are rejected; page through results instead.

## CORS

`access-control-allow-origin` is empty by default, so browsers on other origins are blocked. Set it to your application's origin rather than echoing every origin.
