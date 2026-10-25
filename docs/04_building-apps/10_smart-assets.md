% The code on this page is included verbatim from docs/_samples/: CI typechecks
% smart-asset.ts and update-asset-script.ts, docs/scripts/check_ride_samples.py
% compiles ride/allowlist-token.ride, and docs/scripts/check_install_snippets.py
% installs and imports the `npm install` line below.

# Smart Assets

A smart asset is a {ref}`token <02_decentralchain/02_token(asset):Token (Asset)>` with an asset script. The node runs the script for every transaction that involves the token and rejects the transaction if the script does not return `true`. Holders cannot opt out, because the rule belongs to the token itself. Typical uses are a token that only approved accounts may hold, a token that cannot move before a given height, or one that can only be traded against a particular asset.

```{note}
Verified against node-scala v1.8.0 on 2026-10-25. The script compiles on the public Testnet node (`DecentralChain v1.8.0-dev-e6248f2408`) and the Mainnet node (`DCC v1.3.5`), and the Issue fee was confirmed with both nodes' `POST /transactions/calculateFee`. The TypeScript is typechecked against the published SDK; it has not been broadcast as part of this documentation pass.
```

## Rules

* **The script must be there from the start.** Pass it in the Issue transaction. A token issued without a script can never get one; the node answers `Cannot set script on an asset issued without a script`.
* **Only the issuer can replace it,** with a Set Asset Script transaction that costs 1 DCC, surcharge included. The current script must approve that transaction too. A script that never allows Set Asset Script can never be changed.
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

Save as `ride/allowlist-token.ride`, in a `ride` folder next to your scripts:

```{literalinclude} ../_samples/ride/allowlist-token.ride
:language: text
:lines: 2-
```

The script reads the allowlist each time it runs, so adding or removing an entry takes effect with the next transaction and the script never has to change. Reissue, Update Asset Info and Set Asset Script are allowed because the node already restricts them to the issuer. Burn is allowed so a holder can always destroy their tokens. Mass Transfer, trading on the DEX and attaching the token to a dApp call are rejected outright. Rejecting them is simpler than checking each recipient they might reach.

```bash
npm install @decentralchain/transactions@5.0.1
```

The example imports `compileRide` from {ref}`Compile a Script <04_building-apps/07_smart-contracts-overview:Compile a Script>`. The member address belongs to a throwaway example account; use real ones.

```{literalinclude} ../_samples/smart-asset.ts
:language: typescript
:lines: 2-
```

The issuer pays 1 DCC for the Issue, 0.001 DCC for the Data transaction and 0.005 DCC for the transfer. The token's ID is the ID of its Issue transaction.

A transfer to an account that is not on the list fails at broadcast with the node's message `Transaction is not allowed by token-script`. If the script throws instead of returning `false`, the message starts with `Error while executing token-script:`. The issuer is not on its own list, so tokens cannot be sent back to it unless it adds `allowed_<issuer address>` as well.

## Replacing the Script

To change the rules, for example to also allow Mass Transfer, edit `ride/allowlist-token.ride` and send the new version as long as the current script allows Set Asset Script:

```{literalinclude} ../_samples/update-asset-script.ts
:language: typescript
:lines: 2-
```

If the issuer is a smart account with a verifier complexity above 200, add `additionalFee: 400_000` to both the Issue and the Set Asset Script transaction.

## Inspecting a Smart Asset

`GET /assets/details/{asset ID}` returns the token's parameters. For a smart asset it also returns `scripted: true` and a `scriptDetails` object with the compiled `script` and its `scriptComplexity`. `POST /utils/script/decompile` turns that script back into Ride source.
