% The code on this page is included verbatim from docs/_samples/sponsorship.ts, which
% CI typechecks against the pinned SDK versions. It was run on the public Testnet on
% 2026-10-27 (token 6r7zhATv5CghU4LWomoknB6uRMkDqW6wSbtZx8G32fiL). Rules from
% node-scala: FeeValidation.scala (fee units, the sponsored-fee conversion) and
% DiffsCommon.processSponsor (issuer only, no smart assets).

# Sponsorship

Every transaction needs a fee, and fees are normally paid in DCC. That is a hurdle for someone who just received your token: before they can send it on, they first have to get DCC. Sponsorship removes it. When you sponsor your token, its holders can pay transaction fees in the token itself, and you pay the DCC fee to the network for them.

## How It Works

1. The token's issuer sends a {ref}`Sponsor Fee transaction <02_decentralchain/03_transaction:Sponsor Fee Transaction>` that sets `minSponsoredAssetFee`: the amount of the token that stands in for 0.001 DCC, one fee unit.
2. A holder sends a Transfer or Invoke Script transaction with `feeAssetId` set to the token and a fee in the token.
3. The fee in the token goes to the issuer. The issuer's account pays the block generator the DCC equivalent: `fee in token × 0.001 / minSponsoredAssetFee` DCC.

| Rule | Detail |
|---|---|
| Who can sponsor | Only the token's issuer |
| Which tokens | Any token without an asset script; a {ref}`smart asset <02_decentralchain/02_token(asset):Smart Asset>` can't be sponsored |
| Which transactions can pay in the token | Transfer and Invoke Script |
| Minimum fee in the token | Fee units × `minSponsoredAssetFee`: 1 unit for a Transfer, 5 for an Invoke Script |
| Cost of the Sponsor Fee transaction | 0.001 DCC |
| Turning it off | Send another Sponsor Fee transaction with `minSponsoredAssetFee` of 0 |

The issuer needs enough DCC to cover the fees it pays. If its DCC balance runs out, transactions that pay their fee in the token are rejected until it is topped up. Watch the issuer's balance, or let users fall back to paying in DCC.

## Choose minSponsoredAssetFee

`minSponsoredAssetFee` is in the token's smallest unit. It sets the exchange rate you accept: with 2 decimals, `10` means 0.10 of your token buys 0.001 DCC of fee. Set it too low and users pay almost nothing while you pay full DCC fees; set it too high and fees feel expensive.

A user may pay more than the minimum. You then receive more of the token and pay more DCC, at the same rate.

## Sponsor a Token with the SDK

This script issues a token, sponsors it, gives a user 10 tokens and has the user send 1 token while paying the fee in the token. Run it as in the {doc}`Quick Start <01_quick-start>`, with an issuer account that holds at least 1.003 DCC and any second account as the user:

```bash
npm install @decentralchain/transactions@5.0.1
```

```{literalinclude} ../_samples/sponsorship.ts
:language: typescript
:lines: 2-
```

On the Testnet, the issuer's DCC balance went from 8.997 to 7.994: 1 DCC to issue the token, 0.001 DCC each for the Sponsor Fee and the transfer to the user, and 0.001 DCC paid for the user's fee. The user's DCC balance did not change. The issuer's token balance is 999,010: the 1,000,000 issued, minus the 1,000 sent to the user, plus the 10 the user paid as the fee.

To sponsor a token you already issued, skip step 1 and set `assetId` to the token's ID.

## Check a Token's Sponsorship

`GET /assets/details/{assetId}` on any node returns `minSponsoredAssetFee`: the current amount, or `null` when the token isn't sponsored.

```bash
curl https://testnet-node.decentralchain.io/assets/details/6r7zhATv5CghU4LWomoknB6uRMkDqW6wSbtZx8G32fiL
```

```json
{"assetId": "6r7zhATv5CghU4LWomoknB6uRMkDqW6wSbtZx8G32fiL", "name": "GiftCard", "decimals": 2, "minSponsoredAssetFee": 10, "...": "..."}
```

## Pay a Fee in a Sponsored Token

As a holder, you need nothing from the issuer: set `feeAssetId` to the token and `fee` to at least the minimum, as in step 4 of the script. Wallets do the same when you choose the token as the fee currency.

A node rejects the transaction if the token is not sponsored (`Asset ... is not sponsored, cannot be used to pay fees`), if the fee is below the minimum, or if the issuer can't pay the DCC fee.
