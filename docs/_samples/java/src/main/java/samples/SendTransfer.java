// Illustrates: docs/04_building-apps/sdk/02_java.md, "Sign and Broadcast a Transfer"
package samples;

import io.decentralchain.sdk.Node;
import io.decentralchain.sdk.Profile;
import io.decentralchain.sdk.exceptions.NodeException;
import io.decentralchain.transactions.TransferTransaction;
import io.decentralchain.transactions.account.Address;
import io.decentralchain.transactions.account.PrivateKey;
import io.decentralchain.transactions.common.Amount;
import io.decentralchain.transactions.common.AssetId;
import io.decentralchain.transactions.common.ChainId;

public final class SendTransfer {
    public static void main(String[] args) throws Exception {
        Node node = new Node(Profile.TESTNET);
        PrivateKey privateKey = PrivateKey.fromSeed("your secret seed phrase here");
        Address recipient = Address.as("31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9");

        // Builders default to the Mainnet chain ID, so set the Testnet one explicitly
        TransferTransaction tx = TransferTransaction
                .builder(recipient, Amount.of(100_000_000, AssetId.DCC)) // 1 DCC
                .chainId(ChainId.TESTNET)
                .getSignedWith(privateKey);

        try {
            node.broadcast(tx);
            node.waitForTransaction(tx.id());
            System.out.println("Transaction ID: " + tx.id());
        } catch (NodeException e) {
            // The node rejected the transaction, for example for an insufficient balance
            System.err.println("Rejected (" + e.getErrorCode() + "): " + e.getMessage());
        }
    }
}
