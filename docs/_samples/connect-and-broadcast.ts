// Illustrates: docs/04_building-apps/sdk/01_typescript.md, "Connect to the Testnet" and "Sign and Broadcast"
import { transfer, broadcast, waitForTx } from '@decentralchain/transactions';
import { create } from '@decentralchain/node-api-js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const seed = 'your secret seed phrase here';

// Connect: node-api-js is a typed client for the node's REST API
const api = create(nodeUrl);
const { height } = await api.blocks.fetchHeight();
console.log('Testnet height:', height);

// Sign: the builder signs locally, and nothing leaves your machine until you broadcast
const tx = transfer(
  { recipient: '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9', amount: 100_000_000, chainId: '!' },
  seed,
);

// Broadcast, then wait until the transaction is in a block
try {
  await broadcast(tx, nodeUrl);
  await waitForTx(tx.id, { apiBase: nodeUrl, timeout: 120_000 });
  console.log('Transaction ID:', tx.id);
} catch (error) {
  // A rejected transaction throws an Error whose `data` is the node's response
  const reason = (error as { data?: { error: number; message: string } }).data;
  console.error(reason ? `Rejected (${reason.error}): ${reason.message}` : error);
}
