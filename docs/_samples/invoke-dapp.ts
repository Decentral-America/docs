// Illustrates: docs/04_building-apps/08_creating-and-launching-a-dapp.md, "Call the dApp"
import { invokeScript, broadcast, waitForTx, nodeInteraction } from '@decentralchain/transactions';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const backerSeed = 'backer secret seed phrase here';
const dApp = '31fYMsRvDstHkCPfswAEvpEUVSReqwWVvjP'; // the campaign account from the deploy step

const pledge = invokeScript(
  {
    dApp,
    call: { function: 'pledge', args: [] },
    payment: [{ assetId: null, amount: 100_000_000 }], // 1 DCC
    chainId: '!',
  },
  backerSeed,
);
await broadcast(pledge, nodeUrl);
const info = await waitForTx(pledge.id, { apiBase: nodeUrl, timeout: 120_000 });
console.log('Application status:', info.applicationStatus);

// The callable's data entries are now in the dApp's account data storage.
const total = await nodeInteraction.accountDataByKey('total', dApp, nodeUrl);
console.log('Total pledged (Decentralites):', total?.value);
