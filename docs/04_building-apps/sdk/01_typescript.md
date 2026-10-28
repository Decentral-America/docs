% Every `npm install` line and every `import ... from '@decentralchain/...'`
% on this page is installed and imported on Node.js 24 by CI
% (docs/scripts/check_install_snippets.py), docs/scripts/check_sdk_table.py
% installs and imports every version in the package table, and
% docs/_samples/connect-and-broadcast.ts typechecks the example.

# TypeScript SDK

The TypeScript SDK is a set of `@decentralchain/*` npm packages, developed in [`packages/sdk`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk) of the DecentralChain monorepo under the MIT license. Each package covers one layer, so you install only the ones you use. They all run in Node.js and in the browser.

```{note}
All packages are ESM-only and require Node.js 24 or later. Install the **exact versions** shown on this page: CI installs and imports each of them on every pull request. Several packages have a working release on the npm `next` tag that is newer than `latest`.
```

## Install

For a backend or script that builds, signs and broadcasts transactions and reads chain state:

```bash
npm install @decentralchain/transactions@5.0.1 @decentralchain/node-api-js@2.0.1
```

`transactions` builds and signs every transaction type and can broadcast on its own. `node-api-js` is a typed client for the node's REST API. For a browser dApp, where the user signs in their own wallet, install `signer` and `cubensis-connect-provider` instead of handling seed phrases; see {doc}`Wallet Integration <../04_wallet-integration>`.

## Connect to the Testnet

There is no connection to open: every call is an HTTPS request to a node. Point the client at a node URL, and pass the network's chain ID to the transaction builders:

| Network | Node | Chain ID | Addresses start with |
|---|---|---|---|
| Mainnet | `https://mainnet-node.decentralchain.io` | `'?'` | `3D` |
| Testnet | `https://testnet-node.decentralchain.io` | `'!'` | `31` |

```{literalinclude} ../../_samples/connect-and-broadcast.ts
:language: typescript
:lines: 2-11
```

`create(nodeUrl)` returns a client grouped by API area: `addresses`, `assets`, `blocks`, `transactions`, `leasing`, `utils` and more. For the full list of node endpoints, see {doc}`Node REST API <../../05_node-guide/01_node-rest-api>`.

## Sign and Broadcast

```{literalinclude} ../../_samples/connect-and-broadcast.ts
:language: typescript
:lines: 13-
```

* **Builders sign locally.** `transfer()`, `issue()`, `invokeScript()` and the other builders return a signed transaction with its `id`, without contacting a node. The fee defaults to the minimum for a plain account; pass `fee` for a smart account or smart asset.
* **`broadcast()` sends it.** A `200` response only means the node accepted the transaction into its pool. `waitForTx` waits until it is in a block.
* **A rejected transaction throws.** The node returns HTTP 400, and the thrown `Error` carries the node's response in `data`: an error code and a message. Error 112, for example, is a failed state check such as an insufficient balance.

For more complete examples, such as issuing a token, chaining transactions, airdrops and calling dApps, see the {doc}`How-To Guides <../03_how-to-guides>`.

## Packages

The **Install** column is the version these docs are tested against. `latest` and `next` are the npm dist-tags as of 2026-10-18; check `npm view @decentralchain/<package> dist-tags` for the current values. Where `latest` is older than **Install**, the `latest` release is the one that fails to import on Node.js 24 or predates the API shown in these docs.

| npm package | Install | `latest` | `next` | Description |
|---|---|---|---|---|
| `transactions` | 5.0.1 | 5.0.0 (fails to import on Node.js 24) | 5.0.1 | Build and sign (including multi-sign) transactions and broadcast them |
| `node-api-js` | 2.0.1 | 1.2.5-beta.18 | 2.0.1 | Typed client for the node REST API |
| `node-api-grpc` | not published | — | — | gRPC client: accounts, assets, blockchain, blocks, transactions, blockchain updates |
| `data-service-client-js` | 4.2.0 | 4.2.0 | 4.2.1 | Data service client |
| `signer` | 2.0.1 | 1.1.0-beta (fails to import: missing `tslib`) | 2.0.1 | Signing orchestrator that delegates to a provider so keys never reach your app |
| `cubensis-connect-provider` | 1.0.1 | 1.0.0 | 1.0.1 | Provider for the Cubensis Connect browser wallet |
| `cubensis-connect-types` | 1.0.1 | 1.0.0 | 1.0.1 | Type definitions for the Cubensis Connect extension API |
| `ledger` | 5.1.0 | 5.1.0 | 5.1.1 | Ledger Nano S/X integration (WebUSB, Web Bluetooth, Node HID) |
| `ts-lib-crypto` | 2.0.1 | 2.0.0 | 2.0.1 | Key generation, signatures, hashing, encoding and encryption primitives |
| `crypto` | 1.0.2 | 1.0.1 | 1.0.2 | Async WASM crypto: Ed25519/X25519 keys, signing, AES, seed management |
| `marshall` | 1.0.1 | 0.14.0 | 1.0.1 | Convert transactions and orders between JS objects, binary and JSON |
| `bignumber` | 1.2.1 | 1.2.0 | 1.2.1 | Arbitrary-precision numbers for amounts and fees |
| `parse-json-bignumber` | 2.0.1 | 2.0.0 | 2.0.1 | JSON parser that preserves large-number precision |
| `ts-types` | 2.0.1 | 2.0.0 | 2.0.1 | Shared TypeScript type definitions |
| `data-entities` | 3.0.1 | 3.0.0 | 3.0.1 | Domain classes such as assets and money |
| `assets-pairs-order` | 5.0.2 | 4.0.0 | 5.0.2 | Canonical DEX asset-pair ordering |
| `oracle-data` | 1.0.1 | 1.0.0 | 1.0.1 | Parse, encode and validate oracle data |
| `money-like-to-node` | 1.0.1 | 1.0.0 | 1.0.1 | Convert human-readable money objects to node API format |
| `signature-adapter` | 7.0.1 | 6.1.7 | 7.0.1 | Multi-provider transaction signing adapter |
| `browser-bus` | 1.0.1 | 1.0.0 | 1.0.1 | Cross-window messaging for dApps and wallets |
| `protobuf-serialization` | 3.0.0 | 2.0.0 | 3.0.0 | Protocol Buffers schemas and bindings |
| `ride` | not installable | 2.3.1 (published with unresolved `workspace:*` dependencies; `npm install` fails with `EUNSUPPORTEDPROTOCOL`) | 2.3.1 | JavaScript wrapper around the Ride compiler |

## Source

Each package's README in [`packages/sdk`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk) documents its full API. Report bugs in the [monorepo's issue tracker](https://github.com/Decentral-America/DecentralChain/issues).
