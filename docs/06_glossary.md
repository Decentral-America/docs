# Glossary

Terms as used across this documentation. Each entry links to the page that defines it in full.

```{glossary}
DCC
  DecentralCoin, the native coin of DecentralChain. Amounts are stored in the smallest unit (`10^-8` DCC). See {ref}`Token (Asset) <02_decentralchain/02_token(asset):Token (Asset)>`.

Chain ID
  A single character identifying the network; it is part of every address and transaction. Mainnet is `?` (63) and Testnet is `!` (33). See {ref}`Mainnet, Testnet <02_decentralchain/08_mainnet-testnet-stagenet:Chain ID>`.

Account
  A key pair plus everything associated with it on chain — balances, data entries, aliases and an optional script. See {ref}`Account <02_decentralchain/01_account:Account>`.

Address
  A Base58 string derived from a public key and the chain ID. Mainnet addresses start with `3D`, Testnet addresses with `31`.

Alias
  A short, human-readable name for an address.

Seed
  The secret phrase from which an account's private key is derived. Never share it.

dApp
  A decentralized application: an account with a Ride script whose `@Callable` functions users invoke with invoke script transactions.

Smart account
  An account with a script that must approve every transaction the account sends.

Smart asset
  A token with a script that must approve every transaction involving it.

Ride
  The statically typed, functional smart-contract language of DecentralChain. See the {ref}`Ride language <03_ride-language/index:Ride Language>` section.

LPoS
  Leased Proof of Stake: the consensus in which accounts can lease DCC to generating nodes. See {ref}`Node <02_decentralchain/05_node:Leased Proof of Stake>`.

NG
  The protocol that streams transactions in microblocks between blocks.

Generating balance
  The balance that counts towards the chance of generating the next block, including leased DCC.

Microblock
  A small batch of transactions appended to the current block before the next key block.

Deterministic Finality
  Feature 25: generators endorse blocks with BLS signatures and a block is final once endorsed by two thirds of committed stake. See {ref}`Finality <02_decentralchain/09_protocol:Finality>`.

Blockchain feature
  A numbered protocol change activated on a network by generator vote or network defaults. See {doc}`Features and Activation <05_node-guide/10_features-and-activation>`.

Node
  Software that validates transactions, stores blocks and serves the REST API.

Matcher
  The service that matches orders on the DecentralChain exchange.

Cubensis Connect
  DecentralChain's browser-extension wallet. See {doc}`Wallet Integration <04_building-apps/04_wallet-integration>`.

DecentralScan
  The DecentralChain block explorer.

Decentralite
  The smallest unit of DCC.
```
