// Illustrates: docs/09_user-guides/01_quick-start.md, "Step 2: Create a Testnet Account"
import { libs } from '@decentralchain/transactions';

// 15 random words. Anyone who has them controls the account: never share them or commit them.
const seed = libs.crypto.randomSeed();

console.log('Seed phrase:', seed);
console.log('Testnet address:', libs.crypto.address(seed, '!')); // '!' is the Testnet chain ID
