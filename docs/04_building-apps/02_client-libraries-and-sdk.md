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
| Compile Ride to a script | the node's `POST /utils/script/compileCode` endpoint; see {ref}`Compile with a Node <04_building-apps/01_developer-tools:Compile with a Node>` |
| Try Ride expressions interactively | `@decentralchain/ride-repl@1.6.2`; see {doc}`Ride REPL <developer-tools/01_ride-repl>` |
| Work from Java or the JVM | `io.decentralchain:java-sdk:2.0.2` |

## SDKs by Language

Each page covers installing the SDK, connecting to the Testnet, and signing and broadcasting a transaction.

* {doc}`TypeScript <sdk/01_typescript>`: the `@decentralchain/*` npm packages, for Node.js backends, scripts and browser dApps. The page lists every package with its tested version.
* {doc}`Java <sdk/02_java>`: `io.decentralchain:java-sdk` on Maven Central, for Java and other JVM languages.

```{toctree}
:hidden:

sdk/01_typescript
sdk/02_java
```
