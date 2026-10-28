# Installing on Linux

```{note}
Verified on a clean Ubuntu 24.04 (the `ubuntu:24.04` image, plus `sudo`, `curl` and `git`) against node-scala v1.8.1, 2026-10-27: Temurin 25.0.5, SBT from its APT repository, `sbt packageAll` in 12 minutes, then the tarball synced the public Testnet from genesis to the tip, height 100,132, in 22 minutes, with block IDs matching the public node. The DEB package did not install (see below).
```

For most operators, [Docker](04_install-docker) is simpler than a bare-metal install. Use this page if you need to run the node directly on the host, for example to package it for your own init system.

## Prerequisites

* **Java 25 JDK**: [Eclipse Temurin 25](https://adoptium.net/temurin/releases/?version=25) is the distribution node-scala recommends and tests against.
* **[SBT](https://www.scala-sbt.org/1.x/docs/Installing-sbt-on-Linux.html)** and **Git**, to build the node: node-scala releases ship no node package (the v1.7.0 to v1.8.1 release assets are only `dcc-grpc-server` tarballs).
* **A configuration file** for the network. For the public Testnet, use the one in [Join the Public Testnet](15_join-testnet); the node's built-in `testnet` profile is a different network.
* About 4 GB of free memory and 10 GB of disk for the build; the Testnet data itself was 131 MB at height 99,976.

## Install the JDK (Ubuntu/Debian)

```bash
sudo apt-get update && sudo apt-get install -y wget gpg
wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null
echo "deb https://packages.adoptium.net/artifactory/deb $(. /etc/os-release && echo "$VERSION_CODENAME") main" | sudo tee /etc/apt/sources.list.d/adoptium.list
sudo apt-get update && sudo apt-get install -y temurin-25-jdk
java -version   # openjdk version "25.0.x" ... Temurin
```

This adds Adoptium's signing key as a keyring file. Older instructions pipe it into `apt-key add`, which Ubuntu 24.04 still accepts but reports as deprecated on every `apt-get update`.

For a distribution without APT, install Eclipse Temurin 25 through your package manager or from the [Adoptium releases page](https://adoptium.net/temurin/releases/?version=25).

## Install SBT (Ubuntu/Debian)

These are the commands from the [SBT installation page](https://www.scala-sbt.org/1.x/docs/Installing-sbt-on-Linux.html):

```bash
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo -H gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/scalasbt-release.gpg --import
sudo chmod 644 /etc/apt/trusted.gpg.d/scalasbt-release.gpg
sudo apt-get update && sudo apt-get install -y sbt
```

## Build from source

```bash
git clone https://github.com/Decentral-America/node-scala.git
cd node-scala
git checkout v1.8.1     # the release the public Testnet runs; omit to build main

sbt packageAll          # 12 minutes with 12 cores and 8 GB, including the first download of the dependencies
```

`sbt packageAll` produces:

* the universal tarball `node/target/universal/decentralchain-<version>.tgz` (also copied to `docker/target/dcc.tgz`), and
* DEB packages for `amd64` and `arm64` in `node/target/`. The node package is named `decentralchain` for Mainnet and `decentralchain-<network>` for other networks (for example `decentralchain-testnet`).

`sbt -Dnetwork=testnet packageAll` builds packages whose defaults are the built-in `testnet` profile, not the public Testnet. To join the public Testnet, any build works: the configuration file selects the chain.

There is no single "fat" JAR; the node runs from its `lib/` directory through the launcher script.

To also run the unit tests, run `sbt checkPR` before `packageAll`. It took 81 minutes on the same machine and needs [Node.js](https://nodejs.org/) on the `PATH` as well, for the JavaScript build of the Ride compiler. See the [node-scala README](https://github.com/Decentral-America/node-scala#readme) for integration tests and IDE setup.

## Run from the tarball

Extract the tarball and start the node with its `bin/node` launcher and your configuration file:

```bash
tar -xzf node/target/universal/decentralchain-<version>.tgz
decentralchain-<version>/bin/node path/to/dcc.conf
```

Unless the configuration sets `dcc.directory`, the node keeps its data under `~/.local/share/dcc-<network>`: `~/.local/share/dcc-custom-21` for the public Testnet. To check that it follows the chain, compare its height and block IDs with the public node, as shown in [Join the Public Testnet](15_join-testnet).

## Install the DEB package you built

```{warning}
The v1.8.1 DEB package doesn't install: its post-install script copies `/usr/share/decentralchain/doc/dcc.conf.sample`, but the package ships `decentralchain.conf.sample`, so `dpkg -i` stops with `post-installation script subprocess returned error exit status 1` before it installs the systemd service. Until the package is fixed, run the node from the tarball as above.
```

```bash
sudo dpkg -i node/target/decentralchain_<version>_<arch>.deb           # Mainnet
sudo dpkg -i node/target/decentralchain-testnet_<version>_<arch>.deb   # Testnet
```

Once installed, the package runs the node as a systemd service named after the package (`decentralchain`), as the unprivileged user of the same name, and creates its configuration file at `/etc/decentralchain/dcc.conf` from the sample.

## Next steps

[Configuration](05_configuration) · [Sync and Rollback](06_sync-and-rollback) · [Wallet and Generating](08_wallet-and-generating)
