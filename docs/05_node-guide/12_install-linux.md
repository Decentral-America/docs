# Installing on Linux

```{note}
Verified against node-scala v1.8.0's `README.md` and `build.sbt`. Not run on a clean machine as part of this documentation pass — if a step doesn't match what you see, please report it.
```

For most operators, [Docker](04_install-docker) is simpler than a bare-metal install. Use this page if you need to run the node directly on the host, for example to package it for your own init system.

## Prerequisites

* **Java 25 JDK** — [Eclipse Temurin 25](https://adoptium.net/temurin/releases/?version=25) is the distribution node-scala recommends and tests against.
* A network configuration file — the repository ships defaults for Mainnet and Testnet in `node/src/main/resources/network-defaults.conf`.

## Install the JDK (Ubuntu/Debian)

```bash
wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | sudo apt-key add -
echo "deb https://packages.adoptium.net/artifactory/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/adoptium.list
sudo apt-get update && sudo apt-get install -y temurin-25-jdk
```

For a distribution without APT, install Eclipse Temurin 25 through your package manager or from the [Adoptium releases page](https://adoptium.net/temurin/releases/?version=25).

## Supported path: Docker

node-scala releases do not ship a node DEB package or JAR — the v1.7.0 release assets are only `dcc-grpc-server` tarballs. The supported way to run a node is the [Docker image](04_install-docker) `ghcr.io/decentral-america/node-scala`. To run the node directly on the host, build it from source as below.

## Build from source

```bash
git clone https://github.com/Decentral-America/node-scala.git
cd node-scala

# Compile and run tests
sbt checkPR

# Build the node tarball and DEB packages for one network
sbt packageAll                   # Mainnet
sbt -Dnetwork=testnet packageAll # Testnet
```

`sbt packageAll` produces:

* the universal tarball `node/target/universal/decentralchain-<version>.tgz` (also copied to `docker/target/dcc.tgz`), and
* DEB packages for `amd64` and `arm64` in `node/target/`. The node package is named `decentralchain` for Mainnet and `decentralchain-<network>` for other networks (for example `decentralchain-testnet`).

There is no single "fat" JAR; the node runs from its `lib/` directory through the launcher script.

Building from source additionally requires [SBT](https://www.scala-sbt.org/1.x/docs/Installing-sbt-on-Linux.html). See the [node-scala README](https://github.com/Decentral-America/node-scala#readme) for integration-test setup and IDE configuration.

## Install the DEB package you built

```bash
sudo dpkg -i node/target/decentralchain_<version>_<arch>.deb           # Mainnet
sudo dpkg -i node/target/decentralchain-testnet_<version>_<arch>.deb   # Testnet
```

Installing the package sets up the node as a system service named after the package; see its post-install scripts for the exact paths on your distribution.

## Run from the tarball

If you'd rather not install a package, extract the tarball and start the node with its `bin/` launcher:

```bash
tar -xzf node/target/universal/decentralchain-<version>.tgz
decentralchain-<version>/bin/node path/to/config/dcc.conf
```

## Next steps

[Configuration](05_configuration) · [Sync and Rollback](06_sync-and-rollback) · [Wallet and Generating](08_wallet-and-generating)
