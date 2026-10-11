# Sync, Import, Export and Rollback

```{note}
Verified against node-scala v1.7.0.
```

## Initial sync

A new node downloads and validates the whole chain from its peers. This takes hours to days depending on hardware and network. Track progress with:

```bash
curl -s http://localhost:6869/node/status
curl -s http://localhost:6869/blocks/height
```

The node is fully synced when `stateHeight` equals `blockchainHeight` in `/node/status` and `/blocks/height` is within a few blocks of a public peer's height. If a node stalls after syncing, restart it and check the [logs](09_logging) for fork or invalid-block messages.

## Exporting blocks

The node ships an exporter that writes the blocks (and optionally state snapshots) of a stopped node to files:

| Option | Meaning |
|---|---|
| `-c`, `--config` | Node config file |
| `-o`, `--output-prefix` | Blocks output file name prefix |
| `-s`, `--snapshot-output-prefix` | Snapshots output file name prefix |
| `-h`, `--height` | Export up to this height (must be > 0) |

## Importing blocks

The importer loads blocks from a file (or URL, or stdin with `-`) into an empty or partially synced database, which is much faster than downloading from peers:

| Option | Meaning |
|---|---|
| `-c`, `--config` | Node config file |
| `-i`, `--input-file` | Blockchain data file — **required** |
| `-s`, `--snapshots-file` | Snapshots data file |
| `-h`, `--height` | Import up to this height (must be > 0) |
| `-n`, `--no-verify` | Skip signature verification — only for files you trust |
| `-q`, `--max-queue-size` | Size of the block queue (must be > 0) |

Import stops with an error if a block is not a child of the last stored block, so always import into a node that is stopped and whose database matches the file's starting point.

## Rolling back

Rollback removes the most recent blocks. It is limited by `dcc.db.max-rollback-depth` (2000 blocks by default) and requires the API key:

```bash
curl -X POST http://localhost:6869/debug/rollback \
  -H 'X-Api-Key: my-secret-api-key' \
  -H 'Content-Type: application/json' \
  -d '{"rollbackTo": 1234567, "returnTransactionsToUtx": true}'
```

With `returnTransactionsToUtx` set to `true`, transactions from the removed blocks go back to the unconfirmed pool. A successful call returns the `BlockId` of the new tip.

## Full re-sync

If the database is corrupted or you need to go deeper than the rollback depth, delete the data volume and let the node re-sync from genesis:

```{warning}
This destroys all local chain state. Never stop a node with `docker kill` or `SIGKILL` — an unclean shutdown can corrupt the database. Use `docker stop --time 60`.
```

```bash
docker stop --time 60 dcc-node && docker rm dcc-node
docker volume rm dcc-data
# then start the node again as in "Run a Node with Docker"
```
