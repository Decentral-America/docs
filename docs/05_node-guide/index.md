# Node Guide

A {ref}`node <02_decentralchain/05_node:Node>` is a host connected to the DecentralChain network that validates transactions, stores blocks, and — if it meets the generating-balance requirement — produces new blocks under {ref}`Leased Proof of Stake <02_decentralchain/05_node:Leased Proof of Stake>`. This section covers running your own node: getting the software, building it, and configuring it. For the economics of block generation (rewards, leasing), see the {ref}`Node <02_decentralchain/05_node:Node>` article in the DecentralChain fundamentals section.

```{gallery-grid}
:grid-columns: 1 2 2 3

- header: "Open Source"
  content: "The node is built and maintained in the open at Decentral-America/node-scala."
- header: "JVM-Based"
  content: "Written in Scala, packaged as a runnable JAR or DEB."
- header: "REST API"
  content: "Every node exposes an HTTP API compatible with the Dcc node API shape."
- header: "Mainnet & Testnet"
  content: "The same codebase builds packages for either network."
```

## Getting the Node

The node implementation lives at [Decentral-America/node-scala](https://github.com/Decentral-America/node-scala), forked from Dcc 1.6.x. To run a node from source:

**Prerequisites**
- Java 25 JDK ([Eclipse Temurin 25](https://adoptium.net/temurin/releases/?version=25) is the recommended distribution)
- A network configuration file (network defaults ship in the repo at `node/src/main/resources/network-defaults.conf`)

**Run:**

```bash
java -jar node/target/dcc-all*.jar path/to/config/decentralchain-{network}.conf
```

## Building From Source

```bash
git clone https://github.com/Decentral-America/node-scala.git
cd node-scala

# Compile and run tests
sbt checkPR

# Build a runnable package
sbt packageAll                   # Mainnet
sbt -Dnetwork=testnet packageAll # Testnet

# Install the DEB package (Linux)
sudo dpkg -i node/target/*.deb
```

This requires [SBT](https://www.scala-sbt.org/1.x/docs/Setup.html) in addition to the JDK. See the [node-scala README](https://github.com/Decentral-America/node-scala) for integration test setup and IDE configuration.

## Configuration

Network-specific defaults are defined in [`network-defaults.conf`](https://github.com/Decentral-America/node-scala/blob/main/node/src/main/resources/network-defaults.conf) in the node-scala repository. Pass your own config file (based on the mainnet/testnet template) as the argument to the JAR to override generating-node settings such as the {ref}`block reward vote <02_decentralchain/05_node:Voting>` and wallet seed.

```{toctree}
:caption: Node Guide
:maxdepth: 2

01_node-rest-api
02_node-extensions
03_custom-blockchain
```
