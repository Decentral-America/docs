# Developer Tools

DecentralChain provides several tools to write, test, and deploy RIDE smart contracts without having to interact with the raw node API directly.

## RIDE IDE

[decentralchain-ide.com](https://decentralchain-ide.com/) is a browser-based IDE for RIDE. It provides syntax highlighting, static complexity/type checking, and one-click deployment of account scripts, dApp scripts, and asset scripts to Mainnet or Testnet, without installing anything locally.

## Surfboard

[`surfboard`](https://github.com/Decentral-America/surfboard) is a local development and testing tool for RIDE projects. It lets you compile scripts, run a local development chain, and script deployment/test flows from the command line, which is useful for CI pipelines and for testing dApp logic before deploying to Mainnet or Testnet.

## ride-js

[`ride-js`](https://github.com/Decentral-America/ride-js) provides a JavaScript/TypeScript interface to the RIDE compiler, so scripts can be compiled programmatically as part of a build pipeline or a web-based tool, instead of relying on a separately installed compiler binary.

## Starter Templates

[`dcc-ride-templates`](https://github.com/Decentral-America/dcc-ride-templates) contains ready-to-use RIDE project scaffolding — account scripts, dApp scripts, and asset scripts — as a starting point for new smart contract projects.

For the language itself — syntax, data types, built-in functions, script types, and structures — see the [Ride Language](../03_ride-language/index) section.
