// Illustrates: docs/04_building-apps/03_how-to-guides.md, "Build, Sign, and Broadcast a Transaction"
// Verified against @decentralchain/transactions' README (2026-08 — see that
// page's top-of-file note about the nodeInteraction.broadcast rename).
import { transfer, broadcast } from '@decentralchain/transactions';

const seed = 'your secret seed phrase here';

// Build and sign a Transfer transaction
const signedTx = transfer(
  {
    recipient: '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9', // recipient address or alias (Testnet)
    amount: 100_000_000,                               // 1 DCC (8 decimals, i.e. 10^8 Decentralites)
    chainId: '!',                                      // Testnet chain ID
  },
  seed,
);

// Broadcast it
const result = await broadcast(signedTx, 'https://testnet-node.decentralchain.io');
console.log('Transaction ID:', result.id);
