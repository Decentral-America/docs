# Join the Public Testnet

This page shows how to run your own node on the public DecentralChain Testnet, the network behind `testnet-node.decentralchain.io`. Your node follows the chain and serves its own REST API (and gRPC, if you enable it). It does not forge blocks.

```{important}
The public Testnet is a **custom chain** (`dcc.blockchain.type = CUSTOM`). The node's built-in `testnet` profile (`DCC_NETWORK=testnet` with no config file) is a different network and **will not join it**. Use the configuration file below.
```

```{note}
Every value on this page was checked against the live Testnet on 2026-10-18. The configuration mirrors the Testnet operators' own node configuration (`node-config/testnet/dcc.conf` in the [infra repository](https://github.com/Decentral-America/infra)). If the two ever disagree, the infra file is authoritative.
```

## Network facts

| Item | Value |
|---|---|
| Chain ID | `!` (ASCII 33) |
| Address prefix | `31` |
| Genesis block ID | `5be1Fs9oqWGnUt1vVpBDXaJNN583tqic72hFwY9mmMf56n5WevrmwqMzdLSRVdEu7DWGhuQkVL1zhYBn4iuz9DX4` |
| Genesis timestamp | `1788539579643` (2026-09-04) |
| Target block time | 30 seconds |
| Peer to connect to | `50.116.30.244:6868` |
| P2P port | `6868` |
| Public REST API | `https://testnet-node.decentralchain.io` |
| Node image | `ghcr.io/decentral-america/node-scala:testnet-latest` |
| Finality | Deterministic Finality (feature 25) plus HotStuff fast finality, enabled and authoritative on the Testnet only |
| Data service | `https://testnet-data-service.decentralchain.io/v0` |
| WebSocket API | `wss://testnet-ws.decentralchain.io/ws` |
| Matcher API | `https://testnet-matcher.decentralchain.io/matcher` |
| Matcher public key | `BEtB5b2kX8Yge4sb5RRbTUqd5Va8Ah8PhphowcW31z6Y` |
| Matcher address | `31VMNVAvVh67dPZ41nMnYZvhoZFW7wwPrmq` |
| Explorer | `https://testnet.decentralscan.com/` |
| Faucet | `https://testnet.decentralscan.com/faucet` |
| Wallet and DEX | `https://testnet.decentral.exchange/` |

The exact image digest the Testnet runs is recorded in `node-config/testnet/vps-image.env` in the infra repository. Use that digest instead of `testnet-latest` if you want to run byte-for-byte the same build.

## 1. Write the configuration file

Save this as `dcc.conf`. The `blockchain` section must match the Testnet exactly; any difference (a genesis value, a functionality parameter or the reward settings) makes your node reject the chain.

```text
dcc {
  blockchain {
    type = CUSTOM
    custom {
      address-scheme-character = "!"

      functionality {
        feature-check-blocks-period = 3000
        blocks-for-feature-activation = 2700
        generation-balance-depth-from-50-to-1000-after-height = 0
        block-version-3-after-height = 0
        pre-activated-features = null
        pre-activated-features = {
          1 = 0, 2 = 0, 3 = 0, 4 = 0, 5 = 0, 6 = 0, 7 = 0, 8 = 0
          9 = 0, 10 = 0, 11 = 0, 12 = 0, 13 = 0, 14 = 0, 15 = 0, 16 = 0
          17 = 0, 18 = 0, 19 = 0, 20 = 0, 21 = 0, 22 = 0, 23 = 0
          24 = 0, 25 = 0
        }
        double-features-periods-after-height = 0
        min-asset-info-update-interval = 5
        min-block-time = 5s
        delay-delta = 8
        generation-period-length = 100
        hot-stuff-equivocation-penalty-height = 60000
      }

      rewards {
        term = 100000
        term-after-capped-reward-feature = 50000
        initial = 600000000
        min-increment = 50000000
        voting-interval = 10000
      }

      genesis {
        average-block-delay = 30s
        initial-base-target = 218
        timestamp = 1788539579643
        block-timestamp = 1788539579643
        signature = "5be1Fs9oqWGnUt1vVpBDXaJNN583tqic72hFwY9mmMf56n5WevrmwqMzdLSRVdEu7DWGhuQkVL1zhYBn4iuz9DX4"
        initial-balance = 10000000000000000
        transactions = [
          { recipient = "31VMNVAvVh67dPZ41nMnYZvhoZFW7wwPrmq", amount = 1000000000000000 }
          { recipient = "31LQd8WcvtYXMjHzNKzRrgZy8P3NnLQvPnk", amount = 1000000000000000 }
          { recipient = "31PmKNdHAU5sZbtg8TrzKh8WfE7E8xBc9WD", amount = 2000000000000000 }
          { recipient = "31dLhqhGoGVhtkf5msWFmgZn1ErrVR6b9qV", amount = 2000000000000000 }
          { recipient = "31RPEKcz71a3hdxt8z7qLhTpRMuRV2kUyr6", amount = 4000000000000000 }
        ]
      }
    }
  }

  network {
    port = 6868
    known-peers = ["50.116.30.244:6868"]
    # Set this to your public IP:port if other nodes should be able to dial you.
    # declared-address = "203.0.113.10:6868"
  }

  miner {
    enable = no
  }

  wallet {
    password = ""
  }
}
```

## 2. Start the node

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
  ghcr.io/decentral-america/node-scala:testnet-latest
```

`DCC_NETWORK=custom` keeps the built-in `testnet` profile's peers and port out of the merged configuration; the `blockchain` section of your file selects the chain.

## 3. Check that it follows the chain

Your node replays the chain from genesis, then follows the tip. Compare it with the public node:

```bash
curl -s http://127.0.0.1:6869/blocks/headers/at/1 | jq -r .id
# 5be1Fs9oqWGnUt1vVpBDXaJNN583tqic72hFwY9mmMf56n5WevrmwqMzdLSRVdEu7DWGhuQkVL1zhYBn4iuz9DX4

curl -s http://127.0.0.1:6869/blocks/height
curl -s https://testnet-node.decentralchain.io/blocks/height

curl -s http://127.0.0.1:6869/peers/connected | jq '.peers | length'   # 1 or more
```

Once the two heights match, pick a height a few blocks below the tip and compare the block IDs. They must be identical:

```bash
H=$(( $(curl -s https://testnet-node.decentralchain.io/blocks/height | jq .height) - 5 ))
curl -s http://127.0.0.1:6869/blocks/headers/at/$H | jq -r .id
curl -s https://testnet-node.decentralchain.io/blocks/headers/at/$H | jq -r .id
```

## Getting Testnet DCC

Open the [faucet](https://testnet.decentralscan.com/faucet) and enter a Testnet address (it starts with `31`). To create an address, use the [wallet](https://testnet.decentral.exchange/) or `libs.crypto.address(seed, '!')` from `@decentralchain/transactions` (see [How-To Guides](../04_building-apps/03_how-to-guides)).

## Ports

| Port | Purpose | Open to the internet? |
|---|---|---|
| `6868` | P2P | Yes, if you set `declared-address`; otherwise outbound only is enough |
| `6869` | REST API | No: keep it on localhost or behind a reverse proxy |
