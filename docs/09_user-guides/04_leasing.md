% The code on this page is included verbatim from docs/_samples/lease.ts, which CI
% typechecks against the pinned SDK versions. It was run on the public Testnet on
% 2026-10-27: lease 4iUPjetU9yk6yUFbavDnHYtz6H9rRZ9dtrJERzWNgBh7, cancelled by
% 6Xg95woM7a9wQ2o5MiFquiBd7iYiWewydcfshspjS69Q. Fees from node-scala
% FeeValidation.scala (Lease and LeaseCancel: 1 fee unit, 0.001 DCC).

# Leasing

Leasing lets you put your DCC behind a generating node without sending them to it. The node counts your DCC in its generating balance, which raises its chance to produce blocks, and many node operators share their block rewards with the accounts that lease to them. For how leasing fits into consensus, see {ref}`Leased Proof of Stake <02_decentralchain/05_node:Leased Proof of Stake>`.

## How a Lease Works

* **Your DCC stay in your account.** A lease does not move them. It locks the leased amount so you can't spend it, and you can end the lease at any time with a Lease Cancel transaction.
* **The node gets no control over them.** It can't spend, transfer or lease them on.
* **It takes time to count.** A node's generating balance is the lowest effective balance it had over the last 1,000 blocks, so leased DCC raise it only after they have been leased for 1,000 blocks: about 8 hours on the Testnet and 17 hours on Mainnet. Cancelling removes them at once.
* **Rewards are up to the operator.** The protocol pays block rewards and fees to the generating node, not to the accounts that lease to it. Any payout to lessors is the node operator's own arrangement: check how and how often an operator pays before you lease.
* **Only DCC can be leased.** Tokens can't.

Each Lease and Lease Cancel transaction costs 0.001 DCC (0.005 DCC from an account with a script).

| Balance | Meaning |
|---|---|
| Regular | All the DCC the account holds |
| Available | Regular minus what the account leased out: what it can spend |
| Effective | Available plus what others leased to it |
| Generating | The lowest effective balance over the last 1,000 blocks |

## Choose a Node

Lease only to an address that runs a generating node. The node's account needs a generating balance of at least 1,000 DCC to produce blocks once feature 1 is active (10,000 DCC before that). The block pages on [DecentralScan](https://decentralscan.com/) show which addresses generate blocks.

A lease to an address that doesn't run a node is valid, but it earns nothing. You can't lease to yourself.

## Lease with the SDK

This script leases 5 DCC to a node, checks the lease and then cancels it. Run it as in the {doc}`Quick Start <01_quick-start>`, with your seed phrase in `seed` and the node's address in `generator`:

```bash
npm install @decentralchain/transactions@5.0.1
```

```{literalinclude} ../_samples/lease.ts
:language: typescript
:lines: 2-
```

On the Testnet the output looks like this. The account held 8.998 DCC, so 5 DCC are leased out and 3.998 DCC stay available (the lease fee is already taken):

```text
Lease ID: 4iUPjetU9yk6yUFbavDnHYtz6H9rRZ9dtrJERzWNgBh7
Active leases: 1
Available: 399800000 Leased out: 500000000
Lease cancelled by 6Xg95woM7a9wQ2o5MiFquiBd7iYiWewydcfshspjS69Q
```

To keep the lease, stop the script before the cancel. To cancel later, you only need the lease ID, which is the ID of the Lease transaction.

## Lease in a Wallet

In [Decentral.Exchange](https://decentral.exchange/), log in and open **Leasing** in the wallet menu. Under **Start a lease**, enter the **Node address** and the **Amount to lease**, check the network fee, and press and hold **Hold to start lease** until it signs. Your leases are listed on the same screen; each active one has a **Cancel** button.

A dApp can also ask Cubensis Connect to sign a Lease or Lease Cancel transaction. The confirmation window shows the node and the amount before you approve it.

## Check Your Leases

| What | Where |
|---|---|
| Your active leases | `GET /leasing/active/{address}` on any node, or the **Leases** tab of your address on DecentralScan |
| One lease, active or cancelled | `GET /leasing/info/{leaseId}` |
| Your regular, available, effective and generating balance | `GET /addresses/balance/details/{address}` |

```bash
curl https://testnet-node.decentralchain.io/leasing/info/4iUPjetU9yk6yUFbavDnHYtz6H9rRZ9dtrJERzWNgBh7
```

The response has the lease's `sender`, `recipient`, `amount`, the `height` it started at and a `status` of `active` or `canceled`, with the cancel transaction's ID and height once it is cancelled.

## Running a Node That Accepts Leases

A node operator needs nothing special to accept leases: every lease to the node's address counts toward its generating balance. To pay lessors, operators read the active leases to their address (`GET /leasing/active/{nodeAddress}`) and the blocks the node generated, then send payouts, usually with a {ref}`Mass Transfer <02_decentralchain/03_transaction:Mass Transfer Transaction>`. See the {doc}`Node Guide <../05_node-guide/index>` to run a node.
