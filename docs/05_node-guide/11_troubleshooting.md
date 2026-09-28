# Troubleshooting

```{note}
Verified against node-scala v1.7.0.
```

| Symptom | Likely cause | What to do |
|---|---|---|
| `curl localhost:6869` fails from the host while the container is healthy | REST API bound to the container's loopback | Set `DCC_REST_API_BIND=0.0.0.0` and publish `-p 127.0.0.1:6869:6869` |
| Node stays behind after hours | Still in initial sync, or few peers | Check `/node/status` and `/peers/connected`; open inbound port 6868 (Testnet 6863) |
| No peers | Firewall, wrong network | Confirm `DCC_NETWORK`; add a peer with `POST /peers/connect` |
| Node exits shortly after start | JVM out of memory (`ExitOnOutOfMemoryError`) | Raise `DCC_HEAP_SIZE` |
| Node stops after a network activation | Unsupported feature, auto-shutdown | [Upgrade](07_upgrade) the node |
| `403` from an API call | Missing or wrong `X-Api-Key`, or `api-key-hash` unset | [Configure the API key](05_configuration) |
| Database errors after a crash | Unclean shutdown | Roll back if within depth, otherwise [re-sync](06_sync-and-rollback) |
| Node produces no blocks | Generating balance too low, wallet not loaded, or still syncing | Check `/debug/minerInfo` and [wallet setup](08_wallet-and-generating) |

## Useful checks

```bash
curl -s http://localhost:6869/node/status      # heights, timestamps, generationPeriodLength
curl -s http://localhost:6869/node/version
curl -s http://localhost:6869/peers/connected
curl -s http://localhost:6869/activation/status
```

## Adding a peer at runtime

```bash
curl -X POST http://localhost:6869/peers/connect \
  -H 'X-Api-Key: my-secret-api-key' -H 'Content-Type: application/json' \
  -d '{"host": "<ip>", "port": 6868}'
```

## Reporting an issue

Include the node version, network, `/node/status` output and the relevant log excerpt when opening an issue at [Decentral-America/node-scala](https://github.com/Decentral-America/node-scala).
