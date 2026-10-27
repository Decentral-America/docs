% The code on this page is included verbatim from docs/_samples/java/, which CI
% compiles against the published java-sdk release (`mvn -q compile`).

# Java SDK

`io.decentralchain:java-sdk` is the SDK for Java and other JVM languages. It connects to a node's REST API, creates keys and addresses, and builds and signs every transaction type offline. It is developed in [`packages/jvm/java-sdk`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/jvm/java-sdk) of the DecentralChain monorepo under the MIT license, and published to Maven Central.

```{note}
Verified on 2026-10-25 against release 2.0.2, the latest on Maven Central (`repo1.maven.org/maven2/io/decentralchain/java-sdk/maven-metadata.xml`). The samples compile with JDK 25, and the account and Testnet samples ran against the public Testnet node. The transfer sample has not been broadcast as part of this documentation pass.
```

## Requirements

The SDK requires **Java 25** or later. The 2.0.x jars are compiled for Java 25 (class file version 69), so an older JVM fails with `UnsupportedClassVersionError`. The package README still says Java 11; that applies to older releases only.

`java-sdk` depends on `io.decentralchain:curve25519`, which is licensed GPL-3.0-only. A program that includes it is subject to the GPL-3.0.

## Install

Maven:

```xml
<dependency>
  <groupId>io.decentralchain</groupId>
  <artifactId>java-sdk</artifactId>
  <version>2.0.2</version>
</dependency>
```

Gradle:

```groovy
implementation 'io.decentralchain:java-sdk:2.0.2'
```

The samples below are a minimal Maven project, kept in `docs/_samples/java` of this documentation's [repository](https://github.com/Decentral-America/docs).

## Create an Account

```{literalinclude} ../../_samples/java/src/main/java/samples/CreateAccount.java
:language: java
:lines: 2-
```

An address encodes the network's chain ID: `ChainId.TESTNET` (`'!'`) gives an address starting with `31`, `ChainId.MAINNET` (`'?'`) one starting with `3D`. `PrivateKey.fromSeed` derives the same key from the same seed phrase as every other DecentralChain wallet and SDK.

## Connect to the Testnet

```{literalinclude} ../../_samples/java/src/main/java/samples/ConnectToTestnet.java
:language: java
:lines: 2-
```

`new Node(...)` takes a `Profile` (`MAINNET`, `TESTNET`, `STAGENET` or `LOCAL` for `http://127.0.0.1:6869`) or a node URL. The constructor makes one request, to read the chain ID from the last block, so it throws if the node can't be reached. Every `Node` method is a REST call that returns typed results: `getHeight()`, `getBalance(address)`, `getAssetBalance(address, assetId)`, `getData(address, key)`, `getTransactionInfo(id)` and more.

## Sign and Broadcast a Transfer

```{literalinclude} ../../_samples/java/src/main/java/samples/SendTransfer.java
:language: java
:lines: 2-
```

* **Set the chain ID on Testnet.** Transaction builders use `DccConfig.chainId()`, which defaults to Mainnet. Call `.chainId(ChainId.TESTNET)` on each builder, or set `DccConfig.chainId(ChainId.TESTNET)` once at startup. The node rejects a transaction built for another network.
* **`getSignedWith(privateKey)` signs offline** and sets the sender. The fee defaults to the transaction type's minimum; use `.fee(...)` or `.extraFee(...)` for a smart account or smart asset.
* **`broadcast` returns once the node accepts the transaction into its pool.** `waitForTransaction(id)` waits until it is in a block, and throws if it doesn't arrive in time.
* **A rejection throws `NodeException`.** `getErrorCode()` is the node's error code and `getMessage()` its explanation, for example error 112 for a failed state check such as an insufficient balance.

Every transaction type has a class with a `builder(...)`: `IssueTransaction`, `MassTransferTransaction`, `DataTransaction`, `SetScriptTransaction`, `InvokeScriptTransaction` and the rest, in the `io.decentralchain.transactions` package.
