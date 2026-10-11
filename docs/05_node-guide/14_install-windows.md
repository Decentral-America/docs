# Installing on Windows

```{note}
Verified against node-scala v1.7.0's `README.md`. Not run on a clean machine as part of this documentation pass — if a step doesn't match what you see, please report it.
```

[Docker](04_install-docker) (via Docker Desktop) is the simplest way to run a node on Windows; this page is for running it directly.

## Prerequisites

* **Java 25 JDK** — install [Eclipse Temurin 25](https://adoptium.net/temurin/releases/?version=25) using its Windows installer.
* A network configuration file — the repository ships defaults for Mainnet and Testnet in `node/src/main/resources/network-defaults.conf`.

## Run from the tarball

node-scala releases do not ship a node JAR or a Windows installer (the v1.7.0 release assets are only `dcc-grpc-server` tarballs). The supported way to run a node is Docker Desktop with the [Docker image](04_install-docker) `ghcr.io/decentral-america/node-scala`. To run it directly, [build from source](#build-from-source) below, extract the universal tarball `node/target/universal/decentralchain-<version>.tgz`, and start the node from a terminal (Command Prompt or PowerShell) with the Windows launcher in its `bin\` directory:

```bat
decentralchain-<version>\bin\node.bat path\to\config\dcc.conf
```

There is no single "fat" JAR; the launcher runs the node from the tarball's `lib\` directory.

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
