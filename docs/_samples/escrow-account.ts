// Illustrates: docs/04_building-apps/09_smart-accounts.md, "Walkthrough: an Escrow Account"
import { readFile } from 'node:fs/promises';
import { data, setScript, transfer, broadcast, waitForTx, libs, nodeInteraction } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const escrowSeed = 'escrow account secret seed phrase here';
const buyerSeed = 'buyer secret seed phrase here';
const sellerAddress = '31VgE1dHbGoMeesqWFVr6GoSdB7zX4wS1w8'; // example address: use the seller's own
const amount = 100_000_000; // 1 DCC

// The buyer funds the escrow account with the amount plus 0.008 DCC for its three transactions:
// 0.001 for the settings, 0.002 for the script (1,043 bytes) and 0.005 for the payout.

// 1. Write the settings while the escrow account still signs normally.
const timeoutHeight = (await nodeInteraction.currentHeight(nodeUrl)) + 20_160; // about a week of 30-second blocks
const settings = data(
  {
    data: [
      { key: 'amount', type: 'integer', value: amount },
      { key: 'timeoutHeight', type: 'integer', value: timeoutHeight },
    ],
    chainId: '!',
  },
  escrowSeed,
);
await broadcast(settings, nodeUrl);
await waitForTx(settings.id, { apiBase: nodeUrl, timeout: 120_000 });

// 2. Lock the account with the escrow script.
const source = await readFile(new URL('./ride/escrow.ride', import.meta.url), 'utf8');
const lock = setScript({ script: await compileRide(source, nodeUrl), chainId: '!' }, escrowSeed);
await broadcast(lock, nodeUrl);
await waitForTx(lock.id, { apiBase: nodeUrl, timeout: 120_000 });

// 3. The goods arrived: the buyer releases the funds to the seller.
const release = transfer(
  {
    recipient: sellerAddress,
    amount, // must equal the stored amount
    fee: 500_000, // must equal the script's payoutFee: 0.001 + 0.004 DCC
    senderPublicKey: libs.crypto.publicKey(escrowSeed),
    chainId: '!',
  },
  buyerSeed,
);
await broadcast(release, nodeUrl);
