# Installing on Windows

```{note}
Verified against node-scala v1.7.0's `README.md`. Not run on a clean machine as part of this documentation pass — if a step doesn't match what you see, please report it.
```

[Docker](04_install-docker) (via Docker Desktop) is the simplest way to run a node on Windows; this page is for running it directly.

## Prerequisites

* **Java 25 JDK** — install [Eclipse Temurin 25](https://adoptium.net/temurin/releases/?version=25) using its Windows installer.
* A network configuration file — the repository ships defaults for Mainnet and Testnet in `node/src/main/resources/network-defaults.conf`.

## Run from the JAR

With Temurin 25 installed, download a released JAR (see [Release Notes](../08_release-notes) or the [node-scala releases page](https://github.com/Decentral-America/node-scala/releases)), or [build from source](#build-from-source) below, then run it from a terminal (Command Prompt or PowerShell):

```bash
java -jar node/target/dcc-all*.jar path/to/config/decentralchain-{network}.conf
```

node-scala doesn't publish a Windows installer — run it from the JAR, or use Docker Desktop with the [Docker instructions](04_install-docker) if you'd rather not manage the JVM yourself.

## Build from source

```bash
git clone https://github.com/Decentral-America/node-scala.git
cd node-scala

sbt checkPR
sbt packageAll                   # Mainnet
sbt -Dnetwork=testnet packageAll # Testnet
```

Building from source additionally requires [SBT](https://www.scala-sbt.org/1.0/docs/Installing-sbt-on-Windows.html). See the [node-scala README](https://github.com/Decentral-America/node-scala#readme) for integration-test setup and IntelliJ IDEA configuration.

## Next steps

[Configuration](05_configuration) · [Sync and Rollback](06_sync-and-rollback) · [Wallet and Generating](08_wallet-and-generating)
