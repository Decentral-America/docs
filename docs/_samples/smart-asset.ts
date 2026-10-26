// Illustrates: docs/04_building-apps/10_smart-assets.md, "Walkthrough: a Token Only Allowlisted Accounts Can Hold"
import { readFile } from 'node:fs/promises';
import { issue, data, transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const issuerSeed = 'issuer secret seed phrase here';
const memberAddress = '31V87wCDjEtQ31BadgoWkf25EK4n11kvfTA';

// 1. Issue the token with its script. A token issued without a script can never get one.
const source = await readFile(new URL('./ride/allowlist-token.ride', import.meta.url), 'utf8');
const issueTx = issue(
  {
    name: 'ClubPass',
    description: 'Transferable only to allowlisted accounts',
    quantity: 1_000,
    decimals: 0,
    reissuable: true,
    script: await compileRide(source, nodeUrl),
    chainId: '!',
  },
  issuerSeed,
);
await broadcast(issueTx, nodeUrl);
await waitForTx(issueTx.id, { apiBase: nodeUrl, timeout: 120_000 });

// 2. Allowlist a member in the issuer's account data storage.
const allow = data(
  { data: [{ key: `allowed_${memberAddress}`, type: 'boolean', value: true }], chainId: '!' },
  issuerSeed,
);
await broadcast(allow, nodeUrl);
await waitForTx(allow.id, { apiBase: nodeUrl, timeout: 120_000 });

// 3. Send the member 10 tokens. Every transaction involving the token pays 0.004 DCC extra.
const send = transfer(
  { recipient: memberAddress, amount: 10, assetId: issueTx.id, additionalFee: 400_000, chainId: '!' },
  issuerSeed,
);
await broadcast(send, nodeUrl);
console.log('Asset ID:', issueTx.id, 'issuer:', libs.crypto.address(issuerSeed, '!'));
