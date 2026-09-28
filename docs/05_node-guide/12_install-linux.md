# Installing on Linux

```{note}
Verified against node-scala v1.7.0's `README.md` and `build.sbt`. Not run on a clean machine as part of this documentation pass — if a step doesn't match what you see, please report it.
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

## Install from the DEB package

node-scala publishes DEB packages built with `sbt-native-packager`, for both `amd64` and `arm64`. Get the package for your release (see [Release Notes](../08_release-notes) or the [node-scala releases page](https://github.com/Decentral-America/node-scala/releases)), then:

```bash
sudo dpkg -i dcc-node_<version>_<arch>.deb
```

Installing the package sets up the node as a system service; see its post-install scripts for the exact paths and service name on your distribution.

## Run from the JAR

If you'd rather not install a package, run the node directly:

```bash
java -jar node/target/dcc-all*.jar path/to/config/decentralchain-{network}.conf
```

## Build from source

```bash
git clone https://github.com/Decentral-America/node-scala.git
cd node-scala

# Compile and run tests
sbt checkPR

# Build packages (JAR, DEB, tarball) for one network
sbt packageAll                   # Mainnet
sbt -Dnetwork=testnet packageAll # Testnet

# Install the resulting DEB package
sudo dpkg -i node/target/*.deb
```

Building from source additionally requires [SBT](https://www.scala-sbt.org/1.0/docs/Installing-sbt-on-Linux.html). See the [node-scala README](https://github.com/Decentral-America/node-scala#readme) for integration-test setup and IDE configuration.

## Next steps

[Configuration](05_configuration) · [Sync and Rollback](06_sync-and-rollback) · [Wallet and Generating](08_wallet-and-generating)
