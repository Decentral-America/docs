// Illustrates: docs/09_user-guides/04_leasing.md, "Lease with the SDK"
import { lease, cancelLease, broadcast, waitForTx, libs } from '@decentralchain/transactions';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const seed = 'your secret seed phrase here';
const generator = '31RPEKcz71a3hdxt8z7qLhTpRMuRV2kUyr6'; // the generating node's address
const myAddress = libs.crypto.address(seed, '!');

// Start a lease of 5 DCC. The DCC stay in your account but can't be spent until you cancel.
const leaseTx = lease({ recipient: generator, amount: 500_000_000, chainId: '!' }, seed);
await broadcast(leaseTx, nodeUrl);
await waitForTx(leaseTx.id, { apiBase: nodeUrl, timeout: 120_000 });
console.log('Lease ID:', leaseTx.id); // the lease ID is the Lease transaction's ID

// Your active leases, and your balance split into available and leased-out DCC
const active = await fetch(`${nodeUrl}/leasing/active/${myAddress}`).then((r) => r.json());
console.log('Active leases:', active.length);
const details = await fetch(`${nodeUrl}/addresses/balance/details/${myAddress}`).then((r) => r.json());
console.log('Available:', details.available, 'Leased out:', details.regular - details.available);

// Cancel the lease. The DCC are spendable again as soon as the cancel is in a block.
const cancelTx = cancelLease({ leaseId: leaseTx.id, chainId: '!' }, seed);
await broadcast(cancelTx, nodeUrl);
await waitForTx(cancelTx.id, { apiBase: nodeUrl, timeout: 120_000 });
console.log('Lease cancelled by', cancelTx.id);
