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

The node implementation lives at [Decentral-America/node-scala](https://github.com/Decentral-America/node-scala), forked from Dcc 1.6.x. [Docker](04_install-docker) is the simplest way to run it; to install directly, see [Linux](12_install-linux), [macOS](13_install-macos) or [Windows](14_install-windows). All are written in Scala, built with SBT, and packaged from the same source for either network:

```bash
sbt packageAll                   # Mainnet
sbt -Dnetwork=testnet packageAll # Testnet
```

## Configuration

Network-specific defaults are defined in [`network-defaults.conf`](https://github.com/Decentral-America/node-scala/blob/main/node/src/main/resources/network-defaults.conf) in the node-scala repository. Pass your own config file (based on the mainnet/testnet template) as the argument to the JAR to override generating-node settings such as the {ref}`block reward vote <02_decentralchain/05_node:Voting>` and wallet seed.

```{toctree}
:caption: Node Guide
:maxdepth: 2

01_node-rest-api
02_node-extensions
03_custom-blockchain
04_install-docker
05_configuration
06_sync-and-rollback
07_upgrade
08_wallet-and-generating
09_logging
10_features-and-activation
11_troubleshooting
12_install-linux
13_install-macos
14_install-windows
```
