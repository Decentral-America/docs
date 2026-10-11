// Illustrates: docs/04_building-apps/03_how-to-guides.md, "Reading Blockchain Data"
import { create } from '@decentralchain/node-api-js';

const api = create('https://testnet-node.decentralchain.io');

const { balance } = await api.addresses.fetchBalance('31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9');
console.log('DCC balance (in Decentralites):', balance);

const { height } = await api.blocks.fetchHeight();
console.log('Current height:', height);
