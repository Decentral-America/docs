![github_pages_workflow](https://github.com/Decentral-America/docs/actions/workflows/github_pages_workflow.yml/badge.svg)
<a href="https://gitlocalize.com/repo/8397/whole_project?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/whole_project/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/ar?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/ar/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/bn?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/bn/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/de?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/de/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/es?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/es/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/fr?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/fr/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/hi?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/hi/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/ja?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/ja/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/pt?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/pt/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/ru?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/ru/badge.svg" /> </a>
<a href="https://gitlocalize.com/repo/8397/zh?utm_source=badge"> <img src="https://gitlocalize.com/repo/8397/zh/badge.svg" /> </a>

# DecentralChain

## Documentation

The GitHub-Pages-hosted documentation of this repository can be viewed here:

 * http://docs.decentralchain.io/

---

## 📋 Table of Contents

1. [What is DecentralChain?](#-what-is-decentralchain)
2. [Blockchain Architecture](#️-blockchain-architecture)
3. [Core Features](#-core-features)
4. [Use Cases](#-use-cases)
5. [Developer SDK & Tooling Ecosystem](#-developer-sdk--tooling-ecosystem)
6. [How the SDK Connects to DecentralChain](#-how-the-sdk-connects-to-decentralchain)
7. [Transaction Types Reference](#-transaction-types-reference)
8. [Network Information](#-network-information)
9. [RIDE Smart Contract Language](#-ride-smart-contract-language)
10. [Cubensis Connect — Browser Wallet Extension](#-cubensis-connect--browser-wallet-extension)
11. [Contributing](#-contributing)
12. [License](#-license)

---

## ⛓️ What is DecentralChain?

**DecentralChain** is a Layer-1 blockchain platform built for decentralized applications, digital assets, DeFi, and NFTs. It is a high-performance, **Leased Proof-of-Stake** blockchain engineered for speed, scalability, and ultra-low transaction fees.

| Property | Value |
|---|---|
| **Native Token** | **DCC** (DecentralChain Coin) |
| **Consensus** | Leased Proof of Stake (LPoS) |
| **Account Model** | Account-based with built-in asset issuance |
| **Smart Contracts** | RIDE — purpose-built, Turing-incomplete language |
| **Mainnet Node** | `https://mainnet-node.decentralchain.io/` |
| **Mainnet Matcher (DEX)** | `https://mainnet-matcher.decentralchain.io/` |
| **Documentation** | `http://docs.decentralchain.io/` |
| **GitHub Organization** | `https://github.com/Decentral-America` |

DecentralChain features a unique **account-based model with built-in asset issuance** — developers can create and issue custom tokens directly at the protocol level without writing or deploying smart contracts. Smart contracts (written in RIDE) are available for advanced programmable logic, enabling dApps, smart assets, and decentralized exchanges.

---

## 🏗️ Blockchain Architecture

DecentralChain is designed from the ground up for performance and developer ergonomics. Here is how the core architecture works:

### Consensus: Leased Proof of Stake (LPoS)

Token holders can **lease DCC to full nodes** to increase the node's effective mining power — without transferring ownership or losing custody of their tokens. Leasers earn a share of block rewards proportional to their leased stake. This makes participation in consensus accessible to all DCC holders without requiring them to run a node.

### Block Production

- **Block time**: ~60 seconds average
- Blocks are produced by nodes with the highest effective balance (own balance + leased balance)
- Fair block reward distribution to both node operators and leasers

### Transaction Model

- **16 transaction types** natively supported at the protocol level (no need for smart contracts to transfer tokens or issue assets)
- Native types include: Issue, Transfer, Reissue, Burn, Lease, Lease Cancel, Create Alias, Mass Transfer, Data Transaction, Set Script, Sponsor Fee, Set Asset Script, Invoke Script, and more
- **Protobuf serialization**: All transactions are serialized using Protocol Buffers for maximum efficiency and interoperability

### Account Model

Every DecentralChain address has:
- A **balance** of DCC and any issued tokens
- **On-chain data storage** — arbitrary key-value pairs stored directly in the account state
- An optional **script** attached — turning a regular account into a smart account or a dApp

### Smart Assets

Any token issued on DecentralChain can have a **RIDE script attached**, enabling conditional transfer logic enforced at the protocol level. For example: KYC-gated tokens, non-transferable certificates, or game items with on-chain transfer rules.

### dApps

Accounts can be converted into **decentralized applications (dApps)** by attaching callable RIDE scripts. dApps expose named callable functions that can be invoked from other accounts via `InvokeScript` transactions. This is the foundation for DeFi protocols, governance systems, NFT marketplaces, and more.

---

## 🚀 Core Features

| Feature | Description |
|---|---|
| 🪙 **Token Issuance** | Issue custom tokens in seconds without writing smart contracts |
| 🔁 **DEX (Decentralized Exchange)** | Built-in order matching engine for trading any token pair |
| 📜 **Smart Contracts (RIDE)** | Safe, predictable scripting language for dApps and smart assets |
| 🔗 **Leased Proof of Stake** | Stake without losing custody; lease DCC to earn block rewards |
| 🌉 **ERC-20 Gateway** | Bridge DCC and ERC-20 tokens between Ethereum and DecentralChain |
| 🔐 **Multi-sig & Threshold** | Native multi-signature transaction support at the account level |
| 📦 **Mass Transfers** | Send tokens to up to 100 addresses in a single transaction |
| 🔮 **Oracles** | On-chain data oracle support via Data Transactions |
| 💼 **Sponsored Fees** | Token issuers can sponsor transaction fees, enabling gasless UX for users |
| 🔏 **Ledger Support** | Hardware wallet (Ledger) integration for enterprise-grade key security |

---

## 🌐 Use Cases

DecentralChain's flexible architecture supports a wide range of real-world applications:

- **DeFi** — Lending, borrowing, yield farming, and decentralized exchanges powered by RIDE smart contracts. The built-in DEX matcher enables on-chain order books for any token pair without additional infrastructure.

- **NFTs** — Issue non-fungible tokens natively at the protocol level. Build NFT marketplaces, in-game collectibles, and digital art platforms with smart asset transfer rules.

- **Tokenization** — Tokenize real-world assets — real estate, equity, commodities — with on-chain programmable logic enforced by smart assets and dApps.

- **Enterprise Payments** — Ultra-low-cost mass transfers enable efficient payroll processing, loyalty reward distribution, and supply chain settlement at scale.

- **Identity & Credentials** — Use Data Transactions for on-chain identity, certificates, and verifiable credentials that are permanently stored and publicly auditable.

- **DAO Governance** — Token-weighted voting for decentralized protocol governance using callable dApp scripts and on-chain data storage for vote tallying.

- **Gaming** — In-game assets issued as smart assets with protocol-level transfer rules. Game economies with provably scarce, tradeable items and composable item logic.

---

## 🔧 Developer SDK & Tooling Ecosystem

The [`Decentral-America`](https://github.com/Decentral-America) GitHub organization publishes an open-source SDK and tooling ecosystem for building on DecentralChain. All packages are written in TypeScript with MIT licensing.

| Repository | Language | Description |
|---|---|---|
| [`cubensis-connect`](https://github.com/Decentral-America/cubensis-connect) | TypeScript | Chrome browser extension wallet — lets users securely interact with DecentralChain dApps |
| [`signer`](https://github.com/Decentral-America/signer) | TypeScript | Wallet connection and transaction signing orchestrator for web apps |
| [`decentralchain-signature-adapter`](https://github.com/Decentral-America/decentralchain-signature-adapter) | TypeScript | Multi-provider transaction signing adapter |
| [`transactions`](https://github.com/Decentral-America/transactions) | TypeScript | Build and sign (including multi-sign) all 16 transaction types |
| [`node-api-js`](https://github.com/Decentral-America/node-api-js) | TypeScript | Full Node REST API JavaScript client library |
| [`data-service-client-js`](https://github.com/Decentral-America/data-service-client-js) | TypeScript | HTTP client for the DecentralChain data service API — asset search, tx history, DEX data |
| [`ts-lib-crypto`](https://github.com/Decentral-America/ts-lib-crypto) | TypeScript | Cryptographic primitives — key generation, signing, hashing, base58/base64 encoding |
| [`ts-types`](https://github.com/Decentral-America/ts-types) | TypeScript | Shared TypeScript type definitions for the entire SDK |
| [`data-entities`](https://github.com/Decentral-America/data-entities) | TypeScript | Domain model classes: Asset, Money, OrderPrice |
| [`oracle-data`](https://github.com/Decentral-America/oracle-data) | TypeScript | Oracle data parsing and encoding utilities |
| [`browser-bus`](https://github.com/Decentral-America/browser-bus) | TypeScript | Cross-window browser communication for dApps and wallet extensions |
| [`protobuf-serialization`](https://github.com/Decentral-America/protobuf-serialization) | JavaScript | Protocol Buffer serialization for transactions |
| [`ledger`](https://github.com/Decentral-America/ledger) | TypeScript | Ledger hardware wallet JavaScript interface |
| [`bignumber`](https://github.com/Decentral-America/bignumber) | TypeScript | Arbitrary-precision BigNumber wrapper for the SDK |
| [`parse-json-bignumber`](https://github.com/Decentral-America/parse-json-bignumber) | TypeScript | Safe JSON parser for large numbers — prevents precision loss |
| [`money-like-to-node`](https://github.com/Decentral-America/money-like-to-node) | TypeScript | Convert Money-like objects to blockchain node format |
| [`assets-pairs-order`](https://github.com/Decentral-America/assets-pairs-order) | TypeScript | Determine canonical ordering of asset pairs for DEX |
| [`marshall`](https://github.com/Decentral-America/marshall) | TypeScript | Binary serialization/deserialization for DecentralChain data structures |
| [`cubensis-connect-types`](https://github.com/Decentral-America/cubensis-connect-types) | TypeScript | TypeScript interface definitions for Cubensis Connect |
| [`cubensis-connect-provider`](https://github.com/Decentral-America/cubensis-connect-provider) | TypeScript | Cubensis Connect wallet provider implementation |
| [`dcc-configs`](https://github.com/Decentral-America/dcc-configs) | — | Environment configuration files for DCC network |
| [`dcc-token-filters`](https://github.com/Decentral-America/dcc-token-filters) | — | Token allow/block-list for scam and new token control |
| [`docs`](https://github.com/Decentral-America/docs) | — | This repository — official DecentralChain documentation |

---

## 📡 How the SDK Connects to DecentralChain

The SDK packages work together to provide a complete developer experience — from building and signing transactions to broadcasting them on-chain. Here is the typical flow:

### Server-side / Node.js: Build, Sign & Broadcast

**Step 1 — Install packages:**

```bash
npm install @decentralchain/transactions @decentralchain/node-api-js
```

**Step 2 — Build, sign, and broadcast a Transfer transaction:**

```typescript
import { transfer } from '@decentralchain/transactions';
import { nodeInteraction } from '@decentralchain/node-api-js';

const NODE_URL = 'https://mainnet-node.decentralchain.io';

// Build and sign a Transfer transaction using a seed phrase
const signedTx = transfer(
  {
    recipient: '3P4H4E4DYpaMr84SpAfNNWwSZM5RqQNbmgN', // recipient address or alias
    amount: 100_000_000,                               // 1 DCC (in wavelets, 10^8)
    assetId: null,                                     // null = DCC native token
    fee: 100_000,                                      // 0.001 DCC
    attachment: 'Payment for services',
  },
  'your secret seed phrase here'                       // seed phrase signs the tx
);

// Broadcast to mainnet
const result = await nodeInteraction.broadcast(signedTx, NODE_URL);
console.log('Transaction ID:', result.id);
```

### Browser / dApp: Sign with Cubensis Connect or Signer

In a browser context, users sign transactions with their own wallets using [`cubensis-connect`](https://github.com/Decentral-America/cubensis-connect) and the [`signer`](https://github.com/Decentral-America/signer) orchestrator. Seed phrases and private keys are never exposed to the dApp.

```typescript
import Signer from '@decentralchain/signer';
import CubensisConnectProvider from '@decentralchain/cubensis-connect-provider';

const signer = new Signer({ NODE_URL: 'https://mainnet-node.decentralchain.io' });
signer.setProvider(new CubensisConnectProvider());

// Prompt the user to sign via Cubensis Connect extension
const [broadcastedTx] = await signer
  .transfer({
    recipient: '3P4H4E4DYpaMr84SpAfNNWwSZM5RqQNbmgN',
    amount: 100_000_000,
  })
  .broadcast();

console.log('Transaction ID:', broadcastedTx.id);
```

The `signer` package abstracts over multiple wallet providers — Cubensis Connect, Ledger, seed-based signing — exposing a consistent API regardless of the underlying key management method.

---

## 📄 Transaction Types Reference

DecentralChain natively supports 16 transaction types at the protocol level, eliminating the need for smart contracts to perform common operations like token issuance or leasing.

| Type ID | Name | Description |
|---|---|---|
| 1 | **Genesis** | Initial balance assignment at chain genesis (legacy) |
| 2 | **Payment** | Early DCC payment transaction (legacy, superseded by Transfer) |
| 3 | **Issue** | Create a new token/asset on-chain |
| 4 | **Transfer** | Send tokens to an address or alias |
| 5 | **Reissue** | Increase the supply of a reissuable token |
| 6 | **Burn** | Permanently destroy tokens, reducing total supply |
| 7 | **Exchange** | DEX order matching — settle a matched buy/sell order pair |
| 8 | **Lease** | Lease DCC to a full node for LPoS block rewards |
| 9 | **Lease Cancel** | Cancel an active lease and reclaim full balance control |
| 10 | **Create Alias** | Assign a human-readable alias to an address |
| 11 | **Mass Transfer** | Send tokens to up to 100 recipients in a single transaction |
| 12 | **Data Transaction** | Write arbitrary key-value data to an account's on-chain storage |
| 13 | **Set Script** | Attach a RIDE script to an account (smart account or dApp) |
| 14 | **Sponsor Fee** | Allow users to pay transaction fees in a custom token |
| 15 | **Set Asset Script** | Attach a RIDE script to a smart asset for conditional transfer logic |
| 16 | **Invoke Script** | Call a callable function on a dApp |

---

## 🌍 Network Information

| Parameter | Mainnet | Testnet |
|---|---|---|
| **Network ID / Chain ID** | `?` (63) | `!` (33) |
| **Node API** | `https://mainnet-node.decentralchain.io/` | *(testnet node)* |
| **Matcher (DEX)** | `https://mainnet-matcher.decentralchain.io/` | — |
| **Explorer / Docs** | `http://docs.decentralchain.io/` | — |
| **Native Token** | DCC | DCC |
| **Block Time** | ~60 seconds | ~60 seconds |
| **Consensus** | Leased Proof of Stake (LPoS) | LPoS |

---

## 📜 RIDE Smart Contract Language

**RIDE** is a purpose-built, expression-based smart contract language designed exclusively for the DecentralChain blockchain.

### Key Design Principles

- **Turing-incomplete by design** — Execution cost is deterministic and fully calculable before broadcasting. No unbounded loops; no unexpected failures.
- **Safety and predictability** — Every script's complexity is statically verified at deployment time. Scripts that exceed complexity limits are rejected.
- **Minimal attack surface** — The constrained design eliminates entire classes of vulnerabilities common in Turing-complete languages (re-entrancy, infinite loops, etc.)

### Script Types

| Script Type | Purpose |
|---|---|
| **Account Script (Smart Account)** | Verifier function that controls which transactions are allowed from the account — enables multi-sig and custom signing logic |
| **dApp Script** | Callable functions that can be invoked on-chain via `InvokeScript`; supports `@Callable` annotated functions and a `@Verifier` |
| **Asset Script (Smart Asset)** | Attached to a token; controls whether individual transfers of that token are permitted |

### Development Tools

- **RIDE IDE**: [`https://decentralchain-ide.com/`](https://decentralchain-ide.com/) — browser-based IDE with syntax highlighting, type checking, and one-click deployment
- Complexity limits ensure all scripts execute in bounded time with no infinite loops and no unexpected failures

---

## 🔑 Cubensis Connect — Browser Wallet Extension

**Cubensis Connect** is the primary user-facing wallet for the DecentralChain ecosystem. It is a Chrome browser extension that provides secure key management and dApp integration.

### Security Model

- Seed phrases and private keys are **encrypted locally** and **never exposed to dApps**
- Signs transactions with a user-approval flow — every dApp interaction requires explicit user confirmation
- Each website must be **explicitly approved** by the user before it can access the Cubensis Connect API

### Features

- 🔐 Encrypted local key storage
- 👛 Multiple wallet accounts with easy switching
- ✅ One-click transaction signing for dApps
- 🔗 Full integration with DecentralChain dApps via `window.CubensisConnect` JavaScript API

### JavaScript API (`window.CubensisConnect`)

| Method | Description |
|---|---|
| `auth(data)` | Authenticate a user — returns a signed authentication object proving account ownership |
| `publicState()` | Get the current public state (network, account, balance) |
| `signTransaction(tx)` | Sign a transaction without broadcasting — returns signed tx object |
| `signAndPublishTransaction(tx)` | Sign and broadcast a transaction to the node |
| `signOrder(order)` | Sign a DEX order |
| `encryptMessage(msg, publicKey)` | Encrypt a message for a recipient's public key |
| `decryptMessage(msg, publicKey)` | Decrypt a received encrypted message |
| `on(event, callback)` | Subscribe to wallet events (e.g., account changes, network changes) |

### dApp Integration Example

```typescript
// Check if Cubensis Connect is installed
if (window.CubensisConnect) {
  // Request user authentication
  const authData = await window.CubensisConnect.auth({
    data: 'DecentralChain dApp Login',
  });

  console.log('Authenticated address:', authData.address);

  // Sign and publish a Transfer transaction
  const result = await window.CubensisConnect.signAndPublishTransaction({
    type: 4, // Transfer
    data: {
      recipient: '3P4H4E4DYpaMr84SpAfNNWwSZM5RqQNbmgN',
      amount: { tokens: '1', assetId: 'DCC' },
      fee: { tokens: '0.001', assetId: 'DCC' },
    },
  });

  console.log('Transaction ID:', result.id);
}
```

---

## 🤝 Contributing

We welcome contributions from the community! Here is how to get started:

### For SDK & Tooling Repositories

1. **Fork** the relevant repository from the [`Decentral-America`](https://github.com/Decentral-America) organization
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** — all SDK packages are written in TypeScript
4. **Include tests** where applicable
5. **Open a Pull Request** with a clear description of the changes

### For This Documentation Repository

- The `docs` repository accepts PRs for documentation improvements, corrections, and translations
- Translation contributions via [Gitlocalize](https://gitlocalize.com/repo/8397) are welcome — see the badges at the top of this README
- Open an issue for any documentation gaps or inaccuracies before submitting a large PR

### Reporting Issues

- Open issues in the **appropriate repository** — not the docs repo — for SDK bugs or feature requests
- Include reproduction steps, SDK version, Node.js version, and network (mainnet/testnet) when reporting bugs

---

## 📄 License

Most SDK repositories are released under the **MIT License**. See the individual repository `LICENSE` files for details.

| Repository | License |
|---|---|
| `transactions` | MIT |
| `node-api-js` | MIT |
| `ts-lib-crypto` | MIT |
| `signer` | MIT |
| `cubensis-connect` | MIT |
| All other SDK packages | MIT |

---

<p align="center">
  Built with ❤️ by the <a href="https://github.com/Decentral-America">Decentral America</a> team &nbsp;·&nbsp;
  <a href="http://docs.decentralchain.io/">Documentation</a> &nbsp;·&nbsp;
  <a href="https://github.com/Decentral-America">GitHub</a>
</p>
