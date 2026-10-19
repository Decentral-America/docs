// Illustrates: docs/04_building-apps/06_data-service-api.md, "Example: exchange history for a pair"
import DataServiceClient from '@decentralchain/data-service-client-js';

const client = new DataServiceClient({
  rootUrl: 'https://testnet-data-service.decentralchain.io/v0',
});

const amountAssetId = 'DCC';
const priceAssetId = '<price asset ID>'; // any asset traded on the matcher
const matcherAddress = '31VMNVAvVh67dPZ41nMnYZvhoZFW7wwPrmq'; // Testnet matcher

const { data: candles } = await client.getCandles(amountAssetId, priceAssetId, {
  timeStart: '2026-01-01',
  timeEnd: '2026-12-31',
  interval: '1d',
  matcher: matcherAddress,
});

const result = await client.getExchangeTxs({ limit: 10, sort: 'desc' });
console.log(result.data, candles);
if (result.fetchMore) {
  await result.fetchMore(10);
}
