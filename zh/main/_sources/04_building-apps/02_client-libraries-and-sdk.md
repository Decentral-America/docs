# Client Libraries and SDK

The [`Decentral-America`](https://github.com/Decentral-America) GitHub organization publishes an open-source SDK and tooling ecosystem for building on DecentralChain. All official packages are written in TypeScript and released under the MIT license.

| Package | Description |
|---|---|
| [`transactions`](https://github.com/Decentral-America/transactions) | Build and sign (including multi-sign) all 16 transaction types |
| [`node-api-js`](https://github.com/Decentral-America/node-api-js) | Full Node REST API JavaScript client library |
| [`data-service-client-js`](https://github.com/Decentral-America/data-service-client-js) | HTTP client for the DecentralChain data service API — asset search, transaction history, DEX data |
| [`signer`](https://github.com/Decentral-America/signer) | Wallet connection and transaction signing orchestrator for web apps |
| [`cubensis-connect-provider`](https://github.com/Decentral-America/cubensis-connect-provider) | Cubensis Connect wallet provider implementation, used together with `signer` |
| [`cubensis-connect-types`](https://github.com/Decentral-America/cubensis-connect-types) | TypeScript type definitions for Cubensis Connect |
| [`ts-lib-crypto`](https://github.com/Decentral-America/ts-lib-crypto) | Cryptographic primitives — key generation, signing, hashing, base58/base64 encoding |
| [`ts-types`](https://github.com/Decentral-America/ts-types) | Shared TypeScript type definitions for the SDK |
| [`data-entities`](https://github.com/Decentral-America/data-entities) | Domain model classes: Asset, Money, OrderPrice |
| [`oracle-data`](https://github.com/Decentral-America/oracle-data) | Oracle data parsing and encoding utilities |
| [`protobuf-serialization`](https://github.com/Decentral-America/protobuf-serialization) | Protocol Buffer serialization for transactions |
| [`ledger`](https://github.com/Decentral-America/ledger) | Ledger hardware wallet JavaScript interface |
| [`marshall`](https://github.com/Decentral-America/marshall) | Binary serialization/deserialization for DecentralChain data structures |
| [`java-sdk`](https://github.com/Decentral-America/java-sdk) | Java client library |

## Installing

Install only the packages you need for the layer you're working at. For example, to build, sign, and broadcast transactions from a Node.js backend:

```bash
npm install @decentralchain/transactions @decentralchain/node-api-js
```

To build a browser dApp that lets users sign with their own wallet instead of a raw seed, see [Wallet Integration](04_wallet-integration).

For usage examples, see [How-To Guides](03_how-to-guides).
