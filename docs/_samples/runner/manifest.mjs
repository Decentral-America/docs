// How run-samples.mjs runs each sample against the public Testnet.
//
// A sample not listed here still runs, with the defaults: every
// '<role> secret seed phrase here' placeholder becomes a fresh account funded
// with DEFAULT_FUND_DCC, the example recipient becomes the CI account, and the
// sample passes when it exits with status 0. List a sample here only when it
// needs more than that. Listed samples run first, in this order, so a sample
// can use what an earlier one captured.
//
// Fields (all optional):
//   readOnly  true: needs no account and no DCC.
//   skip      Why the sample can't run unattended. It is reported, not run.
//   helper    Why the file is not a sample (a module other samples import).
//   roles     Placeholder role -> run-wide role name, to share one account
//             between samples (default: an account of this sample only).
//   fund      Role -> DCC to send it before the sample runs (default
//             DEFAULT_FUND_DCC for each role).
//   replace   Exact source text -> replacement: 'ci' (the CI account's
//             address), 'address:<role>' or 'capture:<name>' (in quotes in
//             the source), or any other string, used as is.
//   capture   Name -> regular expression whose first group, found in the
//             sample's output, is kept for later samples.
//   expect    Regular expression the output must match, for samples that
//             catch their own errors and still exit with status 0.
//   ride      Ride file in ride/ -> { exact text -> replacement }, applied to
//             the run's copy of the script before the sample runs. For
//             scripts that name example accounts by public key:
//             'publicKey:<role>' or 'publicKey:ci' becomes base58'<key>'.

export const DEFAULT_FUND_DCC = 1.5;

// The example recipient most samples send to. The runner sends to the CI
// account instead, so the DCC come back.
export const EXAMPLE_RECIPIENT = "'31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9'";

export const samples = {
  'compile-ride.ts': { helper: 'compileRide() for the samples that deploy a script; they exercise it' },
  'ride-repl-types.d.ts': { helper: 'type declarations for ride-repl.ts' },
  'wallet-signer.ts': {
    skip: 'needs a browser with the Cubensis Connect extension for the user to approve the login and the transfer',
  },

  // Read-only
  'read-balance.ts': { readOnly: true },
  'quick-start-account.ts': { readOnly: true },
  'ride-repl.ts': { readOnly: true },
  'data-service-candles.ts': {
    readOnly: true,
    // Any asset traded on the Testnet matcher: DCCCANARY
    replace: { "'<price asset ID>'": "'Hs5y6vFumpwVp6my7rVEmJEQQD3wiQ29qJhnixNqPit5'" },
  },

  // Transfers and tokens
  'transfer.ts': { fund: { your: 1.01 } },
  'quick-start-transfer.ts': { fund: { your: 1.01 } },
  'connect-and-broadcast.ts': { fund: { your: 1.01 }, expect: /Transaction ID: \w+/ },
  'chained-transfer.ts': { fund: { funder: 2.01, 'new account': 0 } },
  'payments.ts': { fund: { customer: 2.51 } },
  'issue-token.ts': { fund: { your: 1.0 } },
  'lease.ts': { fund: { your: 5.01 } },
  'sponsorship.ts': {
    roles: { issuer: 'giftIssuer' },
    fund: { issuer: 1.01, user: 0 },
    capture: { giftToken: /Token: (\w+)/ },
  },
  'airdrop.ts': {
    roles: { 'token holder': 'giftIssuer' },
    fund: { 'token holder': 0.01 },
    replace: { "'your token ID here'": 'capture:giftToken' },
  },
  'oracle-publish.ts': { fund: { oracle: 0.01 } },

  // Matcher
  'matcher-order.ts': { roles: { your: 'matcherTrader' }, fund: { your: 0.01 } },
  'matcher-history.ts': { roles: { your: 'matcherTrader' }, fund: { your: 0 } },

  // Smart contracts
  'deploy-dapp.ts': { roles: { 'campaign account': 'campaign' }, fund: { 'campaign account': 0.02 } },
  'invoke-dapp.ts': {
    fund: { backer: 1.01 },
    replace: { "'31fYMsRvDstHkCPfswAEvpEUVSReqwWVvjP'": 'address:campaign' },
  },
  'smart-asset.ts': {
    roles: { issuer: 'clubIssuer' },
    fund: { issuer: 1.02 },
    capture: { clubPass: /Asset ID: (\w+)/ },
  },
  'update-asset-script.ts': {
    roles: { issuer: 'clubIssuer' },
    fund: { issuer: 1.01 },
    replace: { "'<asset ID from the issue step>'": 'capture:clubPass' },
  },
  'escrow-account.ts': {
    // The buyer only signs; the escrow account holds the amount and pays the fees.
    // The CI account plays the seller, so the payout comes back.
    roles: { buyer: 'escrowBuyer' },
    fund: { 'escrow account': 1.008, buyer: 0 },
    replace: { "'31VgE1dHbGoMeesqWFVr6GoSdB7zX4wS1w8'": 'ci' },
    ride: {
      'escrow.ride': {
        "base58'CPT5HpPYQ1rA8Eot2swk8tuXb4PE5XDhRbQ7Gpp3sr4D'": 'publicKey:escrowBuyer',
        "base58'Emx5RBMowyZLqqn3hX8gGhg4Lgd2UktvDb7UHvHTDjts'": 'publicKey:ci',
      },
    },
  },
  'multisig-account.ts': {
    roles: { 'owner A': 'multisigOwnerA', 'owner C': 'multisigOwnerC' },
    fund: { 'shared account': 1.02, 'owner A': 0, 'owner C': 0 },
    ride: {
      'multisig-2-of-3.ride': {
        "base58'Ch79CxM7xSWXsQ6o1MughNW7ELHaMwJDqV8FDTZMrosq'": 'publicKey:multisigOwnerA',
        "base58'7g2vpXFYV75q2QWuQipD5VwbUdkJuqyi92U9nqbumdLV'": 'publicKey:multisigOwnerC',
      },
    },
  },
  'list-argument.ts': { fund: { 'dApp account': 0.02, caller: 0.01 } },
  'token-exchange.ts': { fund: { 'exchange account': 1.03, trader: 5.02 } },
  'voting.ts': { fund: { 'poll account': 0.02, voter: 0.01 } },
};

// Java samples (java/src/main/java/samples), run with Maven after the
// TypeScript ones. Same fields; the placeholder is the Java string literal.
export const javaSamples = {
  'CreateAccount.java': { readOnly: true },
  'ConnectToTestnet.java': { readOnly: true },
  'SendTransfer.java': { fund: { your: 1.01 }, expect: /Transaction ID: \w+/ },
};
