% Page names, tabs and search rules on this page come from the explorer's source
% (apps/scanner in the DecentralChain monorepo: src/routes.ts, src/Layout.tsx,
% src/components/shared/SearchBar.tsx). URLs checked against the live Testnet
% explorer on 2026-10-27.

# DecentralScan Guide

DecentralScan is the DecentralChain block explorer. It shows every block, transaction, account and token on the chain, read straight from the network's nodes. You don't need an account or a wallet to use it.

Each network has its own explorer. A transaction or address from one network can't be found on the other's explorer.

| Network | Explorer |
|---|---|
| Mainnet | [decentralscan.com](https://decentralscan.com/) |
| Testnet | [testnet.decentralscan.com](https://testnet.decentralscan.com/), with the [Testnet faucet](https://testnet.decentralscan.com/faucet) |

## Search

The search bar at the top of every page takes a block height, a block ID, a transaction ID, an asset ID or an address:

| You type | DecentralScan opens |
|---|---|
| Digits only, for example `99864` | The block at that height |
| A 40- to 79-character ID | The block with that ID; if there is none, the transaction; if there is none, the asset |
| Anything shorter | The address page for it |

Search doesn't resolve aliases. To find the address behind an alias, ask a node: `https://testnet-node.decentralchain.io/alias/by-alias/<alias>` returns it. A block signature (86 to 88 characters) is not an ID: use the **Block ID** shown on the block's page.

## Pages

**Dashboard** gives a network overview: the current height, the latest block, the node version and the most recent blocks. It is the start page.

**Blocks** lists the latest blocks. A block's page shows its height, ID, parent block, generator, timestamp, size, reward, the transactions in it and the raw block data.

**Transactions** has two tabs. **Lookup** finds a transaction by ID and shows its type, status, sender, recipient, amounts, fee, block height and every field of the transaction. **Mempool** lists the unconfirmed transactions waiting for a block.

**Address** shows an account. The **Balances** tab has its DCC and token balances, **Transactions** its history (filter by type, or search by sender or recipient), **NFTs** its non-fungible tokens and **Leases** its active leases.

**Assets** shows a token: name, ID, issuer, decimals, total quantity, whether it is reissuable, its activity, and the raw asset data the node returns. The distribution tool lists the token's holders.

**DEX Pairs** lists the trading pairs on the network's matcher.

**Network** shows the network itself: an **Overview**, the **Peers** of the public node (connected, all, suspended and blacklisted) and the **Node** it reads from.

**Stress** is a read-only monitor of chain activity on the Testnet: blocks, mass transfers, transactions per second and block times.

## Direct Links

Every page has a stable URL, so you can link straight to it from an app, a support answer or a bug report:

| Page | URL |
|---|---|
| Transaction | `https://testnet.decentralscan.com/transaction?id=<transaction ID>` |
| Address | `https://testnet.decentralscan.com/address?addr=<address>` |
| Block by height | `https://testnet.decentralscan.com/blockdetail?height=<height>` |
| Block by ID | `https://testnet.decentralscan.com/blockdetail?id=<block ID>` |
| Asset | `https://testnet.decentralscan.com/asset?id=<asset ID>` |
| Unconfirmed transactions | `https://testnet.decentralscan.com/transaction?tab=mempool` |

For Mainnet, use `https://decentralscan.com` in place of `https://testnet.decentralscan.com`.

## Check a Transaction

To check whether a payment arrived, open its transaction page:

* **Not found** means the node doesn't know the transaction. It was not broadcast, was rejected, or was broadcast to the other network.
* **In the Mempool tab** means the node accepted it but it is not in a block yet. On the Testnet a block comes about every 30 seconds; on Mainnet about every 60.
* **A block height** means it is on the chain. The status shows whether it succeeded. A dApp call can be in a block and still have failed: the fee is charged, but none of its actions happen.

Leased DCC are not spent: they still show in the account's balance, and the lease appears under **Leases** until it is cancelled. See {doc}`Leasing <04_leasing>`.

## Get Testnet DCC

The [Testnet faucet](https://testnet.decentralscan.com/faucet) sends 10 DCC to a Testnet address, once every 24 hours per address. Paste the address and submit. The {doc}`Quick Start <01_quick-start>` shows the same request from the command line.

## Everything Is Public

An explorer shows only what is on the chain, and everything on the chain is public: every balance, every transaction and every data entry of every account. Don't put anything private in an attachment or a data entry.

For the same data from code, use the node's REST API (see {doc}`Node REST API <../05_node-guide/01_node-rest-api>`) or the {doc}`Data Service API <../04_building-apps/06_data-service-api>`.
