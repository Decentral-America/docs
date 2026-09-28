// Illustrates: docs/04_building-apps/03_how-to-guides.md, "Reading Blockchain Data"
import { create } from '@decentralchain/node-api-js';

const api = create('https://nodes.decentralchain.io');

const { balance } = await api.addresses.fetchBalance('3DQAabT4dnFEpVf6jabNisvugEyFCGQZ9MF');
console.log('DCC balance (in Decentralites):', balance);

const { height } = await api.blocks.fetchHeight();
console.log('Current height:', height);
