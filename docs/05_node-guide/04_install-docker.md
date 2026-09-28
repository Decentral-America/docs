# Run a Node with Docker

Docker is the recommended way to run a DecentralChain node. The image is built from `docker/Dockerfile` in [node-scala](https://github.com/Decentral-America/node-scala) and runs the node as the unprivileged user `dcc`.

```{note}
Verified against node-scala v1.7.0.
```

## Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| Docker Engine | 25.x | Latest stable |
| RAM | 4 GB | 8 GB |
| CPU | 2 cores | 4+ cores |
| Disk (Mainnet, SSD) | 200 GB | 500 GB |
| Network | 100 Mbit/s | 1 Gbit/s |

## Image tags

| Tag | Meaning |
|---|---|
| `mainnet-latest` | Latest build for Mainnet |
| `testnet-latest` | Latest build for Testnet |
| `sha-<commit>` | A build pinned to one git commit — use this for reproducible deployments and rollbacks |

All images live at `ghcr.io/decentral-america/node-scala`. Confirmed live: `ghcr.io/v2/decentral-america/node-scala/tags/list` returns `mainnet-latest`, `testnet-latest`, `stagenet-latest`, `1.7.0` and per-commit `sha-*` tags. No image is published under any Docker Hub name tried (`decentral-america/node-scala`, `decentralamerica/*`, `decentralchain/*`).

## Ports

| Port | Purpose | Exposure |
|---|---|---|
| `6868` | P2P, Mainnet (Testnet uses `6863`) | Open to the internet so peers can reach you |
| `6869` | REST API | Keep private: bind to localhost, or place behind a reverse proxy |

## Quick start

```bash
docker run -d \
  --name dcc-node \
  --restart unless-stopped \
  -p 6868:6868 \
  -p 127.0.0.1:6869:6869 \
  -v dcc-data:/var/lib/dcc \
  -e DCC_NETWORK=mainnet \
  -e DCC_HEAP_SIZE=4g \
  -e DCC_REST_API_BIND=0.0.0.0 \
  ghcr.io/decentral-america/node-scala:mainnet-latest
```

```{important}
Inside the container the REST API binds to `127.0.0.1` by default (`DCC_REST_API_BIND`). Docker cannot forward a published port to a service listening only on the container's loopback interface, so without `DCC_REST_API_BIND=0.0.0.0` the API is unreachable from the host. The example above then publishes the port only on the host's loopback (`-p 127.0.0.1:6869:6869`), which keeps the API off the public internet.
```

Data is stored in the `/var/lib/dcc` volume and logs in `/var/log/dcc`. Keep the data volume between restarts and upgrades — losing it forces a full re-sync.

## Docker Compose

```yaml
services:
  dcc-node:
    image: ghcr.io/decentral-america/node-scala:mainnet-latest
    container_name: dcc-node
    restart: unless-stopped
    stop_signal: SIGINT
    stop_grace_period: 60s
    ports:
      - "6868:6868"
      - "127.0.0.1:6869:6869"
    environment:
      DCC_NETWORK: mainnet
      DCC_HEAP_SIZE: 4g
      DCC_LOG_LEVEL: INFO
      DCC_REST_API_BIND: 0.0.0.0
    env_file: .env          # DCC_WALLET_SEED, DCC_WALLET_PASSWORD (chmod 600)
    volumes:
      - dcc-data:/var/lib/dcc
      - dcc-logs:/var/log/dcc

volumes:
  dcc-data:
  dcc-logs:
```

## Verify it is running

```bash
curl -s http://localhost:6869/node/status
docker inspect --format='{{.State.Health.Status}}' dcc-node   # healthy
```

The image's built-in `HEALTHCHECK` polls `/node/status`. See [Configuration](05_configuration) for every environment variable and [Sync and Rollback](06_sync-and-rollback) for what to expect on first start.
