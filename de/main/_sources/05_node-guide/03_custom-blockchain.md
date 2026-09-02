# Custom Blockchain

Besides Mainnet and Testnet, the node software supports running a fully private, custom network — useful for local development or an isolated test environment. This is configured by setting the blockchain type to `CUSTOM` in the node configuration file, as seen in the `devnet` template shipped in [`network-defaults.conf`](https://github.com/Decentral-America/node-scala/blob/master/node/src/main/resources/network-defaults.conf):

```text
dcc {
  blockchain {
    type = CUSTOM
    custom {
      address-scheme-character = "D"
      functionality {
        feature-check-blocks-period = 5
        blocks-for-feature-activation = 4
        # ... additional protocol activation parameters
      }
      rewards {
        term = 100000
        initial = 600000000
        min-increment = 50000000
        voting-interval = 10000
      }
      genesis {
        average-block-delay = 1m
        initial-base-target = 100
        timestamp = 1489352400000
        signature = "..."
        initial-balance = 7700000000000000
        transactions = [
          { recipient = "your-genesis-address", amount = 1000000000000000 }
        ]
      }
    }
  }
  network {
    port = 6863
    known-peers = []
  }
}
```

Key fields:

| Field | Purpose |
|---|---|
| `address-scheme-character` | The network byte that distinguishes your custom network's addresses from Mainnet/Testnet — every address on your network is derived using this character |
| `functionality` | Protocol feature activation thresholds, transaction time offsets, and related consensus parameters |
| `rewards` | Initial {ref}`block reward <02_decentralchain/05_node:Block Reward>` size, minimum increment, and voting interval — same mechanism as Mainnet |
| `genesis` | The network's {ref}`genesis block <02_decentralchain/04_block:Block>`: initial balances, timestamp, and difficulty |
| `network.known-peers` | Seed peers for nodes on your custom network to discover each other — leave empty for a single-node development network |

For a full field reference, use `network-defaults.conf`'s `devnet` block as a starting template and adjust the values for your own network, then point your node at a config file that sets `blockchain.type = CUSTOM` with your own `custom` block instead of `blockchain.type = TESTNET` or `MAINNET`.
