// Illustrates: docs/09_user-guides/01_quick-start.md, "Step 4: Send Your First Transfer"
import { transfer, broadcast, waitForTx } from '@decentralchain/transactions';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const seed = 'your secret seed phrase here';           // the seed phrase from step 2
const recipient = '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9'; // any Testnet address or alias

const tx = transfer(
  {
    recipient,
    amount: 100_000_000, // 1 DCC: amounts are in Decentralites, 10^8 per DCC
    chainId: '!',        // Testnet
  },
  seed,
);

await broadcast(tx, nodeUrl);
console.log('Broadcast, transaction ID:', tx.id);

// A 200 from broadcast means the node accepted it into its pool. Wait for a block.
const confirmed = await waitForTx(tx.id, { apiBase: nodeUrl, timeout: 120_000 });
console.log('In block at height', confirmed.height);
console.log(`https://testnet.decentralscan.com/transaction?id=${tx.id}`);
