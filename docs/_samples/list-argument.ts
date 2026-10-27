// Illustrates: docs/04_building-apps/how-to/05_list-as-argument.md, "Deploy the Script" and "Pass Lists"
import { readFile } from 'node:fs/promises';
import { setScript, invokeScript, broadcast, waitForTx, libs, nodeInteraction } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const dAppSeed = 'dApp account secret seed phrase here';
const callerSeed = 'caller secret seed phrase here';
const dApp = libs.crypto.address(dAppSeed, '!');
const wait = (id: string) => waitForTx(id, { apiBase: nodeUrl, timeout: 120_000 });

// 1. Compile the script and set it on the dApp account
const source = await readFile(new URL('./ride/list-argument.ride', import.meta.url), 'utf8');
const deploy = setScript({ script: await compileRide(source, nodeUrl), chainId: '!' }, dAppSeed);
await broadcast(deploy, nodeUrl);
await wait(deploy.id);

// 2. Pass two lists: each argument is { type: 'list', value: [...] } of typed items
const tx = invokeScript(
  {
    dApp,
    call: {
      function: 'setScores',
      args: [
        {
          type: 'list',
          value: [
            { type: 'string', value: 'alice' },
            { type: 'string', value: 'bob' },
            { type: 'string', value: 'carol' },
          ],
        },
        {
          type: 'list',
          value: [
            { type: 'integer', value: 12 },
            { type: 'integer', value: 7 },
            { type: 'integer', value: 21 },
          ],
        },
      ],
    },
    chainId: '!',
  },
  callerSeed,
);
await broadcast(tx, nodeUrl);
await wait(tx.id);

const carol = await nodeInteraction.accountDataByKey('score_carol', dApp, nodeUrl);
console.log('score_carol:', carol?.value);
