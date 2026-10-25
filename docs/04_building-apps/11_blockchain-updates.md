# Blockchain Updates

Blockchain Updates is a node extension that streams every change the chain goes through. Each block and microblock arrives with the balances, data entries, tokens, leases, scripts and aliases it changed, both before and after. When the node switches to another fork, a rollback event says exactly what to undo. An indexer, an explorer back end or a service that reacts to payments can follow the chain from one subscription, without polling the REST API.

```{note}
Verified against node-scala v1.8.0 on 2026-10-24: the extension's source (`grpc-server/src/main/scala/com/decentralchain/events/`) and its schema, `dcc/events/grpc/blockchain_updates.proto` and `dcc/events/events.proto` in `io.decentralchain:protobuf-schemas` 1.6.6, the version node v1.8.0 builds against. The commands below were not run against a live node as part of this documentation pass.
```

## When to Use It

| You need | Use |
|---|---|
| Current state: one balance, one data entry, one transaction | The {ref}`node REST API <05_node-guide/01_node-rest-api:Node REST API>` |
| History and search: asset lists, past trades, paginated transactions | The [Data Service API](06_data-service-api) |
| Every state change, in order, as it happens, including rollbacks | Blockchain Updates |

## Run It on Your Own Node

```{important}
There is no public Blockchain Updates endpoint. The public nodes do not expose port `6881` (see [Node gRPC API](05_node-grpc)). Run your own node, for example by following [Join the Public Testnet](../05_node-guide/15_join-testnet), and enable the extension there.
```

The extension is part of the node's `grpc-server` module, which the official Docker image already contains. For other installs, see {ref}`Node Extensions <05_node-guide/02_node-extensions:gRPC Server>`. Enable it by adding its class to `dcc.extensions` in the node's configuration file, inside the `dcc { }` block:

```text
dcc {
  # ... the rest of your configuration ...

  extensions = [
    "com.decentralchain.events.BlockchainUpdates"
    # "com.decentralchain.api.grpc.GRPCServerExtension"  # the other gRPC APIs on port 6870, if you also want them
  ]
}
```

With Docker, publish the port on the host's loopback interface only, next to the other ports in the `docker run` command:

```bash
-p 127.0.0.1:6881:6881
```

Settings, under `dcc.blockchain-updates`:

| Setting | Default | Meaning |
|---|---|---|
| `grpc-port` | `6881` | Port the API listens on |
| `min-keep-alive` | `5m` | Shortest interval at which a client may send keep-alive pings. A client that pings more often is disconnected |
| `worker-threads` | `4` | Threads that serve subscriptions |

```{warning}
The extension listens on **all network interfaces** (`0.0.0.0`). Unlike the other gRPC APIs, it does not follow `dcc.grpc.host`, and it has no authentication. Keep port 6881 behind a firewall, or publish it only on `127.0.0.1` as above.
```

### History Starts When You Enable It

The extension keeps its own store in the `blockchain-updates` directory inside the node's data directory, and it records only blocks the node processes while the extension is running. Plan for this:

* **Enable it before the node's first sync** if you need history from genesis. The extension starts before the genesis block is applied, so it records every block from height 1.
* **If you enable it on a node that has already synced,** the extension logs a warning and starts recording from the next block. Earlier heights are not available from this node.
* **The same applies if the store falls behind the chain,** for example after an unclean shutdown. The extension resets and resumes from the next block. A consumer then sees a gap and must fill it from another source.
* If the store is ahead of the chain, the extension rolls it back to the node's height at startup. If the two disagree about the last block, the node refuses to start with `Last update ID ... does not match last block ID`. Deleting the `blockchain-updates` directory clears that error, and recording then resumes from the next block.

## The API

The service is `dcc.events.grpc.BlockchainUpdatesApi`. It has three methods:

| Method | Request | Returns |
|---|---|---|
| `GetBlockUpdate` | `height` | The update for one height |
| `GetBlockUpdatesRange` | `from_height`, `to_height` (both required, both inclusive) | All updates in the range, in one response |
| `Subscribe` | `from_height`, optional `to_height` | A stream: the stored updates from `from_height`, then new ones as they happen |

Rules the node enforces:

* `from_height` must be at least 1. The schema's comment calls it optional, but the default of 0 is rejected (`fromHeight must be > 0`).
* `from_height` cannot be above the node's current height.
* `to_height` of 0, or no `to_height`, makes `Subscribe` run indefinitely. Otherwise the stream ends after that height.
* `GetBlockUpdate` for the current height returns the block as it stands so far, with its microblocks merged in. A height above the current one is an error.
* `GetBlockUpdatesRange` returns the whole range in one message, so keep ranges short. Use `Subscribe` for long stretches.

### Try It with grpcurl

The server supports gRPC reflection, so [grpcurl](https://github.com/fullstorydev/grpcurl) v1.8.8 or later can call it with no `.proto` files. The connection is plaintext:

```bash
# The service list includes dcc.events.grpc.BlockchainUpdatesApi
grpcurl -plaintext 127.0.0.1:6881 list

# One block
grpcurl -plaintext -d '{"height": 1000}' \
  127.0.0.1:6881 dcc.events.grpc.BlockchainUpdatesApi/GetBlockUpdate

# Heights 1000 to 1010, then the stream ends
grpcurl -plaintext -d '{"from_height": 1000, "to_height": 1010}' \
  127.0.0.1:6881 dcc.events.grpc.BlockchainUpdatesApi/Subscribe

# From height 1000 onward, then follow the chain
grpcurl -plaintext -d '{"from_height": 1000}' \
  127.0.0.1:6881 dcc.events.grpc.BlockchainUpdatesApi/Subscribe
```

grpcurl prints byte fields (block and transaction IDs, addresses, public keys) as base64. The REST API shows the same values in Base58, so decode and re-encode them to compare.

### From Code

Generate a client from the node's own schema, `dcc/events/grpc/blockchain_updates.proto` and the files it imports. Its Maven Central artifact is `io.decentralchain:protobuf-schemas:1.6.6` (classifier `protobuf-src`), and the same files are in the SDK monorepo under `packages/sdk/protobuf-schemas`. The TypeScript client `@decentralchain/node-api-grpc` wraps this API as `mkBlockchainUpdatesApi`, but it is not published yet; see {ref}`Node gRPC API <04_building-apps/05_node-grpc:Blockchain Updates>`.

```{warning}
Do not generate a client from the `.proto` files in the published `@decentralchain/protobuf-serialization` 3.0.0 package. They still use the previous protobuf package names, so the client would request a service that a v1.8.0 node does not serve.
```

## What an Update Contains

Each message is a `BlockchainUpdated` with the block `id` and `height` and one of two bodies.

**`append`**, a block or a microblock was added:

| Field | Content |
|---|---|
| `block` or `micro_block` | The block (with `updated_dcc_amount`, the total DCC supply after the block, `activated_features` and `reward_shares`) or the signed microblock |
| `transaction_ids` | The IDs of the transactions it contains, in order |
| `transactions_metadata` | Per transaction: the sender's address and, by type, resolved recipients, order details, or an invocation's function, arguments, payments and result |
| `state_update` | Changes made by the block itself, such as the block reward |
| `transaction_state_updates` | One state update per transaction, in the same order as `transaction_ids` |

**`rollback`**, blocks or microblocks were removed:

| Field | Content |
|---|---|
| `type` | `BLOCK` or `MICROBLOCK` |
| `removed_transaction_ids` | Transactions that are no longer on the chain |
| `removed_blocks` | The removed blocks |
| `rollback_state_update` | The state to restore |
| `deactivated_features` | Features whose activation was undone |

A state update lists changed `balances`, `leasing_for_address`, `data_entries`, `assets`, `individual_leases`, `scripts` and `deleted_aliases`. Balances, leasing totals, data entries, token details and scripts carry their value **before and after** the change, so a consumer can apply or reverse them without looking anything up. A lease update carries only the lease's new status, and a deleted alias only its name. `referenced_assets` on the outer message gives the name and decimals of every token the update mentions.

## Writing a Reliable Consumer

* **Store your position.** After applying an update, save its `height` and `id`. To resume, subscribe from that height; the stream starts with that height again. If the first update's `id` equals the stored one, skip it. If it differs, that height changed while you were away (it gained microblocks or was replaced on a fork), so revert what you applied for it before applying the new update.
* **Treat microblocks as provisional.** The block at the top of the chain grows microblock by microblock, and a `MICROBLOCK` rollback can remove the most recent ones. Apply them, but be ready to undo them.
* **Handle a rollback at any height.** A fork switch rolls back recent blocks. An operator-forced rollback (`POST /debug/rollback`, see {doc}`Sync and Rollback <../05_node-guide/06_sync-and-rollback>`) can reach further back, even below the {ref}`finalized height <02_decentralchain/09_protocol:Finality>`. Undo using `rollback_state_update` and continue with the next append.
* **Keep up.** The node buffers at most 250 updates for each subscriber. If a client falls that far behind, the node ends its stream, and the client must reconnect from its stored height.
* **Ping no more often than `min-keep-alive`.** Set the client's keep-alive interval to 5 minutes or more, or the node disconnects it.
