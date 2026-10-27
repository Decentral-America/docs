// Illustrates: docs/04_building-apps/sdk/02_java.md, "Connect to the Testnet"
package samples;

import io.decentralchain.sdk.Node;
import io.decentralchain.sdk.Profile;
import io.decentralchain.transactions.account.Address;

public final class ConnectToTestnet {
    public static void main(String[] args) throws Exception {
        // Profile.TESTNET is https://testnet-node.decentralchain.io
        Node node = new Node(Profile.TESTNET);

        System.out.println("Chain ID: " + (char) node.chainId());
        System.out.println("Height: " + node.getHeight());

        Address address = Address.as("31LAqgqVTLySNCPuYqgLAYhcgS76wvBaLr9");
        System.out.println("DCC balance (in Decentralites): " + node.getBalance(address));
    }
}
