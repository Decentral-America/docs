# Installing on macOS

```{note}
Verified against node-scala v1.7.0's `README.md`. Not run on a clean machine as part of this documentation pass — if a step doesn't match what you see, please report it.
```

[Docker](04_install-docker) is the simplest way to run a node; this page is for running it directly on macOS.

## Prerequisites

* [Homebrew](https://brew.sh/)
* A network configuration file — the repository ships defaults for Mainnet and Testnet in `node/src/main/resources/network-defaults.conf`.

## Install the JDK

```bash
brew install --cask temurin@25
```

This installs [Eclipse Temurin 25](https://adoptium.net/temurin/releases/?version=25), the JDK version node-scala is built and tested against.

## Run from the JAR

Download a released JAR (see [Release Notes](../08_release-notes) or the [node-scala releases page](https://github.com/Decentral-America/node-scala/releases)), or [build from source](#build-from-source) below, then:

```bash
java -jar node/target/dcc-all*.jar path/to/config/decentralchain-{network}.conf
```

node-scala doesn't publish a macOS package (`.pkg`/Homebrew formula) — run it from the JAR, or use [Docker](04_install-docker) if you'd rather not manage the JVM yourself.

## Build from source

```bash
# JDK, if not already installed
brew install --cask temurin@25

git clone https://github.com/Decentral-America/node-scala.git
cd node-scala

# Compile and run tests
sbt checkPR

# Build packages for one network
sbt packageAll                   # Mainnet
sbt -Dnetwork=testnet packageAll # Testnet
```

Building from source additionally requires [SBT](https://www.scala-sbt.org/1.0/docs/Installing-sbt-on-Mac.html). See the [node-scala README](https://github.com/Decentral-America/node-scala#readme) for integration-test setup.

## Next steps

[Configuration](05_configuration) · [Sync and Rollback](06_sync-and-rollback) · [Wallet and Generating](08_wallet-and-generating)
