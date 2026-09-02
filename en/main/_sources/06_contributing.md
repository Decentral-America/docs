# Contributing

DecentralChain is developed in the open across many repositories under the [Decentral-America](https://github.com/Decentral-America) GitHub organization — the node, SDK packages, wallet, and this documentation site are all separate repos, each accepting contributions.

## Node and Protocol

The node is developed at [node-scala](https://github.com/Decentral-America/node-scala). Fork the repository, work on a feature branch, and open a pull request. For anything beyond a small fix, open an issue first to discuss the change before investing time in an implementation. See the repo's `CODE_OF_CONDUCT.md` for community guidelines.

## SDK and Tooling

Each SDK package ([`transactions`](https://github.com/Decentral-America/transactions), [`node-api-js`](https://github.com/Decentral-America/node-api-js), [`signer`](https://github.com/Decentral-America/signer), [`cubensis-connect`](https://github.com/Decentral-America/cubensis-connect), and the rest listed in [Client Libraries and SDK](04_building-apps/02_client-libraries-and-sdk)) is written in TypeScript under the MIT license:

1. Fork the relevant repository.
2. Create a feature branch (`git checkout -b feature/your-feature-name`).
3. Make your changes, with tests where applicable.
4. Open a pull request with a clear description of the change.

Report bugs or feature requests in the repository the bug actually belongs to, not in this docs repository — include reproduction steps, package version, Node.js version, and network (Mainnet/Testnet) when filing an SDK issue.

## Documentation

This documentation site ([Decentral-America/docs](https://github.com/Decentral-America/docs)) accepts pull requests for corrections, missing content, and new articles. If you spot a gap or an inaccuracy, opening an issue first is welcome, especially before a large rewrite.

The docs are also translated via [Gitlocalize](https://gitlocalize.com/repo/8397) — translation contributions in any of the supported languages are welcome; see the badges on the [repository README](https://github.com/Decentral-America/docs#readme) for current translation coverage per language.
