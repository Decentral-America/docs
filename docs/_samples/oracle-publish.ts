// Illustrates: docs/02_decentralchain/07_oracle.rst, "Example: A Price Oracle"
import { data, broadcast, waitForTx } from '@decentralchain/transactions';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const oracleSeed = 'oracle secret seed phrase here';

// Fetch the value from the outside world. Here it is fixed: 1 DCC = 2.50 USD.
const priceUsd = 2.5;

// Ride has no decimals, so publish an integer with a fixed scale (8 decimal places)
// and the time it was observed, so readers can reject a stale price.
const tx = data(
  {
    data: [
      { key: 'price_DCC_USD', type: 'integer', value: Math.round(priceUsd * 1e8) },
      { key: 'price_DCC_USD_timestamp', type: 'integer', value: Date.now() },
    ],
    chainId: '!',
  },
  oracleSeed,
);
await broadcast(tx, nodeUrl);
await waitForTx(tx.id, { apiBase: nodeUrl, timeout: 120_000 });
console.log('Published in', tx.id);
