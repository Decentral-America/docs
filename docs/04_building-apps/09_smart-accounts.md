% Every `npm install` line and every `import ... from '@decentralchain/...'`
% on this page is installed and imported on Node.js 24 by CI
% (docs/scripts/check_install_snippets.py). docs/_samples/multisig-account.ts and
% docs/_samples/escrow-account.ts typecheck the full examples, and
% docs/scripts/check_ride_samples.py compiles docs/_samples/ride/multisig-2-of-3.ride
% and docs/_samples/ride/escrow.ride.

# Smart Accounts

A smart account is an account with an account script. Normally a node accepts a transaction from an account when proof 0 is a valid signature by the account's key. Once the account has a script, the node runs the script instead, and the script alone decides. That turns an account into a set of rules: several people must agree, money may only go to certain addresses, or funds unlock at a given height.

```{note}
Verified against node-scala v1.8.0 on 2026-10-24. Both scripts compile on the public Testnet node (`DecentralChain v1.8.0-dev-e6248f2408`) and the Mainnet node (`DCC v1.3.5`), and the fees were confirmed with the Testnet node's `POST /transactions/calculateFee`. The TypeScript is typechecked against the published SDK; it has not been broadcast as part of this documentation pass.
```

## How Verification Works

* **The script replaces the signature check; it does not add to it.** The node no longer checks any proof by itself. If the rule needs a signature, the script must call `sigVerify` itself. A script that just returns `true` lets anyone spend from the account.
* **It runs for everything the account sends.** That means every transaction, including the Set Script that would change or remove the script, and every order placed on the DEX. It does not run when the account receives something.
* **It sees the whole transaction.** The built-in `tx` holds the transaction being checked, with all its fields, `bodyBytes` (the signed bytes) and `proofs`. The script can also read chain state: `height`, balances, and data entries of any account. `this` is the account's own address.
* **There are up to 8 proofs.** In Ride, `tx.proofs` always has 8 elements. Proofs the sender left out are empty, and `sigVerify` returns `false` for an empty proof, so a script can test any position without failing.
* **A complex script costs a fee.** If the script's complexity is above 200, every transaction from the account costs 0.004 DCC more. Both scripts on this page are above that line (the multisig is 609, the escrow 742), so their transactions pass `additionalFee: 400_000`.
* **Removing the script is a transaction like any other.** Send Set Script with `script: null`. The current script must approve it.

The language side is in {ref}`Account Script <03_ride-language/04_script-types:Account Script>`.

```bash
npm install @decentralchain/transactions@5.0.1
```

The examples import `compileRide` from {ref}`Compile a Script <04_building-apps/07_smart-contracts-overview:Compile a Script>`.

## Walkthrough: a 2-of-3 Multisig Account

Three owners share one account. Any two of them together can send a transaction from it; one alone cannot.

Save as `multisig-2-of-3.ride`, with your owners' public keys in place of the example ones:

```text
{-# STDLIB_VERSION 5 #-}
{-# CONTENT_TYPE EXPRESSION #-}
{-# SCRIPT_TYPE ACCOUNT #-}

# Public keys of the three owners. Owner A signs into proof 0, B into proof 1, C into proof 2.
let ownerA = base58'Ch79CxM7xSWXsQ6o1MughNW7ELHaMwJDqV8FDTZMrosq'
let ownerB = base58'8DAes8dPJqgRZ8J3YgXh2ppgTxQea9VcccRJfB71GZct'
let ownerC = base58'7g2vpXFYV75q2QWuQipD5VwbUdkJuqyi92U9nqbumdLV'

func approvals(proofIndex: Int, owner: ByteVector) =
  if (sigVerify(tx.bodyBytes, tx.proofs[proofIndex], owner)) then 1 else 0

approvals(0, ownerA) + approvals(1, ownerB) + approvals(2, ownerC) >= 2
```

Each owner has a fixed proof position. Fixed positions keep the script cheap, and they stop one owner from counting twice by putting the same signature in two slots.

The script has no `match`, so it applies to every kind of transaction. Changing the owners later is itself a Set Script transaction, so it also needs two approvals.

```typescript
import { readFile } from 'node:fs/promises';
import { setScript, transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const sharedSeed = 'shared account secret seed phrase here';
const ownerASeed = 'owner A secret seed phrase here';
const ownerCSeed = 'owner C secret seed phrase here';
const sharedPublicKey = libs.crypto.publicKey(sharedSeed);

// Once: install the script. After this, the shared account's own seed can no longer sign for it.
const install = setScript(
  { script: await compileRide(await readFile('multisig-2-of-3.ride', 'utf8'), nodeUrl), chainId: '!' },
  sharedSeed,
);
await broadcast(install, nodeUrl);
await waitForTx(install.id, { apiBase: nodeUrl, timeout: 120_000 });

// Owner A builds the transfer and signs it into proof 0.
const proposal = transfer(
  {
    recipient: '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9',
    amount: 100_000_000, // 1 DCC
    senderPublicKey: sharedPublicKey, // the account that sends and pays, not the signer
    additionalFee: 400_000, // the script's complexity is above 200
    chainId: '!',
  },
  [ownerASeed],
);

// Owner C receives the proposal (for example as JSON), checks it and adds a signature to proof 2.
const approved = transfer(proposal, [null, null, ownerCSeed]);
await broadcast(approved, nodeUrl);
```

Points worth knowing:

* **`senderPublicKey` names the shared account.** That account sends the transaction and pays its fee. The seeds passed as the second argument only add proofs.
* **A seed array maps to proof positions.** `[ownerASeed]` fills proof 0, and `[null, null, ownerCSeed]` fills proof 2 without touching the others. Passing an already signed transaction back to the builder keeps its existing proofs, timestamp and fee.
* **Owners sign the same bytes.** The transaction's ID depends only on its body, not on its proofs. Every owner can check that they are approving the same transaction by comparing IDs before signing.
* **There is a time limit.** A node rejects a transaction whose timestamp is more than 120 minutes older than the last block, so collect the signatures within about two hours of creating the transaction.
* **The fee here is 0.005 DCC:** 0.001 for the transfer and 0.004 for the script.

## Walkthrough: an Escrow Account

A buyer pays for goods in advance, but the seller should only get the money once the goods arrive. The buyer moves the payment into a fresh escrow account and locks that account with this script. From then on, the funds can only go to the seller or back to the buyer, and only with the right signature:

| Funds go to | Allowed if signed by |
|---|---|
| Seller | the buyer (goods received) or the arbiter |
| Buyer | the seller (refund) or the arbiter, or the buyer alone once `timeoutHeight` has passed |
| Anywhere else, or any other transaction | never |

```text
{-# STDLIB_VERSION 5 #-}
{-# CONTENT_TYPE EXPRESSION #-}
{-# SCRIPT_TYPE ACCOUNT #-}

let buyer = base58'CPT5HpPYQ1rA8Eot2swk8tuXb4PE5XDhRbQ7Gpp3sr4D'
let seller = base58'Emx5RBMowyZLqqn3hX8gGhg4Lgd2UktvDb7UHvHTDjts'
let arbiter = base58'FzQmZTezonLeREVNQdbBAx5i9cUHqevug78VUgYWjSMg'

# After this height the buyer can take the funds back alone.
let timeoutHeight = 120000

func signedBy(key: ByteVector) = sigVerify(tx.bodyBytes, tx.proofs[0], key)

match tx {
  case t: TransferTransaction =>
    let to = addressFromRecipient(t.recipient)
    if (isDefined(t.assetId)) then false
    else if (to == addressFromPublicKey(seller)) then signedBy(buyer) || signedBy(arbiter)
    else if (to == addressFromPublicKey(buyer)) then
      signedBy(seller) || signedBy(arbiter) || (signedBy(buyer) && height >= timeoutHeight)
    else false
  case _ => false
}
```

This script inspects the transaction, not only its signatures. `match tx` picks out Transfer transactions. `addressFromRecipient` resolves the recipient, which may be an alias, to an address. `isDefined(t.assetId)` rejects transfers of anything but DCC. Every other transaction type falls into `case _ => false`, so the escrow account can never get a new script, lease its balance or write data.

The buyer releases the funds once the goods arrive:

```typescript
import { readFile } from 'node:fs/promises';
import { setScript, transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const escrowSeed = 'escrow account secret seed phrase here';
const buyerSeed = 'buyer secret seed phrase here';
const sellerAddress = '31VgE1dHbGoMeesqWFVr6GoSdB7zX4wS1w8';

// The buyer funds the escrow account with 1.006 DCC: 1 DCC for the seller, 0.001 DCC to set
// the script and 0.005 DCC for the release transfer. Then the escrow account locks itself.
const lock = setScript(
  { script: await compileRide(await readFile('escrow.ride', 'utf8'), nodeUrl), chainId: '!' },
  escrowSeed,
);
await broadcast(lock, nodeUrl);
await waitForTx(lock.id, { apiBase: nodeUrl, timeout: 120_000 });

// The goods arrived: the buyer releases the funds to the seller.
const release = transfer(
  {
    recipient: sellerAddress,
    amount: 100_000_000, // 1 DCC
    senderPublicKey: libs.crypto.publicKey(escrowSeed),
    additionalFee: 400_000, // paid by the escrow account: 0.001 + 0.004 DCC
    chainId: '!',
  },
  buyerSeed,
);
await broadcast(release, nodeUrl);
```

Things to settle before locking the account:

* **The escrow account pays the fees.** Fund it with the amount plus what the transactions cost: 0.001 DCC for the Set Script and 0.005 DCC for each transfer out of it.
* **Choose `timeoutHeight` relative to the current height.** At 30-second blocks, 2,880 blocks is about a day. `GET /blocks/height` returns the current height.
* **Everyone must agree on the script before the funds move.** The seller and the arbiter should decompile the deployed script (`GET /addresses/scriptInfo/{address}`, then `POST /utils/script/decompile`) and check it before shipping anything.
* **Use a fresh account.** Throw away its seed after the Set Script transaction. The seed has no power once the script is set, but keeping it around invites confusion.

## Inspecting a Smart Account

`GET /addresses/scriptInfo/{address}` returns the account's compiled `script`, its `complexity`, its `verifierComplexity` and the `extraFee` its transactions must add. If the account has no script, `script` is `null`.

When a transaction is rejected, `broadcast()` rejects with the node's message. It reads `Transaction is not allowed by account-script` when the script returned `false`, and it includes the script's error when the script failed.
