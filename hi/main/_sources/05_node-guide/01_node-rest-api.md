# Node REST API

Every DecentralChain node exposes an HTTP REST API, compatible in shape with the Dcc node API it was forked from. It's how wallets, explorers, and SDKs read chain state (balances, blocks, transactions) and broadcast signed transactions, without needing their own indexer.

You normally don't call this API with raw HTTP requests — use [`@decentralchain/node-api-js`](https://github.com/Decentral-America/node-api-js), the typed JavaScript/TypeScript client, as shown in [How-To Guides](../04_building-apps/03_how-to-guides). Its namespaces map directly onto the REST API's resource areas:

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
