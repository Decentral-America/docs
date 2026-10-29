# Installing on Windows

```{note}
Verified on Windows Server 2025 (x64, a GitHub Actions `windows-2025` runner) against node-scala v1.8.1, 2026-10-28: Temurin 25.0.5 from its Windows installer, and the node tarball (built on Ubuntu 24.04, see [Build the tarball](#build-the-tarball)) extracted with Windows' `tar` and started from Command Prompt with the `java` command below and the configuration from [Join the Public Testnet](15_join-testnet). The node synced from genesis to the tip, height 102,325, in 5 minutes, and its block IDs matched the public node's. Two of node-scala's own steps don't work on Windows in v1.8.1: the repository can't be cloned, and the tarball's `bin\node.bat` launcher can't start. This page works around both.
```

[Docker](04_install-docker) (via Docker Desktop) is the simplest way to run a node on Windows; this page is for running it directly.

## Prerequisites

* **Java 25 JDK** — install [Eclipse Temurin 25](https://adoptium.net/temurin/releases/?version=25) using its Windows installer. Its default options put `java` on the `PATH`.
* The node tarball, built on Linux, macOS or in WSL: see [Build the tarball](#build-the-tarball).
* A node configuration file. For the public Testnet, use the one in [Join the Public Testnet](15_join-testnet): the node's built-in `testnet` profile is a different network.

## Run from the tarball

node-scala releases do not ship a node JAR or a Windows installer (the v1.7.0 to v1.8.1 release assets are only `dcc-grpc-server` tarballs). The supported way to run a node is Docker Desktop with the [Docker image](04_install-docker) `ghcr.io/decentral-america/node-scala`. To run it directly, extract the tarball and start the node from Command Prompt:

```bat
tar -xzf decentralchain-<version>.tgz
java -server -Xmx2g -XX:+ExitOnOutOfMemoryError -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:+UseStringDeduplication -Dfile.encoding=UTF-8 --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED -cp "decentralchain-<version>\lib\*" com.decentralchain.Application path\to\config\dcc.conf
```

These are the options in the tarball's `conf\application.ini`, the ones its launcher would pass. Don't use the launcher, `bin\node.bat`: in v1.8.1 it lists every JAR in `lib\` on one line, longer than Command Prompt's 8,191-character limit, and stops with `The input line is too long.` There is no single "fat" JAR; the node runs from the tarball's `lib\` directory.

The node keeps its chain data, wallet and logs in `%LOCALAPPDATA%\dcc-custom-21` with the Testnet configuration (`21` is the chain ID `!` in hexadecimal). Stop the node with Ctrl+C and delete that folder to sync again from scratch.

## Build the tarball

node-scala can't be built on Windows itself in v1.8.1. Its repository holds a file whose name contains `?` (`node/src/main/resources/patches/CancelLeasesToDisabledAliases-?.json`, a patch for the Mainnet, whose chain ID is `?`), and a Windows file name can't contain `?`. `git clone` stops with `error: invalid path` and leaves no files to build.

Build the tarball with the [Linux](12_install-linux) steps instead, on a Linux or macOS machine or in [WSL](https://learn.microsoft.com/windows/wsl/install) on the same PC (clone into your WSL home directory, not onto a Windows drive under `/mnt/`):

```bash
git clone https://github.com/Decentral-America/node-scala.git
cd node-scala

sbt packageAll   # builds the node tarball (and DEB packages)
```

Then copy `node/target/universal/decentralchain-<version>.tgz` to Windows. The tarball holds only JAR files and launchers, so the same file runs on every operating system.

The network comes from the configuration file you start the node with; for the public Testnet, use the one in [Join the Public Testnet](15_join-testnet). To also run the unit tests, run `sbt checkPR` first: it takes over an hour and needs [Node.js](https://nodejs.org/) on the `PATH`. See the [node-scala README](https://github.com/Decentral-America/node-scala#readme) for integration-test setup and IntelliJ IDEA configuration.

## Next steps

[Configuration](05_configuration) · [Sync and Rollback](06_sync-and-rollback) · [Wallet and Generating](08_wallet-and-generating)
