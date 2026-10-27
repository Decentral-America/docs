% The TypeScript example on this page is included verbatim from
% docs/_samples/compile-ride.ts, which CI typechecks. The Ride samples it refers
% to live in docs/_samples/ride/ and are compiled by docs/scripts/check_ride_samples.py.

# Smart Contracts Overview

A smart contract on DecentralChain is a {doc}`Ride <../03_ride-language/index>` script attached to an account or to a token. The node runs the script every time a transaction touches the thing it is attached to. The script either decides whether that transaction may happen, or, for a dApp, works out what a call does.

```{note}
Verified against node-scala v1.8.0 on 2026-10-25. Limits and fees come from the node source. Every Ride sample in this section was compiled by the public Testnet node (`DecentralChain v1.8.0-dev-e6248f2408`) and the public Mainnet node (`DCC v1.3.5`).
```

## Three Kinds of Script

| | dApp script | Account script | Asset script |
|---|---|---|---|
| Attached to | An account, which becomes a dApp | An account, which becomes a smart account | A token, which becomes a smart asset |
| Runs when | Someone invokes one of its `@Callable` functions | The account sends a transaction or an order | A transaction or a dApp action involves the token |
| Produces | Script actions: data entries, transfers, issues, leases | Allow (`true`) or reject (`false` or an error) | Allow (`true`) or reject (`false` or an error) |
| Installed by | Set Script | Set Script | Issue, then Set Asset Script to replace it |
| Directives | `CONTENT_TYPE DAPP`, `SCRIPT_TYPE ACCOUNT` | `CONTENT_TYPE EXPRESSION`, `SCRIPT_TYPE ACCOUNT` | `CONTENT_TYPE EXPRESSION`, `SCRIPT_TYPE ASSET` |
| Guide | [Creating and Launching a dApp](08_creating-and-launching-a-dapp) | [Smart Accounts](09_smart-accounts) | [Smart Assets](10_smart-assets) |

A dApp script can also contain one `@Verifier` function. It does the same job as an account script for the dApp's own account: it approves or rejects every transaction the dApp account sends. Without one, the node only checks that the dApp account's key signed the transaction.

An account holds at most one script, so an account is either a dApp or a smart account, not both. The full language reference for each kind is in {doc}`Script Types <../03_ride-language/04_script-types>`.

## From Source to Chain

1. **Write** the script. Every script starts with three directives: `STDLIB_VERSION`, `CONTENT_TYPE` and `SCRIPT_TYPE`.
2. **Compile** it to bytes with a node. The result is a base64 string plus the script's complexity.
3. **Deploy** the bytes with a transaction: {ref}`Set Script <02_decentralchain/03_transaction:Set Script Transaction>` for a dApp or account script, {ref}`Issue <02_decentralchain/03_transaction:Issue Transaction>` for a new smart asset, {ref}`Set Asset Script <02_decentralchain/03_transaction:Set Asset Script Transaction>` to replace an asset's script.
4. **Use** it. Users call a dApp with an {ref}`Invoke Script <02_decentralchain/03_transaction:Invoke Script Transaction>` transaction. Account and asset scripts run on their own whenever a transaction they cover reaches the node.

### Compile a Script

The `@decentralchain/ride` npm package cannot be installed yet (see {ref}`ride-js and @decentralchain/ride <04_building-apps/01_developer-tools:ride-js and @decentralchain/ride>`), so compile with a node's `POST /utils/script/compileCode` endpoint. It accepts the Ride source as plain text and does not write anything to the chain. The examples in this section import this helper from `compile-ride.ts`:

```{literalinclude} ../_samples/compile-ride.ts
:language: typescript
:lines: 4-
```

For the {ref}`2-of-3 multisig script <04_building-apps/09_smart-accounts:Walkthrough: a 2-of-3 Multisig Account>`, the Testnet node answers:

```json
{
  "script": "base64:...",
  "complexity": 609,
  "verifierComplexity": 609,
  "callableComplexities": {},
  "extraFee": 400000
}
```

`callableComplexities` lists each `@Callable` function of a dApp. `extraFee` is the surcharge, in Decentralites, that every transaction sent from an account with this script must add to its fee (see [Fees](#fees)).

Compile on the network you deploy to. Complexity is estimated by the network's own rules, and the two public networks differ: the same multisig script estimates at 609 on the Testnet and 643 on Mainnet.

### Choose a Standard Library Version

The `STDLIB_VERSION` directive must name a version the target network has activated:

| Network | Node | Highest active feature | Highest usable `STDLIB_VERSION` |
|---|---|---|---|
| Testnet | v1.8.0 | 26 | 9 |
| Mainnet | v1.3.5 | 16 | 5 |

The samples in this section use version 5, so the same scripts deploy on both networks. What each later version adds is listed in {doc}`Standard Library Versions <../03_ride-language/08_stdlib-versions>`.

## Limits

Values on the Testnet (node v1.8.0, features 1 to 26 active):

| Limit | Value |
|---|---|
| Account script or asset script size | 8 KB (8,192 bytes) |
| dApp script size | 160 KB (32 KB on Mainnet, where feature 17 is not active) |
| Complexity of an account script or of a dApp's `@Verifier` | 2,000 |
| Complexity of an asset script | 4,000 |
| Complexity of a `@Callable` function | 52,000 for `STDLIB_VERSION` 6 and later, 10,000 for version 5 |
| Total complexity of one invocation, across every callable it reaches through dApp-to-dApp calls and every smart asset script they trigger | 52,000 for `STDLIB_VERSION` 6 and later, 26,000 for version 5 |
| Verifier complexity that adds no fee | 200 |
| Payments attached to one invocation | 10 |

Limits on script actions, data weight and nested calls are listed under {ref}`Limitations <03_ride-language/07_dapp-to-app-invocation:Limitations>`.

## Fees

Fees are in DCC. The full table is under {ref}`Minimum Fee <02_decentralchain/03_transaction:Minimum Fee>`; these are the ones that matter for scripts:

* **Set Script:** 0.001 DCC for each started kilobyte of compiled script on the Testnet. The 2,058-byte pledge-drive dApp costs 0.003 DCC. Mainnet charges a flat 0.01 DCC because feature 17 is not active there. `setScript()` from `@decentralchain/transactions` computes the Testnet value, so pass `fee: 1_000_000` on Mainnet.
* **Invoke Script:** 0.005 DCC, plus 1 DCC for every token the call issues that is not an NFT.
* **Issue:** 1 DCC, with or without a script.
* **Set Asset Script:** 1 DCC. This already includes the smart asset surcharge for the token itself, so do not add 0.004 DCC to it.
* **Smart account surcharge:** 0.004 DCC on every transaction sent by an account whose verifier complexity is above 200. This also applies to a dApp with a costly `@Verifier`.
* **Smart asset surcharge:** 0.004 DCC for each smart asset a transaction involves, except Invoke Script transactions. A transfer of a smart asset costs 0.001 + 0.004 = 0.005 DCC.

The transaction builders do not add either surcharge on their own. Pass `additionalFee: 400_000` for each one that applies.

## Failed Transactions

When a callable function throws, or a smart asset rejects one of its actions, the outcome depends on how much computation already ran. Before a complexity of 1,000, the node rejects the transaction outright and the sender pays nothing. After that point, the transaction is still written to a block, marked `"applicationStatus": "script_execution_failed"`, and the sender pays the fee. None of its other changes are applied. See {ref}`Fee for Failed Transactions <02_decentralchain/03_transaction:Fee for Failed Transactions>`.

## Common Mistakes

* **Leaving out `chainId`.** `transfer()` and `massTransfer()` take the chain ID from the recipient's address. Every other builder in `@decentralchain/transactions` falls back to chain ID 76 (`'L'`), which no DecentralChain network uses, so the node rejects the transaction. Always pass `chainId: '!'` for the Testnet or `chainId: '?'` for Mainnet.
* **Locking an account by accident.** A script also checks the transaction that would replace it. If it can never approve a Set Script (or a Set Asset Script for a token), it is permanent. If it rejects everything, the account's funds can never move again. Try every script on the Testnet first.
* **Forgetting the signature check.** An account script replaces the node's signature check entirely. A script that returns `true` without calling `sigVerify` lets anyone spend from the account.
* **Trusting a dApp's deployer by default.** A dApp with no `@Verifier` can be rewritten, or emptied with a plain transfer, by whoever holds the dApp account's seed. Before you send funds to a dApp, fetch its script with `GET /addresses/scriptInfo/{address}` and turn the `script` field back into Ride source with `POST /utils/script/decompile`.

## Next Steps

* [Creating and Launching a dApp](08_creating-and-launching-a-dapp): write, deploy and call a dApp on the Testnet.
* [Smart Accounts](09_smart-accounts): a multisig account and an escrow account.
* [Smart Assets](10_smart-assets): a token with transfer rules.
* [Blockchain Updates](11_blockchain-updates): follow every state change on the chain from your own node.
