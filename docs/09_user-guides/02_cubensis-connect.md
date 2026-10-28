% Screen and button names on this page are the extension's English UI strings
% (apps/cubensis-connect/src/i18n/locales/en/extension.en.json in the
% DecentralChain monorepo), and the network list is its NETWORK_CONFIG
% (apps/cubensis-connect/src/constants.ts).

# Cubensis Connect User Guide

Cubensis Connect is the DecentralChain browser wallet. It keeps your seed phrases and private keys encrypted inside the extension and signs transactions for websites without ever showing them your keys. A dApp asks; you see exactly what it wants to sign and approve or reject it.

This page is for people using the wallet. If you are building a dApp that talks to it, see {doc}`Wallet Integration <../04_building-apps/04_wallet-integration>`.

## Install the Extension

Cubensis Connect is not listed in the Chrome, Firefox, Edge or Opera extension stores yet, and it has no published release package. Until it does, build it from source. You need Git and Node.js 24.17 or later.

```bash
git clone https://github.com/Decentral-America/DecentralChain.git
cd DecentralChain
corepack enable        # provides the pnpm version the repository pins
pnpm install
cd apps/cubensis-connect
NODE_ENV=production node scripts/build.mjs
```

The build writes one folder per browser under `apps/cubensis-connect/dist/`: `chrome`, `edge`, `firefox` and `opera`. Then load it:

* **Chrome, Edge, Brave and other Chromium browsers.** Open `chrome://extensions` (`edge://extensions` in Edge), turn on **Developer mode**, click **Load unpacked** and select the `dist/chrome` folder (`dist/edge` for Edge).
* **Firefox.** Open `about:debugging#/runtime/this-firefox`, click **Load Temporary Add-on** and select `dist/firefox/manifest.json`. Firefox removes a temporary add-on when it restarts.

```{note}
These build steps follow the extension's release runbook (`apps/cubensis-connect/docs/RELEASE-RUNBOOK.md`). They were not run for this page.
```

Pin the extension to the toolbar so you can see when a website asks for a signature.

## Create an Account

1. Click the Cubensis Connect icon and then **Get Started**.
2. On **Protect Your Account**, create a password and confirm it, accept the terms and click **Continue**. The password encrypts your accounts on this device only. It is not a recovery method.
3. Click **Create a new account** and pick one of the offered addresses by its avatar. Each avatar belongs to a different new address, so it helps you recognise the account later. You can't change it afterwards.
4. Write down the 15-word backup phrase shown on the next screen, then confirm it by tapping the words in the right order. If you lose the phrase, nobody can restore the account.
5. Give the account a name. The name is stored only in your extension.

## Import an Existing Account

Click **Add account** and choose **Or import via**:

| Option | Use it for |
|---|---|
| **Seed Phrase or Private Key** | The 15 words of an account, a base58-encoded seed (**Encoded seed** tab) or a raw private key (**Private key** tab) |
| **Keystore File** | A file exported from Cubensis Connect with **Export accounts** |
| **Ledger** | A Ledger device with the DCC app open; the keys stay on the device |

An account created with the SDK, for example in the {doc}`Quick Start <01_quick-start>`, imports with its seed phrase.

## Switch Networks

The network menu at the bottom of the popup switches between **Mainnet**, **Testnet**, **Stagenet** and **Custom**. Each network has its own list of accounts, because the same seed phrase gives a different address on each network.

| Network | Chain ID | Node |
|---|---|---|
| Mainnet | `?` | `https://mainnet-node.decentralchain.io` |
| Testnet | `!` | `https://testnet-node.decentralchain.io` |
| Stagenet | `S` | No public Stagenet yet |
| Custom | Any | A node you run, for example on a {doc}`custom blockchain <../05_node-guide/03_custom-blockchain>` |

**Edit** next to the network opens its **Node address** and **Matcher address**, so you can point the wallet at your own node.

To try things out without real money, switch to **Testnet**, copy your address and get free DCC from the [Testnet faucet](https://testnet.decentralscan.com/faucet).

## Send Tokens

Open an asset in the wallet and click **Send**. Fill in the **Recipient** (an address or alias on the same network), the **Amount** and an optional **Attachment** of up to 140 bytes that the recipient sees. Review the confirmation screen, including the fee, and approve it.

## Use a dApp

The first time a website calls Cubensis Connect, the extension asks whether to **Allow access**. Allowing it shares your address and public key with the site, never your seed or private key. If you reject it, the site is blocked and gets the error `Api rejected by user` for every later request, until you allow it in **Permissions control**.

After that, every transaction the site wants opens a confirmation window with the transaction type, amounts, recipient, fee and, for a dApp call, the function and its arguments. Click **Approve** to sign it or **Reject** to refuse. Check the details every time: an approved transaction cannot be undone.

For a site you trust and use often, **Permission details** can allow automatic signing for 15, 30 or 60 minutes up to a **Spending limit**. Leave it at **Don't automatically sign** unless you need it.

## Settings and Safety

**Settings** holds:

* **Permissions control**: the sites you approved or rejected. Revoke a site here at any time.
* **Network**: the node and matcher addresses of each network.
* **Export and import**: save your accounts and address book to an encrypted keystore file, or load one.
* **Session timeout**: how long the extension stays unlocked after you stop using it.
* **Auto-click protection** and **Suspicious assets protection**: defences against scripted clicks and scam tokens.
* **Change password**, **Change language** and **Delete accounts**.

If you forget the password, click **I forgot password** on the login screen. Cubensis Connect cannot decrypt your accounts without it, so the only way back is to delete every account (you type `DELETE ALL ACCOUNTS` to confirm), set a new password and import each account again from its seed phrase.

Never type your seed phrase into a website. A dApp that works with Cubensis Connect never needs it.
