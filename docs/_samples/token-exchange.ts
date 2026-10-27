// Illustrates: docs/04_building-apps/how-to/03_token-exchange.md, "Deploy the Exchange" and "Trade"
import { readFile } from 'node:fs/promises';
import { issue, data, setScript, invokeScript, broadcast, waitForTx, libs } from '@decentralchain/transactions';
import { compileRide } from './compile-ride.js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const exchangeSeed = 'exchange account secret seed phrase here';
const traderSeed = 'trader secret seed phrase here';
const exchange = libs.crypto.address(exchangeSeed, '!');
const wait = (id: string) => waitForTx(id, { apiBase: nodeUrl, timeout: 120_000 });

// 1. Issue the token from the exchange account, so the account holds the whole supply
const token = issue(
  {
    name: 'Coupon',
    description: 'Sold at a fixed price by a dApp',
    quantity: 1_000_000, // 10,000.00 tokens
    decimals: 2,
    reissuable: false,
    chainId: '!',
  },
  exchangeSeed,
);
await broadcast(token, nodeUrl);
await wait(token.id);

// 2. Set the token and its price: 1 DCC per whole token is 1,000,000 Decentralites per 0.01 token
const settings = data(
  {
    data: [
      { key: 'assetId', type: 'string', value: token.id },
      { key: 'price', type: 'integer', value: 1_000_000 },
    ],
    chainId: '!',
  },
  exchangeSeed,
);
await broadcast(settings, nodeUrl);
await wait(settings.id);

// 3. Compile the script and set it on the exchange account
const source = await readFile(new URL('./ride/token-exchange.ride', import.meta.url), 'utf8');
const deploy = setScript({ script: await compileRide(source, nodeUrl), chainId: '!' }, exchangeSeed);
await broadcast(deploy, nodeUrl);
await wait(deploy.id);

// 4. The trader buys 5 tokens for 5 DCC...
const buy = invokeScript(
  {
    dApp: exchange,
    call: { function: 'buy', args: [] },
    payment: [{ assetId: null, amount: 500_000_000 }],
    chainId: '!',
  },
  traderSeed,
);
await broadcast(buy, nodeUrl);
await wait(buy.id);

// ...and sells 2 of them back for 2 DCC
const sell = invokeScript(
  {
    dApp: exchange,
    call: { function: 'sell', args: [] },
    payment: [{ assetId: token.id, amount: 200 }],
    chainId: '!',
  },
  traderSeed,
);
await broadcast(sell, nodeUrl);
const info = await wait(sell.id);
console.log('Sell status:', info.applicationStatus);
