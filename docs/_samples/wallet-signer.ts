// Illustrates: docs/04_building-apps/04_wallet-integration.md, "Recommended: Signer + Provider"
import { Signer } from '@decentralchain/signer';
import { ProviderCubensis } from '@decentralchain/cubensis-connect-provider';

const signer = new Signer({ NODE_URL: 'https://testnet-node.decentralchain.io' });
await signer.setProvider(new ProviderCubensis());

// Prompt the user to connect and authenticate via the Cubensis Connect extension
const user = await signer.login();
console.log('Logged in as:', user.address);

// Build, sign (via the extension) and broadcast a Transfer
const broadcastedTx = await signer
  .transfer({
    recipient: '31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9', // Testnet address
    amount: 100_000_000, // 1 DCC
  })
  .broadcast();

console.log('Transaction ID:', broadcastedTx.id);
