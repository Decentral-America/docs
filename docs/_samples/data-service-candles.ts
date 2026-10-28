// Illustrates: docs/04_building-apps/06_data-service-api.md, "Example: exchange history for a pair"
import DataServiceClient from '@decentralchain/data-service-client-js';

const rootUrl = 'https://testnet-data-service.decentralchain.io/v0';
const client = new DataServiceClient({ rootUrl });

// A pair traded on the Testnet matcher: DCCCANARY, priced in DCC
const amountAsset = 'Hs5y6vFumpwVp6my7rVEmJEQQD3wiQ29qJhnixNqPit5';
const priceAsset = 'DCC';
const matcher = '31VMNVAvVh67dPZ41nMnYZvhoZFW7wwPrmq'; // Testnet matcher

// The pair's last 10 trades, newest first, then the 10 before them
const trades = await client.getExchangeTxs({ amountAsset, priceAsset, matcher, limit: 10, sort: 'desc' });
console.log('Trades:', trades.data.length);
if (trades.fetchMore) {
  const older = await trades.fetchMore(10);
  console.log('Older trades:', older.data.length);
}

// Daily candles for the last 7 days. In data-service-client-js 4.2.0, getCandles() throws
// "Invalid maxHeight: null" when a day in the range has no trades, so read the candles
// endpoint directly and drop the empty days (their prices and volumes are null).
const timeEnd = Date.now();
const query = new URLSearchParams({
  timeStart: String(timeEnd - 7 * 24 * 60 * 60 * 1000),
  timeEnd: String(timeEnd),
  interval: '1d',
  matcher,
});
const response = await fetch(`${rootUrl}/candles/${amountAsset}/${priceAsset}?${query}`);
const body = (await response.json()) as { data: { data: { time: string; close: number | null; volume: number | null } }[] };
const candles = body.data.map((c) => c.data).filter((c) => c.close !== null);
for (const c of candles) console.log(`${c.time.slice(0, 10)} close ${c.close} DCC, volume ${c.volume}`);
