##############
DecentralChain
##############

.. _overview:

********
Overview
********

Decentral Exchange is an open blockchain protocol and development toolset for Web 3.0 applications and decentralized solutions. Blockchain is a distributed ledger that ensures data immutability and transparency.

Accounts
========

Decentral Exchange uses an account-based model. Each transaction is created on behalf of an account, all assets and data are associated with an account. An account has a pair of cryptographically bound keys: a private key that the account uses to sign transactions, and a public key that allows anyone to verify the signature. More about :ref:`accounts <documentation:Account>`

To create an account, store keys, and sign transactions, you can use `Decentral.Exchange <https://decentral.exchange/>`_. 

.. image:: _static/image.jpg

To create an account, store keys, and sign transactions, you can use :ref:`prueba <elguru:development>`

Transactions and Blocks
=======================

Blockchain data is presented as transactions. A transaction is a record of an action, such as token issue, cryptocurrency transfer, smart contract creation or invocation, etc.

Transactions are stacked into blocks. Besides transactions, every block contains the hash of the previous block and the digital signature of the node that generated the block. The previous block contains the data hash of its preceding block, and so on. As a result, the signature of each block depends on the data of all the preceding blocks.

In other words, the blockchain is a sequence of blocks linked by cryptographic hashes. Each transaction stays intact indefinitely. An attempt to change any data in a block would invalidate the block and all the later blocks.

.. image:: _static/image.jpg

Nodes
=====

A node is a computer that serves the blockchain network. The Waves node stores a full copy of the blockchain data, validates transactions and blocks, verifies signatures and hashes, and synchronizes the data with other nodes.

The Waves network consists of hundreds of nodes hosted around the world. This ensures that the blockchain data is protected against counterfeit or deletion, malicious or occasional. Everyone can `launch a node <https://placeholder/>`_ and join the network. The node that holds at least 1,000 WAVES (by ownership or :ref:`lease <documentation:Leased Proof of Stake>`), can participate in block generation and receive :ref:`block generation rewards <documentation:Block Reward>` and transaction fees. The more tokens the node holds, the greater is its chance to add the next block.

dApps
=====

A decentralized application (dApp) is an application empowered by blockchain. A dApp can store data on the blockchain and invoke a script assigned to an account. There is, therefore, no centralized database that might be hacked or compromised. Any user can view the script code and the result of its invocation.

.. _account:

*******
Account
*******

Waves uses an account-based model:

* Each :ref:`transaction <documentation:Transaction>` is created on behalf of a certain account. 
* All the :ref:`tokens <documentation:Token (Asset)>` belong to certain accounts.
* All data is associated with accounts. For details, see the :ref:`Account Data Storage <documentation:Account Data Storage>` article.

Account Keys
============

Unlike centralized applications, users do not have usernames and passwords on the blockchain. User identification and validation of their actions are performed using a cryptographically bound key pair:

* The private key is used to sign transactions or orders.
* The public key allows to verify the digital signature.

Each transaction contains the public key of the sender account. The sender generates a digital signature of the transaction using the account's private key. The signature and the sender's public key are used to verify the authenticity of the transaction data and to check that the signature of the transaction matches the public key.

.. image:: _static/image.jpg

Waves uses an asymmetric cryptographic system based on the elliptic curve Curve25519-ED25519 with X25519 keys. The guideline for generating keys and signatures is given in the :ref:`Cryptographic Practical Details <documentation:Cryptographic Practical Details>` article.
The private and public keys are 32 byte arrays. In UIs, the keys are displayed as base58 encoded strings. Base58-encoded keys can be of different length, the maximum length is 44 characters.

Example private key in base58:

.. code-block:: console

  6yCStrsBs4VgTmYcSgF37pmQhCo6t9LZk5bQqUyUNSAs

Example public key in base58:

.. code-block:: console

  5cqzmxsmFPBHm4tb7D8DMA7s5eutLXTDnnNMQKy2AYxh

Secret (Seed) Phrase
====================

The private key can be generated from some random seed phrase using hashing functions. The public key is obtained from the private key using an elliptic curve multiplication. Account :ref:`address <documentation:Address>` is obtained from the public key. All these transformations are unidirectional. The opposite direction is almost impossible in terms of the required computations.

.. image:: _static/image.jpg

The secret phrase (a.k.a. seed phrase, backup phrase) can be any combination of symbols, words, or bytes. Waves wallet apps typically use a random set of 15 English words out of 2048 words available. Using such a phrase is secure: the probability of generating two identical seed phrases is 1/204815, so brute-force will take millions of years on an average CPU. The point of using a secret phrase (rather than a private key) is to simplify user experience: the secret phrase is much easier to write down or remember. 

Example of a secret phrase:

.. code-block:: console

  body key praise enter toss road cup result shrimp bus blame typical sphere pottery claim

Security Information:

* The secret phrase or the private key derived from it provides complete control over the account, including the ability to dispose of funds. Do not give your secret phrase and private key to anyone, and do not publish or send them.
* The secret phrase cannot be changed: another secret phrase (even one that differs by a single character) will generate a different key pair, and therefore a different account.
* If you lose your secret phrase and private key, you will no longer be able to access your account permanently. We strongly encourage you to write down the secret phrase on a piece of paper and store it in a safe place.
* If the secret phrase is compromised (you have accidentally sent it to someone or suspect that it was taken by fraudsters), immediately create a new account and transfer all assets to it.

For ways to generate account keys, see the :ref:`Creating an Account <documentation:Creating an Account>` article.

Address
=======

Address is an :ref:`account <documentation:Account>` attribute derived from the :ref:`public key <documentation:Account Keys>`. The address also contains the chain ID that identifies the blockchain network, therefore the address on the Mainnet cannot be used on the Testnet and vice versa.

The address is a 26 byte array (see the :ref:`Address Binary Format <documentation:Address Binary Format>`). In UIs the address is displayed as a base58 encoded string.

.. code-block:: console

  3PDfnPknnYrg2k2HMvkNLDb3Y1tDTtEnp9X


Normally, the address starting with 3P refers to the Mainnet, and the address starting with 3M or 3N refers to Testnet or Stagenet.

The address is used to obtain information about the account:

* :ref:`token balances <documentation:Account Balance>`,
* entries of :ref:`account data storage <documentation:Account Data Storage>`,
* :ref:`aliases <documentation:Alias>`,
* :ref:`assigned script <documentation:dApp and Smart Account>`, etc.

See examples in the :ref:`How to Retrieve Information from the Blockchain <documentation:placeholder>` article. The address is indicated:

* in :ref:`Transfer <documentation:Transfer Transaction>`, :ref:`Mass Transfer <documentation:MassTransferTransaction>` and :ref:`Lease <documentation:LeaseTransaction>` transaction to identify a recipient;
* in :ref:`Invoke Script <documentation:InvokeScriptTransaction>` transactions to identify an invoked dApp.

Creating an Account
===================

To create a Waves account, you don't need to register anywhere. To create a Waves account means to generate an :ref:`account key pair <documentation:Account Keys>` and :ref:`address <documentation:Address>` based on a :ref:`secret (seed) phrase <documentation:Secret (Seed) Phrase>`.

You can use one of the recommended apps to create an account:

* :ref:`Waves Keeper <documentation:placeholder>` browser extension. See instructions in the :ref:`Getting Started with Waves Keeper <documentation:placeholder>` article.
* `Decentral.Exchange <https://decentral.exchange/>`_ online. See instructions in the `Create Account <https://placeholder/>`_ articles of Waves.Exchange documentation.
* `WavesFX <https://wavesfx.github.io/>`_ app developed by the third party team from the community.

Alternatively, you can use one of the :ref:`client libraries <documentation:placeholder>`, such as:

* TypeScript/JavaScript library `ts-lib-crypto <https://github.com/wavesplatform/ts-lib-crypto>`_ (it is also included in `waves-transactions <https://wavesplatform.github.io/waves-transactions/index.html>`_):

.. code-block:: console

  const libCrypto = require('@waves/ts-lib-crypto')
  const seed = libCrypto.randomSeed() // or input your existing seed
  const sk = libCrypto.privateKey(seed)
  const pk = libCrypto.publicKey(seed)
  const addressBase58 = libCrypto.address(seed) // address for Mainnet
  const addressTestnetBase58 = libCrypto.address(seed, 'T') // address for Testnet

* Python module `Pywaves <https://github.com/PyWaves/PyWaves>`_

.. code-block:: console

  import pywaves as pw
  # pw.setChain('testnet') # Mainnet by default
  # generate a new address
  myAddress = pw.Address(seed='<insert your seed here>')
  print(f'Your seed:   {myAddress.seed}')
  print(f'Private Key: {myAddress.privateKey}')
  print(f'Public Key:  {myAddress.publicKey}')
  print(f'Address:     {myAddress.address}')

* Java library `WavesJ <https://github.com/wavesplatform/WavesJ>`_

.. code-block:: console

  String seed = Crypto.getRandomSeedPhrase();
  PrivateKey privateKey = PrivateKey.fromSeed(seed);
  PublicKey publicKey = PublicKey.from(privateKey);
  Address address = Address.from(publicKey);

Please note:

* An account key pair and address are generated and stored locally. No data needs to be sent to the node or anywhere else.
* The address is immediately available for transferring tokens. In particular, it can be specified as the recipient in the :ref:`Transfer transaction <documentation:TransferTransaction>`.
* The address appears on the blockchain along with the first transaction in which the account participates.
* To use your account in another application or on another device, you need to enter a secret phrase on it and repeat the key pair generation.


Alias
=====

Alias Requirements
------------------

Create Alias
------------

View Aliases
------------

Binary Format
-------------

Account Balance
===============

Account Balance in Decentral Coin
---------------------------------

View Account Balance
--------------------

Top up Balance
--------------

Account Data Storage
====================

View Account Data
-----------------

Add, Modify, Delete Entries
---------------------------

dApp and Smart Account
======================

.. _token:

*************
Token (Asset)
*************

Token Issue
===========

Token ID
========

Token Operations
================

Operations Available Only to Issuer
-----------------------------------

Token Types
===========

Non-Fungible Token
------------------

Issue of NFT
^^^^^^^^^^^^

Smart Asset
-----------

Tokens of Other Blockchains
---------------------------

Decentral Coin
==============

Decentral Coin Parameters
-------------------------

Leasing
-------

How to Get Decentral Coin
-------------------------

Token Custom Parameters
=======================

Atomic Unit
-----------

.. _transaction:

***********
Transaction
***********

Transaction Issue
=================

How to Sign and Send Transaction
--------------------------------

Transaction Sender and Signature
--------------------------------

After Transaction Is Sent
-------------------------

Transaction Proofs
==================

Verification by Script
----------------------

Transaction Fees
================

Regular Fees
------------

Minimum Fee
^^^^^^^^^^^

Fee for Failed Transactions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fee in Sponsored Asset
^^^^^^^^^^^^^^^^^^^^^^

Sponsored Fees
--------------

Sponsored Asset
^^^^^^^^^^^^^^^

How It Works
^^^^^^^^^^^^

How to Enable Sponsorship
^^^^^^^^^^^^^^^^^^^^^^^^^

How to Disable Sponsorship
^^^^^^^^^^^^^^^^^^^^^^^^^^

Restrictions
^^^^^^^^^^^^

Transaction Representations
===========================

JSON Representation
-------------------

Binary Format
-------------

Transaction Types
=================

Tokenization
------------

IssueTransaction
^^^^^^^^^^^^^^^^

ReissueTransaction
^^^^^^^^^^^^^^^^^^

BurnTransaction
^^^^^^^^^^^^^^^

SetAssetScriptTransaction
^^^^^^^^^^^^^^^^^^^^^^^^^

UpdateAssetInfoTransaction
^^^^^^^^^^^^^^^^^^^^^^^^^^

Usage
-----

TransferTransaction
^^^^^^^^^^^^^^^^^^^

ExchangeTransaction
^^^^^^^^^^^^^^^^^^^

CreateAliasTransaction
^^^^^^^^^^^^^^^^^^^^^^

MassTransferTransaction
^^^^^^^^^^^^^^^^^^^^^^^

DataTransaction
^^^^^^^^^^^^^^^

SetScriptTransaction
^^^^^^^^^^^^^^^^^^^^

InvokeScriptTransaction
^^^^^^^^^^^^^^^^^^^^^^^

Network
-------

LeaseTransaction
^^^^^^^^^^^^^^^^

LeaseCancelTransaction
^^^^^^^^^^^^^^^^^^^^^^

SponsorFeeTransaction
^^^^^^^^^^^^^^^^^^^^^

Genesis
-------

GenesisTransaction
^^^^^^^^^^^^^^^^^^

Transaction Validation
======================

Validation Result
-----------------

.. _block:

*****
Block
*****

Block Generation
================

Base Target
-----------

Generation Signature
--------------------

Block Height
============

Block Signature
===============

Block Timestamp
===============

Genesis Block
=============

Transactions Root Hash
======================

transactionsRoot Сalculation
----------------------------

Proof of Transaction in Block
-----------------------------

Tools
-----

.. _node:

****
Node
****

Generating Node
===============

Validating Node
===============

Generator’s Income
==================

Block Reward
============

Current Reward Size
-------------------

The Change of Block Reward Size Over Time
-----------------------------------------

Voting
------

How Votes are Counted
---------------------

Leased Proof of Stake
=====================

Leasing Benefits for the Node Owner
-----------------------------------

Leasing Benefits for the Token Holder
-------------------------------------

Rewards
^^^^^^^

LPoS transactions
-----------------

.. _order:

*****
Order
*****

Asset Pair
==========

Order's Amount and Price
========================

Amount
------

Price
-----

Price Asset Quantity Calculation
--------------------------------

Order Cancellation
==================

Order Expiration Date
=====================

Order Timestamp
===============

Order Binary Format
===================

.. _oracle:

******
Oracle
******

Sources of the Outside World
============================

Oracles Issue
=============

Consensus of Oracles
====================

.. _mainnet:

**************************
Mainnet, Testnet, Stagenet
**************************

Connecting Node to Blockchain Network
=====================================

Chain ID
========

Tools
=====

API of Pool of Public Nodes
---------------------------

Data Service API
----------------

Waves.Exchange
--------------

API of Waves.Exchange Matcher
-----------------------------

Waves Explorer
--------------

Faucet: Obtaining Tokens
------------------------

Waves IDE
---------

Waves Keeper
------------

.. _protocols:

************************
Protocols & Data Formats
************************

Cryptographic Practical Details
===============================

Description
-----------

Bytes Encoding Base58
---------------------

Creating a Private Key from a Seed
----------------------------------

Creating Address from a Public Key
----------------------------------

Signing
-------

Calculating Transaction ID
--------------------------

Waves-NG Solution
=================

Reasoning
---------

Waves-NG Solution With Technical Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Microblock Structure
^^^^^^^^^^^^^^^^^^^^

Economy
-------

Related Protocol Changes
------------------------

Configuration
-------------

API changes
-----------

Waves-NG Protocol
=================

Scalability Limits and Challenges in Current Blockchain Systems
---------------------------------------------------------------

Problem Statement and Motivation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Weaknesses of Current Proposals to Improve Scalability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Brief Summary of Bitcoin-NG
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Waves-NG Overlay
----------------

Waves-NG operations
^^^^^^^^^^^^^^^^^^^

Waves-NG reward mechanisms
^^^^^^^^^^^^^^^^^^^^^^^^^^

Fair Proof of Stake
===================

Blockchain Data Types
=====================

Binary Format
=============

Address Binary Format
---------------------

Alias Binary Format
--------------------

Block Binary Format
-------------------

Network Message Binary Format	
-----------------------------

Block Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checkpoint Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get Block Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get Peers Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get Signatures Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Handshake Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Peers Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Score Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signatures Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transaction Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Order Binary Format
-------------------

Transaction Binary Format
-------------------------

Protobuf
^^^^^^^^

Burn Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create Alias Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exchange Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Genesis Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Invoke Script Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Issue Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lease Cancel Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lease Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mass Transfer Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reissue Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set Asset Script Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set Script Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sponsor Fee Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfer Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update Asset Info Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transaction Proofs Binary Format
--------------------------------

Validation Rules
================

Account Validation
------------------

Transactions Validation
-----------------------

Transfer transaction
^^^^^^^^^^^^^^^^^^^^

Issue transaction
^^^^^^^^^^^^^^^^^

Reissue transaction
^^^^^^^^^^^^^^^^^^^

Block Validations
-----------------

Consensus data validation
^^^^^^^^^^^^^^^^^^^^^^^^^

Transactions data validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unconfirmed Transactions Pool Validation
----------------------------------------

.. _glossary:

********
Glossary
********

A
=

:strong:`Account`

:strong:`Account Data Storage`

:strong:`Account Script`

:strong:`Address`

:strong:`Airdrop`

:strong:`Alias`

:strong:`Asset`

:strong:`Asset Script`

B
=

:strong:`Block`

:strong:`Blockchain`

:strong:`Block Height`

:strong:`Blockchain Height`

:strong:`Blockchain Network`

:strong:`Block Signature`

C
=

:strong:`Consensus`

:strong:`Cryptocurrency`

D
=

:strong:`dApp`

:strong:`dApp Script`

:strong:`Decentralized Application`

E
=

:strong:`Explorer`

F
=

:strong:`Faucet`

G
=

:strong:`Gateway`

:strong:`Genesis Block`

:strong:`Genesis Transaction`

H
=

:strong:`Hash`

:strong:`Hash Function`

I
=

J
=

K
=

:strong:`Keeper`

L
=

:strong:`Leasing`

:strong:`LPoS`

M
=

:strong:`Mainnet`

:strong:`Matcher`

:strong:`Matcher Fee`

:strong:`Miner`

:strong:`Mining`

:strong:`Mining Account`

:strong:`Mining Node`

:strong:`Multisignature`

N
=

:strong:`NFT`

:strong:`Node`

O
=

:strong:`Oracle`

:strong:`Oracle Card`

:strong:`Order`

P
=

:strong:`PoS`

:strong:`PoW`

:strong:`Private Key`

:strong:`Public Key`

Q
=

R
=

:strong:`Ride`

S
=

:strong:`Script`

:strong:`Smart Account`

:strong:`Smart Asset`

:strong:`Stagenet`

T
=

:strong:`Test Network`

:strong:`Token`

:strong:`Token Rating`

:strong:`Transaction`

:strong:`Transaction Body Bytes`

U
=

:strong:`UTX pool`

V
=

:strong:`Validating Node`

W
=

:strong:`WAVELET`

:strong:`WAVES`

:strong:`WCT`

X
=

Y
=

Z
=


