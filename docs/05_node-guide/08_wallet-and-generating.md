# Node Wallet and Block Generation

```{note}
Verified against node-scala v1.7.0.
```

## The node wallet

A node keeps an encrypted wallet file at `dcc.wallet.file` (default `<directory>/wallet/wallet.dat`). It holds the accounts the node may sign for — most importantly the account that generates blocks.

The wallet stores a **base seed**, from which account keys are derived. It is not an account seed itself. If `dcc.wallet.seed` is not set, the node generates a new one on first start. To use an existing seed, set `dcc.wallet.seed` (Base58) and `dcc.wallet.password`, or pass `DCC_WALLET_SEED` and `DCC_WALLET_PASSWORD` to the Docker image.

```{warning}
Whoever holds the seed controls the funds. Keep secrets in a `chmod 600` `.env` file or a secrets manager, never in shell history or a committed file.
```

## Wallet endpoints

These require the [API key](05_configuration):

```bash
curl -H 'X-Api-Key: my-secret-api-key' http://localhost:6869/addresses            # list wallet addresses
curl -X POST -H 'X-Api-Key: my-secret-api-key' http://localhost:6869/addresses    # derive a new address
curl http://localhost:6869/addresses/balance/<address>                            # public balance query
```

## Generating blocks

A node produces blocks when a wallet account meets the generating-balance requirement under {ref}`Leased Proof of Stake <02_decentralchain/05_node:Leased Proof of Stake>` — its own DCC plus DCC leased to it. To grow a generating balance, other accounts can lease to the node's address.

Check what the miner sees with the privileged `/debug/minerInfo` endpoint, which lists each generating account and its mining balance.

For reward economics and the block-reward vote, see the {ref}`Node <02_decentralchain/05_node:Node>` article.
