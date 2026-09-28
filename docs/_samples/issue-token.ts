// Illustrates: docs/04_building-apps/03_how-to-guides.md, "Issuing a Token"
import { issue, broadcast } from '@decentralchain/transactions';

const seed = 'your secret seed phrase here';

const signedTx = issue(
  {
    name: 'MyToken',
    description: 'A token issued on DecentralChain',
    quantity: 1_000_000,
    decimals: 2,
    reissuable: true,
  },
  seed,
);

await broadcast(signedTx, 'https://nodes.decentralchain.io');
