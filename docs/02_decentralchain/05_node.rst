****
Node
****

A node is a host connected to the blockchain network. Node functions are:

* :ref:`Block <02_decentralchain/04_block:Block>` storage.
* :ref:`Transaction validation <02_decentralchain/03_transaction:Transaction Validation>`.
* Sending :ref:`transactions <02_decentralchain/03_transaction:Transaction>`.

Generating Node
===============

Generating node is a node that generates blocks. Each generating node is a :ref:`validating node <02_decentralchain/05_node:Validating Node>`. Generating account is an :ref:`account <02_decentralchain/01_account:Account>` that a node uses for :ref:`signing <02_decentralchain/04_block:Block Signature>` generated blocks. A node can generate blocks if the following conditions are met:

* The node's generating balance is at least :math:`10000` :ref:`DecentralCoins <02_decentralchain/02_token(asset):DecentralCoin>`. This means that the account balance in DecentralCoins, taking into account leasing, was not less than :math:`10000` DecentralCoins in each of the last :math:`1000` blocks (more details in the :ref:`account balance <02_decentralchain/01_account:Account Balance>` article). The greater the generating balance, the higher is your chance of being eligible to generate the next block.
* Node's account is not a :ref:`smart account or dApp <02_decentralchain/01_account:dApp and Smart Account>`.
* Block generation is not disabled in node settings. By default, block generation is enabled.
* The node is connected to at least the number of peers specified in the required parameters (:math:`1` by default).

Validating Node
===============

A validating node is a node that :ref:`validates <02_decentralchain/03_transaction:Transaction Validation>` transactions.

Generator’s Income
==================

A node's income from adding a new block to the blockchain consists of the following amounts:

1. Block reward: The current reward size is :math:`6` :ref:`DecentralCoins <02_decentralchain/02_token(asset):DecentralCoin>` but it can be changed by voting, see the :ref:`block reward <02_decentralchain/05_node:Block Reward>` article.

2. :math:`40\%` of the total transaction fees in the current block. The exact value is calculated as follows:

  * :math:`\sum_{i}^{} 2 * (\frac{f_i}{5})`
  * Here f :math:`_i` is the fee for the :math:`i`-th transaction. For each transaction fee, an integer division by :math:`5` is performed, then a multiplication by :math:`2`, and finally they are summed up.

3. :math:`60\%` of the total transaction fees in the previous block.

  * :math:`\sum_{i}^{} (f_i - 2 * (\frac{f_i}{5}))`
  * The block generator receives exactly the part of the fee that the previous block generator did not receive.

If the :ref:`transaction fees <02_decentralchain/03_transaction:Transaction Fees>` are specified in a sponsored asset, then the block generators receive the fee equivalent in DecentralCoins instead of the fee (as a general rule, in a :math:`\frac{40}{60}` ratio):

.. code-block:: none

  feeInDecentralCoins = feeInSponsoredAsset × 0.001 / minSponsoredAssetFee

minSponsoredAssetFee is the amount of the sponsored asset equivalent to :math:`0.001` DecentralCoins. The sponsor sets this value when enabling sponsorship. For details, see the :ref:`sponsored fees <02_decentralchain/03_transaction:Sponsored Fees>` article.

Block Reward
============

Block reward is a blockchain feature under which :ref:`generating nodes <02_decentralchain/05_node:Generating Node>` receive a fixed fee in :ref:`DecentralCoins <02_decentralchain/02_token(asset):DecentralCoin>` for each :ref:`generated block <02_decentralchain/04_block:Block Generation>`.
Block rewards are paid due to the additional issue of the DecentralCoin token.
The community of generating nodes can change the size of reward through voting.

Current Reward Size
-------------------

You can view the current reward size by making a request to the :ref:`Node REST API <documentation:placeholder>`. In response to the request, a JSON file is returned,  the value of the currentReward field of which is the current block reward size in Decentralites. 

Example of response:

.. code-block:: none

  {
    "height": 1742254,
    "totalDecentralCoinsAmount": 10001353000000000,
    "currentReward": 600000000,
    "minIncrement": 50000000,
    "term": 100000,
    "nextCheck": 1839999,
    "votingIntervalStart": 1830000,
    "votingInterval": 10000,
    "votingThreshold": 5001,
    "votes": {
      "increase": 0,
      "decrease": 0
    }
  }

In the example above, the value of the JSON's currentReward field is 600,000,000 Decentralites— i.e. it's 6 :ref:`DecentralCoins <02_decentralchain/02_token(asset):DecentralCoin>`.

The Change of Block Reward Size Over Time
-----------------------------------------

Every :math:`100,000` blocks, i.e. approximately every :math:`70` days, a new voting for the current reward size change begins among the generators.
The voting duration is :math:`10,000` blocks. During this time, generating nodes vote to increase, decrease or leave the current reward size unchanged.
The elected reward size remains unchanged for :math:`100,000` blocks following the end of voting.

Voting
------

A generating node specifies the new desired reward size via settings in the node configuration file, the setting value is specified in Decentralites. If the value is greater than the current reward size, then the generator votes for the current reward size increase; if the value is smaller — for the decrease. If the setting value is not specified in the configuration file, then the generator votes for keeping the current reward size.
When a node generates a block, it writes into that block the value of the desired reward size specified in the setting from its own node configuration file. If the setting value is not specified in the configuration file, then :math:`-1` is written to the block.
During the voting time in :math:`10,000` blocks, a single node can generate several blocks, therefore one node can vote several times. How often a node generates blocks is determined by the LPoS consensus.

How Votes are Counted
---------------------

To count the votes, all :math:`10,000` blocks generated during the voting period are inspected.
If either :math:`-1` or the value that is equal to the current reward size is recorded to the block, then the generator votes for keeping the current reward size.
If the value recorded to the block is greater than the current reward size, then the generator votes for the current reward size increase; if the value is smaller — for the decrease.
The block reward is increased/decreased only if more than half of the :math:`10,000` votes — i.e. :math:`5,001` votes or more — were given for increase/decrease. The amount of the current reward is increased/decreased by :math:`0.5` :ref:`DecentralCoins <02_decentralchain/02_token(asset):DecentralCoin>`.

:strong:`Example 1`

At the blockchain height of :math:`2,000,000`, the block reward equals :math:`5` DecentralCoins. At the height of :math:`2,090,000`, another voting starts.
During the :math:`10,000` blocks of voting :math:`6,000` votes were given for reward increase, :math:`1,000` — for decrease, :math:`3,000` — for keeping the current reward size.
From the height of :math:`2`, :math:`100,000` to the height of :math:`2,199,999`, the new reward size will be :math:`5.5` DecentralCoins, because the reward change step is :math:`0.5` DecentralCoins.
The next voting will take place from the height of :math:`2,190,000` to :math:`2,199,999`.

:strong:`Example 2`

At the blockchain height of :math:`2,100,000`, the block reward equals :math:`5.5` DecentralCoins. At the height of :math:`2,190,000`, another voting starts.
During the :math:`10,000` blocks of voting :math:`4,500` votes were given for reward increase, :math:`4,000` — for decrease, :math:`1,500` — for keeping the current reward size.
From the height of :math:`2,200,000` to the height of :math:`2,299,999`, the "new" reward size will be the same — :math:`5.5` DecentralCoins. Although the highest number of votes were given for the reward increase, it was not enough to change the current reward size. In order for the current reward size to be increased, at least :math:`5,001` votes must be given for the increase.
The next voting will take place from the height of :math:`2,290,000` to :math:`2,299,999`.

Leased Proof of Stake
=====================

Leased Proof of Stake (LPoS) is an enhanced type of proof of stake consensus algorithm 
by which the DecentralChain blockchain network aims to achieve the distributed consensus to secure the network.

Leasing Benefits for the Node Owner
-----------------------------------

:ref:`Nodes <02_decentralchain/05_node:Node>` can use the leased tokens to generate blocks and get the :ref:`mining reward <02_decentralchain/05_node:Block Reward>`. For that purpose, the generating balance of a node must be at least :math:`10000` :ref:`DecentralCoins <02_decentralchain/02_token(asset):DecentralCoin>`.

Leasing Benefits for the Token Holder
-------------------------------------

LPoS allows the token holders to lease their tokens to the DecentralChain nodes and earn a percentage of the payout as a reward.
By using LPoS, lessors will be able to participate in the process of generating new blocks because the larger the amount that is leased to a DecentralChain node, the higher the chances for that node to be selected to generate the next block. If that node is selected, then the leaser will receive a reward.
When the user starts leasing the tokens, those leased tokens are locked and remain in the same address with the full control of their owner (they are not transferred to the node, they just remain unspendable until the lease is canceled by the lessor).
The only thing to consider when leasing is to choose the right node operator, as the operator's node may work with different efficiency and send back different percentages as rewards.

Rewards
^^^^^^^

* The node owner may send the lessor a part of the rewards according to his conditions.
* The more transactions that are made on the network, the more rewards the lessors get.
* These rewards mostly are in :ref:`DecentralCoins <02_decentralchain/02_token(asset):DecentralCoin>` but also they can be in the form of different tokens with the unique DecentralCoins feature where different tokens can be accepted as a fee.

LPoS Transactions
-----------------

To start leasing, the token holder needs to create a lease transaction and specify the recipient address (node address) along with the amount of :ref:`DecentralCoins <02_decentralchain/02_token(asset):DecentralCoin>` to lease. There are two types of transactions which are used in the LPoS:

* :ref:`Lease transaction <02_decentralchain/03_transaction:Lease Transaction>` to activate the leasing process.
* :ref:`Lease cancel transaction <02_decentralchain/03_transaction:Lease Cancel Transaction>` to deactivate the leasing process.

Create a Lease
--------------

You can use `Decentral.Exchange <https://decentral.exchange/>`_ online to create a lease. 

* Make sure you are logged into your account. On the main screen navigate to Wallet > Leasing. 
* On the next screen click Start Lease and then select the recipient between the list of nodes and indicate the amount you want to lease.
* Verify all the information and click Start Lease again to confirm.
