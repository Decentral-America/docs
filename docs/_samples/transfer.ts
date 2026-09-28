// Illustrates: docs/04_building-apps/03_how-to-guides.md, "Build, Sign, and Broadcast a Transaction"
// Verified against @decentralchain/transactions' README (2026-08 — see that
// page's top-of-file note about the nodeInteraction.broadcast rename).
import { transfer, broadcast } from '@decentralchain/transactions';

const seed = 'your secret seed phrase here';

// Build and sign a Transfer transaction
const signedTx = transfer(
  {
    recipient: '3DQAabT4dnFEpVf6jabNisvugEyFCGQZ9MF', // recipient address or alias
    amount: 100_000_000,                               // 1 DCC (8 decimals, i.e. 10^8 Decentralites)
  },
  seed,
);

// Broadcast it
const result = await broadcast(signedTx, 'https://nodes.decentralchain.io');
console.log('Transaction ID:', result.id);
