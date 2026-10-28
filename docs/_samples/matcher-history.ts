// Illustrates: docs/04_building-apps/12_matcher-api.md, "Requests Signed with Your Key"
import { libs } from '@decentralchain/transactions';

const matcherUrl = 'https://testnet-matcher.decentralchain.io';
const seed = 'your secret seed phrase here';
const publicKey = libs.crypto.publicKey(seed);

// Sign your public key's bytes followed by the current time as an 8-byte big-endian number
const timestamp = Date.now();
const timestampBytes = new Uint8Array(8);
new DataView(timestampBytes.buffer).setBigUint64(0, BigInt(timestamp));
const signature = libs.crypto.signBytes(
  seed,
  libs.crypto.concat(libs.crypto.base58Decode(publicKey), timestampBytes),
);
const headers = { Timestamp: String(timestamp), Signature: signature };

const orders = await fetch(`${matcherUrl}/matcher/orderbook/${publicKey}?activeOnly=false`, { headers })
  .then((r) => r.json());
console.log('Orders:', orders);

const reserved = await fetch(`${matcherUrl}/matcher/balance/reserved/${publicKey}`, { headers })
  .then((r) => r.json());
console.log('Reserved by open orders:', reserved);
