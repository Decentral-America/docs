# Tokenomics

DecentralCoin (DCC) has a fixed supply of 100,000,000, minted in full at genesis on 20 July 2021
and never inflated since. Block reward issuance has never activated, so miners earn transaction
fees and nothing else. This chapter is the official record of how that supply is allocated, when
it unlocks, and what reduces it.

```{note}
The full document, including custody mapping and open risks, is available as a PDF:
{download}`DecentralChain DCC Tokenomics v1.0 <../_static/02_decentralchain/downloads/DecentralChain-DCC-Tokenomics.pdf>`.
Figures were read from mainnet at height 2,322,348 on 30 August 2026.
```

## Supply and issuance

One DCC divides into 100,000,000 dcclets, so every on-chain amount carries eight decimals. Total
supply is 100,000,000 DCC, created in block 1 across four genesis transactions. No DCC has been
issued since.

That follows from feature 14, *Block Reward and Community Driven Monetary Policy*, never having
activated. The mainnet node reports its status as `VOTING`, and `GET /blockchain/rewards` returns
error 199. Miners earn transaction fees only, split under NG at 40% to the block including a
transaction and 60% to the next block's producer.

The node carries a complete reward implementation should feature 14 ever activate: 6 DCC per block
initially, 100,000-block terms, 0.5 DCC vote increments. DecentralChain removed the DAO and buyback
recipients that the upstream design pays a share to, so the entire reward would go to the block
producer. At 60-second blocks that is 3,153,600 DCC per year, an initial inflation rate of 3.15%.

**DecentralChain commits to leaving feature 14 deactivated. Total supply stays at 100,000,000 DCC
permanently.**

Stated plainly: feature activation requires 18,000 votes inside a 20,000-block window, and one
address currently produces 100% of blocks, so that operator could activate feature 14 unilaterally.
The commitment is a governance promise backed by the custody separation described in the PDF. It is
not yet a technical impossibility.

## Current distribution

98,091,614 DCC, or 98.09% of supply, sits in six addresses traceable to the four genesis wallets.
External float is 1,908,386 DCC, of which roughly 900,000 is held in four identifiable wallets, so
genuinely dispersed supply is close to 1,000,000 DCC.

| Address | DCC | Origin |
|---|---:|---|
| `3Dg7jsTxj1gYp359u1hT7dsg8GZEwhii1Kr` | 30,000,098 | genesis |
| `3DTpBtthd1uJE2aRq5iqRY7d7vcp94AFeqe` | 30,000,010 | funded from genesis |
| `3DhKtKgynxyh9K2YrEMLgLBM8AMuLkKdkRn` | 20,039,654 | genesis, sole active block producer |
| `3DYhnLbQUTrd9jKaCzvJx1PULj4GDnAcbYc` | 10,000,000 | genesis, untouched since 2021 |
| `3Dm78oJoNcb1xBtWkjo194u7GgNdV89kvWE` | 5,010,001 | funded from genesis |
| `3DUM611HQFwQcCQDQnA5W92Xs219smEHaaP` | 3,041,851 | genesis |
| **Controlled** | **98,091,614** | **98.09%** |

Balances and transfer history are read from the mainnet node and can be reproduced by anyone.
Custody is a separate claim from balance.

## Allocation

Percentages are given against total supply of 100,000,000.

| Bucket | DCC | % of supply |
|---|---:|---:|
| **Community and ecosystem** | **53,000,000** | **53.00%** |
| Usage and airdrop program | 22,000,000 | 22.00% |
| Validator and staking rewards | 15,000,000 | 15.00% |
| Liquidity | 12,000,000 | 12.00% |
| Grants and integrations | 4,000,000 | 4.00% |
| Treasury reserve | 20,000,000 | 20.00% |
| Team and contributors | 15,000,000 | 15.00% |
| Foundation and operations | 10,000,000 | 10.00% |
| Operating float | 91,614 | 0.09% |

There was never a private round, a seed allocation, or a venture investor, so there is no such line
in the table.

The validator bucket replaces the block reward the chain does not pay. It starts near 2.5M in year
one and tapers toward 1M by year five. Years one through four spend 7.2M, and the remaining 7.8M
covers through year twelve at the floor, meaning a flat 1M per year with no further taper. Part of
it is leased instead of spent: LPoS leasing is non-custodial, so the treasury keeps the coins while
giving a new validator the weight to clear the 10,000 DCC generating minimum.

## Release schedule

Circulating supply today is about 2.0M DCC. At that float, price is undefined and any quoted market
capitalisation is fiction.

| Bucket | Y1 | Y2 | Y3 | Y4 | Beyond |
|---|---:|---:|---:|---:|---:|
| Usage and airdrop | 8.0M | 8.0M | 4.0M | 2.0M | |
| Validator and staking | 2.5M | 2.0M | 1.5M | 1.2M | 7.8M |
| Liquidity | 6.0M | 3.0M | 2.0M | 1.0M | |
| Grants | 1.0M | 1.0M | 1.0M | 1.0M | |
| Foundation | 2.0M | 3.0M | 3.0M | 2.0M | |
| Team | 0 | 5.0M | 5.0M | 5.0M | |
| Treasury | 0 | 0 | 0 | 0 | 20.0M |
| **Released** | **19.5M** | **22.0M** | **16.5M** | **12.2M** | **27.8M** |

Circulating supply reaches 21.5M after year one, 43.5M after year two, 60.0M after year three, and
72.2M after year four. Team unlocks begin in year two, so the 12-month cliff puts insiders behind
the airdrop cohort.

## Revenue and burn

Supply never rises. It falls when the chain is used, through three sinks, all denominated in DCC.

**AMM protocol fee.** Pools charge 35 basis points per swap. A protocol share, configured at 12%,
routes to a burn address instead of accruing entirely to liquidity providers.

**Matcher fee.** The DEX charges a flat 0.003 DCC per order in dynamic mode. A share routes to the
same burn address.

**Namespace auctions.** Short aliases and premium asset tickers sell by Dutch auction, paid in DCC,
burned in full. This sink prices scarcity of names, not throughput, so it produces burn at low
transaction volume.

```{warning}
Two of the three sinks are not yet live. The AMM protocol fee is configured on chain but the
deployed PoolCore contract never reads `config:protocolFeePct`, so `applySwap` skims nothing.
The auction mechanism does not exist yet. Only the matcher fee is live.
```

## Status

Version 1.0, 30 August 2026. The allocation and schedule become binding once the RIDE lock
contracts are deployed at published addresses, and after that point the contracts govern, not this
page. Changes to total supply would require activating feature 14, which this chapter commits
against.
