# Developer Tools

Tools for writing, testing and deploying Ride scripts on DecentralChain. All of them are developed under the [Decentral-America](https://github.com/Decentral-America) GitHub organization. To call the chain from your own code, see {doc}`Client Libraries and SDK <02_client-libraries-and-sdk>`.

## At a Glance

| Tool | What it's for | State (2026-10-25) |
|---|---|---|
| {ref}`A node's compiler endpoints <04_building-apps/01_developer-tools:Compile with a Node>` | Compile, estimate and decompile scripts | On every node, including the public Testnet node. The method these docs use |
| {doc}`Ride REPL <developer-tools/01_ride-repl>` | Try expressions and read chain state interactively | `@decentralchain/ride-repl@1.6.2` on npm, tested on Node.js 24 |
| {ref}`dcc-ride-templates <04_building-apps/01_developer-tools:Starter Templates>` | Starting points for new contracts | Source repository |
| {ref}`surfboard <04_building-apps/01_developer-tools:Surfboard>` | Command-line compiling and testing | `2.2.6` on npm. Last updated 2022 |
| {ref}`ride-js <04_building-apps/01_developer-tools:ride-js and @decentralchain/ride>` | Compile Ride from JavaScript | Not usable from npm yet |
| DecentralChain IDE | Browser IDE for Ride | No public instance hosted |

## Compile with a Node

Every node compiles Ride for you: `POST /utils/script/compileCode` takes the source as plain text and returns the compiled script, its complexity and any extra fee. It writes nothing to the chain.

```bash
curl -s -X POST -H 'Content-Type: text/plain' \
  --data-binary $'{-# STDLIB_VERSION 6 #-}\n{-# CONTENT_TYPE EXPRESSION #-}\n{-# SCRIPT_TYPE ACCOUNT #-}\nsigVerify(tx.bodyBytes, tx.proofs[0], tx.senderPublicKey)' \
  https://testnet-node.decentralchain.io/utils/script/compileCode
```

```json
{"script":"base64:BgEJAPQDAwgFAnR4CWJvZHlCeXRlcwkAkQMCCAUCdHgGcHJvb2ZzAAAIBQJ0eA9zZW5kZXJQdWJsaWNLZXkGZtJY","complexity":182,"verifierComplexity":182,"callableComplexities":{},"extraFee":0}
```

The `script` value goes into a Set Script, Set Asset Script or Issue transaction. For a dApp, `callableComplexities` gives the complexity of each callable function. In TypeScript, the `compileRide` helper in {ref}`Compile a Script <04_building-apps/07_smart-contracts-overview:Compile a Script>` wraps this call.

Two more endpoints take a compiled script, the `base64:...` string, as the plain-text body:

* `POST /utils/script/estimate` returns the same complexity figures for an already compiled script.
* `POST /utils/script/decompile` turns a compiled script back into Ride source, for example to read the script on an account you didn't write. Comments and formatting are lost.

## Ride REPL

The {doc}`Ride REPL <developer-tools/01_ride-repl>` evaluates Ride line by line, offline or against a node's live state, from a Node.js script or a web page.

```{toctree}
:hidden:

developer-tools/01_ride-repl
```

## Starter Templates

[`dcc-ride-templates`](https://github.com/Decentral-America/dcc-ride-templates) is a collection of Ride contract templates, shared modules and composition examples to start a new project from. Compile a template with a node before you deploy it, and read the script: a template is a starting point, not an audited contract for your use case.

The runnable examples in these docs are smaller, self-contained contracts with a Testnet walkthrough each: the {doc}`pledge drive <08_creating-and-launching-a-dapp>`, the {doc}`multisig and escrow accounts <09_smart-accounts>`, the {doc}`smart assets <10_smart-assets>`, and the {doc}`token exchange, poll and list-argument dApps <03_how-to-guides>`.

## Surfboard

[`surfboard`](https://github.com/Decentral-America/surfboard) (`@decentralchain/surfboard` on npm) is a command-line tool to compile scripts, run Mocha tests against a node, and script deployments. The repository has not been updated since 2022. Release 2.2.6 still pulls its compiler and transaction library from packages outside the DecentralChain organization, and declares support for Node.js 8, so it is not covered by these docs' checks. For new projects, compile with a node and test with the TypeScript SDK, as the {doc}`How-To Guides <03_how-to-guides>` do.

## ride-js and @decentralchain/ride

[`ride-js`](https://github.com/Decentral-America/ride-js) wraps the Ride compiler for JavaScript. On npm:

* `@decentralchain/ride-js` 2.3.0 depends on compiler packages outside the DecentralChain organization.
* `@decentralchain/ride` 2.3.1, its successor in the monorepo's [`packages/ride/ts`](https://github.com/Decentral-America/DecentralChain/tree/main/packages/ride/ts), can't be installed: its `package.json` still declares `workspace:*` dependencies, and `npm install` fails with `EUNSUPPORTEDPROTOCOL`.

Until a fixed `@decentralchain/ride` release is published, compile with a node.

## DecentralChain IDE

The DecentralChain IDE is a browser IDE for Ride, with syntax highlighting, type and complexity checking, and deployment of account, dApp and asset scripts. No public instance is currently hosted. Use the REPL and a node's compiler instead.

## Explorer and Faucet

* [DecentralScan](https://decentralscan.com/) shows blocks, transactions, accounts, tokens and the data entries of dApps, so you can check the result of every call. The Testnet explorer is at [testnet.decentralscan.com](https://testnet.decentralscan.com/).
* The [Testnet faucet](https://testnet.decentralscan.com/faucet) sends free Testnet DCC to an address starting with `31`.

For the language itself, see the {doc}`Ride Language <../03_ride-language/index>` section.
