# Client Libraries and SDK

DecentralChain's SDK is developed in one open-source monorepo, [Decentral-America/DecentralChain](https://github.com/Decentral-America/DecentralChain), released under the MIT license. The TypeScript packages are published to npm under the `@decentralchain` scope; the Java SDK is published to Maven Central.

```{note}
Publication status and published names/versions checked directly against the npm registry (2026-09-28), by installing each package and reading its actual exports — not assumed from a README. The monorepo's `main` branch is ahead of what's released: several packages are being renamed there (dropping a `-js`/`-serialization` suffix, or splitting `ts-types` into `types`) and a few are new. **This page follows what `npm install` actually fetches today**, not the in-progress monorepo names, and calls out the rename explicitly wherever one is pending. All packages are ESM-only and require Node.js 24 or later.
```

```{warning}
`@decentralchain/node-api-grpc` is the only package with **no published npm release at all** yet — genuinely new, not a rename. Everything else below has something installable today, even where the monorepo is mid-rename.
```

## Which package do I need?

| I want to… | Use (current npm name) |
|---|---|
| Build, sign and broadcast transactions | [`@decentralchain/transactions`](https://www.npmjs.com/package/@decentralchain/transactions) |
| Read chain state from a node (REST) | [`@decentralchain/node-api-js`](https://www.npmjs.com/package/@decentralchain/node-api-js) — being renamed to `node-api` in the monorepo; that name isn't published yet |
| Read chain data over gRPC / subscribe to blockchain updates | `@decentralchain/node-api-grpc` — ⚠️ not on npm at all yet; see [Node gRPC API](05_node-grpc) |
| Let browser users sign with their own wallet | [`@decentralchain/signer`](https://www.npmjs.com/package/@decentralchain/signer) + [`@decentralchain/cubensis-connect-provider`](https://www.npmjs.com/package/@decentralchain/cubensis-connect-provider) |
| Sign with a Ledger hardware wallet | [`@decentralchain/ledger`](https://www.npmjs.com/package/@decentralchain/ledger) |
| Query the data service (asset search, history, DEX data) | [`@decentralchain/data-service-client-js`](https://www.npmjs.com/package/@decentralchain/data-service-client-js) — being renamed to `data-service-client`; see [Data Service API](06_data-service-api) |
| Compile or decompile Ride | [`@decentralchain/ride`](https://www.npmjs.com/package/@decentralchain/ride) |
| Work from Java or the JVM | [`io.decentralchain:java-sdk`](https://central.sonatype.com/artifact/io.decentralchain/java-sdk) |

## TypeScript packages

Versions are each package's `latest` tag on npm, not the monorepo's (ahead-of-release) version — check `npm view @decentralchain/<package> version` before pinning one, this table will drift.

| npm package (install this) | Version | Monorepo name, if renamed | Description |
|---|---|---|---|
| `transactions` | 5.0.0 | — | Build and sign (including multi-sign) transactions and broadcast them |
| `node-api-js` | 2.0.0 | `node-api` | Typed client for the node REST API |
| `node-api-grpc` | ❌ not published | — | gRPC client: accounts, assets, blockchain, blocks, transactions, blockchain updates |
| `data-service-client-js` | 4.2.0 | `data-service-client` | Data service client |
| `signer` | 1.1.0-beta | — | Signing orchestrator that delegates to a provider so keys never reach your app |
| `cubensis-connect-provider` | 1.0.0 | — | Provider for the Cubensis Connect browser wallet |
| `cubensis-connect-types` | 1.0.0 | — | Type definitions for the Cubensis Connect extension API |
| `ledger` | 5.1.0 | — | Ledger Nano S/X integration (WebUSB, Web Bluetooth, Node HID) |
| `ts-lib-crypto` | 2.0.0 | — | Key generation, signatures, hashing, encoding and encryption primitives |
| `crypto` | 1.0.1 | — | Async WASM crypto: Ed25519/X25519 keys, signing, AES, seed management |
| `marshall` | 0.14.0 | — | Convert transactions and orders between JS objects, binary and JSON |
| `bignumber` | 1.2.0 | — | Arbitrary-precision numbers for amounts and fees |
| `parse-json-bignumber` | 2.0.0 | — | JSON parser that preserves large-number precision |
| `ts-types` | 2.0.0 | `types` | Shared TypeScript type definitions |
| `data-entities` | 3.0.0 | — | Domain classes such as assets and money |
| `assets-pairs-order` | 4.0.0 | — | Canonical DEX asset-pair ordering |
| `oracle-data` | 1.0.0 | — | Parse, encode and validate oracle data |
| `money-like-to-node` | 1.0.0 | — | Convert human-readable money objects to node API format |
| `signature-adapter` | 6.1.7 | — | Multi-provider transaction signing adapter |
| `browser-bus` | 1.0.0 | — | Cross-window messaging for dApps and wallets |
| `protobuf-serialization` | 2.0.0 | `protobuf-schemas` | Protocol Buffers schemas and bindings |
| `ride` | 2.3.1 | — | JavaScript wrapper around the Ride compiler |

## Installing

Install only the layers you need. For a Node.js backend that builds, signs, broadcasts and reads state:

```bash
npm install @decentralchain/transactions @decentralchain/node-api-js
```

`transactions`' own `broadcast()` is enough to send a signed transaction to a node without `node-api-js` at all — see [How-To Guides](03_how-to-guides).

For a browser dApp, see [Wallet Integration](04_wallet-integration).

## Java SDK

`io.decentralchain:java-sdk` supports node interaction, offline transaction signing, and address and key creation. It requires Java 11 or later (Java 25 recommended, matching the node). Confirmed published at Maven Central (`repo1.maven.org/maven2/io/decentralchain/java-sdk/`), version 2.0.1 as of this check.

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
