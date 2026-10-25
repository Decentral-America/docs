% Every `npm install` line and every `import ... from '@decentralchain/...'`
% on this page is installed and imported on Node.js 24 by CI
% (docs/scripts/check_install_snippets.py). docs/_samples/smart-asset.ts and
% docs/_samples/update-asset-script.ts typecheck the full examples, and
% docs/scripts/check_ride_samples.py compiles docs/_samples/ride/allowlist-token.ride.

# Smart Assets

A smart asset is a {ref}`token <02_decentralchain/02_token(asset):Token (Asset)>` with an asset script. The node runs the script for every transaction that involves the token and rejects the transaction if the script does not return `true`. Holders cannot opt out, because the rule belongs to the token itself. Typical uses are a token that only approved accounts may hold, a token that cannot move before a given height, or one that can only be traded against a particular asset.

```{note}
Verified against node-scala v1.8.0 on 2026-10-24. The script compiles on the public Testnet node (`DecentralChain v1.8.0-dev-e6248f2408`) and the Mainnet node (`DCC v1.3.5`), and the Issue fee was confirmed with both nodes' `POST /transactions/calculateFee`. The TypeScript is typechecked against the published SDK; it has not been broadcast as part of this documentation pass.
```

## Rules

* **The script must be there from the start.** Pass it in the Issue transaction. A token issued without a script can never get one; the node answers `Cannot set script on an asset issued without a script`.
* **Only the issuer can replace it,** with a Set Asset Script transaction that costs 1 DCC. The current script must approve that transaction too. A script that never allows Set Asset Script can never be changed.
* **It cannot be removed.** A Set Asset Script transaction must carry a script (`Cannot set empty script`), so a smart asset stays smart.
* **It must be an expression.** `CONTENT_TYPE EXPRESSION` with `SCRIPT_TYPE ASSET`, up to 8 KB and a complexity of 4,000.
* **It cannot be sponsored.** Sponsor Fee is refused for a smart asset (`Sponsorship smart assets is disabled.`), so its holders always pay fees in DCC.
* **Every transaction involving it costs 0.004 DCC more,** whatever the script's complexity, for each smart asset involved. Invoke Script transactions are the exception. A transfer of a smart asset costs 0.005 DCC.

## What the Script Checks

The script runs for each of these, with `tx` set to the transaction:

| Transaction or action | Ride type `tx` matches |
|---|---|
| Transfer of the token | `TransferTransaction` |
| Mass Transfer of the token | `MassTransferTransaction` |
| Reissue, Burn | `ReissueTransaction`, `BurnTransaction` |
| Exchange where the token is either asset of the pair | `ExchangeTransaction` |
| Set Asset Script, Update Asset Info for the token | `SetAssetScriptTransaction`, `UpdateAssetInfoTransaction` |
| Invoke Script with the token attached as a payment | `InvokeScriptTransaction` |
| A dApp's `ScriptTransfer`, `Reissue` or `Burn` action on the token | `TransferTransaction`, `ReissueTransaction` or `BurnTransaction`, with `fee` 0 and the dApp as sender |
| A dApp's `invoke()` with the token attached as a payment | `InvokeScriptTransaction` |

The script does not run for the Issue transaction that creates the token. It cannot see proofs, so it cannot check signatures; that is the sender's account script's job. It can read the transaction's other fields and chain state. `this` is the token itself, an {ref}`Asset <03_ride-language/05_structures:Asset>` structure with fields such as `issuer`, `quantity` and `decimals`.

Because dApp actions arrive as ordinary transaction types, one rule for `TransferTransaction` covers both a user's transfer and a dApp paying the token out.

The language side is in {ref}`Asset Script <03_ride-language/04_script-types:Asset Script>`.

## Walkthrough: a Token Only Allowlisted Accounts Can Hold

The issuer keeps an allowlist in its own {ref}`account data storage <02_decentralchain/01_account:Account Data Storage>`: a Boolean entry `allowed_<address>` for each account that may receive the token. Transfers to anyone else fail.

Save as `allowlist-token.ride`:

```text
{-# STDLIB_VERSION 5 #-}
{-# CONTENT_TYPE EXPRESSION #-}
{-# SCRIPT_TYPE ASSET #-}

# The issuer keeps the allowlist in its own account data storage: one Boolean entry
# "allowed_<address>" per account that may receive the token.
func isAllowed(recipient: Address) =
  getBoolean(this.issuer, "allowed_" + toString(recipient)).valueOrElse(false)

match tx {
  # Covers Transfer transactions and ScriptTransfer actions of dApps.
  case t: TransferTransaction => isAllowed(addressFromRecipient(t.recipient))
  case _: ReissueTransaction | BurnTransaction | SetAssetScriptTransaction | UpdateAssetInfoTransaction => true
  # Mass Transfer, Exchange, payments attached to invocations and everything else.
  case _ => false
}
```

The script reads the allowlist each time it runs, so adding or removing an entry takes effect with the next transaction and the script never has to change. Reissue, Update Asset Info and Set Asset Script are allowed because the node already restricts them to the issuer. Burn is allowed so a holder can always destroy their tokens. Mass Transfer, trading on the DEX and attaching the token to a dApp call are rejected outright. Rejecting them is simpler than checking each recipient they might reach.

```bash
npm install @decentralchain/transactions@5.0.1
```

```typescript
import { readFile } from 'node:fs/promises';
import { issue, data, transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const issuerSeed = 'issuer secret seed phrase here';
const memberAddress = '31V87wCDjEtQ31BadgoWkf25EK4n11kvfTA';

// 1. Issue the token with its script. A token issued without a script can never get one.
const issueTx = issue(
  {
    name: 'ClubPass',
    description: 'Transferable only to allowlisted accounts',
    quantity: 1_000,
    decimals: 0,
    reissuable: true,
    script: await compileRide(await readFile('allowlist-token.ride', 'utf8'), nodeUrl),
    chainId: '!',
  },
  issuerSeed,
);
await broadcast(issueTx, nodeUrl);
await waitForTx(issueTx.id, { apiBase: nodeUrl, timeout: 120_000 });

// 2. Allowlist a member in the issuer's account data storage.
const allow = data(
  { data: [{ key: `allowed_${memberAddress}`, type: 'boolean', value: true }], chainId: '!' },
  issuerSeed,
);
await broadcast(allow, nodeUrl);
await waitForTx(allow.id, { apiBase: nodeUrl, timeout: 120_000 });

// 3. Send the member 10 tokens. Every transaction involving the token pays 0.004 DCC extra.
const send = transfer(
  { recipient: memberAddress, amount: 10, assetId: issueTx.id, additionalFee: 400_000, chainId: '!' },
  issuerSeed,
);
await broadcast(send, nodeUrl);
console.log('Asset ID:', issueTx.id, 'issuer:', libs.crypto.address(issuerSeed, '!'));
```

The issuer pays 1 DCC for the Issue, 0.001 DCC for the Data transaction and 0.005 DCC for the transfer. The token's ID is the ID of its Issue transaction.

A transfer to an account that is not on the list fails at broadcast with the node's message `Transaction is not allowed by token-script`. If the script throws instead of returning `false`, the message starts with `Error while executing token-script:`. The issuer is not on its own list, so tokens cannot be sent back to it unless it adds `allowed_<issuer address>` as well.

## Replacing the Script

The issuer can replace the script, for example to also allow Mass Transfer, as long as the current script allows Set Asset Script:

```typescript
import { readFile } from 'node:fs/promises';
import { setAssetScript, broadcast } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const issuerSeed = 'issuer secret seed phrase here';
const assetId = '<asset ID from the issue step>';

// The current asset script must allow this transaction, and only the issuer can send it.
const update = setAssetScript(
  { assetId, script: await compileRide(await readFile('allowlist-token.ride', 'utf8'), nodeUrl), chainId: '!' }, // fee defaults to 1 DCC
  issuerSeed,
);
await broadcast(update, nodeUrl);
```

If the issuer is a smart account with a verifier complexity above 200, add `additionalFee: 400_000` to both the Issue and the Set Asset Script transaction.

## Inspecting a Smart Asset

`GET /assets/details/{asset ID}` returns the token's parameters. For a smart asset it also returns `scripted: true` and a `scriptDetails` object with the compiled `script` and its `scriptComplexity`. `POST /utils/script/decompile` turns that script back into Ride source.
