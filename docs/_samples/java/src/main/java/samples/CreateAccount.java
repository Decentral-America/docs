// Illustrates: docs/04_building-apps/sdk/02_java.md, "Create an Account"
package samples;

import io.decentralchain.crypto.Crypto;
import io.decentralchain.transactions.account.Address;
import io.decentralchain.transactions.account.PrivateKey;
import io.decentralchain.transactions.account.PublicKey;
import io.decentralchain.transactions.common.ChainId;

public final class CreateAccount {
    public static void main(String[] args) {
        String seed = Crypto.getRandomSeedPhrase(); // keep it secret: it controls the account
        PrivateKey privateKey = PrivateKey.fromSeed(seed);
        PublicKey publicKey = PublicKey.from(privateKey);
        Address address = Address.from(ChainId.TESTNET, publicKey); // starts with 31

        System.out.println("Address: " + address);
    }
}
