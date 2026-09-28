# Terminology sheet (internal — not published)

Canonical names. CI fails on the forbidden strings.

| Use | Never use |
|---|---|
| DCC, DecentralCoin | any other project's coin or unit names |
| Decentralite (10^-8 DCC) | smallest-unit names from other chains |
| Cubensis Connect (wallet) | other wallet product names |
| `@decentralchain/*` packages | other vendors' package scopes |
| `decentralchain-{network}.conf`, `dcc.*` config keys | other projects' config prefixes |
| DecentralScan (explorer), Decentral.Exchange | other explorers and exchanges |
| Chain IDs: Mainnet `?` (63), Testnet `!` (33) | any other chain ID |
| Address prefixes: Mainnet `3D`, Testnet `31` | any other prefix |

Baseline: **node-scala v1.7.0**. Every page that states protocol facts should say "Verified against node-scala v1.7.0" (or the version it was checked against).
