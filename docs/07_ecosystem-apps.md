% Every URL on this page was requested on 2026-10-27 and answered 200, except the
% ones marked as not available. Re-check them when a service moves.

# Ecosystem Apps

Tools and services built around DecentralChain. Each one runs separately per network: Mainnet holds real DCC, the public Testnet holds free test DCC with no value, and an address or transaction on one network doesn't exist on the other.

| App | Mainnet | Testnet |
|---|---|---|
| Decentral.Exchange | [decentral.exchange](https://decentral.exchange/) | [testnet.decentral.exchange](https://testnet.decentral.exchange/) |
| DecentralScan | [decentralscan.com](https://decentralscan.com/) | [testnet.decentralscan.com](https://testnet.decentralscan.com/) |
| Faucet | None | [testnet.decentralscan.com/faucet](https://testnet.decentralscan.com/faucet) |
| Cubensis Connect | Browser extension, both networks | Browser extension, both networks |
| Matcher | Not available yet | `https://testnet-matcher.decentralchain.io` |
| Data Service | `https://data-service.decentralchain.io` | `https://testnet-data-service.decentralchain.io` |
| Public node | `https://mainnet-node.decentralchain.io` | `https://testnet-node.decentralchain.io` |

New here? The {doc}`Quick Start <09_user-guides/01_quick-start>` uses the faucet, a public node and DecentralScan to send a first Testnet transaction.

## Decentral.Exchange

The web wallet and decentralized exchange. In a browser you can create or import an account, see your balances, send and receive DCC and tokens, lease DCC to a node, create aliases and trade token pairs. Your keys stay in your browser, and trades settle on the chain, so the exchange never holds your funds.

* **Mainnet:** [decentral.exchange](https://decentral.exchange/)
* **Testnet:** [testnet.decentral.exchange](https://testnet.decentral.exchange/)
* **Guides:** {doc}`Leasing <09_user-guides/04_leasing>` shows the wallet's leasing screen. Trading needs a matcher, and the public matcher runs on the Testnet only for now.

## DecentralScan

The block explorer. It shows every block, transaction, address and token, the trading pairs on the matcher, and the state of the network and its peers. You don't need an account to use it.

* **Mainnet:** [decentralscan.com](https://decentralscan.com/)
* **Testnet:** [testnet.decentralscan.com](https://testnet.decentralscan.com/)
* **Guide:** {doc}`DecentralScan Guide <09_user-guides/03_decentralscan>`: search, each page, and direct links to transactions and addresses.

## Testnet Faucet

Free Testnet DCC for development and testing: 10 DCC per address, once every 24 hours. Use it with a Testnet address (chain ID `!`, addresses starting with `31`), as described in {ref}`Mainnet, Testnet <02_decentralchain/08_mainnet-testnet-stagenet:Network Parameters>`.

* **Web page:** [testnet.decentralscan.com/faucet](https://testnet.decentralscan.com/faucet)
* **API:** `POST https://testnet.decentralscan.com/api/faucet` with `{"address": "<Testnet address>"}`. It returns the transfer's `txId`, `429` if the address already received DCC in the last 24 hours, and `400` for an address of another network.
* **Guide:** {ref}`Quick Start, Step 3 <09_user-guides/01_quick-start:Step 3: Get Testnet DCC>`.

There is no Mainnet faucet.

## Cubensis Connect

The browser-extension wallet. It keeps your keys encrypted in the extension and lets dApps ask for signatures without ever seeing a seed phrase. It works on Mainnet, Testnet and a custom network you choose. It is not in the browser extension stores yet, so you build it from the [DecentralChain repository](https://github.com/Decentral-America/DecentralChain/tree/main/apps/cubensis-connect).

* **Guide for users:** {doc}`Cubensis Connect User Guide <09_user-guides/02_cubensis-connect>`: install, create an account, switch networks and approve requests.
* **Guide for developers:** {doc}`Wallet Integration <04_building-apps/04_wallet-integration>`: connect a dApp to it.

## Matcher

The order-matching service behind Decentral.Exchange. It takes signed buy and sell orders, matches them and settles each trade on the chain as an Exchange transaction.

* **Mainnet:** not available yet.
* **Testnet:** `https://testnet-matcher.decentralchain.io`, with an OpenAPI reference at [`/api-docs/index.html`](https://testnet-matcher.decentralchain.io/api-docs/index.html).
* **Guide:** {doc}`Matcher API <04_building-apps/12_matcher-api>`: markets, placing and cancelling orders, and order history.

## Data Service

An indexed API over the chain's history: asset search, transaction history by type and DEX candles and trades, which a node's REST API doesn't index.

* **Mainnet:** `https://data-service.decentralchain.io`
* **Testnet:** `https://testnet-data-service.decentralchain.io`
* **Guide:** {doc}`Data Service API <04_building-apps/06_data-service-api>`.

## Public Nodes

Nodes run for anyone to read chain state and broadcast signed transactions. Use them for development and light use; run your own node for production traffic.

* **Mainnet:** `https://mainnet-node.decentralchain.io`
* **Testnet:** `https://testnet-node.decentralchain.io`
* **Guides:** {doc}`Node REST API <05_node-guide/01_node-rest-api>`, and the {doc}`Node Guide <05_node-guide/index>` to run your own.

## Ride Tooling

No browser IDE for Ride is hosted at the moment. To write and test Ride, use the {doc}`Ride REPL <04_building-apps/developer-tools/01_ride-repl>` and a node's compiler endpoints; see {doc}`Developer Tools <04_building-apps/01_developer-tools>`.

Test link (removed in the next commit): [dead](https://eco-205-dead-link.decentralchain.io/).
