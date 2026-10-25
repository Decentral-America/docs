// Illustrates: docs/04_building-apps/08_creating-and-launching-a-dapp.md, "Configure and Deploy"
import { readFile } from 'node:fs/promises';
import { data, setScript, broadcast, waitForTx, libs, nodeInteraction } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const campaignSeed = 'campaign account secret seed phrase here';
const beneficiary = '31ekkhvBGr91ygJf4st72hAEVU9BUBs3Ats'; // receives the DCC if the goal is met

// 1. Write the settings while the account still signs normally.
const deadline = (await nodeInteraction.currentHeight(nodeUrl)) + 2_880; // about one day of 30-second blocks
const settings = data(
  {
    data: [
      { key: 'beneficiary', type: 'string', value: beneficiary },
      { key: 'goal', type: 'integer', value: 500_000_000 }, // 5 DCC
      { key: 'deadline', type: 'integer', value: deadline },
    ],
    chainId: '!',
  },
  campaignSeed,
);
await broadcast(settings, nodeUrl);
await waitForTx(settings.id, { apiBase: nodeUrl, timeout: 120_000 });

// 2. Compile the dApp script and set it on the same account.
const source = await readFile(new URL('./ride/pledge-drive.ride', import.meta.url), 'utf8');
const script = await compileRide(source, nodeUrl);
const deploy = setScript({ script, chainId: '!' }, campaignSeed);
await broadcast(deploy, nodeUrl);
await waitForTx(deploy.id, { apiBase: nodeUrl, timeout: 120_000 });

console.log('dApp address:', libs.crypto.address(campaignSeed, '!'));
