// Illustrates: docs/04_building-apps/03_how-to-guides.md, "Sending a Transaction That Depends on Another"
import { transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const funderSeed = 'funder secret seed phrase here';
const newAccountSeed = 'new account secret seed phrase here';
const newAccountAddress = libs.crypto.address(newAccountSeed, '!');

// Parent: fund a new, empty account
const parent = transfer(
  { recipient: newAccountAddress, amount: 200_000_000, chainId: '!' },
  funderSeed,
);
await broadcast(parent, nodeUrl);

// The node validates new transactions against block (liquid) state only, not against other
// unconfirmed transactions. Wait until the parent is in a block before spending its output.
await waitForTx(parent.id, { apiBase: nodeUrl, timeout: 120_000 });

// Child: spends the funds the parent delivered. Broadcasting it before waitForTx resolves
// is rejected with HTTP 400 ("negative dcc balance").
const child = transfer(
  { recipient: '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9', amount: 100_000_000, chainId: '!' },
  newAccountSeed,
);
await broadcast(child, nodeUrl);
