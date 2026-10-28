// Illustrates: docs/04_building-apps/12_matcher-api.md, "Place and Cancel an Order"
import { order, submitOrder, cancelOrder, cancelSubmittedOrder, type WithId } from '@decentralchain/transactions';

// order()'s declared return type leaves out `id` and `proofs`, though the order it returns has both
type SignedOrder = Parameters<typeof submitOrder>[0] & WithId;

const matcherUrl = 'https://testnet-matcher.decentralchain.io';
const seed = 'your secret seed phrase here';

// From GET /matcher (the matcher's public key) and GET /matcher/orderbook (its markets)
const matcherPublicKey = 'BEtB5b2kX8Yge4sb5RRbTUqd5Va8Ah8PhphowcW31z6Y';
const amountAsset = 'Hs5y6vFumpwVp6my7rVEmJEQQD3wiQ29qJhnixNqPit5'; // DCCCANARY, 8 decimals
const priceAsset = null;                                            // null means DCC

// Buy 1 DCCCANARY at 0.001 DCC. For order versions 1 to 3 the price is scaled by
// 10^(8 + priceAssetDecimals - amountAssetDecimals): here 10^8, so 0.001 DCC is 100_000.
const buy = order(
  {
    matcherPublicKey,
    amountAsset,
    priceAsset,
    orderType: 'buy',
    amount: 100_000_000, // 1 DCCCANARY
    price: 100_000,      // 0.001 DCC per DCCCANARY
    matcherFee: 300_000, // 0.003 DCC, the matcher's base fee (GET /matcher/settings)
    version: 3,          // the matcher accepts order versions 1, 2 and 3
  },
  seed,
) as SignedOrder;
console.log('Placed:', await submitOrder(buy, { matcherUrl }));

const status = await fetch(
  `${matcherUrl}/matcher/orderbook/${amountAsset}/DCC/${buy.id}`,
).then((r) => r.json());
console.log('Status:', status.status); // Accepted, PartiallyFilled, Filled or Cancelled

// Cancel it: sign a cancel request with the same seed
const cancel = cancelOrder({ orderId: buy.id }, seed);
console.log('Cancelled:', await cancelSubmittedOrder(cancel, amountAsset, priceAsset, matcherUrl));
