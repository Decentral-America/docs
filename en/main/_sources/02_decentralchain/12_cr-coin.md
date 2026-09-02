# CR Coin

CR Coin is an asset issued on DecentralChain mainnet by Blockchain Costa Rica. It is not the network's
native token; DCC is. CR Coin is included here because it is a sponsored asset, meaning holders can
pay DecentralChain network fees with it, and because its supply is capped by the asset itself rather
than by policy.

```{note}
Two documents back this chapter:
{download}`CR Coin tokenomics <../_static/02_decentralchain/downloads/CRCoin-Tokenomics.pdf>` and
{download}`CR Coin holder distribution <../_static/02_decentralchain/downloads/CRCoin-Holder-Distribution.pdf>`,
the latter listing the hundred largest holders. Figures were read from mainnet at height 2,322,445
on 30 August 2026.
```

## The asset

| Property | Value |
|---|---|
| Asset ID | `G9TVbwiiUZd5WxFxoY7Tb6ZPjGGLfynJK4a3aoC59cMo` |
| Issued | 10 August 2021, height 30,008 |
| Issuer | `3DUM611HQFwQcCQDQnA5W92Xs219smEHaaP` |
| Original quantity | 21,000,000 |
| Current supply | 20,999,894.42 (105.58 burned) |
| Reissuable | No |
| Decimals | 8 |
| Sponsored fee | 0.5 CR |
| Holders | 3,844 |

The issue transaction set `reissuable` to false. No transaction mints another CR Coin, and no vote,
key, or upgrade creates one. The cap is a property of the asset, not a commitment that a future key
holder could reverse.

## Distribution

| Holding | CR | Share |
|---|---:|---:|
| Community, already distributed | 12,057,231.10 | 57.42% |
| Issuing wallet | 8,942,663.32 | 42.58% |
| **Total** | **20,999,894.42** | **100%** |

The community holding was airdropped years ago and is liquid today, with no vesting, cliff, or
claw-back. Excluding the issuer, the largest single holder controls 10.54% of circulating CR, and
2,651 addresses hold between 1 and 10,000 CR.

The issuing wallet divides into four buckets, each moving to its own RIDE lock contract:

| Bucket | CR | % of supply |
|---|---:|---:|
| Merchant and adoption | 3,000,000 | 14.29% |
| Treasury reserve | 2,442,663 | 11.63% |
| Team and contributors | 2,000,000 | 9.52% |
| Liquidity | 1,500,000 | 7.14% |

Team and contributors carries a 12-month cliff and a 36-month linear vest, so it unlocks behind the
merchant and liquidity buckets. Circulating supply rises from 57.4% today to 88.4% after four years,
with the treasury reserve locked beyond that.

## Fee sponsorship

CR Coin is a sponsored asset, so a holder can pay a DecentralChain transaction fee in CR Coin rather
than DCC. The node settles it inside the transaction: the sender is debited in CR Coin, and the
issuer is debited the equivalent in DCC and credited the CR Coin.

Two consequences follow. Sponsorship moves CR Coin into the issuing wallet as the network is used,
so left alone it concentrates supply. It is also a redemption path that needs no counterparty, order
book, or permission, backed by the DCC balance of the issuing wallet.

The tokenomics commits every CR Coin received through sponsorship to be burned quarterly by Burn
transaction from a published address. Usage then reduces supply, and each burn is paid for in DCC
from the reserve. If nobody transacts, nothing burns.

```{warning}
The posted rate of 0.5 CR against a 0.001 DCC network fee values one CR Coin at 0.002 DCC, while the
AMM pool prices it near 2.11 DCC. At that rate no holder will choose to pay fees in CR Coin, so
sponsorship is live, funded, and unused until `minSponsoredAssetFee` is repriced.
```

## Open items

The address `3DdSXx71R8bnm8xqeyfvDtwRuPFnhfBAp4A`, aliased `burnaddress` and `burn`, holds 27,262.69
CR. Those coins are held, not burned, and count toward the total above. Only a Burn transaction would
change that.

The asset description written on chain in 2021 cites `crcoin.io`, which has no DNS record.
`blockchaincostarica.org` resolves over HTTP but has no working HTTPS. The description can be
corrected with an UpdateAssetInfo transaction.

No lock contract has been deployed. Until one is, the issuing wallet remains fully liquid.
