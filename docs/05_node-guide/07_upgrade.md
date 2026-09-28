# Upgrade a Node

```{note}
Verified against node-scala v1.7.0.
```

Upgrading replaces the software, not the data: keep the data volume and configuration.

## Docker

1. Record the current height: `curl -s http://localhost:6869/blocks/height`
2. Pull the new image, and note its digest so you can pin it:

   ```bash
   docker pull ghcr.io/decentral-america/node-scala:mainnet-latest
   docker inspect --format='{{.RepoDigests}}' ghcr.io/decentral-america/node-scala:mainnet-latest
   ```

3. Stop the node gracefully. The image uses `STOPSIGNAL SIGINT` to trigger a clean JVM shutdown; give it time to flush and close the database:

   ```bash
   docker stop --time 60 dcc-node && docker rm dcc-node
   ```

4. Start a new container with the same volume, environment and ports as before (see [Run a Node with Docker](04_install-docker)).
5. Confirm the height continues from where it stopped.

## Reverting an upgrade

If the new version fails to start, stop it and start the previous image using its pinned `sha-<commit>` tag against the same volume. Only if the state itself is corrupted should you fall back to a [full re-sync](06_sync-and-rollback).

## From a JAR

Stop the process with a normal `SIGINT`/`SIGTERM` (not `kill -9`), replace the JAR with the new release, and start it again with the same configuration file.

## Network upgrades

New protocol behaviour is switched on by [feature activation](10_features-and-activation), not by upgrading alone. A node that does not support an activated feature stops following the chain, so upgrade before an announced activation height.
