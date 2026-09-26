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

.. list-table:: Parameters shipped in node v1.7.0 (``network-defaults.conf``)
  :header-rows: 1
  :widths: 2 2 2

  * - Parameter
    - Mainnet
    - Testnet
  * - Chain ID
    - ``?`` (63)
    - ``!`` (33)
  * - Address prefix (Base58)
    - 3D
    - 31
  * - P2P port
    - 6868
    - 6863
  * - REST API port
    - 6869
    - 6869
  * - Minimum peer connections
    - 5
    - 5

Stagenet is planned but not yet available as a public network; no Stagenet parameters are published.

The default known peers for each network are listed in ``network-defaults.conf`` in the `node-scala <https://github.com/Decentral-America/node-scala>`_ repository.

Tools
=====

API of Pool of Public Nodes
---------------------------

Chain ID is a symbol that is passed over a network during a handshake and allows nodes not to connect to the nodes of other networks. The chain ID is used while building account addresses, therefore, an address on one blockchain network cannot be used on another network. The chain ID is also indicated in transactions so it is impossible to move transactions between different blockchain networks.

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

The addresses for order sending and market data obtaining are as follows:

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