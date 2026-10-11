# Logging

```{note}
Verified against node-scala v1.7.0.
```

## Docker

The image writes two streams:

* **Console** — at the level in `DCC_LOG_LEVEL` (default `INFO`). Read it with `docker logs`.
* **Files** — under `/var/log/dcc` (volume), written at `TRACE` level by the entrypoint.

```bash
docker logs -f dcc-node               # follow
docker logs --tail 200 dcc-node       # last 200 lines
```

Levels, from quietest to noisiest: `OFF`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`. Use `INFO` in production; `DEBUG` helps with sync and peer issues but is very verbose.

## Custom logback configuration

Logging is configured with [Logback](https://logback.qos.ch/). Point the JVM at your own file through `JAVA_OPTS`:

```bash
-e JAVA_OPTS="-Dlogback.configurationFile=/etc/dcc/logback.xml"
```

For a JAR install, pass the same `-Dlogback.configurationFile=...` system property to `java`.

## Logs worth watching

* `Fork` and `InvalidBlock` messages — the node is on a different chain or received a bad block.
* Out-of-memory exits — the entrypoint starts the JVM with `ExitOnOutOfMemoryError`, so raise `DCC_HEAP_SIZE`.
