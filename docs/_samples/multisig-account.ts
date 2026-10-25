// Illustrates: docs/04_building-apps/09_smart-accounts.md, "Walkthrough: a 2-of-3 Multisig Account"
import { readFile } from 'node:fs/promises';
import { setScript, transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const sharedSeed = 'shared account secret seed phrase here';
const ownerASeed = 'owner A secret seed phrase here';
const ownerCSeed = 'owner C secret seed phrase here';
const sharedPublicKey = libs.crypto.publicKey(sharedSeed);

// Once: install the script. After this, the shared account's own seed can no longer sign for it.
const source = await readFile(new URL('./ride/multisig-2-of-3.ride', import.meta.url), 'utf8');
const install = setScript({ script: await compileRide(source, nodeUrl), chainId: '!' }, sharedSeed);
await broadcast(install, nodeUrl);
await waitForTx(install.id, { apiBase: nodeUrl, timeout: 120_000 });

// Owner A builds the transfer and signs it into proof 0.
const proposal = transfer(
  {
    recipient: '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9',
    amount: 100_000_000, // 1 DCC
    senderPublicKey: sharedPublicKey, // the account that sends and pays, not the signer
    additionalFee: 400_000, // the script's complexity is above 200
    chainId: '!',
  },
  [ownerASeed],
);

// Owner C receives the proposal (for example as JSON), checks it and adds a signature to proof 2.
const approved = transfer(proposal, [null, null, ownerCSeed]);
await broadcast(approved, nodeUrl);
