# Client Libraries and SDK

DecentralChain's SDK is developed in one open-source monorepo, [Decentral-America/DecentralChain](https://github.com/Decentral-America/DecentralChain), released under the MIT license. The TypeScript packages are published to npm under the `@decentralchain` scope; the Java SDK is published to Maven Central.

```{note}
Every `npm install` line in these docs pins an exact version that CI installs and imports on Node.js 24 on every pull request (`docs/scripts/check_install_snippets.py`). Several packages have a newer working release on the npm `next` tag than on `latest`; until those are promoted, **install the exact versions shown here**, not a bare package name. All packages are ESM-only and require Node.js 24 or later.
```

```{warning}
`@decentralchain/node-api-grpc` has **no published npm release** yet. See [Node gRPC API](05_node-grpc).
```

## Which package do I need?

| I want to… | Install |
|---|---|
| Build, sign and broadcast transactions | `@decentralchain/transactions@5.0.1` |
| Read chain state from a node (REST) | `@decentralchain/node-api-js@2.0.1` |
| Read chain data over gRPC / subscribe to blockchain updates | not published yet; see [Node gRPC API](05_node-grpc) |
| Let browser users sign with their own wallet | `@decentralchain/signer@2.0.1` + `@decentralchain/cubensis-connect-provider@1.0.1` |
| Sign with a Ledger hardware wallet | `@decentralchain/ledger@5.1.0` |
| Query the data service (asset search, history, DEX data) | `@decentralchain/data-service-client-js@4.2.0`; see [Data Service API](06_data-service-api) |
| Compile Ride to a script | the node's `POST /utils/script/compileCode` endpoint (the `@decentralchain/ride` npm package is not installable yet, see below) |
| Work from Java or the JVM | `io.decentralchain:java-sdk:2.0.1` |

## TypeScript packages

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

## Installing

Install only the layers you need. For a Node.js backend that builds, signs, broadcasts and reads state:

```bash
npm install @decentralchain/transactions@5.0.1 @decentralchain/node-api-js@2.0.1
```

`transactions`' own `broadcast()` is enough to send a signed transaction to a node without `node-api-js` at all — see [How-To Guides](03_how-to-guides).

For a browser dApp, see [Wallet Integration](04_wallet-integration).

## Java SDK

`io.decentralchain:java-sdk` supports node interaction, offline transaction signing, and address and key creation. It requires Java 11 or later (Java 25 recommended, matching the node). The current release on Maven Central is 2.0.1 (`repo1.maven.org/maven2/io/decentralchain/java-sdk/maven-metadata.xml`, checked 2026-10-18).

```xml
<dependency>
  <groupId>io.decentralchain</groupId>
  <artifactId>java-sdk</artifactId>
  <version>2.0.1</version>
</dependency>
```

```java
String seed = Crypto.getRandomSeedPhrase();
PrivateKey privateKey = PrivateKey.fromSeed(seed);
PublicKey publicKey = PublicKey.from(privateKey);
Address address = Address.from(publicKey);
```

## Ride tooling

`@decentralchain/ride` 2.3.1, the only published version, cannot be installed from npm: its `package.json` still declares `workspace:*` dependencies. Until a fixed release is published, compile scripts with any node's REST API:

```bash
curl -s -X POST -H 'Content-Type: text/plain' \
  --data-binary $'{-# STDLIB_VERSION 6 #-}\n{-# CONTENT_TYPE EXPRESSION #-}\n{-# SCRIPT_TYPE ACCOUNT #-}\ntrue' \
  https://testnet-node.decentralchain.io/utils/script/compileCode
```

The response's `script` field is the compiled script in base64. The monorepo also contains the Scala compiler and REPL under `packages/ride`. See the [Ride language reference](../03_ride-language/index).
