// Illustrates: docs/04_building-apps/how-to/01_airdrop.md, "Send the Airdrop"
import { massTransfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const issuerSeed = 'token holder secret seed phrase here';
const assetId = 'your token ID here'; // the ID of the token's Issue transaction; null sends DCC

const recipients = [
  '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9',
  '31ekkhvBGr91ygJf4st72hAEVU9BUBs3Ats',
  // ...as many addresses or aliases as you need
];
const amountEach = 1_000; // in the token's smallest unit: 10 tokens of a token with 2 decimals
const attachment = libs.crypto.base58Encode(libs.crypto.stringToBytes('Community airdrop'));

// One Mass Transfer transaction holds at most 100 transfers
for (let start = 0; start < recipients.length; start += 100) {
  const batch = recipients.slice(start, start + 100);
  const tx = massTransfer(
    {
      assetId,
      transfers: batch.map((recipient) => ({ recipient, amount: amountEach })),
      attachment,
      chainId: '!',
    },
    issuerSeed,
  );
  await broadcast(tx, nodeUrl);
  // Wait for each batch, so a failed run can restart from the first unconfirmed batch
  await waitForTx(tx.id, { apiBase: nodeUrl, timeout: 120_000 });
  console.log(`Batch from #${start}: ${batch.length} transfers, fee ${tx.fee} Decentralites, ID ${tx.id}`);
}
