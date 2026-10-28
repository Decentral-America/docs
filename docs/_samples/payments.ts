// Illustrates: docs/04_building-apps/how-to/02_payments.md, "Pay an Invoice" and "Check for Payment"
import { transfer, broadcast, waitForTx, libs } from '@decentralchain/transactions';
import { create } from '@decentralchain/node-api-js';

const nodeUrl = 'https://testnet-node.decentralchain.io';
const merchant = '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9';
const invoice = { id: 'INV-1042', amount: 250_000_000 }; // 2.5 DCC, in Decentralites

// Customer: pay the invoice and put its ID in the attachment
const customerSeed = 'customer secret seed phrase here';
const payment = transfer(
  {
    recipient: merchant,
    amount: invoice.amount,
    attachment: libs.crypto.base58Encode(libs.crypto.stringToBytes(invoice.id)),
    chainId: '!',
  },
  customerSeed,
);
await broadcast(payment, nodeUrl);
await waitForTx(payment.id, { apiBase: nodeUrl, timeout: 120_000 });

// Merchant: look for a confirmed DCC transfer that pays this invoice in full
const api = create(nodeUrl);
const recent = await api.transactions.fetchTransactions(merchant, 100);
const paidBy = recent.find(
  (tx) =>
    tx.type === 4 &&
    tx.recipient === merchant &&
    tx.assetId === null &&
    Number(tx.amount) >= invoice.amount &&
    libs.crypto.bytesToString(libs.crypto.base58Decode(tx.attachment ?? '')) === invoice.id,
);
console.log(paidBy ? `Invoice ${invoice.id} paid by ${paidBy.id}` : `Invoice ${invoice.id} not paid yet`);
