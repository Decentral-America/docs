// Illustrates: docs/04_building-apps/06_data-service-api.md, "Example: exchange history for a pair"
import DataServiceClient from '@decentralchain/data-service-client-js';

const client = new DataServiceClient({
  rootUrl: 'https://<your-data-service-host>/v0',
});

const amountAssetId = 'DCC';
const priceAssetId = '8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS';
const matcherAddress = 'MATCHER_ADDRESS';

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
