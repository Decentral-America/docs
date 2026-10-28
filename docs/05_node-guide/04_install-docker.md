# Run a Node with Docker

Docker is the recommended way to run a DecentralChain node. The image is built from `docker/Dockerfile` in [node-scala](https://github.com/Decentral-America/node-scala) and runs the node as the unprivileged user `dcc`.

```{note}
Verified on a clean Docker host (macOS 15.5, Docker Desktop 29.2.1, no earlier node images or volumes) against node-scala v1.8.1, 2026-10-27: following [Join the Public Testnet](15_join-testnet), the node synced the public Testnet from genesis to the tip, height 99,976, in 31 minutes, and its block IDs matched the public node.
```

## Which Network You Can Join

| Network | Status |
|---|---|
| Public Testnet | Supported. Follow [Join the Public Testnet](15_join-testnet): it gives the configuration file the node needs. |
| Mainnet | Not with this image yet. The live DCC Mainnet runs an earlier node line (its public node reports `DCC v1.3.5`), and node-scala's built-in Mainnet profile ships no peers until the Mainnet migration. A `mainnet-latest` container starts, but never finds a peer and stays at the genesis block. |

## Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| Docker Engine | 25.x | Latest stable |
| RAM | 4 GB | 8 GB |
| CPU | 2 cores | 4+ cores |
| Disk (SSD) | 1 GB for the Testnet (its data was 131 MB at height 99,976) | 10 GB, to leave room for the chain to grow |
| Network | 100 Mbit/s | 1 Gbit/s |

## Image tags

All images live at `ghcr.io/decentral-america/node-scala`. No image is published on Docker Hub.

| Tag | Meaning |
|---|---|
| `1.8.1`, `1.8.0`, ... | One release. Use a release tag, or a digest, for a node you want to keep stable |
| `testnet-latest`, `mainnet-latest`, `latest` | The newest build. On 2026-10-27 all three were the same v1.8.1 image (`sha256:3b04d066…`): the network a container joins comes from its configuration, not from the tag |
| `sha-<commit>` | A build of one git commit |

## Ports

| Port | Purpose | Exposure |
|---|---|---|
| `6868` | P2P | Open to the internet if other nodes should be able to dial you; outbound only is enough to sync |
| `6869` | REST API | Keep private: bind to localhost, or place behind a reverse proxy |

## The Configuration File Is Required

Mount a configuration file at `/etc/dcc/dcc.conf`. Besides selecting the network, it must set the wallet password (`dcc.wallet.password`, which may be `""`). Without a mounted file the node has no wallet password, can't ask for one, and exits with code 61 (`CANNOT GET CONSOLE TO ASK WALLET PASSWORD` in the log); with `--restart unless-stopped`, Docker then restarts it in a loop. `DCC_WALLET_PASSWORD` doesn't help on its own: the entrypoint applies it only on top of a mounted file. See [Configuration](05_configuration).

## Quick start

Write `dcc.conf` as shown in [Join the Public Testnet](15_join-testnet), then start the node from the same directory:

```bash
docker run -d \
  --name dcc-testnet \
  --restart unless-stopped \
  -p 6868:6868 \
  -p 127.0.0.1:6869:6869 \
  -v "$PWD/dcc.conf:/etc/dcc/dcc.conf:ro" \
  -v dcc-testnet-data:/var/lib/dcc \
  -e DCC_NETWORK=custom \
  -e DCC_HEAP_SIZE=2g \
  -e DCC_REST_API_BIND=0.0.0.0 \
  ghcr.io/decentral-america/node-scala:1.8.1
```

```{important}
Inside the container the REST API binds to `127.0.0.1` by default (`DCC_REST_API_BIND`). Docker cannot forward a published port to a service listening only on the container's loopback interface, so without `DCC_REST_API_BIND=0.0.0.0` the API is unreachable from the host. The example above then publishes the port only on the host's loopback (`-p 127.0.0.1:6869:6869`), which keeps the API off the public internet.
```

Data is stored in the `/var/lib/dcc` volume and logs in `/var/log/dcc`. Keep the data volume between restarts and upgrades: losing it forces a full re-sync.

## Docker Compose

The same node with Docker Compose, with `dcc.conf` next to `compose.yaml`:

```yaml
services:
  dcc-testnet:
    image: ghcr.io/decentral-america/node-scala:1.8.1
    container_name: dcc-testnet
    restart: unless-stopped
    stop_signal: SIGINT
    stop_grace_period: 60s
    ports:
      - "6868:6868"
      - "127.0.0.1:6869:6869"
    environment:
      DCC_NETWORK: custom
      DCC_HEAP_SIZE: 2g
      DCC_LOG_LEVEL: INFO
      DCC_REST_API_BIND: 0.0.0.0
    volumes:
      - ./dcc.conf:/etc/dcc/dcc.conf:ro
      - dcc-testnet-data:/var/lib/dcc
      - dcc-testnet-logs:/var/log/dcc

volumes:
  dcc-testnet-data:
  dcc-testnet-logs:
```

```{note}
To give the node a wallet seed and password without writing them into `dcc.conf`, add `env_file: .env` with `DCC_WALLET_SEED` and `DCC_WALLET_PASSWORD` (and `chmod 600 .env`). The entrypoint layers them on top of the mounted `dcc.conf`; without the mounted file they are ignored.
```

## Verify it is running

```bash
curl -s http://localhost:6869/node/status
curl -s http://localhost:6869/blocks/height
docker inspect --format='{{.State.Health.Status}}' dcc-testnet   # healthy
```

The image's built-in `HEALTHCHECK` polls `/node/status`. On the first start the node replays the chain from genesis; [Join the Public Testnet](15_join-testnet) shows how to check it has reached the tip. See [Configuration](05_configuration) for every environment variable and [Sync and Rollback](06_sync-and-rollback) for what to expect on first start.
