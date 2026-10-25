// Illustrates: docs/04_building-apps/09_smart-accounts.md, "Walkthrough: an Escrow Account"
import { readFile } from 'node:fs/promises';
import { setScript, transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const escrowSeed = 'escrow account secret seed phrase here';
const buyerSeed = 'buyer secret seed phrase here';
const sellerAddress = '31VgE1dHbGoMeesqWFVr6GoSdB7zX4wS1w8';

// The buyer funds the escrow account with 1.006 DCC: 1 DCC for the seller, 0.001 DCC to set
// the script and 0.005 DCC for the release transfer. Then the escrow account locks itself.
const source = await readFile(new URL('./ride/escrow.ride', import.meta.url), 'utf8');
const lock = setScript({ script: await compileRide(source, nodeUrl), chainId: '!' }, escrowSeed);
await broadcast(lock, nodeUrl);
await waitForTx(lock.id, { apiBase: nodeUrl, timeout: 120_000 });

// The goods arrived: the buyer releases the funds to the seller.
const release = transfer(
  {
    recipient: sellerAddress,
    amount: 100_000_000, // 1 DCC
    senderPublicKey: libs.crypto.publicKey(escrowSeed),
    additionalFee: 400_000, // paid by the escrow account: 0.001 + 0.004 DCC
    chainId: '!',
  },
  buyerSeed,
);
await broadcast(release, nodeUrl);
