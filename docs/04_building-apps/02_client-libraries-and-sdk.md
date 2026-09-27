# Client Libraries and SDK

DecentralChain's SDK lives in one open-source monorepo, [Decentral-America/DecentralChain](https://github.com/Decentral-America/DecentralChain), released under the MIT license. The TypeScript packages are published to npm under the `@decentralchain` scope; the Java SDK is published to Maven Central.

```{note}
Package names and versions verified against the monorepo `main` branch. All TypeScript packages are ESM-only and require Node.js 24 or later.
```

## Which package do I need?

| I want to… | Use |
|---|---|
| Build, sign and broadcast transactions | [`@decentralchain/transactions`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/transactions) |
| Read chain state from a node (REST) | [`@decentralchain/node-api`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/node-api) |
| Read chain data over gRPC / subscribe to blockchain updates | [`@decentralchain/node-api-grpc`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/node-api-grpc) — see [Node gRPC API](05_node-grpc) |
| Let browser users sign with their own wallet | [`@decentralchain/signer`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/signer) + [`@decentralchain/cubensis-connect-provider`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/cubensis-connect-provider) |
| Sign with a Ledger hardware wallet | [`@decentralchain/ledger`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/ledger) |
| Query the data service (asset search, history, DEX data) | [`@decentralchain/data-service-client`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/sdk/data-service-client) — see [Data Service API](06_data-service-api) |
| Compile or decompile Ride | [`@decentralchain/ride`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/ride/ts) |
| Work from Java or the JVM | [`io.decentralchain:java-sdk`](https://central.sonatype.com/artifact/io.decentralchain/java-sdk) |

## TypeScript packages

| Package | Description |
|---|---|
| `transactions` | Build and sign (including multi-sign) transactions and broadcast them |
| `node-api` | Typed client for the node REST API |
| `node-api-grpc` | gRPC client: accounts, assets, blockchain, blocks, transactions, blockchain updates |
| `data-service-client` | Data service client |
| `signer` | Signing orchestrator that delegates to a provider so keys never reach your app |
| `cubensis-connect-provider` | Provider for the Cubensis Connect browser wallet |
| `cubensis-connect-types` | Type definitions for the Cubensis Connect extension API |
| `ledger` | Ledger Nano S/X integration (WebUSB, Web Bluetooth, Node HID) |
| `ts-lib-crypto` | Key generation, signatures, hashing, encoding and encryption primitives |
| `crypto` | Async WASM crypto: Ed25519/X25519 keys, signing, AES, seed management |
| `marshall` | Convert transactions and orders between JS objects, binary and JSON |
| `bignumber` | Arbitrary-precision numbers for amounts and fees |
| `parse-json-bignumber` | JSON parser that preserves large-number precision |
| `types` | Shared type definitions |
| `data-entities` | Domain classes such as assets and money |
| `assets-pairs-order` | Canonical DEX asset-pair ordering |
| `oracle-data` | Parse, encode and validate oracle data |
| `money-like-to-node` | Convert human-readable money objects to node API format |
| `signature-adapter` | Multi-provider transaction signing adapter |
| `browser-bus` | Cross-window messaging for dApps and wallets |
| `protobuf-schemas` | Protocol Buffers schemas and bindings |
| `@decentralchain/ride` | JavaScript wrapper around the Ride compiler |

## Installing

Install only the layers you need. For a Node.js backend that builds, signs and reads state:

```bash
npm install @decentralchain/transactions @decentralchain/node-api
```

For a browser dApp, see [Wallet Integration](04_wallet-integration). For code samples see [How-To Guides](03_how-to-guides).

## Java SDK

`io.decentralchain:java-sdk` supports node interaction, offline transaction signing, and address and key creation. It requires Java 11 or later (Java 25 recommended, matching the node).

```xml
<dependency>
  <groupId>io.decentralchain</groupId>
  <artifactId>java-sdk</artifactId>
  <version>LATEST</version> <!-- use the current release from Maven Central -->
</dependency>
```


```java
String seed = Crypto.getRandomSeedPhrase();
PrivateKey privateKey = PrivateKey.fromSeed(seed);
PublicKey publicKey = PublicKey.from(privateKey);
Address address = Address.from(publicKey);
```

## Ride tooling

`@decentralchain/ride` compiles, decompiles and inspects Ride scripts from JavaScript, and the monorepo also contains the underlying Scala compiler and REPL under `packages/ride`. See the [Ride language reference](../03_ride-language/index).
