# Configuration

A node reads a [HOCON](https://github.com/lightbend/config/blob/master/HOCON.md) configuration file whose settings live under the `dcc` key. Built-in defaults (`application.conf` and `network-defaults.conf`) are merged with your file, so your file only needs the settings you want to change.

```{note}
Verified against node-scala v1.7.0. Do not use the shipped `application.conf` as your own config file; it is a defaults file.
```

## Environment variables (Docker)

The Docker entrypoint translates these variables into JVM options:

| Variable | Default | Effect |
|---|---|---|
| `DCC_NETWORK` | `mainnet` | Sets `dcc.defaults.blockchain.type` — the network the node joins |
| `DCC_HEAP_SIZE` | `2g` | JVM `-Xmx` |
| `DCC_LOG_LEVEL` | `INFO` | Console log level: `OFF`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE` |
| `DCC_REST_API_BIND` | `127.0.0.1` | Sets `dcc.rest-api.bind-address` |
| `DCC_WALLET_SEED` | — | Base58 wallet seed, written to a private temporary config file at start-up and then unset |
| `DCC_WALLET_PASSWORD` | — | Wallet file password, handled the same way |
| `JAVA_OPTS` | — | Extra JVM options |

To use your own file, mount it at `/etc/dcc/dcc.conf`. The entrypoint loads it automatically and layers wallet secrets on top.

## Ports and network defaults

| Network | P2P port | Minimum connections |
|---|---|---|
| Mainnet | 6868 | 5 |
| Testnet | 6863 | 5 |

The REST API listens on port `6869` on every network. Known peers for each network ship in `network-defaults.conf`.

## Commonly changed settings

| Key | Default | Description |
|---|---|---|
| `dcc.directory` | `""` | Base directory for node data |
| `dcc.db.max-rollback-depth` | `2000` | Maximum number of blocks a rollback can undo |
| `dcc.db.store-transactions-by-address` | `true` | Index transactions by address (needed by address history endpoints) |
| `dcc.wallet.file` | `<directory>/wallet/wallet.dat` | Wallet file path |
| `dcc.wallet.password` | unset | Wallet file password |
| `dcc.wallet.seed` | unset | Base58 seed; if unset the node generates one |
| `dcc.rest-api.enable` | `yes` | Turn the REST API on or off |
| `dcc.rest-api.bind-address` | `127.0.0.1` | Interface the API listens on |
| `dcc.rest-api.port` | `6869` | API port |
| `dcc.rest-api.api-key-hash` | `""` | Hash of the API key that protects privileged endpoints |
| `dcc.rest-api.cors-headers.access-control-allow-origin` | `""` | Set to a specific origin in production |
| `dcc.rest-api.transactions-by-address-limit` | `1000` | Max results for address transaction history |
| `dcc.rest-api.blocks-request-limit` | `100` | Max blocks per range request |
| `dcc.utx.max-size` | `100000` | Max unconfirmed transactions held |
| `dcc.network.max-inbound-connections` | `100` | Inbound peer limit |
| `dcc.network.max-outbound-connections` | `100` | Outbound peer limit |
| `dcc.hotstuff.enabled` | `false` | Experimental fast-finality engine — leave off (see [Features and Activation](10_features-and-activation)) |

## API key

Privileged endpoints (wallet, rollback, `/debug/*`, `/node/stop`) require an `X-Api-Key` header. The node stores only a hash of the key. Generate the hash with the node itself:

```bash
curl -X POST http://localhost:6869/utils/hash/secure \
  -H 'Content-Type: text/plain' -d 'my-secret-api-key'
```

Put the `hash` value from the JSON response in `dcc.rest-api.api-key-hash`, restart, and send `my-secret-api-key` in `X-Api-Key`.

## Example: minimal Mainnet file

```text
dcc {
  directory = "/var/lib/dcc"
  rest-api {
    bind-address = "127.0.0.1"
    api-key-hash = "<hash from /utils/hash/secure>"
  }
  wallet {
    password = "change-me"
  }
}
```
