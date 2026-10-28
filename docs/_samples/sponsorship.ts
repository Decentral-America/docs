// Illustrates: docs/09_user-guides/05_sponsorship.md, "Sponsor a Token with the SDK"
import { issue, sponsorship, transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const issuerSeed = 'issuer secret seed phrase here';
const userSeed = 'user secret seed phrase here';
const userAddress = libs.crypto.address(userSeed, '!');

// 1. Issue a token with 2 decimals (fee: 1 DCC)
const issueTx = issue(
  { name: 'GiftCard', description: 'Sponsored token example', quantity: 1_000_000, decimals: 2, reissuable: false, chainId: '!' },
  issuerSeed,
);
await broadcast(issueTx, nodeUrl);
await waitForTx(issueTx.id, { apiBase: nodeUrl, timeout: 120_000 });
const assetId = issueTx.id; // a token's ID is the ID of its Issue transaction

// 2. Enable sponsorship (fee: 0.001 DCC). 10 = 0.10 GiftCard stands in for 0.001 DCC of fee.
const sponsorTx = sponsorship({ assetId, minSponsoredAssetFee: 10, chainId: '!' }, issuerSeed);
await broadcast(sponsorTx, nodeUrl);
await waitForTx(sponsorTx.id, { apiBase: nodeUrl, timeout: 120_000 });

// 3. Give a user some tokens
const giveTx = transfer({ recipient: userAddress, amount: 1_000, assetId, chainId: '!' }, issuerSeed);
await broadcast(giveTx, nodeUrl);
await waitForTx(giveTx.id, { apiBase: nodeUrl, timeout: 120_000 });

// 4. The user sends tokens and pays the fee in the token, not in DCC
const userTx = transfer(
  {
    recipient: '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9',
    amount: 100,          // 1.00 GiftCard
    assetId,
    fee: 10,              // 0.10 GiftCard: the minimum for a transfer (1 fee unit)
    feeAssetId: assetId,
    chainId: '!',
  },
  userSeed,
);
await broadcast(userTx, nodeUrl);
await waitForTx(userTx.id, { apiBase: nodeUrl, timeout: 120_000 });
console.log('Token:', assetId, 'sponsored transfer:', userTx.id);
