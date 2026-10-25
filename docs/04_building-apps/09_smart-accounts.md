% The code on this page is included verbatim from docs/_samples/: CI typechecks
% multisig-account.ts and escrow-account.ts, docs/scripts/check_ride_samples.py
% compiles ride/multisig-2-of-3.ride and ride/escrow.ride, and
% docs/scripts/check_install_snippets.py installs and imports the `npm install` line below.

# Smart Accounts

A smart account is an account with an account script. Normally a node accepts a transaction from an account when proof 0 is a valid signature by the account's key. Once the account has a script, the node runs the script instead, and the script alone decides. That turns an account into a set of rules: several people must agree, money may only go to certain addresses, or funds unlock at a given height.

```{note}
Verified against node-scala v1.8.0 on 2026-10-25. Both scripts compile on the public Testnet node (`DecentralChain v1.8.0-dev-e6248f2408`) and the Mainnet node (`DCC v1.3.5`), and the fees were confirmed with the Testnet node's `POST /transactions/calculateFee`. The TypeScript is typechecked against the published SDK; it has not been broadcast as part of this documentation pass.
```

## How Verification Works

* **The script replaces the signature check; it does not add to it.** The node no longer checks any proof by itself. If the rule needs a signature, the script must call `sigVerify` itself. A script that just returns `true` lets anyone spend from the account.
* **It runs for everything the account sends.** That means every transaction, including the Set Script that would change or remove the script, and every order placed on the DEX. It does not run when the account receives something.
* **It sees the whole transaction.** The built-in `tx` holds the transaction being checked, with all its fields, `bodyBytes` (the signed bytes) and `proofs`. The script can also read chain state: `height`, balances, and data entries of any account. `this` is the account's own address.
* **There are up to 8 proofs.** In Ride, `tx.proofs` always has 8 elements. Proofs the sender left out are empty, and `sigVerify` returns `false` for an empty proof, so a script can test any position without failing.
* **A complex script costs a fee.** If the script's complexity is above 200, every transaction from the account costs 0.004 DCC more. Both scripts on this page are above that line (the multisig is 609, the escrow 768), so their transactions pay 0.001 + 0.004 = 0.005 DCC.
* **Removing the script is a transaction like any other.** Send Set Script with `script: null`. The current script must approve it.

The language side is in {ref}`Account Script <03_ride-language/04_script-types:Account Script>`.

```bash
npm install @decentralchain/transactions@5.0.1
```

The examples import `compileRide` from {ref}`Compile a Script <04_building-apps/07_smart-contracts-overview:Compile a Script>` and read their scripts from a `ride` folder next to them. The public keys and addresses in the examples belong to throwaway example accounts. Deployed unchanged, a script would hand control to whoever holds those accounts' seeds, so always replace them with your own.

## Walkthrough: a 2-of-3 Multisig Account

Three owners share one account. Any two of them together can send a transaction from it; one alone cannot.

Save as `ride/multisig-2-of-3.ride`, with your owners' public keys in place of the example ones:

```{literalinclude} ../_samples/ride/multisig-2-of-3.ride
:language: text
:lines: 2-
```

Each owner has a fixed proof position. Fixed positions keep the script cheap, and they stop one owner from counting twice by putting the same signature in two slots.

The script has no `match`, so it applies to every kind of transaction. Changing the owners later is itself a Set Script transaction, so it also needs two approvals.

```{literalinclude} ../_samples/multisig-account.ts
:language: typescript
:lines: 2-
```

Points worth knowing:

* **`senderPublicKey` names the shared account.** That account sends the transaction and pays its fee. The seeds passed as the second argument only add proofs.
* **A seed array maps to proof positions.** `[ownerASeed]` fills proof 0, and `[null, null, ownerCSeed]` fills proof 2 without touching the others. Passing an already signed transaction back to the builder keeps its existing proofs, timestamp and fee.
* **Owners sign the same bytes.** The transaction's ID depends only on its body, not on its proofs. Every owner can check that they are approving the same transaction by comparing IDs before signing.
* **There is a time limit.** A node rejects a transaction whose timestamp is more than 120 minutes older than the last block, so collect the signatures within about two hours of creating the transaction.
* **The fee here is 0.005 DCC:** 0.001 for the transfer and 0.004 for the script.

## Walkthrough: an Escrow Account

A buyer pays for goods in advance, but the seller should only get the money once the goods arrive. The buyer moves the payment into a fresh escrow account and locks that account with this script. From then on, the funds can leave exactly once, in one piece, and only with the right signature:

| Funds go to | Allowed if signed by |
|---|---|
| Seller | the buyer (goods received) or the arbiter |
| Buyer | the seller (refund) or the arbiter, or the buyer alone once `timeoutHeight` has passed |
| Anywhere else, or any other transaction | never |

Save as `ride/escrow.ride`, with the real parties' public keys in place of the example ones:

```{literalinclude} ../_samples/ride/escrow.ride
:language: text
:lines: 2-
```

This script inspects the transaction, not only its signatures:

* `match tx` picks out Transfer transactions. Every other transaction type falls into `case _ => false`, so the escrow account can never get a new script, lease its balance or write data.
* `addressFromRecipient` resolves the recipient, which may be an alias, to an address.
* `validPayout` only accepts a transfer of exactly the escrowed `amount` in DCC, with exactly the 0.005 DCC fee paid in DCC. Without it, a party allowed to sign a payout could send the funds away as a huge fee, or in many small pieces that each burn a fee. The escrow holds only enough for one payout, so the first valid one empties it.
* `amount` and `timeoutHeight` come from the account's own data storage. They are written before the script is set, so they can be computed at that moment, and nobody can change them afterwards.

The buyer sets up the escrow, and later releases the funds once the goods arrive:

```{literalinclude} ../_samples/escrow-account.ts
:language: typescript
:lines: 2-
```

Things to settle before locking the account:

* **The escrow account pays the fees.** Fund it with the amount plus 0.008 DCC: 0.001 for the settings, 0.002 for the Set Script (the script is 1,043 bytes) and 0.005 for the payout. If it holds less, no payout can succeed until someone sends it the difference.
* **Pick a timeout that suits the deal.** The sample sets `timeoutHeight` about a week (20,160 blocks of 30 seconds) after the current height.
* **Everyone must agree on the script before the funds move.** The seller and the arbiter should decompile the deployed script (`GET /addresses/scriptInfo/{address}`, then `POST /utils/script/decompile`) and read its data (`GET /addresses/data/{address}`) before shipping anything.
* **Use a fresh account.** Throw away its seed after the Set Script transaction. The seed has no power once the script is set, but keeping it around invites confusion.

## Inspecting a Smart Account

`GET /addresses/scriptInfo/{address}` returns the account's compiled `script`, its `complexity`, its `verifierComplexity` and the `extraFee` its transactions must add. If the account has no script, `script` is `null`.

When a transaction is rejected, `broadcast()` rejects with the node's message. It reads `Transaction is not allowed by account-script` when the script returned `false`, and it includes the script's error when the script failed.
