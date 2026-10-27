// Illustrates: docs/04_building-apps/how-to/04_voting.md, "Deploy the Poll", "Vote" and "Count the Votes"
import { readFile } from 'node:fs/promises';
import { data, setScript, invokeScript, broadcast, waitForTx, libs, nodeInteraction } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const pollSeed = 'poll account secret seed phrase here';
const voterSeed = 'voter secret seed phrase here';
const poll = libs.crypto.address(pollSeed, '!');
const wait = (id: string) => waitForTx(id, { apiBase: nodeUrl, timeout: 120_000 });

// 1. Write the deadline: voting stays open for about one day of 30-second blocks
const deadline = (await nodeInteraction.currentHeight(nodeUrl)) + 2_880;
const settings = data({ data: [{ key: 'deadline', type: 'integer', value: deadline }], chainId: '!' }, pollSeed);
await broadcast(settings, nodeUrl);
await wait(settings.id);

// 2. Compile the script and set it on the poll account
const source = await readFile(new URL('./ride/voting.ride', import.meta.url), 'utf8');
const deploy = setScript({ script: await compileRide(source, nodeUrl), chainId: '!' }, pollSeed);
await broadcast(deploy, nodeUrl);
await wait(deploy.id);

// 3. Vote
const vote = invokeScript(
  {
    dApp: poll,
    call: { function: 'vote', args: [{ type: 'string', value: 'yes' }] },
    chainId: '!',
  },
  voterSeed,
);
await broadcast(vote, nodeUrl);
await wait(vote.id);

// 4. Count the votes: the script keeps a running count per option
for (const option of ['yes', 'no', 'abstain']) {
  const entry = await nodeInteraction.accountDataByKey(`count_${option}`, poll, nodeUrl);
  console.log(`${option}: ${entry?.value ?? 0}`);
}
