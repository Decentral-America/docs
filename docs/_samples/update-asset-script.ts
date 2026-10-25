// Illustrates: docs/04_building-apps/10_smart-assets.md, "Replacing the Script"
import { readFile } from 'node:fs/promises';
import { setAssetScript, broadcast } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const issuerSeed = 'issuer secret seed phrase here';
const assetId = '<asset ID from the issue step>';

// Edit allowlist-token.ride first: this sends whatever the file contains as the token's new script.
// The current asset script must allow this transaction, and only the issuer can send it.
const source = await readFile(new URL('./ride/allowlist-token.ride', import.meta.url), 'utf8');
const update = setAssetScript(
  { assetId, script: await compileRide(source, nodeUrl), chainId: '!' }, // fee defaults to 1 DCC
  issuerSeed,
);
await broadcast(update, nodeUrl);
