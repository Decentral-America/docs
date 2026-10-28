# Installing on macOS

```{note}
Verified on macOS 15.5 (Intel, x86_64) against node-scala v1.8.1, 2026-10-28, in a clean environment rather than a new machine: an empty home directory, with Temurin 25.0.5 and Homebrew's `sbt` the only JDK and build tool on the `PATH`, `sbt packageAll` built the tarball in 8 minutes. Started with the configuration from [Join the Public Testnet](15_join-testnet), the node synced from genesis to the tip, height 100,688, in 17 minutes, and its block IDs matched the public node's. The JDK came from the Temurin 25 tarball, the same build `brew install --cask temurin@25` installs (the cask needs an administrator password). Not yet verified on Apple silicon.
```

[Docker](04_install-docker) is the simplest way to run a node; this page is for running it directly on macOS.

## Prerequisites

* [Homebrew](https://brew.sh/)
* [SBT](https://www.scala-sbt.org/1.x/docs/Installing-sbt-on-Mac.html), to build the node: `brew install sbt`
* A node configuration file. For the public Testnet, use the one in [Join the Public Testnet](15_join-testnet): the node's built-in `testnet` profile is a different network.

## Install the JDK

```bash
brew install --cask temurin@25
```

This installs [Eclipse Temurin 25](https://adoptium.net/temurin/releases/?version=25), the JDK version node-scala is built and tested against.

## Run from the tarball

node-scala releases do not ship a node JAR or package (the v1.7.0 to v1.8.1 release assets are only `dcc-grpc-server` tarballs), and node-scala doesn't publish a macOS package (`.pkg`/Homebrew formula). The supported way to run a node is the [Docker image](04_install-docker) `ghcr.io/decentral-america/node-scala`. To run it directly on macOS, [build from source](#build-from-source) below, then extract the universal tarball and start the node with its `bin/` launcher:

```bash
tar -xzf node/target/universal/decentralchain-<version>.tgz
decentralchain-<version>/bin/node path/to/config/dcc.conf
```

There is no single "fat" JAR; the launcher runs the node from the tarball's `lib/` directory.

The node keeps its chain data, wallet and logs in `~/Library/Application Support/dcc-custom-21` with the Testnet configuration (`21` is the chain ID `!` in hexadecimal). Stop the node and delete that folder to sync again from scratch.

## Build from source

```bash
# JDK and SBT, if not already installed
brew install --cask temurin@25
brew install sbt

git clone https://github.com/Decentral-America/node-scala.git
cd node-scala

sbt packageAll   # builds the node tarball (and DEB packages)
```

The network comes from the configuration file you start the node with; for the public Testnet, use the one in [Join the Public Testnet](15_join-testnet). To also run the unit tests, run `sbt checkPR` first: it takes over an hour and needs [Node.js](https://nodejs.org/) on the `PATH`.

See the [node-scala README](https://github.com/Decentral-America/node-scala#readme) for integration-test setup.

## Next steps

[Configuration](05_configuration) · [Sync and Rollback](06_sync-and-rollback) · [Wallet and Generating](08_wallet-and-generating)
