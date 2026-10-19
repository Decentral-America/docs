**************************
Mainnet, Testnet, Stagenet
**************************

Connecting Node to Blockchain Network
=====================================

You can launch your node in any blockchain network. Select the network in the node configuration file. 

* For more information about the configuration file, see the :ref:`node configuration <05_node-guide/index:Configuration>` article. 
* For installing a node, see the :ref:`install DecentralChain node <05_node-guide/index:Getting the Node>` article. 
* For starting your own blockchain network, see the :ref:`custom blockchain <05_node-guide/03_custom-blockchain:Custom Blockchain>` article.

Chain ID
========

Chain ID is a symbol that is passed over a network during a handshake and allows nodes not to connect to the nodes of other networks. The chain ID is used while building account addresses, therefore, an address on one blockchain network cannot be used on another network. The chain ID is also indicated in transactions so it is impossible to move transactions between different blockchain networks.

.. csv-table:: Chain ID
  :file: ../_static/02_decentralchain/tables/024_Chain-ID.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Network Parameters
==================

.. list-table:: Network parameters
  :header-rows: 1
  :widths: 2 2 2

  * - Parameter
    - Mainnet
    - Public Testnet
  * - Chain ID
    - ``?`` (63)
    - ``!`` (33)
  * - Address prefix (Base58)
    - 3D
    - 31
  * - P2P port
    - 6868
    - 6868
  * - REST API port
    - 6869
    - 6869
  * - Target block time
    - 60 seconds
    - 30 seconds

Stagenet has chain ID ``S`` (83) and a built-in profile in the node (``dcc.defaults.blockchain.type = STAGENET``, P2P port 6862 in ``network-defaults.conf``), but there is no public Stagenet network yet.

.. note::

   The public DecentralChain Testnet (``testnet-node.decentralchain.io``) is a custom chain (``dcc.blockchain.type = CUSTOM``, chain ID ``!``). The node's built-in ``testnet`` profile (``DCC_NETWORK=testnet`` without a config file) is a different network and will not join it. To run a node on the public Testnet, follow :doc:`Join the Public Testnet <../05_node-guide/15_join-testnet>`, which gives the genesis, the configuration file and the peer to connect to.

Tools
=====

API of Pool of Public Nodes
---------------------------

.. csv-table:: API of Pool of Public Nodes
  :file: ../_static/02_decentralchain/tables/025_API-of-Pool-of-Public-Nodes.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3

Data Service API
----------------

.. csv-table:: Data Service API
  :file: ../_static/02_decentralchain/tables/026_Data-Service-API.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3

Decentral.Exchange
------------------

`Decentral.Exchange <https://decentral.exchange/>`_ is a decentralized exchange.

.. csv-table:: Decentral.Exchange
  :file: ../_static/02_decentralchain/tables/027_Decentral.Exchange.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3

API of Decentral.Exchange Matcher
---------------------------------

The addresses for order sending and market data obtaining are as follows. The Testnet matcher's public key is ``BEtB5b2kX8Yge4sb5RRbTUqd5Va8Ah8PhphowcW31z6Y`` and its address is ``31VMNVAvVh67dPZ41nMnYZvhoZFW7wwPrmq``.

.. csv-table:: API of Decentral.Exchange Matcher
  :file: ../_static/02_decentralchain/tables/028_API-of-Decentral.Exchange-Matcher.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3

DecentralChain Explorer
-----------------------

`DecentralChain Explorer <https://decentralscan.com/>`_ is a service for browsing blockchain data.

.. csv-table:: DecentralChain Explorer
  :file: ../_static/02_decentralchain/tables/029_DecentralChain-Explorer.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 4

Faucet: Obtaining Tokens
------------------------

.. csv-table:: Faucet: Obtaining Tokens
  :file: ../_static/02_decentralchain/tables/030_Faucet-Obtaining-Tokens.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3