############
Intermediate
############

********
Overview
********

DecentralChain  is an open blockchain protocol and development toolset for Web :math:`3.0` applications and decentralized solutions. Blockchain is a distributed ledger that ensures data immutability and transparency.

Accounts
========

DecentralChain uses an account-based model. Each transaction is created on behalf of an account, all assets and data are associated with an account. An account has a pair of cryptographically bound keys: a private key that the account uses to sign transactions, and a public key that allows anyone to verify the signature. :ref:`More about accounts <02_intermediate:Account>`.

To create an account, store keys, and sign transactions, you can use `Decentral.Exchange <https://decentral.exchange/>`_. 

.. image:: _static/image.jpg

Transactions and Blocks
=======================

Blockchain data is presented as transactions. A transaction is a record of an action, such as a token issue, cryptocurrency transfer, smart contract creation or invocation and more. :ref:`More about transactions <02_intermediate:Transaction>`.

Transactions are stacked into blocks. Besides transactions, every block also contains the hash of the previous block and the digital signature of the node that generated the block. The previous block contains the data hash of its preceding block, and so on. As a result, the signature of each block depends on the data of all the preceding blocks. :ref:`More about blocks <02_intermediate:Block>`.

In other words, the blockchain is a sequence of blocks linked by cryptographic hashes. Each transaction stays intact indefinitely. An attempt to change any data in a block would invalidate the block and all the later blocks.

.. image:: _static/image.jpg

Nodes
=====

A node is a computer that serves the blockchain network. The DecentralChain nodes store a full copy of the blockchain data, validate transactions and blocks, verify signatures and hashes, and synchronize the data with other nodes.

The DecentralChain network consists of nodes hosted around the world. This ensures that the blockchain’s data is protected against counterfeit or deletion, either malicious or accidental. Everyone can :ref:`launch a node <documentation:placeholder>` and join the network. The nodes that hold at least :math:`1,0000` :ref:`DecentralCoins <02_intermediate:DecentralCoin>` (by ownership or :ref:`lease <02_intermediate:Leased Proof of Stake>`), can participate in block generation to receive :ref:`block generation rewards <02_intermediate:Block Reward>` and transaction fees. The more tokens the node holds, the greater its chance to add the next block. :ref:`More about nodes <02_intermediate:Node>`.

dApps
=====

A decentralized application (dApp) is an application empowered by the blockchain. A dApp can store data on the blockchain and invoke a script assigned to an account. There is, therefore, no centralized database that might be hacked or compromised. Any user can view the script code and the result of its invocation. :ref:`More about dApps <02_intermediate:dApp and Smart Account>`.

*******
Account
*******

DecentralChain uses an account-based model:

* Each :ref:`transaction <02_intermediate:Transaction>` is created on behalf of a certain account. 
* All the :ref:`tokens <02_intermediate:Token (Asset)>` belong to certain accounts.
* All the data is associated with accounts. For details, see the :ref:`account data storage <02_intermediate:Account Data Storage>` article.

Account Keys
============

Unlike centralized applications, users do not have usernames and passwords on the blockchain. User identification and validation of their actions are performed using a cryptographically bound key pair:

* The private key is used to sign transactions or orders.
* The public key allows the verification of the digital signature.

Each transaction contains the public key of the sender's account. The sender generates a digital signature of the transaction using the account's private key. The signature and the sender's public key are used to verify the authenticity of the transaction's data and to check that the signature of the transaction matches the public key.

.. image:: _static/image.jpg

DecentralChain uses an asymmetric cryptographic system based on the elliptic curve Curve25519-ED25519 with X25519 keys. The guideline for generating keys and signatures is given in the :ref:`cryptographic practical details <02_intermediate:Cryptographic Practical Details>` article.
The private and public keys are :math:`32` byte arrays. In UIs, the keys are displayed as base58 encoded strings. Base58-encoded keys can be of different lengths, the maximum length is :math:`44` characters.

Example private key in base58:

.. code-block:: none

  6yCStrsBs4VgTmYcSgF37pmQhCo6t9LZk5bQqUyUNSAs

Example public key in base58:

.. code-block:: none

  5cqzmxsmFPBHm4tb7D8DMA7s5eutLXTDnnNMQKy2AYxh

Secret (Seed) Phrase
====================

The private key can be generated from some random seed phrase using hashing functions. The public key is obtained from the private key using an elliptic curve multiplication. The :ref:`account address <02_intermediate:Address>` is obtained from the public key. All these transformations are unidirectional. The opposite direction is almost impossible in terms of the required computations.

.. image:: _static/image.jpg

The secret phrase (a.k.a. seed phrase, backup phrase) can be any combination of symbols, words, or bytes. DecentralChain wallet apps typically use a random set of :math:`15` English words out of :math:`2048` words available. Using such a phrase is secure since the probability of generating two identical seed phrases is :math:`\frac{1}{2048^{15}}`, so brute-force will take millions of years on an average CPU. The point of using a secret phrase (rather than a private key) is to simplify user experience: the secret phrase is much easier to write down or remember. 

Example of a secret phrase:

.. code-block:: none

  body key praise enter toss road cup result shrimp bus blame typical sphere pottery claim

Security Information:

* The secret phrase or the private key derived from it provide complete control over the account, including the ability to dispose of funds. Do not give your secret phrase or private key to anyone, and do not publish or send them.
* The secret phrase cannot be changed: another secret phrase (even one that differs by a single character) will generate a different key pair, and therefore a different account.
* If you lose your secret phrase or private key, you will no longer be able to access your account ever again. We strongly encourage you to :ref:`backup of your secret phrase <02_intermediate:Backup Seed Phrase>`.
* If the secret phrase is compromised (you have accidentally sent it to someone or suspect that it was taken by fraudsters), immediately create a new account and transfer all the assets to it.

For ways to generate account keys, see the :ref:`creating an account <02_intermediate:Creating an Account>` article.

Creating an Account
===================

To create an account means to generate an :ref:`account key pair <02_intermediate:Account Keys>` and :ref:`address <02_intermediate:Address>` based on a :ref:`secret (seed) phrase <02_intermediate:Secret (Seed) Phrase>`.

You can use `Decentral.Exchange <https://decentral.exchange/>`_ online to create an account. 

* On the main screen click Create Account then in the Create Password box type in the password, type it again in the Confirm Password box, accept the Terms and Conditions as well as the Privacy Policy and click Continue.
* On the next screen select Create Account and then choose the avatar you like the most for your account and click Continue.
* After that, select the name you want the account to have on that particular device and click Continue.
* At this point you will be forwarded to your wallet page. You must do a :ref:`backup of your seed phrase <02_intermediate:Backup Seed Phrase>`.

Backup Seed Phrase
==================

* Open `Decentral.Exchange <https://decentral.exchange/>`_ main screen and make sure you are logged into your account. Click on the account avatar and navigate to Settings > Security.
* Click Show in the Backup Phrase box.
* Write down the phrase and store it in a secure location.

Do not store the backup phrase unencrypted on any electronic device. We strongly recommend backing up the seed phrase, since this is the only way to restore access to your account in case of loss or theft of the device.

Log in to Account
=================

* Open `Decentral.Exchange <https://decentral.exchange/>`_ main screen and click Create Account then in the Create Password box type in the password, type it again in the Confirm Password box, accept the Terms and Conditions as well as the Privacy Policy and click Continue.
* On the next screen select Import Accounts, then choose the Seed or Key option.
* After that type in the seed you backed up in the past and click Continue, then select the name you want the account to have on that particular device and click Continue.
* At this point you will be forwarded to your wallet page. 

Forgot Password
===============

* Open `Decentral.Exchange <https://decentral.exchange/>`_ main screen and click Forgot Password then select the Reset All option.
* On the next screen, in the Create Password box type in the password, type it again in the Confirm Password box, accept the Terms and Conditions as well as the Privacy Policy and click Continue.
* When this is done, select Import Accounts, then choose the Seed or Key option.
* After that type in the seed you backed up in the past and click Continue, then select the name you want the account to have on that particular device and click Continue.
* At this point you will be forwarded to your wallet page. 

Address
=======

Address is an :ref:`account <02_intermediate:Account>` attribute derived from the :ref:`public key <02_intermediate:Account Keys>`. The address also contains the :ref:`chain ID <02_intermediate:Chain ID>` that identifies the blockchain network, therefore the address on the Mainnet cannot be used on the Testnet and vice versa.

The address is a :math:`26` byte array (see the :ref:`address binary format <02_intermediate:Address Binary Format>`). In UIs the address is displayed as a base58 encoded string.

.. code-block:: none

  3PDfnPknnYrg2k2HMvkNLDb3Y1tDTtEnp9X

Normally, the address starting with 3P refers to the Mainnet, and the address starting with 3M or 3N refers to Testnet or Stagenet.

The address is used to obtain information about the account:

* :ref:`Token balances <02_intermediate:Account Balance>`,
* Entries of :ref:`account data storage <02_intermediate:Account Data Storage>`,
* :ref:`Aliases <02_intermediate:Alias>`,
* :ref:`Assigned script <02_intermediate:dApp and Smart Account>`, etc.

The address is indicated:

* In :ref:`transfer <02_intermediate:Transfer Transaction>`, :ref:`mass transfer <02_intermediate:Mass Transfer Transaction>` and :ref:`lease transaction  <02_intermediate:Lease Transaction>` to identify a recipient;
* In :ref:`invoke script transactions <02_intermediate:Invoke Script Transaction>` to identify an invoked dApp.

Get Personal Address
====================

* Open `Decentral.Exchange <https://decentral.exchange/>`_ main screen and make sure you are logged into your account. Click on the account avatar and navigate to Address.
* Copy the address and use it, or you can also use the generated QR code.

Alias
=====

Alias is a short, easy to remember, name of the :ref:`address <02_intermediate:Address>`. The alias is unique on the blockchain. One address can have several aliases. The alias can be used instead of the address:

* In :ref:`transfer <02_intermediate:Transfer Transaction>`, :ref:`mass transfer <02_intermediate:Mass Transfer Transaction>` and :ref:`lease transaction <02_intermediate:Lease Transaction>` to identify a recipient; as well as in :ref:`invoke script transactions <02_intermediate:Invoke Script Transaction>` to identify an invoked dApp.
* To find an account in `DecentralChain Explorer <https://decentralscan.com/>`_.

The alias cannot be deleted.

Alias Requirements
------------------

The length of an alias can be from :math:`4` to :math:`30` bytes (:math:`1` character can take up to :math:`4` bytes). The following characters are allowed:

* lowercase Latin letters
* numbers
* dot
* underscore
* hyphen
* @

Create Alias
------------

You can use `Decentral.Exchange <https://decentral.exchange/>`_ online to create an alias. 

* Make sure you are logged into your account. On the main screen click on the account avatar and navigate to Aliases. 
* On the next screen select Create New and then type in the name of the alias and click Create New again to complete the process.

View Aliases
------------

The list of account aliases, as well as other blockchain data, is public and can be read by anyone. For example, you can see aliases in `DecentralChain Explorer <https://decentralscan.com/>`_. To do this, find an account by its :ref:`address <02_intermediate:Address>` and switch to the Aliases tab.

Using :ref:`Node REST API <documentation:placeholder>`, you can obtain a list of aliases by address using the GET/alias/by-address/{address} method and an address by alias using the GET /alias/by-alias/{alias} method.

Binary Format
-------------

See the :ref:`alias binary format <02_intermediate:Alias Binary Format>` article.

Account Balance
===============

Account balance is the amount of a :ref:`token (asset) <02_intermediate:Token (Asset)>` that belongs to the :ref:`account <02_intermediate:Account>`.

One account can store different tokens in different amounts. For example, an account can have :math:`50` :ref:`DecentralCoins <02_intermediate:DecentralCoin>` and USD-N at the same time. The amount of the Y token on the account is called the account balance in Y token. If there is no Y token on the account, it is said that the account balance in Y token is equal to zero.

Account Balance in DecentralCoin
---------------------------------

There are four types of balances in DecentralChain:

* regular
* available
* effective
* generating

The regular balance is the amount of :ref:`DecentralCoins <02_intermediate:DecentralCoin>` that belongs directly to the account. Thе other types of balances are determined counting :ref:`leased <02_intermediate:Leased Proof of Stake>` DecentralCoins.

Let us introduce the following notation:

.. code-block:: none

  R is the regular balance,
  Lo is the amount of DecentralCoins which the account leased to other accounts,
  Li is the amount of DecentralCoins which are leased to the account by other accounts.

Then:

.. code-block:: none

  Available balance = R – Lo
  Effective balance = R – Lo + Li
  Generating balance is the minimum value of the effective balance during the last 1000 blocks.

The generating balance of a :ref:`node <02_intermediate:Node>` account affects the ability to participate in block generation. To generate blocks, you need a generating balance of at least :math:`10000` DecentralCoins. The larger the generating balance, the greater the chance to add the next block is.

View Account Balance
--------------------

The balances of any account, as well as other blockchain data, are public and can be read by anyone. 

For example, you can see the list of tokens and their amount on the account in `DecentralChain Explorer <https://decentralscan.com/>`_. To do this, find an account by its address or alias. Balances in :ref:`DecentralCoin <02_intermediate:DecentralCoin>` are displayed right under the address, balances in other assets are at the Assets tab, and :ref:`non-fungible tokens (NFT) <02_intermediate:Non-Fungible Token>` are at the Non-fungible tokens tab.

.. image:: _static/image.jpg

Top up Balance
--------------

You can buy DecentralCoin tokens at `Decentral.Exchange <https://decentral.exchange/>`_.

Account Data Storage
====================

Account data storage is a key-value storage associated with an :ref:`account <02_intermediate:Account>`. 
The key of each entry is a unique string. The value is the data being stored, it’s store using one of the types:

* String
* Boolean
* Integral
* Array of bytes

The size of an account data storage is unlimited. For key and value size limitations, see the :ref:`data transaction <02_intermediate:Data Transaction>` article.

View Account Data
-----------------

Data storage of any account, as well as other blockchain data, are public and can be read by anyone. For example, you can see data entries in `DecentralChain Explorer <https://decentralscan.com/>`_. To do this, find an account by its :ref:`address <02_intermediate:Address>` or :ref:`alias <02_intermediate:Alias>` and switch to the Data tab.

.. image:: _static/image.jpg

Add, Modify, Delete Entries
---------------------------

The account owner can add, modify or delete entries of the account data storage via a :ref:`data transaction <02_intermediate:Data Transaction>`. 

A :ref:`dApp script <02_intermediate:dApp and Smart Account>` can add, modify or delete entries in the dApp's data storage as a result of an :ref:`invoke script <02_intermediate:Invoke Script Transaction>` transaction via script actions:

* :ref:`BinaryEntry <03_advanced:BinaryEntry>`
* :ref:`BooleanEntry <03_advanced:BooleanEntry>`
* :ref:`IntegerEntry <03_advanced:IntegerEntry>`
* :ref:`StringEntry <03_advanced:StringEntry>`
* :ref:`DeleteEntry <03_advanced:DeleteEntry>`

dApp and Smart Account
======================

An account with a script assigned to it becomes a dApp or smart account.
dApp is the account with the :ref:`dApp script <03_advanced:dApp Script>` assigned. dApp is an application whose functions can be called from other accounts via an :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>`. Callable functions can accept payments to the dApp and also perform actions applied to the blockchain:

* Add, modify or delete entries of the dApp account data storage.
* Transfer tokens from the dApp balance.
* Issue, reissue, burn tokens on behalf of the dApp, sponsorship setup.

Beyond that, a dApp script can comprise the verifier function that allows or denies transactions and orders that are sent on behalf of the dApp account depending on the specified conditions. The verifier function replaces the default verification that is used  to verify the sender's signature and allows you to set more complex rules, such as multisignature.

Using dApps, you can implement various blockchain-empowered applications: gaming and gambling, DeFi, digital identity, supply chains, and many others. 

A smart account is an account with the :ref:`account script <03_advanced:Account Script>` assigned. The account script is similar to a verifier function of a dApp script. Please note:

* To assign a script to an account, you have to send a :ref:`set script transaction <02_intermediate:Set Script Transaction>` on behalf of the account.
* You can also change or delete the script via the set script transaction, unless the script itself prohibits it.
* The :ref:`minimum fee <02_intermediate:Minimum Fee>` for any transaction sent from a dApp or smart account is increased by :math:`0.004` DecentralCoins if the complexity of sender's account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`. 

*************
Token (Asset)
*************

Token is a digital asset on the blockchain. A token can be used:

* As a cryptocurrency to pay for goods and services within a project, as well as for crowdfunding;
* As an object or resource in games etc.

A token can represent a physical or an intangible object. The words “token” and “asset” are used interchangeably in the DecentralChain ecosystem.
DecentralCoin is the native token on the DecentralChain blockchain. :ref:`More about DecentralCoin <02_intermediate:DecentralCoin>`.

All other tokens are custom tokens issued on behalf of some account. Any account that has enough DecentralCoins to pay the fee can issue its own token. The new token is immediately available:

* For transfers between accounts,
* For trading on `Decentral.Exchange <https://decentral.exchange/>`_ (except for :ref:`NFTs <02_intermediate:Non-Fungible Token>`; :ref:`smart assets <02_intermediate:Smart Asset>` trading is temporarily unavailable),
* For payments attached to dApp :ref:`script invocation <02_intermediate:Invoke Script Transaction>`.

Token Issue
===========

You can use `Decentral.Exchange <https://decentral.exchange/>`_ online to create an asset. 

* On the main screen make sure you are logged into your account, then click on Create Token.
* On the next screen specify the token parameters:

  * Name: The name of the created asset can not be shorter than :math:`4` characters.
  * Description: A short description where you can include website links that can be particularly useful.
  * Quantity: Define the total supply of your asset. The total supply can either be fixed at the issuance or increased later by making the asset re-issuable.
  * Reissuable: Defines if the asset total supply can be increased later. If set to reissuable, the issuer can increase the supply at any time (If reissuable is selected when the asset is created, it can be changed to not reissuable at a later stage).
  * Decimals: Specify how many decimals your asset will have. For example, if you specify :math:`8` decimals, as in Bitcoin, your asset can be divided down to :math:`0.00000001`.
  * :ref:`Smart asset <02_intermediate:Smart Asset>`: A smart asset is an asset with an attached script that places conditions on every transaction made for the asset in question.
  * Script (for issuing a smart asset).

* Before creating a new asset, carefully read the creation conditions. If necessary, change the name of the asset according to the conditions, then select the I understand... checkbox and click Generate.
* On the next screen double-check the entered data and if everything is correct click Send to finish the creation or click Go Back to make corrections..

The transaction fee is :math:`1` DecentralCoin for a regular token or :math:`0.001` DecentralCoins for a :ref:`non-fungible token (NFT) <02_intermediate:Non-Fungible Token>`.
Moreover, the token can be issued by the :ref:`dApp script <03_advanced:dApp Script>` as a result of the :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>` when the callable function result contains the :ref:`issue action <03_advanced:Issue>`. The minimum fee for invoke script transaction is increased by :math:`1` DecentralCoin for each non-NFT token issued.

Token ID
========

Token ID is a byte array calculated as follows:

* If the token is issued by :ref:`issue transaction <02_intermediate:Issue Transaction>`, the token ID is the same as the transaction ID.
* If the token is issued by :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>` when the callable function of :ref:`dApp script <02_intermediate:dApp and Smart Account>` performed the :ref:`issue action <03_advanced:Issue>`, the token ID is calculated as the BLAKE2b-256 hash of the byte array containing transaction ID and the fields of the Issue structure.

In the :ref:`Node REST API <documentation:placeholder>`, the token identifier is encoded in base58. For example:

.. code-block:: none

 "assetId": "8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS"

The :ref:`DecentralCoin <02_intermediate:DecentralCoin>` token has no identifier. The Node REST API uses null for DecentralCoin.

Token Operations
================

* Transfer to another account

Can be done via a :ref:`transfer transaction <02_intermediate:Transfer Transaction>` or a :ref:`mass transfer transaction <02_intermediate:Mass Transfer Transaction>`.
A :ref:`dApp script <02_intermediate:dApp and Smart Account>` can transfer the token via a :ref:`script transfer script action <03_advanced:Issue>` as a result of an :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>`.

* Exchange (trade deal)

Three accounts can participate in the exchange: one user creates an :ref:`order <02_intermediate:Order>` to buy a token, the other creates an order to sell a token. The matcher combines buy and sell orders with suitable parameters and creates an :ref:`exchange transaction <02_intermediate:Exchange Transaction>`.

* Burning

Decreases the amount of token on the account and thereby the total amount of the token on the blockchain. Any token owner can burn it, not only the issuer. It is impossible to burn :ref:`DecentralCoin <02_intermediate:DecentralCoin>`. Can be done via a :ref:`burn transaction <02_intermediate:Burn Transaction>`.
A dApp script can burn the token via a :ref:`burn script action <03_advanced:Burn>` as a result of the Invoke script transaction.

* Payment to :ref:`dApp <02_intermediate:dApp and Smart Account>`

An :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>` can contain up to two payments to the dApp. Payment amount and token are available to the callable function.

Operations Available Only to Issuer
-----------------------------------

The following token operations can only be performed by the account that issued the token:

* Sponsorship setup

The token issuer can enable sponsorship which allows all users to pay fees in this token (instead of DecentralCoins) for invoke script transactions and transfer transactions. :ref:`More about sponsorship <02_intermediate:Sponsored Fees>`. Enabling or disabling sponsorship can be done via a :ref:`sponsor fee transaction<02_intermediate:Sponsor Fee Transaction>`. A dApp script can set up sponsorship using a :ref:`SponsorFee <03_advanced:SponsorFee>` as a result of the invoke script transaction.

* Reissue

Increases the amount of token on the blockchain. The reissuable field of token determines whether the token can be reissued. Can be done via a :ref:`reissue transaction <02_intermediate:Reissue Transaction>`.
A dApp script can reissue the token via a :ref:`reissue script action <03_advanced:Reissue>` as a result of the invoke script transaction.

* Replacing the asset script

Can be done via a :ref:`set asset script transaction <02_intermediate:Set Asset Script Transaction>`. If the token is not a smart asset, that is, the script was not attached when the token was issued, then it is impossible to attach the script later.

* Modifying the token name and / or description

Can be done via an :ref:`update asset info transaction <02_intermediate:Update Asset Info Transaction>`.

Token Types
===========

Non-Fungible Token
------------------

Non-fungible token or NFT is a special type of a :ref:`token <02_intermediate:Token (Asset)>` that is issued with the following parameters:

* "quantity": :math:`1`
* "decimals": :math:`0`
* "reissuable": false

NFT is a singular entity that has a unique ID. This contrasts with a regular token, two coins of which (for example, two WBTC) cannot be distinguished from each other. NFTs can be used as in-game items, collectibles, certificates, or unique coupons. 

Issue of NFT
^^^^^^^^^^^^

NFT can be issued in the same ways as a regular token, see :ref:`token issue <02_intermediate:Token Issue>`. The minimum fee for an NFT issue is :math:`0.001` DecentralCoins, :math:`1000` times less than for a regular token.

Smart Asset
-----------

Smart asset is a :ref:`token <02_intermediate:Token (Asset)>` that has an :ref:`asset script <03_advanced:Asset Script>` assigned to it.
By default, tokens on the DecentralChain blockchain are not smart contracts, and any transactions with them are allowed. The script endows a token with functionality that sets the rules for its circulation. Each transaction involving a smart asset is automatically checked against the conditions specified in the script. If the asset's script allows the transaction, it will be executed; if the script denies the transaction, it is either not put onto the blockchain at all or saved as failed (for details, see the :ref:`transaction validation <02_intermediate:Transaction Validation>` article).

Using smart assets, you can implement various financial instruments on the blockchain (options, interval trading, taxation), game mechanics (allowing transactions only between characters with certain properties). Please note:

* If a token is issued without a script, then the script cannot be added later.
* The script cannot be removed, so it is impossible to turn a smart asset into a regular one.
* The asset script can be changed using the :ref:`set asset script transaction <02_intermediate:Set Asset Script Transaction>`, unless prohibited by the asset script itself (as well as by the :ref:`dApp or account script <02_intermediate:dApp and Smart Account>` assigned to the issuer account).
* The :ref:`minimum fee <02_intermediate:Minimum Fee>` for transaction is increased by :math:`0.004` DecentralCoins for each smart asset involved, except for:

  * :ref:`Invoke script transactions <02_intermediate:Invoke Script Transaction>`,
  * Smart assets used as matcher fee in :ref:`exchange transaction <02_intermediate:Exchange Transaction>`.

Tokens of Other Blockchains
---------------------------

A token issued on another blockchain cannot be used directly on the DecentralChain blockchain. A new token representing the original one can be issued on the DecentralChain blockchain, and a gateway that pegs the two tokens :math:`1:1` can be deployed. 

DecentralCoin
==============

DecentralCoin is the native :ref:`token <02_intermediate:Token (Asset)>` of the DecentralChain blockchain. :ref:`Block generators <02_intermediate:Generating Node>` receive :ref:`transaction fees <02_intermediate:Transaction Fees>` and :ref:`block rewards <02_intermediate:Block Reward>` in DecentralCoins, which encourages generators to maintain and develop the blockchain network infrastructure. The more DecentralCoins the generator holds (by ownership or lease), the greater its chance to add the next block is.

DecentralCoin Parameters
-------------------------

DecentralCoins are present on the blockchain since inception, there is no issue transaction for it, therefore the DecentralCoin token does not have an ID. The REST API uses null for DecentralCoins.
The number of decimal places (decimals) for DecentralCoins is :math:`8`. The atomic unit called Decentralite is :math:`\frac{1}{100,000,000}` DecentralCoins.

Leasing
-------

The owner of DecentralCoins can lease them via a :ref:`lease transaction <02_intermediate:Lease Transaction>`. DecentralCoins received on lease are included in the :ref:`generating balance <02_intermediate:Account Balance>`. Block generators send back different percentages as rewards to lessors. A lessor can cancel the lease at any time via a :ref:`lease cancel transaction <02_intermediate:Lease Cancel Transaction>`. :ref:`More about leasing <02_intermediate:Leased Proof of Stake>`.

How to Get DecentralCoin
-------------------------

You can buy DecentralCoins tokens at `Decentral.Exchange <https://decentral.exchange/>`_, or at one of the centralized exchanges. In addition, cryptocurrency gateways can be used to transfer external cryptocurrencies such as Bitcoin, Ethereum etc. from the external blockchain to the DecentralChain blockchain and vice versa. The gateway provides the user with the address on the external blockchain. After receiving a confirmation of transfer to this external address, the gateway transfers the corresponding asset (minus the fee) to the user's DecentralChain address. 

Token Custom Parameters
=======================

Below is an example of JSON representation returned by the GET /assets/details/{assetId} method of :ref:`Node REST API <documentation:placeholder>`:

.. code-block:: none

  {
    "assetId": "DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p",
    "issueHeight": 1806810,
    "issueTimestamp": 1574429393962,
    "issuer": "3PC9BfRwJWWiw9AREE2B3eWzCks3CYtg4yo",
    "issuerPublicKey": "BRnVwSVctnV8pge5vRpsJdWnkjWEJspFb6QvrmZvu3Ht",
    "name": "USD-N",
    "description": "Neutrino USD",
    "decimals": 6,
    "reissuable": false,
    "quantity": 999999999471258900,
    "scripted": false,
    "minSponsoredAssetFee": 7420,
    "originTransactionId": "DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p"
  }

.. csv-table:: Token Custom Parameters
  :file: _static/02_intermediate/tables/001_Token-Custom-Parameters.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

Atomic Unit
-----------

The amount of token is displayed differently in UIs and in the :ref:`JSON representation <02_intermediate:JSON Representation>` used by the :ref:`Node REST API <documentation:placeholder>`. In API requests and responses, amount values are integers indicated in atomic units to avoid precision issues in floating-point calculations. An atomic unit is the minimum fraction (“cent”) of a token, it is equal to :math:`10^{-decimals}`. The amount of token in JSON is the real quantity multiplied by :math:`10^{decimals}`.

For USD-N in the example above:

* decimals = :math:`6`,
* atomic unit is :math:`\frac{1}{1,000,000}` USD-N.
* "quantity": :math:`999999999471258900` corresponds to :math:`999,999,999,471.258900` USD-N in UIs, "minSponsoredAssetFee": :math:`7420` corresponds to :math:`0.007420` USD-N.

***********
Transaction
***********

Transaction Issue
=================

How to Sign and Send Transactions
---------------------------------

* In `Decentral.Exchange <https://decentral.exchange/>`_ you can create some types of transactions such as transfer, issue/reissue/burn, sponsor fee transaction, set asset script, create alias.
* Via :ref:`Node REST API <documentation:placeholder>`:

  * The POST /transactions/broadcast method sends a signed transaction to a node;
  * The POST /transactions/sign method generates transaction signature (but this method is only available to the node owner).

Transaction Sender and Signature
--------------------------------

Each transaction contains the public key of the sender’s account, on behalf of which the action is performed on the blockchain. :ref:`Smart accounts and dApps <02_intermediate:dApp and Smart Account>` can set their own rules for outgoing transactions verification. 

Transactions that are sent from an ordinary account (without script) must contain the sender's digital signature. The sender generates a signature using the account's private key. Along with the signature, the transaction contains the sender's public key, so the node (and anyone) can verify the integrity of the transaction data and the authenticity of the signature, that is, make sure that the signature of the transaction matches the public key.

After Transaction is Sent
-------------------------

Upon receiving a transaction, the node validates its signature, checks the sender's balance, and so on, see the :ref:`transaction validation <02_intermediate:Transaction Validation>` article for details. If the transaction is valid, the node puts the transaction to the UTX pool, which is a list of transactions awaiting to be added, and also broadcasts the transaction to other nodes of the blockchain network.

Due to block size limitation (:math:`1` MB) the transaction may not get to the block immediately. First of all, nodes add the most “profitable” transactions with the highest fee per byte.
After being added to a block, the transaction changes the blockchain state: account balances, records in the account data storage, and so on.
The transaction may never be added to a block if it becomes invalid while waiting in the UTX pool. For example, the transaction has expired (the timestamp is more than :math:`2` hours behind current time) or another transaction has changed the blockchain state and now the sender's balance is insufficient to execute the transaction or the account or asset script denies the transaction.

Transaction Proofs
==================

Verification by Script
----------------------

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, then the transaction is verified by the script assigned to the account instead of signature verification. The script allows or denies the transaction depending on whether it meets the specified conditions. In particular, the script can run various verifications of the proofs.

A common example is a smart account with a multisignature where three co-owner users store shared funds. 

Transaction Fees
================

Transaction fee is a fee that an :ref:`account <02_intermediate:Account>` owner pays to send a :ref:`transaction <02_intermediate:Transaction>`. A transaction sender can specify any amount of fee but not less than the minimum amount. The larger the fee is, the quicker the transaction will be added to the new :ref:`block <02_intermediate:Block>`.
For :ref:`invoke script transactions <02_intermediate:Invoke Script Transaction>` and :ref:`transfer transaction <02_intermediate:Transfer Transaction>`, a sender can specify a transaction fee nominated in a sponsored asset instead of :ref:`DecentralCoins <02_intermediate:DecentralCoin>`, see the section :ref:`fee in sponsored asset <02_intermediate:Fee in Sponsored Asset>` below.

Regular Fees
------------

Minimum Fee
^^^^^^^^^^^

The minimum fees in DecentralCoins for each type of transaction are listed below.

* If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. If the order sender in :ref:`exchange transaction <02_intermediate:Exchange Transaction>` is a dApp or smart account, this does nor affect the minimum fee.
* The minimum fee is increased by :math:`0.004` DecentralCoins for each smart asset involved, except for:

  * :ref:`Invoke script transactions <02_intermediate:Invoke Script Transaction>`,
  * :ref:`Smart assets <02_intermediate:Smart Asset>` used as matcher fees in exchange transactions.

:strong:`Example 1`

* The minimum fee for a transfer transaction:
* No smart account or smart assets: :math:`0.001` DecentralCoins.
* Transfer from smart account*: :math:`0.001 + 0.004 = 0.005` DecentralCoins.
* Transfer of smart asset: :math:`0.001 + 0.004 = 0.005` DecentralCoins.
* Transfer of smart asset sent from smart account*: :math:`0.001 + 0.004 + 0.004 = 0.009` DecentralCoins.

If the account script complexity is higher than the :ref:`sender complexity threshold <03_advanced:Limitations>`.

:strong:`Example 2`

The minimum fee for an Invoke Script transaction:

* No smart account, no assets issued: :math:`0.005` DecentralCoins.
* dApp script invocation is sent from a smart account*: :math:`0.005 + 0.004 = 0.009` DecentralCoins.
* dApp script invocation issues an asset that is not :ref:`non-fungible tokens <02_intermediate:Non-Fungible Token>`: :math:`0.005 + 1 = 1.005` DecentralCoins.
* dApp script invocation is sent from smart account*, and :math:`10` assets that are not non-fungible tokens are issued: :math:`0.005 + 0.004 + 10 × 1 = 10.009` DecentralCoins.

If the account script complexity is higher than the :ref:`sender complexity threshold <03_advanced:Limitations>`.

.. csv-table:: Minimum Fees
  :file: _static/02_intermediate/tables/002_Minimum-Fees.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 2 1 3

Fee for Failed Transactions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Invoke script transactions <02_intermediate:Invoke Script Transaction>` and :ref:`exchange transactions <02_intermediate:Exchange Transaction>` can be saved on the blockchain even if the result of a dApp script or asset script execution failed. In this case, the sender is charged a fee. For an exchange transaction, the matcher is charged the transaction fee but the order senders are not charged the matcher fee. :ref:`More about transaction validation<02_intermediate:Transaction Validation>`.

Fee in Sponsored Asset
^^^^^^^^^^^^^^^^^^^^^^

An issuer of an asset can set up sponsorship — so that any user can specify a transaction fee in this asset for :ref:`invoke script transactions <02_intermediate:Invoke Script Transaction>` and :ref:`transfer transactions <02_intermediate:Transfer Transaction>`.
To activate sponsorship, the issuer puts a :ref:`sponsor fee transaction<02_intermediate:Sponsor Fee Transaction>` that specifies an amount of asset that is equivalent to the minimum fee of :math:`0.001` DecentralCoins. For example, if minSponsoredAssetFee: :math:`5`, then the fee in this asset for an invoke script transaction equals :math:`5 * \frac{0.005}{0.001} = 25`. 

Sponsored Fees
--------------

Users of DecentralChain-based apps should pay a fee for each transaction. This is the entry threshold for new users. Sometimes users don't know anything about :ref:`DecentralCoins <02_intermediate:DecentralCoin>` or don't understand how to get DecentralCoins or don't want to spend money. Sponsorship enables launching apps that do not require DecentralCoins from users.

Sponsored Asset
^^^^^^^^^^^^^^^

An account that issued an asset can enable sponsorship, that is, allow all users to pay a fee in this asset for :ref:`invoke script transactions <02_intermediate:Invoke Script Transaction>` and :ref:`transfer transactions <02_intermediate:Transfer Transaction>`. The sponsor can distribute the sponsored asset among app users.

How to Enable Sponsorship
^^^^^^^^^^^^^^^^^^^^^^^^^

You can use `Decentral.Exchange <https://decentral.exchange/>`_ online to enable sponsorship. 

* Make sure you are logged into your account. Find the desired asset in the list, hover cursor over it and in its menu (⋮) click Enable Sponsorship.
* Carefully read the Terms and Conditions before proceeding and then in the Amount per transaction box specify the required amount of sponsored asset to be charged to users. Then click Continue.
* In the following window double-check the entered data and if everything is correct click Send or click Go Back to make corrections. Activation will be processed with the next block.
* After activation you'll be able to change the specified amount without deactivation. To do so, find your asset in the list, hover cursor over it and in its menu (⋮) click Change Sponsorship.

The fee for this type of transaction is :math:`0.001` DecentralCoins.

How to Disable Sponsorship
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use `Decentral.Exchange <https://decentral.exchange/>`_ online to disable sponsorship. 

* Make sure you are logged into your account. Find the desired asset in the list, hover cursor over it and in its menu (⋮) click Disable Sponsorship.
* In the following window click Sign to deactivate the sponsorship. Deactivation will be processed with the next block.

Restrictions
^^^^^^^^^^^^

* Only the issuer of the asset can be a sponsor.
* Smart assets cannot be sponsored assets.
* Sponsorship only works if the sponsor's account balance is greater than :math:`1.005` DecentralCoins. If the account balance becomes less than :math:`1.005` DecentralCoins, the sponsorship is suspended, and if the balance becomes more than :math:`1.005` DecentralCoins the sponsorship is resumed.
* The fee in the sponsored asset can only be specified for :ref:`invoke script transactions <02_intermediate:Invoke Script Transaction>` and :ref:`transfer transactions <02_intermediate:Transfer Transaction>`.

How It Works
^^^^^^^^^^^^

After :ref:`enabling sponsorship <02_intermediate:How to Enable Sponsorship>`, if the requirements described in the :ref:`restrictions <02_intermediate:Restrictions>` section are met, the sponsorship works as follows:

* A user broadcasts a transaction and specifies a fee in the sponsored asset.
* The sponsor receives the fee in the sponsored asset from the user's account.
* Block generators receive the fee in DecentralCoins from the sponsor's account (in accordance with the :ref:`DecentralChain-M5 protocol <02_intermediate:DecentralChain-M5 Protocol>`, the fee is distributed between the current block generator and the next block generator in a ratio of :math:`\frac{40}{60}`.

The script on the sponsor's account is not executed and does not affect the sponsorship because the transaction is sent from the user's account.

.. image:: _static/image.jpg

The fee in :ref:`DecentralCoins <02_intermediate:DecentralCoin>` charged to the sponsor is proportional to the fee specified by the transaction sender:

.. code-block:: none

  feeInDecentralCoins = feeInSponsoredAsset × 0,001 / minSponsoredAssetFee

minSponsoredAssetFee is the amount of sponsored asset equivalent to :math:`0.001` DecentralCoins. The sponsor sets this value when enabling sponsorship.
For example, if the sponsor sets :math:`3` tokens = :math:`0.001` DecentralCoins, then the minimum fee for :ref:`invoke script transactions <02_intermediate:Invoke Script Transaction>` is :math:`15` tokens, which corresponds to :math:`0.005` DecentralCoins. Please note:

* The user can use the sponsored asset to pay for transactions that are not related to a certain app.
* The user can specify any amount of fee, such as the one significantly exceeding the minimum.

Transaction Representations
===========================

JSON Representation
-------------------

The :ref:`Node REST API <documentation:placeholder>` of DecentralChain nodes uses the JSON representation of transactions. You can send transactions to a node and read transactions stored on the blockchain via REST API in JSON. Here is an example of JSON representation:

.. code-block:: none

  {
    "senderPublicKey": "BVv1ZuE3gKFa6krwWJQwEmrLYUESuUabNCXgYTmCoBt6",
    "sender": "3N8S4UtauvDAzpLiaRyDdHn9muexWHhBP4D",
    "feeAssetId": null,
    "proofs": [
      "22QJfRKX7kUQt4qjdnUqZAnhqukqhnofE27uvP8Q5xnBf8M6PCNtWVGq2ngm6m7Voe7duys59D1yU9jhKrmdXDCe"
    ],
    "fee": 100000,
    "alias": "91f452553298770f",
    "id": "AD7KmXwoVNc2fXsmaxsHsrnT1tfPF3HsWYtfjFijVsvM",
    "type": 10,
    "version": 2,
    "timestamp": 1548443069053,
    "height": 466104
  }

.. csv-table:: JSON Representation
  :file: _static/02_intermediate/tables/003_JSON-Representation.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

The sender, id, applicationStatus, and height fields do not need to be filled when sending a transaction, and they are not stored on the blockchain. The node calculates these fields when providing transaction data via the Node REST API.
The fields that depend on the type of transaction are listed in the description of each :ref:`type of transaction <02_intermediate:Transaction Types>`.

Binary Format
-------------

Transactions are stored on the blockchain in the binary format (byte representation). :ref:`Node extensions <documentation:placeholder>` such as :ref:`gRPC server <documentation:placeholder>` can work directly with data in binary format.
The transaction signature and ID are also formed on the basis of the binary format. The guideline for generating a signature and ID is given in the :ref:`cryptographic practical details <02_intermediate:Cryptographic Practical Details>` article.
Transaction binary format is described in the :ref:`transaction binary format <02_intermediate:Transaction Binary Format>` article.

You can get the transaction by ID, or the list of transactions by certain account address, or the list of all transactions in the block:

 * In `DecentralChain Explorer <https://decentralscan.com/>`_.
 * Via :ref:`Node REST API <documentation:placeholder>` using the following methods:

   * GET /transactions/info/{id} returns transaction data by transaction ID.
   * GET /transactions/address/{address}/limit/{limit} returns the list of transactions where the specified address is involved.
   * GET /blocks/at/{height} returns block data at the specified height including all transactions in the block.

Transaction Types
=================

Tokenization
------------

.. csv-table:: Tokenization
  :file: _static/02_intermediate/tables/004_Tokenization.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 3

Issue Transaction
^^^^^^^^^^^^^^^^^

Issue transaction creates a new :ref:`token <02_intermediate:Token (Asset)>`.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for an issue transaction is :math:`1` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`, in case of issue of a :ref:`non-fungible tokens (NFT) <02_intermediate:Non-Fungible Token>` :math:`0.001` DecentralCoins.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "2M25DqL2W4rGFLCFadgATboS8EPqyWAN3DjH12AH5Kdr",
    "quantity": 50000,
    "fee": 100000000,
    "description": "Script true.",
    "type": 3,
    "version": 2,
    "reissuable": true,
    "script": "base64:AQa3b8tH",
    "sender": "3Mz9N7YPfZPWGd4yYaX6H53Gcgrq6ifYiH7",
    "feeAssetId": null,
    "chainId": 84,
    "proofs": [
      "4yjVxzrLuXUq5y2QCa2LDn1Fp9P63hPBmqDLGQCqn41EB1uZ1pys79NP81h7FxRBnZSbpNGbz1xjwckHcPAQHmFX"
    ],
    "assetId": "7Xpp9PPeZbG4wboJrcbRQdq3SxCJqbeFRUjjKccM1DsD",
    "decimals": 2,
    "name": "Smart",
    "id": "7Xpp9PPeZbG4wboJrcbRQdq3SxCJqbeFRUjjKccM1DsD",
    "timestamp": 1548653407494,
    "height": 469677
  }

.. csv-table:: Issue Transaction JSON Representation
  :file: _static/02_intermediate/tables/005_Issue-Transaction-JSON.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

The assetId field does not need to be filled when sending a transaction, and it is not stored on the blockchain. The node calculates these fields when providing transaction data via the REST API. The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`issue transaction binary format <02_intermediate:Issue Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`IssueTransaction structure <03_advanced:IssueTransaction>` is used for transaction handling in smart contracts.

Reissue Transaction
^^^^^^^^^^^^^^^^^^^

Reissue transaction increases the amount of the :ref:`token <02_intermediate:Token (Asset)>` on the blockchain and/or prohibits its reissue. Only the token issuer can send a reissue transaction. The additional amount of token increases the balance of the transaction sender. The reissuable field of the token determines whether the token can be reissued.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a reissue transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`. If the token is a smart asset, the minimum fee is increased by :math:`0.004` DecentralCoins.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "DjYEAb3NsQiB6QdmVAzkwJh7iLgUs3yDLf7oFEeuZjfM",
    "quantity": 200000,
    "fee": 100000000,
    "type": 5,
    "version": 2,
    "reissuable": true,
    "sender": "3PLJciboJqgKsZWLj7k1VariHgre6uu4S2T",
    "feeAssetId": null,
    "chainId": 87,
    "proofs": [
      "5mEveeUwBdBqe8naNoV5eAe5vj6fk8U743eHGkhxhs3v9PMsb3agHqpe4EtzpUFdpASJegXyjrGSbynZg557cnSq"
    ],
    "assetId": "GA4gB3Lf3AQdF1vBCbqGMTeDrkUxY7L83xskRx6Z7kEH",
    "id": "27ETigYaHym2Zbdp4x1gnXnZPF1VJCqQpXmhszC35Qac",
    "timestamp": 1548521785933,
    "height": 1368623
  }

.. csv-table:: Reissue Transaction JSON Representation
  :file: _static/02_intermediate/tables/006_Reissue-Transaction-JSON.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4
   
The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`reissue transaction binary format <02_intermediate:Reissue Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`ReissueTransaction structure <03_advanced:ReissueTransaction>` is used for transaction handling in smart contracts.

Burn Transaction
^^^^^^^^^^^^^^^^

Burn transaction decreases the amount of token on sender's account and thereby the total amount of the token on the blockchain. Any account that owns a token (not necessarily the token issuer) can send the burn transaction. Burned tokens cannot be restored back to the account.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a burn transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`, in case of burning a smart asset :math:`0.005` DecentralCoins.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "9GaQj7gktEiiS1TTTjGbVjU9bva3AbCiawZ11qFZenBX",
    "amount": 9999,
    "fee": 100000,
    "type": 6,
    "version": 2,
    "sender": "3P9QZNrHbyxXj8P9VrJZmVu2euodNtA11UW",
    "feeAssetId": null,
    "chainId": 87,
    "proofs": [
      "61jCivdv3KTuTY6QHgxt4jaGrXcszWg3vb9TmUR26xv7mjWWwjyqs7X5VDUs9c2ksndaPogmdunHDdjWCuG1GGhh"
    ],
    "assetId": "FVxhjrxZYTFCa9Bd4JYhRqXTjwKuhYbSAbD2DWhsGidQ",
    "id": "csr25XQHT1c965Fg7cY2vJ7XHYVsudPYrUbdaFqgaqL",
    "timestamp": 1548660675277,
    "height": 1370971
  }

.. csv-table:: Burn Transaction JSON Representation
  :file: _static/02_intermediate/tables/007_Burn-Transaction-JSON.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`burn transaction binary format <02_intermediate:Burn Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`BurnTransaction structure <03_advanced:BurnTransaction>` is used for transaction handling in smart contracts.

Set Asset Script Transaction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set asset script transaction replaces the :ref:`asset script <03_advanced:Asset Script>`. Only the token issuer can send an asset script transaction. If a token is issued without a script, then no script can be assigned to it. It is also impossible to remove the script and turn the smart asset into a regular one.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a set asset script transaction is :math:`1` :ref:`DecentralCoin <02_intermediate:DecentralCoin>`. 

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "AwQYJRHZNd9bvF7C13uwnPiLQfTzvDFJe7DTUXxzrGQS",
    "fee": 100000000,
    "type": 15,
    "version": 1,
    "script": "base64:AQa3b8tH",
    "sender": "3P67JUW8Djit7hMjKhADmn6CWvKPbRuh2sQ",
    "feeAssetId": null,
    "chainId": 87,
    "proofs": [
      "nzYhVKmRmd7BiFDDfrFVnY6Yo98xDGsKrBLWentF7ibe4P9cGWg4RtomHum2NEMBhuyZb5yjThcW7vsCLg7F8NQ"
    ],
    "assetId": "7qJUQFxniMQx45wk12UdZwknEW9cDgvfoHuAvwDNVjYv",
    "id": "FwYSpmVDbWQ2BA5NCBZ9z5GSjY39PSyfNZzBayDiMA88",
    "timestamp": 1547201038106,
    "height": 1346345
  }

.. csv-table:: Set Asset Script Transaction JSON Representation
  :file: _static/02_intermediate/tables/008_Set-Asset-Script-Transaction-JSON.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`set asset script transaction binary format <02_intermediate:Set Asset Script Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`SetAssetScriptTransaction structure <03_advanced:SetAssetScriptTransaction>` is used for transaction handling in smart contracts.

Update Asset Info Transaction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update asset info transaction modifies the name and description of the token. 

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for an update asset info transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`, in case of a smart asset :math:`0.005` DecentralCoins.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "6a6r9d3r2ccyE9SvuxmdZbfSHXmKPUoExnigvippJLfu",
    "fee": 100000,
    "description": "xxxXXXxxx",
    "type": 17,
    "version": 1,
    "applicationStatus": "succeeded",
    "sender": "3MQdH4MAmM5RNz5TAT43UXXCvMtCa9YgHq9",
    "feeAssetId": null,
    "chainId": 83,
    "proofs": [
      "4DfvJL4cVisQaMuMB7ar15EtYZTvTZzAUQQMkq4RA3uTMzziVYLrbNHSL2a1eCqBV3YQb7dddXdjywETXHuu65ij"
    ],
    "assetId": "syXBywr2HVY7wxqkaci1jKY73KMpoLh46cp1peJAZNJ",
    "name": "zzzz",
    "id": "4DL8K4bRvYb9Qrys9Auq7hSGuLGq8XsUYZqDDBBfVGMf",
    "timestamp": 1591886337668,
    "height": 411389
  }

.. csv-table:: Update Asset Info Transaction JSON Representation
  :file: _static/02_intermediate/tables/009_Update-Asset-Info-Transaction-JSON.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`update asset info transaction binary format <02_intermediate:Update Asset Info Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`UpdateAssetInfoTransaction structure <03_advanced:UpdateAssetInfoTransaction>` is used for transaction handling in smart contracts.

Usage
-----

.. csv-table:: Usage
  :file: _static/02_intermediate/tables/010_Usage.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 3

Transfer Transaction
^^^^^^^^^^^^^^^^^^^^

Transfer transaction transfers a certain amount of token to another account.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a transfer transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`, in case of transferring a smart asset :math:`0.005` DecentralCoins.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "Cs4DShy4nTx6WyxjKRoDtoYsGhvT663pYLysPCLeVZHE",
    "amount": 15540,
    "signature": "5EaYqFx2xFJmdvwZ1gT3yLecKr88z3jByCj5GE1MjE1ossvehExZKoT7uhGatiYCGM9Co8iUR8Q5ce52XDmno3rn",
    "fee": 100000,
    "type": 4,
    "version": 1,
    "attachment": "3vrgtyozxuY88J9RqMBBAci2UzAq9DBMFTpMWLPzMygGeSWnD7k",
    "sender": "3PN2bVFxJjgudPKqEGZ41TVsD5ZJmxqnPSu",
    "feeAssetId": null,
    "proofs": [
      "5EaYqFx2xFJmdvwZ1gT3yLecKr88z3jByCj5GE1MjE1ossvehExZKoT7uhGatiYCGM9Co8iUR8Q5ce52XDmno3rn"
    ],
    "assetId": "7uncmN7dZfV3fYVvNdYTngrrbamPYMgwpDnYG1bGy6nA",
    "recipient": "3PFmoN5YLoPNsL4cmNGkRxbUKrUVntwyAhf",
    "feeAsset": null,
    "id": "D79kL1Jr5xyL2Rmw2FnafQHugJGvuBhNEbLnhMuwMkDC",
    "timestamp": 1548660895034,
    "height": 1370973
  }

.. csv-table:: Transfer Transaction JSON Representation
  :file: _static/02_intermediate/tables/011_Transfer-Transaction-JSON.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`transfer transaction binary format <02_intermediate:Transfer Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`TransferTransaction structure <03_advanced:TransferTransaction>` is used for transaction handling in smart contracts.

Exchange Transaction
^^^^^^^^^^^^^^^^^^^^

Exchange transaction exchanges two different tokens between two accounts. Commonly the exchange transaction is created by the matcher service that executes orders to buy and sell tokens. The exchange transaction contains two counter orders: a buy order and a sell order. The blockchain guarantees that the terms of the exchange are not worse than those indicated in each order.

An order can be filled partially. An order can participate in several exchange transactions, with different counter orders. One of the two exchanged tokens is the amount asset (base currency): it represents the amount of token in orders and in the Exchange transaction. Another token is a price asset (quote currency): it represents the price.

.. image:: _static/image.jpg

:strong:`Transaction Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for an exchange transaction is :math:`0.003` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`. In case of exchange of a :ref:`smart asset <02_intermediate:Smart Asset>` for an ordinary asset the minimum fee is :math:`0.007` DecentralCoins, in case of exchange of two smart assets the minimum fee is :math:`0.011` DecentralCoins.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`Matcher Fee`

The matcher receives a fee for order execution from each order sender. The minimum matcher fee is set by the matcher. The order sender specifies the fee not less than the minimum amount.

If the order is fully filled with one exchange transaction, the matcher receives the entire fee specified in the order. If the order is partially filled, the matcher receives a part of the fee. The blockchain guarantees that the total matcher fee received from the order sender in all exchange transactions does not exceed the fee specified in the order.

.. image:: _static/image.jpg

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "9cpfKN9suPNvfeUNphzxXMjcnn974eme8ZhWUjaktzU5",
    "amount": 100000000,
    "fee": 300000,
    "type": 7,
    "version": 2,
    "sellMatcherFee": 750,
    "sender": "3PEjHv3JGjcWNpYEEkif2w8NXV4kbhnoGgu",
    "feeAssetId": null,
    "proofs": [
      "LQD8VoFhHEW2b6o2e2ujzDHdZatwMMwigC2tmoSHcFNRGXrowA1yyVxD6nZBNeABLWjs59dnuLhgNP7UMfFKDuR"
    ],
    "price": 1134500,
    "id": "EHLccXcemZPEvUpM9UkASG1GciwMt9R5B3QuYFxywj9g",
    "order2": {
      "version": 3,
      "id": "JCiF3gmprLc8u7xdWR7KUkJ3YfM6yfgxB6CvhJYGJFAa",
      "sender": "3PRBeeFD64wvTMfS3HEoDDFPXfJs3gFdAxk",
      "senderPublicKey": "ytgWVbKG9e6TSsQ5buMryr2QyxNoL3RezXP3f9RJ2As",
      "matcherPublicKey": "9cpfKN9suPNvfeUNphzxXMjcnn974eme8ZhWUjaktzU5",
      "assetPair": {
        "amountAsset": null,
        "priceAsset": "DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p"
      },
      "orderType": "sell",
      "amount": 40000000000,
      "price": 1134500,
      "timestamp": 1591356602063,
      "expiration": 1593862202062,
      "matcherFee": 300000,
      "matcherFeeAssetId": null,
      "signature": "3D2Ngr7H6MQRs1izMQSix3dMHmDfg4bcRjxamFXFsb4Ku28neNWHdtwE6LtR3eq69Jqr1CvEsAKCWkQEeEEomcoK",
      "proofs": [
        "3D2Ngr7H6MQRs1izMQSix3dMHmDfg4bcRjxamFXFsb4Ku28neNWHdtwE6LtR3eq69Jqr1CvEsAKCWkQEeEEomcoK"
      ]
    },
    "order1": {
      "version": 3,
      "id": "FNvEGPgUqEWnrnpxevZQnaZS3DUTBGE2wa6L75xCw7mo",
      "sender": "3PDxxx7eSeYLgzTAtuAV7gUCtHeeXeU85fP",
      "senderPublicKey": "3WEkbavP3Sw4y5tsgxbZvKkWh87BdB3CPVVxhcRUDBsJ",
      "matcherPublicKey": "9cpfKN9suPNvfeUNphzxXMjcnn974eme8ZhWUjaktzU5",
        "assetPair": {
        "amountAsset": null,
        "priceAsset": "DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p"
      },
      "orderType": "buy",
      "amount": 100000000,
      "price": 1134500,
      "timestamp": 1591356752271,
      "expiration": 1593862352271,
      "matcherFee": 300000,
      "matcherFeeAssetId": null,
      "signature": "2gvqaYy2BFbK4BJZS8taRJnhgfQ1z2CytF2RqjcyEfzFiu9tkTjN5q4UyFXpPqS3E6eD2WQBUaYCTYDKv98iW1sy",
      "proofs": [
        "2gvqaYy2BFbK4BJZS8taRJnhgfQ1z2CytF2RqjcyEfzFiu9tkTjN5q4UyFXpPqS3E6eD2WQBUaYCTYDKv98iW1sy"
      ]
    },
    "buyMatcherFee": 300000,
    "timestamp": 1591356752456,
    "height": 2093333
  }

.. csv-table:: Exchange Transaction JSON Representation
  :file: _static/02_intermediate/tables/012_Exchange-Transaction-JSON.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`exchange transaction binary format <02_intermediate:Exchange Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`ExchangeTransaction structure <03_advanced:ExchangeTransaction>` is used for transaction handling in smart contracts.

Create Alias Transaction
^^^^^^^^^^^^^^^^^^^^^^^^

Create Alias transaction creates an :ref:`alias <02_intermediate:Alias>` for the sender's address.A created alias cannot be deleted.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a Create Alias transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey":"BVv1ZuE3gKFa6krwWJQwEmrLYUESuUabNCXgYTmCoBt6",
    "sender":"3N8S4UtauvDAzpLiaRyDdHn9muexWHhBP4D",
    "feeAssetId":null,
    "proofs": [
      "22QJfRKX7kUQt4qjdnUqZAnhqukqhnofE27uvP8Q5xnBf8M6PCNtWVGq2ngm6m7Voe7duys59D1yU9jhKrmdXDCe"
    ],
    "fee":100000,
    "alias":"91f452553298770f",
    "id":"AD7KmXwoVNc2fXsmaxsHsrnT1tfPF3HsWYtfjFijVsvM",
    "type":10,
    "version":2,
    "timestamp":1548443069053,
    "height":466104
  }

.. csv-table:: Create Alias Transaction JSON Representation
  :file: _static/02_intermediate/tables/013_Create-Alias-Transaction-JSON.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`create alias transaction binary format <02_intermediate:Create Alias Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`CreateAliasTransaction structure <03_advanced:CreateAliasTransaction>` is used for transaction handling in smart contracts.

Mass Transfer Transaction
^^^^^^^^^^^^^^^^^^^^^^^^^

Mass transfer transaction transfers a :ref:`token <02_intermediate:Token (Asset)>` to several accounts, from :math:`1` :ref:`DecentralCoin <02_intermediate:DecentralCoin>` to :math:`100` DecentralCoins .

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a Mass Transfer transaction is :math:`0.001 + 0.0005 × N` DecentralCoins, in case of transferring a :ref:`smart asset <02_intermediate:Smart Asset>` :math:`0.001 + 0.0005 × N` DecentralCoins, where :math:`N` DecentralCoins is the number of recipients. The fee value is rounded up to three decimals.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "5DphrhGy6MM4N3yxfB2uR2oFUkp2MNMpSzhZ4uJEm3U1",
    "fee": 5100000,
    "type": 11,
    "transferCount": 100,
    "version": 1,
    "totalAmount": 500000000000,
    "attachment": "xZBWqm9Ddt5BJVFvHUaQwB7Dsj78UQ5HatQjD8VQKj4CHG48WswJxUUeHEDZJkHgt9LycUpHBFc8ENu8TF8vvnDJCgfy1NeKaUNydqy9vkACLZjSqaVmvfaM3NQB",
    "sender": "3P2rvn2Hpz6pJcH8oPNrwLsetvYP852QQ2m",
    "feeAssetId": null,
    "proofs": [
      "FmGBaWABAy5bif7Qia2LWQ5B4KNmBnbXETL1mE6XEy4AAMjftt3FrxAa8x2pZ9ux391oY5c2c6ZSDEM4nzrvJDo"
    ],
    "assetId": "Fx2rhWK36H1nfXsiD4orNpBm2QG1JrMhx3eUcPVcoZm2",
    "transfers": [
      {
        "recipient": "3PHnjQrdK389SbzwPEJHYKzhCqWvaoy3GQB",
        "amount": 5000000000
      },
      {
        "recipient": "3PGNLwUG2GPpw74teTAxXFLxgFt3T2uQJsF",
        "amount": 5000000000
      },
      {
        "recipient": "3P5kQneM9EdpVUbFLgefD385LLYTXY5J32c",
        "amount": 5000000000
      },
      ...
    ],
    "id": "3LRfudet7avpQcW1AdauiBGb8SSRAaoCugDzngDPLVcv",
    "timestamp": 1528973951321,
    "height": 1041197
  }

.. csv-table:: Mass Transfer Transaction JSON Representation
  :file: _static/02_intermediate/tables/014_Mass-Transfer-Transaction-JSON.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

The transferCount and totalAmount fields do not need to be filled when sending a transaction, and they are not stored on the blockchain. The node calculates these fields when providing transaction data via the REST API.

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`mass transfer transaction binary format <02_intermediate:Mass Transfer Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`MassTransferTransaction structure <03_advanced:MassTransferTransaction>` is used for transaction handling in smart contracts.

Data Transaction
^^^^^^^^^^^^^^^^

Data transaction adds, modifies and deletes data entries in sender's :ref:`account data storage <02_intermediate:Account Data Storage>`. Limitations are as follows:

* The maximum number of entries is :math:`100`.
* For a transaction version 2 the maximum data size (keys + values) is :math:`165,890` bytes.
* For a transaction version 1 the maximum transaction size (except proofs) is :math:`153,600` bytes.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a Data transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>` per kilobyte, the size is rounded up to an integer number of kilobytes.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "38bYRUxFCaoa9h822nMnsoTX1qfczqtHJLgouNcNnd8h",
    "data": [
      {
        "type": "boolean",
        "value": true,
        "key": "bool"
      },
      {
        "type": "binary",
        "value": "base64:SGVsbG8gV2F2ZXM=",
        "key": "bin"
      },
      {
        "type": "integer",
        "value": 1234567,
        "key": "int"
      },
      {
        "type": "string",
        "value": "some text",
        "key": "str"
      }
    ],
    "sender": "3N4iKL6ikwxiL7yNvWQmw7rg3wGna8uL6LU",
    "feeAssetId": null,
    "proofs": [
      "kE1hjN1yW68j8DsYGNB7Gg1ydC4hqRmt3wBaFQUPkftnbiM7QfJCn1gTHgveJ7pCLXvvqffhKBmiF8qS1Uqk6SR"
    ],
    "fee": 100000,
    "id": "3EPJuvQiJYiu9Y5g6mYDQgHVu8GFUfnZurHrVwwF1ViH",
    "type": 12,
    "version": 2,
    "timestamp": 1591351545000,
    "height": 1029815
  }

.. csv-table:: Data Transaction JSON Representation
  :file: _static/02_intermediate/tables/015_Data-Transaction-JSON.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`data transaction binary format <02_intermediate:Data Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`DataTransaction structure <03_advanced:Limitations>` is used for transaction handling in smart contracts.

Set Script Transaction
^^^^^^^^^^^^^^^^^^^^^^

Set script transaction assigns the dApp script :ref:`dApp script <03_advanced:dApp Script>` or :ref:`account script <03_advanced:Account Script>` to the sender's account.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a Set Script transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "7nLAwoiRA4fWF4VHd6gRsbwF2UFFmRADXHqRcgy3h27w",
    "sender": "3N9yCRmNsLK2aPStjLBne3EUiPSKvVHYgKk",
    "feeAssetId": null,
    "chainId": 84,
    "proofs": [
      "2ihGFLUbvJHEpuGRqx5MXEXsEzwMuCmB8FgUTZgSPdANA4iab4M3nsNJ7a7hyiuqjrvwNCHoWn69hvUeziJiSAie"
    ],
    "fee": 1400000,
    "id": "28hbeFhYBq6uir1bbjt2dxbpqxCM2B6GKq4c7zf7AbkX",
    "type": 13,
    "version": 1,
    "script": "base64:AAIDAAAAAAAAAAYIARIAEgAAAAACAQAAAApyYW5kb21pemVyAAAAAQAAAANpbnYEAAAACGxhc3RQbGF5BAAAAAckbWF0Y2gwCQAEHAAAAAIFAAAABHRoaXMCAAAACGxhc3RQbGF5AwkAAAEAAAACBQAAAAckbWF0Y2gwAgAAAApCeXRlVmVjdG9yBAAAAAFzBQAAAAckbWF0Y2gwBQAAAAFzAwkAAAEAAAACBQAAAAckbWF0Y2gwAgAAAARVbml0BAAAAAFhBQAAAAckbWF0Y2gwAQAAAAxXYXZlc0xvdHRvVjIJAQAAAAV0aHJvdwAAAAAEAAAABHJhbmQJAADLAAAAAgkAAMsAAAACCQAAywAAAAIJAADLAAAAAgkAAMsAAAACBQAAAAhsYXN0UGxheQgFAAAAA2ludgAAAA10cmFuc2FjdGlvbklkCAUAAAADaW52AAAAD2NhbGxlclB1YmxpY0tleQgFAAAACWxhc3RCbG9jawAAABNnZW5lcmF0aW9uU2lnbmF0dXJlCQABmgAAAAEIBQAAAAlsYXN0QmxvY2sAAAAJdGltZXN0YW1wCQABmgAAAAEIBQAAAAlsYXN0QmxvY2sAAAAGaGVpZ2h0CQAB9wAAAAEFAAAABHJhbmQBAAAACnN0YXJ0TG90dG8AAAABAAAAA2ludgQAAAAJcGxheUxpbWl0CQAAaQAAAAIJAQAAAAx3YXZlc0JhbGFuY2UAAAABBQAAAAR0aGlzAAAAAAAAAABkBAAAAAdwYXltZW50CQEAAAAHZXh0cmFjdAAAAAEIBQAAAANpbnYAAAAHcGF5bWVudAMJAQAAAAEhAAAAAQkBAAAACWlzRGVmaW5lZAAAAAEIBQAAAANpbnYAAAAHcGF5bWVudAkAAAIAAAABAgAAAB9TaG91bGQgYmUgd2l0aCBQYXltZW50IGluIFdhdmVzAwkBAAAACWlzRGVmaW5lZAAAAAEIBQAAAAdwYXltZW50AAAAB2Fzc2V0SWQJAAACAAAAAQIAAAAaUGF5bWVudCBzaG91bGQgYmUgaW4gV2F2ZXMDCQAAZgAAAAIIBQAAAAdwYXltZW50AAAABmFtb3VudAUAAAAJcGxheUxpbWl0CQAAAgAAAAEJAAEsAAAAAgIAAAAcUGF5bWVudCBzaG91bGQgYmUgbGVzcyB0aGFuIAkAAaQAAAABBQAAAAlwbGF5TGltaXQEAAAACHJhbmRoYXNoCQEAAAAKcmFuZG9taXplcgAAAAEFAAAAA2ludgQAAAALd2luVHJhbnNmZXIJAQAAAAtUcmFuc2ZlclNldAAAAAEJAARMAAAAAgkBAAAADlNjcmlwdFRyYW5zZmVyAAAAAwgFAAAAA2ludgAAAAZjYWxsZXIJAABpAAAAAgkAAGgAAAACCAUAAAAHcGF5bWVudAAAAAZhbW91bnQAAAAAAAAAAL4AAAAAAAAAAGQFAAAABHVuaXQFAAAAA25pbAQAAAANd3JpdGVMYXN0UGxheQkBAAAACFdyaXRlU2V0AAAAAQkABEwAAAACCQEAAAAJRGF0YUVudHJ5AAAAAgIAAAAIbGFzdFBsYXkFAAAACHJhbmRoYXNoBQAAAANuaWwDCQAAZgAAAAIAAAAAAAAAAfQJAABqAAAAAgkABLEAAAABBQAAAAhyYW5kaGFzaAAAAAAAAAAD6AkBAAAADFNjcmlwdFJlc3VsdAAAAAIFAAAADXdyaXRlTGFzdFBsYXkFAAAAC3dpblRyYW5zZmVyCQEAAAAMU2NyaXB0UmVzdWx0AAAAAgUAAAANd3JpdGVMYXN0UGxheQkBAAAAC1RyYW5zZmVyU2V0AAAAAQUAAAADbmlsAAAAAgAAAANpbnYBAAAABWxvdHRvAAAAAAkBAAAACnN0YXJ0TG90dG8AAAABBQAAAANpbnYAAAADaW52AQAAAAdkZWZhdWx0AAAAAAkBAAAACnN0YXJ0TG90dG8AAAABBQAAAANpbnYAAAAA4XqnJg==",
    "timestamp": 1592408917668,
    "height": 1047736
  }

.. csv-table:: Set Script Transaction JSON Representation
  :file: _static/02_intermediate/tables/016_Set-Script-Transaction-JSON.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`set script transaction binary format <02_intermediate:Set Script Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`SetScriptTransaction structure <03_advanced:SetScriptTransaction>` is used for transaction handling in smart contracts.

Invoke Script Transaction
^^^^^^^^^^^^^^^^^^^^^^^^^

Invoke script transaction invokes the :ref:`callable function <03_advanced:Callable Function>` of the :ref:`dApp <02_intermediate:dApp and Smart Account>`. 

In addition to the dApp address, callable function name, and arguments, the Invoke Script transaction can contain payments to dApp. The maximum number of payments is 10.

:strong:`Fee`

The sender can specify a transaction fee nominated in a sponsored asset instead of DecentralCoins, see the :ref:`sponsored fee <02_intermediate:Sponsored Fees>` article.

The :ref:`minimum fee <02_intermediate:Minimum Fee>` in :ref:`DecentralCoins <02_intermediate:DecentralCoin>` for an invoke script transaction is Fee :math:`= 0.005 + S + 1 × I`.

* If the transaction sender is a dApp or smart account, and that the complexity of the account script or dApp script verifier function exceeds the sender complexity threshold, then :math:`S = 0.004`, otherwise :math:`S = 0`.
* :math:`I` is the number of issued assets that are not :ref:`NFT <02_intermediate:Non-Fungible Token>`.

:strong:`Total Complexity`

A dApp callable function can invoke a callable function of another dApp, or another callable function of the same dApp, or even itself. All invoked functions are executed within a single Invoke Script transaction. :ref:`More about dApp-to-dApp invocation <03_advanced:dApp-to-App Invocation>`.

The total :ref:`complexity <03_advanced:Script Complexity>` is limited by :math:`26,000` for all callable functions and asset scripts of involved smart assets in a single invoke script transaction. The sender's account script complexity is not included in that limit.

:strong:`JSON Representation`

.. code-block:: none

  {
    "type": 16,
    "id": "DN9Ny8mph4tLjn58e9CqhckPymH9zwPqBSZtcv2bBi3u",
    "sender": "3Mw48B85LvkBUhhDDmUvLhF9koAzfsPekDb",
    "senderPublicKey": "BvJEWY79uQEFetuyiZAF5U4yjPioMj9J6ZrF9uTNfe3E",
    "fee": 500000,
    "feeAssetId": null,
    "timestamp": 1601652119485,
    "proofs": [
      "2536V2349X3cuVEK1rSxQf3HneJwLimjCmCfoG1QyMLLq1CNp6dpPKUG3Lb4pu76XqLe3nWyo3HAEwGoALgBhxkF"
    ],
    "version": 2,
    "chainId": 84,
    "dApp": "3N28o4ZDhPK77QFFKoKBnN3uNeoaNSNXzXm",
    "payment": [],
    "call": {
      "function": "foo",
      "args": [
        {
          "type": "list",
          "value": [
            {
              "type": "string",
              "value": "alpha"
            },
            {
              "type": "string",
              "value": "beta"
            },
            {
              "type": "string",
              "value": "gamma"
            }
          ]
        }
      ]
    },
    "height": 1203100,
    "applicationStatus": "succeeded",
    "stateChanges": {
      "data": [
        {
          "key": "3Mw48B85LvkBUhhDDmUvLhF9koAzfsPekDb",
          "type": "string",
          "value": "alphabetagamma"
        }
      ],
      "transfers": [],
      "issues": [],
      "reissues": [],
      "burns": [],
      "sponsorFees": [],
      "leases": [],
      "leaseCancels": [],
      "invokes": []
    }
  }

.. csv-table:: Invoke Script Transaction JSON Representation
  :file: _static/02_intermediate/tables/017_Invoke-Script-Transaction-JSON.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

The stateChanges structure does not need to be filled when sending a transaction, and it is not stored on the blockchain. The node returns this structure when providing transaction data via the REST API.

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`invoke script transaction binary format <02_intermediate:Invoke Script Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`InvokeScriptTransaction structure <03_advanced:InvokeScriptTransaction>` is used for transaction handling in smart contracts.

Network
-------

.. csv-table:: Network
  :file: _static/02_intermediate/tables/018_Network.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2

Lease Transaction
^^^^^^^^^^^^^^^^^

Lease transaction leases :ref:`DecentralCoins <02_intermediate:DecentralCoin>` to another account. After :math:`1000` block the leased tokens are accounted for by the recipient's generating balance. The larger the generating balance of the node is, the higher the chances for that node to be selected to generate the next block. Commonly node owners share the reward for generated blocks with lessors. :ref:`More about leasing <02_intermediate:Leased Proof of Stake>`.

Leased tokens remain locked on the sender's account with the full control of their owner. The sender can cancel the lease at any time by the :ref:`lease cancel transaction <02_intermediate:Lease Cancel Transaction>`. 

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a lease transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "b8AB1PQWE7kH55cS48uDTV5fezrAyDTCf7iePyXNzNm",
    "amount": 500000000,
    "signature": "3n34MYd3Acx1JpTtvYffdVYCVySuRgZvSbHMA3AxqQwr4xvfZedv9UbqSB9k84PGY5C8RSwGRjDnMGcYwQu2x7B5",
    "fee": 100000,
    "type": 8,
    "version": 1,
    "sender": "3P6iv9tYo3ELne7tc9HR8BzhK3LE2aDDu1A",
    "feeAssetId": null,
    "proofs": [
      "3n34MYd3Acx1JpTtvYffdVYCVySuRgZvSbHMA3AxqQwr4xvfZedv9UbqSB9k84PGY5C8RSwGRjDnMGcYwQu2x7B5"
    ],
    "recipient": "3P2HNUd5VUPLMQkJmctTPEeeHumiPN2GkTb",
    "id": "7k4EPgA3VxoE56TMJLjvF9FMpywyfeS5qRJSEEN9XGuU",
    "timestamp": 1528813353617,
    "status": "canceled",
    "height": 1038624
  }

.. csv-table:: Lease Transaction JSON Representation
  :file: _static/02_intermediate/tables/019_Lease-Transaction-JSON.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

The status field does not need to be filled when sending a transaction, and it is not stored on the blockchain. The node calculates these fields when providing transaction data via the REST API.

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`lease transaction binary format <02_intermediate:Lease Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`LeaseTransaction structure <03_advanced:LeaseTransaction>` is used for transaction handling in smart contracts.

Lease Cancel Transaction
^^^^^^^^^^^^^^^^^^^^^^^^

Lease cancel transaction cancels the leasing. See the :ref:`lease transaction <02_intermediate:Lease Transaction>` article.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for a lease cancel transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "type": 9,
    "id": "6rzxZ3rEsCxgmkcn6DDPB9f9Phi28D4JWZsCtwcViD8C",
    "sender": "3Mx7kNAFcGrAeCebnt3yXceiRSwru6N3XZd",
    "senderPublicKey": "81fxJw7HM2VX1ucq1vNKiedM1XBGX7H2TDUtxN6ib68Z",
    "fee": 100000,
    "feeAssetId": null,
    "timestamp": 1622579112096,
    "proofs": [
      "3eFnprsRSeczc371bQ7AUsbh6qjiUFze6y5BZGKbxyHG27K1cU6jVUgRdthYz9uWVw1FgVpLjMciGCb64rJnMp3k"
    ],
    "version": 2,
    "leaseId": "BhHPPHBZpfp8FBy8DE7heTpWGJySYg2uU2r4YM6qaisw",
    "chainId": 84,
    "height": 1551763,
    "applicationStatus": "succeeded",
    "lease": {
      "id": "BhHPPHBZpfp8FBy8DE7heTpWGJySYg2uU2r4YM6qaisw",
      "originTransactionId": "BhHPPHBZpfp8FBy8DE7heTpWGJySYg2uU2r4YM6qaisw",
      "sender": "3Mx7kNAFcGrAeCebnt3yXceiRSwru6N3XZd",
      "recipient": "3Mz9N7YPfZPWGd4yYaX6H53Gcgrq6ifYiH7",
      "amount": 124935000,
      "height": 1551763,
      "status": "canceled"
    }
  }

.. csv-table:: Lease Cancel Transaction JSON Representation
  :file: _static/02_intermediate/tables/020_Lease-Cancel-Transaction-JSON.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

The lease structure does not need to be filled when sending a transaction, and it is not stored on the blockchain. The node returns this structure when providing transaction data via the REST API.

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`lease cancel transaction binary format <02_intermediate:Lease Cancel Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`LeaseCancelTransaction structure <03_advanced:LeaseCancelTransaction>` is used for transaction handling in smart contracts.

Sponsor Fee Transaction
^^^^^^^^^^^^^^^^^^^^^^^

Sponsor fee transaction enables or disables sponsorship. Sponsorship allows any user to pay a fee in the sponsored asset (instead of DecentralCoins) for invoke script transactions and transfer transactions. :ref:`More about sponsorship <02_intermediate:Sponsored Fees>`.

Only the asset issuer can set up sponsorship. Smart asset cannot be a sponsored asset.

:strong:`Fee`

The :ref:`minimum fee <02_intermediate:Minimum Fee>` for the sponsor fee transaction is :math:`0.001` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`.

If the transaction sender is a :ref:`dApp or smart account <02_intermediate:dApp and Smart Account>`, and the complexity of the account script or dApp script verifier function exceeds the :ref:`sender complexity threshold <03_advanced:Limitations>`, the minimum fee is increased by :math:`0.004` DecentralCoins. 

:strong:`JSON Representation`

.. code-block:: none

  {
    "senderPublicKey": "5HNegWomhj1nzyggf1oAvujNJGCqbzFjM72BLYtrBecw",
    "sender": "3N3ErpmUdJWy6DW4ruAr14YDis9UaiTwHd6",
    "feeAssetId": null,
    "proofs": [
      "5jF8WpF7jxf5SBMHMbc2WcfqX3R6fRvssBGSNfzAM8p3uSmno9XzYy5b565ez5fG9vqUGrENFvcrbhk36bzCaqkP"
    ],
    "assetId": "p1vuxnGyfH9VFiuyKmsh25rn6MedjGbQu7d6Zt1sY4U",
    "fee": 100000000,
    "minSponsoredAssetFee": 100,
    "id": "5gHUMzmBfn4KP3tELzHtw3EYR947rzWUp5PuyF7hUW23",
    "type": 14,
    "version": 1,
    "timestamp": 1585725309659,
    "height": 934757
  }

.. csv-table:: Sponsor Fee Transaction JSON Representation
  :file: _static/02_intermediate/tables/021_Sponsor-Fee-Transaction-JSON.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

The fields that are common to all types of transactions are described in the :ref:`transaction <02_intermediate:Transaction>` article.

:strong:`Binary Format`

See the :ref:`sponsor fee transaction binary format <02_intermediate:Sponsor Fee Transaction Binary Format>`.

:strong:`Ride Structure`

The :ref:`SponsorFeeTransaction structure <03_advanced:SponsorFeeTransaction>` is used for transaction handling in smart contracts.

Genesis
-------

.. csv-table:: Genesis
  :file: _static/02_intermediate/tables/022_Genesis.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 3

Genesis Transaction
^^^^^^^^^^^^^^^^^^^

Genesis transaction accrues :ref:`DecentralCoins <02_intermediate:DecentralCoin>` to account upon the initial distribution of DecentralCoins during the creation of the blockchain. The first block of the blockchain, the genesis block, consists of genesis transactions.

:strong:`Binary Format`

See the :ref:`genesis transaction binary format <02_intermediate:Genesis Transaction Binary Format>`.

Transaction Validation
======================

A DecentralChain node validates each transaction in the following cases:

* The node receives the transaction via the broadcast endpoint of :ref:`Node extensions <documentation:placeholder>` or :ref:`gRPC server <documentation:placeholder>`.
* The node receives the transaction from another node of the blockchain network using the binary protocol.
* The block generator adds the transaction to a block.
* The node receives a block (or microblock) from another node in the network.

Full transaction validation includes the following checks:

1. Transaction fields check including:

  1. Timestamp check: the transaction timestamp should be not more than :math:`2` hours ago or :math:`1.5` hours ahead from the current block timestamp.
  2. Transaction version check: all the features required to support this version should be activated.
  3. Transaction type check: all the features required to support this type should be activated.
  4. Check of token amounts: the values must be non-negative.
  5. Check different fields depending on the transaction type.

2. Sender's balance check.
  
  1. The sender should have enough funds to pay the fee. If a sponsored asset is used for the fee, the sponsor's balance is also checked.
  2. Depending on the type of transaction, the sender should have enough assets for transfer or for payments attached to the :ref:`invoke script transactions <02_intermediate:Invoke Script Transaction>`. Order senders in the :ref:`exchange transaction <02_intermediate:Exchange Transaction>` should have enough funds to exchange.

3. The sender's signature verification 

  1. For ordinary accounts (without script).
  2. For account script execution if the sender is a :ref:`smart account <02_intermediate:dApp and Smart Account>`.
  3. For verifier function execution if the sender is :ref:`dApp <02_intermediate:dApp and Smart Account>`. 
  4. A similar check is performed for orders in an :ref:`exchange transaction <02_intermediate:Exchange Transaction>`.

4. For the invoke script transaction:

  1. Calculation of the result of dApp callable function.
  2.  dApp balance check: dApp account should have enough funds for :ref:`dApp script actions <03_advanced:Script Actions>`.
  3.  Check that the transaction fee is not less than the :ref:`minimum fee <02_intermediate:Minimum Fee>` based on script actions.

5. Execution of asset scripts if the transaction uses :ref:`smart assets <02_intermediate:Smart Asset>`, including scripts of assets used in dApp script actions.

When receiving the transaction via the broadcast endpoint, or adding a transaction to a block, or receiving a block over the network, the node performs full validation of the transaction. When receiving an invoke script transaction over the network, the node performs calculations of the callable function (check 4.1) up to the :ref:`threshold for saving unsuccessful transactions <03_advanced:Limitations>`.

Validation Result
-----------------

When the transaction is received via broadcast or over the network:

* If one of the checks fails, the transaction is discarded.
* If all the checks passed, the transaction is added to the UTX pool, which is the list of transactions waiting to be added to the block.

When adding the transaction to the block, the result of validation depends on the transaction type.

For the invoke script transaction:

* If one of the checks 1–3 failed, the transaction is discarded.
* If checks 1–3 passed, and the calculation of the result of the dApp callable function (check 4.1) failed with an error or :ref:`throwing an exception <03_advanced:Exceptions>` before the :ref:`complexity <03_advanced:Script Complexity>` of performed calculations exceeded the :ref:`threshold for saving failed transactions <03_advanced:Limitations>`, the transaction is also discarded.
* If checks 1–3 passed but checks 4–5 failed and besides the result of the callable function is calculated successfully or the complexity exceeded the threshold, the transaction is saved on the blockchain but marked as failed: "applicationStatus": "script_execution_failed". The sender is charged the transaction fee. The transaction doesn't entail any other changes to the state of the blockchain.
* If all checks passed, the transaction is saved on the blockchain as successful: "applicationStatus": "succeeded" and the sender is charged the fee.

For the exchange transaction:

* If one of the checks 1–3 failed, the transaction is discarded.
* If checks 1–3 passed but check 5 failed, the transaction is saved on the blockchain but marked as failed: "applicationStatus": "script_execution_failed". The sender of the transaction (matcher) is charged the transaction fee. The transaction doesn't entail any other changes in balances, in particular, the order senders don't pay the matcher fee.
* If all checks passed, the transaction is saved on the blockchain as successful: "applicationStatus": "succeeded". The matcher is charged the transaction fee as well as the order senders are charged the matcher fee.

For the other transactions:

* If one of the checks fails, the transaction is discarded.
* If all checks passed, the transaction is saved on the blockchain as successful and the sender is charged the fee.

*****
Block
*****

A block is a link in the chain of the blockchain. Block contains transactions. A block has its height.

The maximum block size is :math:`1` MB. The maximum total complexity of scripts in transactions of the block is :math:`2,500,000`. The complexity of all executed scripts is taken into account: dApp scripts, account scripts, and asset scripts. 

Block Generation
================

A block generation is a creation of a new :ref:`block <02_intermediate:Block>` on the blockchain.
Blocks are generated by :ref:`generating nodes <02_intermediate:Generating Node>` according to :ref:`FPoS algorithm <02_intermediate:Fair Proof of Stake>` and the :ref:`DecentralChain-M5 protocol <02_intermediate:DecentralChain-M5 Protocol>`.
The block generator signs the block headers only. The block headers contain the merkle root hash of the block transactions. This makes it possible to verify the block headers apart from transactions and to provide evidence of the presence of transactions in the block without the presence of all transactions. See details in the :ref:`transactions root hash <02_intermediate:Transactions Root Hash>` article.

Base Target
-----------

The base target is the variable in the average block generation time formula that adjusts :ref:`block generation <02_intermediate:Block Generation>` time to :math:`60` seconds.

Generation Signature
--------------------

Generation signature is the variable in the average block generation time formula. It is used to check whether the current :ref:`generating node <02_intermediate:Generating Node>` is eligible to generate the next block.
The generation signature is calculated using VRF (verifiable random function with short proofs and keys) — a pseudo-random function that uses a message and the private key of an account to provide a non-interactively verifiable proof for the correctness of its output.

This improvement allows resisting stake grinding attacks aimed at influencing block generation randomness to skip miner's opportunity to create a block.
The use of VRF makes signature generation unpredictable because of the need to know the private key for calculation. Only the holder of the private key can compute the hash, but verifying the correctness of the hash using the public key from block header is available to anyone.

The VRF contains calculateVRF function, which calculates proof for some message, and verifyVRF function, which verifies proof from calculateVRF function with a message and the public key of the signer.
Considering that a block’s generation signature is equal to calculateVRF output for a previous generation signature with account private key sk (of generator of :math:`i+1` th block):

.. code-block:: none

  generationSignaturei+1 = VRFproof = calculateVRFsk(VRFi)

The output of calculateVRF function is a VRF proof, which means that the validity of the signature can be checked.
The output of function verifyVRF(pk :math:`_i`, generationSignature :math:`_i`) is used to define the time delay between :math:`i+99` and :math:`i+100` blocks for concrete block generator.

Block Height
============

The block height is a sequence number of a :ref:`block <02_intermediate:Block>` in the blockchain.

Block Signature
===============

A block signature is a hash that a :ref:`generating node <02_intermediate:Generating Node>` acquires when it signs the :ref:`generated block <02_intermediate:Block Generation>` with the private key of the account from the node's wallet.

Block Timestamp
===============

A block timestamp is a time of :ref:`block generation <02_intermediate:Block Generation>`. The time is specified in milliseconds that have passed since the beginning of the unix epoch.

When the :ref:`node <02_intermediate:Node>` receives a new block from the blockchain network, it verifies that the timestamp value of the block does not outpace the UTC time by more than :math:`100` milliseconds.
The timestamp value of the block is validated by nodes using the formula from FPoS.

Genesis Block
=============

A genesis block is the first :ref:`block <02_intermediate:Block>` of the blockchain. A genesis block contains one or more :ref:`genesis transactions <02_intermediate:Genesis Transaction>`. There is one genesis block in the blockchain.

Transactions Root Hash
======================

The transactionsRoot field in the block header contains the root hash of the Merkle tree 
of transactions of the block. The root hash is the proof that the block contains all the transactions in the proper order. The transactions root hash in the block header has the following purposes:

* To prove the integrity of transactions in the block without presenting all transactions.
* To sign the block header only, separately from its transactions.

transactions Root Сalculation
-----------------------------

.. image:: _static/image.jpg

1. The hash of each transaction in the block is calculated. For example:

  * :math:`H_A` = hash(:math:`T_A`)
  * :math:`H_B` = hash(:math:`T_B`)

2. Each pair of adjacent hashes is concatenated, and the hash is calculated for each resulting concatenation:

  * :math:`H_{AB}` = hash(:math:`H_A` + :math:`H_B`)
  * If the last hash does not have a pair, it is concatenated with the zero byte hash: :math:`H_{GH}` = hash(:math:`H_G` + hash(0))

3. Step 2 is repeated until the root hash is obtained:

  * :math:`H_{ABCDEFGH}`
  * The root hash is written in the transactionsRoot field.

If the block is empty, then transactionsRoot = hash(0). DecentralChain blockchain uses BLAKE2b-256 hashing function.

Proof of Transaction in Block
-----------------------------

Let's suppose that side :math:`1` stores the full blockchain data and side :math:`2` stores the block headers only. To prove that the block contains a given transaction, side :math:`1` provides the following data:

* T: Transaction to check.
* merkleProofs: Array of sibling hashes of the Merkle tree, bottom-to-top.
* index: Index of the transaction in the block.

.. image:: _static/image.jpg

For example, for the :math:`T_D` transaction:

* merkleProofs = [ :math:`H_C`, :math:`H_{AB}`, :math:`H_{EFGH}` ]
* index = :math:`3`

Side 2 checks the proof:

1. It calculates the hash of the transaction being checked (all the transaction data is hashed, including the signature): :math:`H_D` = hash(:math:`T_D`)

2. It concatenates the current hash with the corresponding hash of the merkleProofs array and calculates the hash of concatenation.
index determines in which order to concatenate the hashes:

   * If the nth bit of index from the end is :math:`0`, then the order is: the current hash + the nth hash of the merkleProofsarray (proof hash is on the right). 
   * If the nth bit is :math:`1` , the order is: the nth hash of the merkleProofsarray + the current hash (proof hash is on the left). For example, index = :math:`3_{10}` = :math:`11_2` , thus:

      * merkleProofs[0] = :math:`H_{C}` is on the left, 
      * merkleProofs[1] = :math:`H_{AB}` is on the left, 
      * merkleProofs[2] = :math:`H_{EFGH}` is on the right.

3. It repeats step 2 until the root hash is obtained: :math:`H_{ABCDEFGH}`

4. It compares the root hash obtained with the already known transactionsRoot from the block header. If the hashes match, then the transaction exists in the block.

Tools
-----

The following Node API methods accept transaction IDs and provide the proof that the transaction is in a block for each transaction:

* GET /transactions/merkleProof
* POST /transactions/merkleProof

The methods are described in the :ref:`transaction <02_intermediate:Transaction>` article. You can check a transaction on the same blockchain without using a root hash, since the DecentralChain nodes store the entire blockchain data, including all transactions. Use the following built-in Ride function:

.. code-block:: none

  transactionHeightById(id: ByteVector): Int|Unit

The function returns the block height if the transaction with the specified ID exists. Otherwise, it returns a unit. See the function description in the :ref:`blockchain functions <03_advanced:Blockchain Functions>` article. To check a transaction in a block on the external blockchain you can use the following built-in Ride function:

.. code-block:: none

  createMerkleRoot(merkleProofs: List[ByteVector], valueBytes: ByteVector, index: Int): ByteVector

This function is applicable if the external blockchain uses the same algorithm for calculating the root hash of transactions. The createMerkleRoot function calculates the root hash from the transaction hash and sibling hashes of the merkle tree (see Steps 1–3). To check a transaction in a block, compare the calculated root hash with the transactionsRoot value in the block header.

.. _node:

****
Node
****

A node is a host connected to the blockchain network. Node functions are:

* :ref:`Block <02_intermediate:Block>` storage.
* :ref:`Transaction validation <02_intermediate:Transaction Validation>`.
* Sending :ref:`transactions <02_intermediate:Transaction>`.

Generating Node
===============

Generating node is a node that generates blocks. Each generating node is a :ref:`validating node <02_intermediate:Validating Node>`. Generating account is an :ref:`account <02_intermediate:Account>` that a node uses for :ref:`signing <02_intermediate:Block Signature>` generated blocks. A node can generate blocks if the following conditions are met:

* The node's generating balance is at least :math:`10000` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`. This means that the account balance in DecentralCoins, taking into account leasing, was not less than :math:`10000` DecentralCoins in each of the last :math:`1000` blocks (more details in the :ref:`account balance <02_intermediate:Account Balance>` article). The greater the generating balance, the higher is your chance of being eligible to generate the next block.
* Node's account is not a :ref:`smart account or dApp <02_intermediate:dApp and Smart Account>`.
* Block generation is not disabled in node settings. By default, block generation is enabled.
* The node is connected to at least the number of peers specified in the required parameters (:math:`1` by default).

Validating Node
===============

A validating node is a node that :ref:`validates <02_intermediate:Transaction Validation>` transactions.

Generator’s Income
==================

A node's income from adding a new block to the blockchain consists of the following amounts:

1. Block reward: The current reward size is :math:`6` :ref:`DecentralCoins <02_intermediate:DecentralCoin>` but it can be changed by voting, see the :ref:`block reward <02_intermediate:Block Reward>` article.

2. :math:`40\%` of the total transaction fees in the current block. The exact value is calculated as follows:

  * :math:`\sum_{i}^{} 2 * (\frac{f_i}{5})`
  * Here f :math:`_i` is the fee for the :math:`i`-th transaction. For each transaction fee, an integer division by :math:`5` is performed, then a multiplication by :math:`2`, and finally they are summed up.

3. :math:`60\%` of the total transaction fees in the previous block.

  * :math:`\sum_{i}^{} (f_i - 2 * (\frac{f_i}{5}))`
  * The block generator receives exactly the part of the fee that the previous block generator did not receive.

If the :ref:`transaction fees <02_intermediate:Transaction Fees>` are specified in a sponsored asset, then the block generators receive the fee equivalent in DecentralCoins instead of the fee (as a general rule, in a :math:`\frac{40}{60}` ratio):

.. code-block:: none

  feeInDecentralCoins = feeInSponsoredAsset × 0.001 / minSponsoredAssetFee

minSponsoredAssetFee is the amount of the sponsored asset equivalent to :math:`0.001` DecentralCoins. The sponsor sets this value when enabling sponsorship. For details, see the :ref:`sponsored fees <02_intermediate:Sponsored Fees>` article.

Block Reward
============

Block reward is a blockchain feature under which :ref:`generating nodes <02_intermediate:Generating Node>` receive a fixed fee in :ref:`DecentralCoins <02_intermediate:DecentralCoin>` for each :ref:`generated block <02_intermediate:Block Generation>`.
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

In the example above, the value of the JSON's currentReward field is 600,000,000 Decentralites— i.e. it's 6 :ref:`DecentralCoins <02_intermediate:DecentralCoin>`.

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
The block reward is increased/decreased only if more than half of the :math:`10,000` votes — i.e. :math:`5,001` votes or more — were given for increase/decrease. The amount of the current reward is increased/decreased by :math:`0.5` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`.

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

:ref:`Nodes <02_intermediate:Node>` can use the leased tokens to generate blocks and get the :ref:`mining reward <02_intermediate:Block Reward>`. For that purpose, the generating balance of a node must be at least :math:`10000` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`.

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
* These rewards mostly are in :ref:`DecentralCoins <02_intermediate:DecentralCoin>` but also they can be in the form of different tokens with the unique DecentralCoins feature where different tokens can be accepted as a fee.

LPoS Transactions
-----------------

To start leasing, the token holder needs to create a lease transaction and specify the recipient address (node address) along with the amount of :ref:`DecentralCoins <02_intermediate:DecentralCoin>` to lease. There are two types of transactions which are used in the LPoS:

* :ref:`Lease transaction <02_intermediate:Lease Transaction>` to activate the leasing process.
* :ref:`Lease cancel transaction <02_intermediate:Lease Cancel Transaction>` to deactivate the leasing process.

Create a lease
--------------

You can use `Decentral.Exchange <https://decentral.exchange/>`_ online to create a lease. 

* Make sure you are logged into your account. On the main screen navigate to Wallet > Leasing. 
* On the next screen click Start Lease and then select the recipient between the list of nodes and indicate the amount you want to lease.
* Verify all the information and click Start Lease again to confirm.

*****
Order
*****

Order is the instruction from the :ref:`account <02_intermediate:Account>` to matcher to buy or sell a :ref:`token <02_intermediate:Token (Asset)>` on the exchange. 

Asset Pair
==========

Each order contains amount asset / price asset pair, also called asset pair.

:strong:`Example`

.. code-block:: none

  "assetPair": {
      "amountAsset": "3QvxP6YFBKpWJSMAfYtL8Niv8KmmKsnpb9uQwQpg8QN2",
      "priceAsset": "null"
  }

:strong:`Asset Pair Fields`

.. csv-table:: Asset Pair Fields
  :file: _static/02_intermediate/tables/023_Asset-Pair-Fields.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

Order's Amount and Price
========================

In the user interface, the amount and price are usually presented as values with a fractional part (for example, :math:`0.74585728` DecentralCoins), i.e. in the denormalized form. The denormalized form is convenient for humans, but not for calculations. To solve the problem of calculation accuracy, the normalization is performed.

In the user interface, the amount and price are usually presented as values with a fractional part (for example, :math:`0.74585728` :ref:`DecentralCoins <02_intermediate:DecentralCoin>`), i.e. in the denormalized form. The denormalized form is convenient for humans, but not for calculations. To solve the problem of calculation accuracy, the normalization is performed, i.e. amount and price are represented as an integer. So, :math:`0.74585728` DecentralCoins is :math:`0.74585728 × 10^{8}` or :math:`74585728` Decentralites. In this case, the exponent is :math:`8`, because DecentralCoins has :math:`8` decimals after the decimal point. Other assets may have different amount of decimals. For example, TDX has 2 decimals.

Amount
------

Consider buying :math:`2.13` TDX at the price of :math:`0.35016774` DecentralCoins for one TDX. Here the asset pair is TDX / DecentralCoins. The amount in the order is the number of units sold or bought in conventional "pennies". This value in the current case is :math:`213`, since :math:`2.13` TDX :math:`= 2.13 × 10^{2}` = 213` "pennies" of TDX. So, to bring the amount to the normalized form, it is multiplied by :math:`10^{amountAssetDecimals}`.

Price
-----

Price is the value of 1 unit of the amount asset, expressed in the price asset.
In the TDX / DecentralCoins example above, this is the price in DecentralCoins for 1 TDX.
To normalize price, it is multiplied by:

* In orders of versions 1, 2, 3: :math:`10^{(8 + priceAssetDecimals - amountAssetDecimals)}`.
* In orders of version 4: at :math:`10^{8}`.

The exponent of :math:`8` is selected because there cannot be an asset with the exceeding quantity of decimals on the DecentralChain blockchain.
The matcher algorithm has a limitation in relation to price: the last N digits of the normalized price must be zeros (N is price_decimals minus amount_decimals). If this is not so, then the matcher rejects the order on placement.

Price Asset Quantity Calculation
--------------------------------

The quantity of price asset in normalized form which:

* Will be given by sender if order is BUY.
* Will be acquired by sender if order is SELL.

Is calculated by the following formula: amount × price × :math:`10^{(priceAssetDecimals - amountAssetDecimals - 8)}`.

* In orders of versions 1, 2, 3: amount × price × :math:`10^{-8}`
* In orders of version 4: amount × price × :math:`10^{(priceAssetDecimals - amountAssetDecimals - 8)}`.

If the result of the calculation is a value with a fractional part, then the fractional part is discarded. Designations in the above formula:

* Amount — amount in normalized form.
* Price — price in normalized form.
* PriceAssetDecimals — the number of decimal places of the price asset.
* AmountAssetDecimals — the number of decimal places of the amount asset.

Order Cancellation
==================

The order sender may cancel the order before it is executed. Unexecuted orders are automatically canceled at the date and time specified by the order sender.
 
Order Expiration Date
=====================

Order expiration date is the date and time of automatic cancellation of an unexecuted order.
The date is specified in milliseconds which have passed since the beginning of the unix epoch. The expiration time can't be earlier than matcher time + :math:`1` minute and later than matcher time + :math:`30` days.

Order Timestamp
===============

Order timestamp is the time when the matcher added the order to the order book. The time is specified in milliseconds that have passed since the beginning of the unix epoch.

Order Binary Format
===================

See the :ref:`order binary format <02_intermediate:Order Binary Format>` page.

******
Oracle
******

Oracle is a data provider from the outside world on the blockchain.

Sources of the Outside World
============================

Software oracles handle data accessible on the web. For example, the temperature, costs of products and merchandise, flight or train delays, etc. The information originates from online sources, e.g. API. The product prophet extricates the required data and pushes it into the blockchain.

Hardware oracles track real-world objects with devices and sensors. For example, a video camera with an analytics function virtual line crossing tracks vehicles entering a specific zone. If an event is detected, the oracle writes about it on the blockchain. Based on the data of such oracle, some script of decentralized application on the blockchain may be triggered. In this case, for example, a fine and the write-off of tokens from the account of the vehicle owner. But it is not in oracle scope, it is in the scope of the script that is based on the data of such an oracle.

Human oracles imply that the data is entered by a human being.

Oracles Issue
=============

The oracle is a way of connecting the blockchain with the outside world. The major problem that is solved by the usage of oracles is the very point that blockchains can only access data that is stored on the blockchain. Here, in blockchain, the point is that it is important that decentralized applications can only access data that is stored on the blockchain so that every execution of the script leads to the same result at a given point in time. Therefore, decentralized applications are not able to access data from outside the blockchain, e.g., provided by web services or other external sources of data. Nevertheless, many interesting applications need access to the outside world, e.g., decentralized applications for insurances, decentralized betting systems, financial services and so forth.

Here, the solution is quite straightforward: if external data is necessary for the execution of a decentralized application, this data needs to be stored on the blockchain. To achieve this, there are usually small programs implemented that access the necessary data and write it to the blockchain. Those little programs are called oracles.

Consensus of Oracles
====================

One source may be unsafe if it does not have the authority or high rating. However, several oracles can be used to stay away from the monopoly and be safer. For example, get information from ten oracles and only if the data of :math:`6` out of :math:`10` oracles coincide, to accept them. This is the consensus of the oracles.

**************************
Mainnet, Testnet, Stagenet
**************************

Connecting Node to Blockchain Network
=====================================

You can launch your node in any blockchain network. Select the network in the node configuration file. 

* For more information about the configuration file, see the :ref:`node configuration <documentation:placeholder>` article. 
* For installing a node, see the :ref:`install DecentralChain node <documentation:placeholder>` article. 
* For starting your own blockchain network, see the :ref:`custom blockchain <documentation:placeholder>` article.

Chain ID
========

Chain ID is a symbol that is passed over a network during a handshake and allows nodes not to connect to the nodes of other networks. The chain ID is used while building account addresses, therefore, an address on one blockchain network cannot be used on another network. The chain ID is also indicated in transactions so it is impossible to move transactions between different blockchain networks.

.. csv-table:: Chain ID
  :file: _static/02_intermediate/tables/024_Chain-ID.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Tools
=====

API of Pool of Public Nodes
---------------------------

Chain ID is a symbol that is passed over a network during a handshake and allows nodes not to connect to the nodes of other networks. The chain ID is used while building account addresses, therefore, an address on one blockchain network cannot be used on another network. The chain ID is also indicated in transactions so it is impossible to move transactions between different blockchain networks.

.. csv-table:: API of Pool of Public Nodes
  :file: _static/02_intermediate/tables/025_API-of-Pool-of-Public-Nodes.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3

Data Service API
----------------

.. csv-table:: Data Service API
  :file: _static/02_intermediate/tables/026_Data-Service-API.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3

Decentral.Exchange
------------------

`Decentral.Exchange <https://decentral.exchange/>`_ is a decentralized exchange.

.. csv-table:: Decentral.Exchange
  :file: _static/02_intermediate/tables/027_Decentral.Exchange.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3

API of Decentral.Exchange Matcher
---------------------------------

The addresses for order sending and market data obtaining are as follows:

.. csv-table:: API of Decentral.Exchange Matcher
  :file: _static/02_intermediate/tables/028_API-of-Decentral.Exchange-Matcher.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3

DecentralChain Explorer
-----------------------

`DecentralChain Explorer <https://decentralscan.com/>`_ is a service for browsing blockchain data.

.. csv-table:: DecentralChain Explorer
  :file: _static/02_intermediate/tables/029_DecentralChain-Explorer.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 4

Faucet: Obtaining Tokens
------------------------

.. csv-table:: Faucet: Obtaining Tokens
  :file: _static/02_intermediate/tables/030_Faucet-Obtaining-Tokens.csv 
  :header-rows: 0 
  :class: longtable
  :widths: 1 3

************************
Protocols & Data Formats
************************

Cryptographic Practical Details
===============================

Description
-----------

This section describes all the details of cryptographic algorithms which are used to:

* Create private and public keys from seed. 
* Create addresses from public keys.
* Create blocks and transactions signing.

We use Blake2b256 and Keccak256 algorithms (in the form of hash chain) to create cryptographic hashes. And Curve25519 (ED25519 with X25519 keys) to create and verify signatures.
Base58 to create the string form of bytes.

Bytes Encoding Base58
---------------------

All arrays of bytes in the project are encoded by Base58 algorithm with Bitcoin alphabet to make it ease human readable (text readability).

:strong:`Example`

The string teststring is coded into the bytes :math:`[5, 83, 9, -20, 82, -65, 120, -11]`. The bytes :math:`[1, 2, 3, 4, 5]` are coded into the string 7bWpTW.

Creating a Private Key From a Seed
----------------------------------

A seed string is a representation of entropy, from which you can re-create deterministically all the private keys for one wallet. It should be long enough so that the probability of selection is an unrealistic negligible.
In fact, seed should be an array of bytes but for ease of memorization lite wallet uses Brainwallet, to ensure that the seed is made up of words and easy to write down or remember. The application takes the UTF-8 bytes of the string and uses them to create keys and addresses.
For example, 

.. code-block:: none

  seed string manage manual recall harvest series desert melt police rose hollow moral pledge kitten position add

After reading this string as UTF-8 bytes and encoding them to Base58, the string will be coded as:

.. code-block:: none

  xrv7ffrv2A9g5pKSxt7gHGrPYJgRnsEMDyc4G7srbia6PhXYLDKVsDxnqsEqhAVbbko7N1tDyaSrWCZBoMyvdwaFNjWNPjKdcoZTKbKr2Vw9vu53Uf4dYpyWCyvfPbRskHfgt9q

A seed string is involved with the creation of private keys. To create a private key using the official web wallet or the node, to :math:`4` bytes of int 'nonce' field (big-endian representation), which initially has a value of :math:`0` and increases every time you create the new address, should be prepended to seed bytes. Then we use this array of bytes to calculate hash keccak256(blake2b256(bytes)). This resulting array of bytes we call account seed, from it you can definitely generate one private and public key pair. Then this bytes hash passed in the method of creating a pair of public and private key of Curve25519 algorithm.
DecentralChain uses Curve25519-ED25519 signature with X25519 keys (montgomery form), but most embedded cryptography devices and libraries don't support X25519 keys.
There are libraries with conversion functions from:

* ED25519 keys to X25519 (Curve25519) crypto_sign_ed25519_pk_to_curve25519(curve25519_pk, ed25519_pk) for public key.
* Crypto_sign_ed25519_sk_to_curve25519(curve25519_sk, ed25519_skpk) for private key.

NOTE: Not all random :math:`32` bytes can be used as private keys (but any bytes of any size can be a seed). The signature scheme for the ED25519 introduces restrictions on the keys, so create the keys only through the methods of the Curve25519 libraries and be sure to make a test of the ability to sign data with a private key and then check it with a public key, however obvious this test might seem.
There are valid Curve25519 realizations for different languages:

* `Java <https://github.com/signalapp/curve25519-java/>`_
* `C <https://github.com/signalapp/curve25519-java/tree/master/android/jni>`_
* `Python <https://github.com/tgalal/python-axolotl-curve25519>`_

Also some Curve25519 libraries (as the one used in our project) have the Sha256 hashing integrated, some not (such as most of c/c++/python libraries), so you may need to apply it manually. Note that the private key is clamped, so not any random :math:`32` bytes can be a valid private key.

:strong:`Example`

Brainwallet seed string 

.. code-block:: none

  manage manual recall harvest series desert melt police rose hollow moral pledge kitten position add

As UTF-8 bytes encoded

.. code-block:: none

  xrv7ffrv2A9g5pKSxt7gHGrPYJgRnsEMDyc4G7srbia6PhXYLDKVsDxnqsEqhAVbbko7N1tDyaSrWCZBoMyvdwaFNjWNPjKdcoZTKbKr2Vw9vu53Uf4dYpyWCyvfPbRskHfgt9q

Account seed bytes with nonce :math:`0` before apply hash function in Base58

.. code-block:: none
  
  1111xrv7ffrv2A9g5pKSxt7gHGrPYJgRnsEMDyc4G7srbia6PhXYLDKVsDxnqsEqhAVbbko7N1tDyaSrWCZBoMyvdwaFNjWNPjKdcoZTKbKr2Vw9vu53Uf4dYpyWCyvfPbRskHfgt9q

blake2b256(account seed bytes)

.. code-block:: none

  6sKMMHVLyCQN7Juih2e9tbSmeE5Hu7L8XtBRgowJQvU7

Account seed ( keccak256(blake2b256(account seed bytes)))

.. code-block:: none

  H4do9ZcPUASvtFJHvESapnxfmQ8tjBXMU7NtUARk9Jrf

Account seed after Sha256 hashing (optional, if your library does not do it yourself)

.. code-block:: none

  49mgaSSVQw6tDoZrHSr9rFySgHHXwgQbCRwFssboVLWX

Created private key

.. code-block:: none

  3kMEhU5z3v8bmer1ERFUUhW58Dtuhyo9hE5vrhjqAWYT

Created public key

.. code-block:: none

  HBqhfdFASRQ5eBBpu2y6c6KKi1az6bMx8v1JxX4iW1Q8

Creating Address from a Public Key
----------------------------------

Our network address obtained from the public key depends on the byte chainID ('T' for Testnet, 'W' for Mainnet, 'S' for Stagenet), so different networks obtained a different address for a single seed (and hence public keys).

:strong:`Example`

For the public key:

.. code-block:: none

  HBqhfdFASRQ5eBBpu2y6c6KKi1az6bMx8v1JxX4iW1Q8

Created public key:

.. code-block:: none

  3PPbMwqLtwBGcJrTA5whqJfY95GqnNnFMDX

Signing
-------

Curve25519 is used for all the signatures in the project. The process is as follows: create the special bytes for signing for transaction or block, then create a signature using these bytes and the private key bytes.
For the validation of signatures it’s enough with signature bytes, signed object bytes and the public key.
Do not forget that there are many valid (not unique!) signatures for a one array of bytes (block or transaction). Also you should not assume that the ID of the block or transaction is unique. The collision can occur one day! They have already taken place for some weak keys.

:strong:`Example`

Transaction Data:

.. csv-table:: Transaction Data
  :file: _static/02_intermediate/tables/031_Signing-Transaction-Data.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2

Bytes:

.. csv-table:: Bytes
  :file: _static/02_intermediate/tables/032_Signing-Bytes.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 2 1 1 3

Total data bytes for sign

.. code-block:: none

  Ht7FtLJBrnukwWtywum4o1PbQSNyDWMgb4nXR5ZkV78krj9qVt17jz74XYSrKSTQe6wXuPdt3aCvmnF5hfjhnd1gyij36hN1zSDaiDg3TFi7c7RbXTHDDUbRgGajXci8PJB3iJM1tZvh8AL5wD4o4DCo1VJoKk2PUWX3cUydB7brxWGUxC6mPxKMdXefXwHeB4khwugbvcsPgk8F6YB

Signature of transaction data bytes (one of an infinite number of valid signatures)

.. code-block:: none

  2mQvQFLQYJBe9ezj7YnAQFq7k9MxZstkrbcSKpLzv7vTxUfnbvWMUyyhJAc1u3vhkLqzQphKDecHcutUrhrHt22D

Total transaction bytes with signature:

.. code-block:: none

  6zY3LYmrh981Qbzj7SRLQ2FP9EmXFpUTX9cA7bD5b7VSGmtoWxfpCrP4y5NPGou7XDYHx5oASPsUzB92aj3623SUpvc1xaaPjfLn6dCPVEa6SPjTbwvmDwMT8UVoAfdMwb7t4okLcURcZCFugf2Wc9tBGbVu7mgznLGLxooYiJmRQSeAACN8jYZVnUuXv4V7jrDJVXTFNCz1mYevnpA5RXAoehPRXKiBPJLnvVmV2Wae2TCNvweHGgknioZU6ZaixSCxM1YzY24Prv9qThszohojaWq4cRuRHwMAA5VUBvUs

Calculating Transaction ID
--------------------------

Transaction ID is not stored in the transaction bytes and for most transactions (except Payment) it can be easily calculated from the special bytes for signing using blake2b256(bytes_for_signing). For payments, the transaction ID is just the signature of this transaction.

DecentralChain-M5 Solution
==========================

Reasoning
---------

The maximum rate of transactions in blockchain systems is limited by the choice of two parameters: block size and block interval.

The block interval defines the average amount of time that passes between the creation of two blocks. If we reduce this time, forks will appear more frequently, which will lead to either non-resolved forks or to decreased throughput since a considerable amount of time would be spent on resolving these forks.
Larger blocks lead to huge network usage spikes during block propagation, which in turn will lead to throughput problems and huge forks.

DecentralChain-M5 Solution With Technical Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DecentralChain addresses this issue by allowing the miner to continuously farm a block during the time of mining. This continuously increasing block is called liquid block, which becomes immutable when the next block referencing it is built and appended. A liquid block consists of a key block and chain of microblocks. The process of creating liquid block goes as follows:

* When a miner node observes it has the right to create a block, it creates and sends keyBlock, which is regularly just an empty block.
* After that, it creates and sends microblocks every :math:`3` seconds. Microblock is very similar to a regular block: it's a non-empty pack of transactions, which references its parent: previous microblock or key block.
* Microblocks are continuously mined and propagated to the network until a new key block, referencing the current liquid block appears.

Microblock Structure
^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

  generator: PublicKeyAccount
  transactionData: Seq[Transaction]
  prevResBlockSig: BlockId
  totalResBlockSig: BlockId
  signature: ByteStr

totalResBlockSigis the new total signature of a block with all transactions from blockId=prevResBlockSigand owntransactionData. This means that having a_liquid block_consisting of 1_keyblock_and 3_microblock_s:
KEYBLOCK() <-MICRO1(tx1,tx2) <-MICRO2(tx3,tx4) <-MICRO3(tx5,tx6)
We have 4 versions of last block:

.. csv-table:: Microblock Structure
  :file: _static/02_intermediate/tables/033_Microblock-Structure.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Next miner can reference any of these ids in its keyBlock.

Economy
-------

For a miner, it might seem a good idea to reference KEYBLOCK from previous example and pack all txs from microblocks to its own (micro)block(s). In order to make 'stealing' transactions less profitable than referencing the best-known version of liquid block(= the last known microblock), we change the mechanics of fees: After activating M5, miner will receive :math:`40\%` of fees from the block it creates and  :math:`60\%` of fees from the block he references.

Related Protocol Changes
------------------------

* A block can contain up to :math:`65535` transactions and doesn't require transaction sorting.
* By default miners will first create an empty key block. It's a regular block, propagated byBlockForgedmessage, but it now gets broadcasted if it's empty.
* Microblocks are propagated by broadcasting its header for every node which applied it (MicroBlockInv)MicroBlockInv contains a verifiable signature to prevent a node from being flooded. Microblock will be requested afterward via MicroBlockRequestand received back withinMicroBlockResponse.Microblocks will be re-requested from another node which has it if a node doesn't respond.

Configuration
-------------
The following miner parameters can be tuned(though it's best not to change them in order to maximize final version of your liquid block in the resulting blockchain):

* KeyBlock size (maxTransactionsInKeyBlock, default = :math:`0`). If changed, it won't be rebroadcasted and the usual extension requesting mechanics will be used.
* Microblock mining interval (microBlockInterval, default = :math:`3` s).
* Max amount of transactions per microblock (maxTransactionsInMicroBlock, default = :math:`200`).
* Miner will try to reference the best-known microblock with at leastminMicroBlockAgeage(default = :math:`3` s). This is required in order for a miner to reference already-propagated block so its key block doesn't get orphaned.
* Microblock synchronization mechanism can be tuned with waitResponseTimeout(default = :math:`2` s), processedMicroBlocksCacheTimeout(default = :math:`10` s),invCacheTimeout(default = :math:`10` s) which are basically time of awaiting a microblock and times to cache a processed microblock ids and a list of nodes which have a microblock(by id).

API changes
-----------

* Upon applying every microblock, the last block gets changed, which means/blocks/lastand/blocks/at/...will reflect that.
* /peers/blacklistednow expose ban reason, one can clear a node's blacklist via/peers/clearblacklist
* /debug/and/consensus/section are expanded, _stateHash _doesn't take _liquid block _into consideration.

DecentralChain-M5 Protocol
==========================

Scalability Limits and Challenges in Current Blockchain Systems
---------------------------------------------------------------

Problem Statement and Motivation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Blockchains protocols have some scalability limits and challenges that tradeoff between throughput and latency. The current blockchain technology is not fast enough and does not scale to include more transactions into the system so we have a performance challenge to be considered.
There is a united agreement between miners, consumers, and developers with several perspectives that we need to deploy scalability measures, and there has been an ongoing argument on how to improve Bitcoin’s scalability. Current proposals have focused on how big to make the blocks and how to handle the block size increases in the future.

All proposals suffer from a major scalability bottleneck:
No matter what block size is chosen, the blockchain system can at best reach a proper transaction throughput, increasing from ~ :math:`3` transactions per second to ~ :math:`7` transactions per second. This is so far from the :math:`30,000` transactions per second which are necessary to compete with the existing systems such as VISA transactions. The same major limitations apply to litecoin, Ethereum, and all other currencies that share Bitcoin’s blockchain protocol.

DecentralChain-M5 will address the scalability bottleneck by making the network reach the highest throughput depending on the network conditions. It will not only enhance the transaction throughput, it will also reduce transaction latencies. So it will be possible to get an initial transaction confirmation in seconds rather than in minutes.

Weaknesses of Current Proposals to Improve Scalability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Blockchain Systems can process transactions and the maximum rate of these transactions is limited by the choice of two parameters: block size and block interval.

* The block interval defines the average amount of time that passes between the creation of two blocks. By deciding to reduce the block interval to solve the latency limit, the system will have less security (increase forks probability) due to the reason of new miners for every second which will lead to instability where the blockchain is subject to reorganization and the system is in disagreement (Figure 1). If we reduce the time per block, then we will have a situation where a significant number of blocks are solved in less time than it takes to relay a solved block throughout the network. So there will be no way to know which block is the "real" one and which one is a "fork" because the transactions that appeared to have multiple confirmations suddenly have fewer confirmations (or possibly go back to being unconfirmed).

.. image:: _static/image.jpg

Figure 1: Increasing block frequency with static block size will result in less security.

* The throughput of a system is bounded by the maximum block size (given a fixed block interval), as the maximum number of included transactions is directly dependent on the block size. 
* Larger blocks do however cause slower propagation speeds, which causes more discarded blocks (orphaning risk). An unlimited blocksize could, for example, result in a DoS attack on the system by creating a block that takes a long time to validate. If the choice is to Increase block size in order to improve throughput, there will be Network spikes with longer time to propagate in the network (Figure 2).

.. image:: _static/image.jpg

Figure 2: Increasing block size with Static block frequency will lead to more discarded blocks and network spikes.

Brief Summary of Bitcoin-M5
^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is a next-generation blockchain protocol which is an alternative bitcoin scaling solution that does not involve increasing the size of blocks or decreasing the block time interval. This reduces the risk of forks amongst other advantages. Bitcoin-M5 describes that the basic tradeoffs in Bitcoin can be reduced with an alternative blockchain protocol, offering a consensus delay and bandwidth limited only by the Network Plane. The protocol splits time into time periods(epoch). In each time period, a particular leader is responsible for serializing transactions (Figure 3). The leaders take the rule of generating blocks:

* Key blocks for the election of a leader.
* Micro blocks for ledger records.

.. image:: _static/image.jpg

Figure 3: Bitcoin-M5 time periods structure with serializing transactions.

DecentralChain-M5 Overlay
-------------------------

DecentralChain-M5 is based on the bitcoin next generation protocol that serializes transactions and offers important improvements in the transaction latency(lower latency) and bandwidth(higher throughput) in comparison to Bitcoin without sacrificing other properties.
DecentralChain approaches this scalability matter by providing the miner with the ability to farm a block during the time of mining in a continuous approach. This block continues increments called liquid blocks. This liquid block is unchangeable over time once the next block referencing is created and appended.
This approach increases effective bandwidth and speed of block creation, which is described as being “especially significant for businesses” using the DecentralChain-M5 protocol since it allows for conducting micro-transactions - without any delays that are typical with traditional blockchain systems.
Furthermore, it allows the blockchain to withstand high loads, such as distribution of tokens following crowdsales and airdrops of bonus tokens. The speed of processing trading transactions on the exchange gets increased as well.

DecentralChain-M5 operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The main and core idea of DecentralChain-M5 is to split the Liquid block into two types, Key blocks and Micro blocks. The process of creating liquid block works as follows:

* The miner node gets the permission to create a block.
* The miner node creates and sends the key block (which does not contain transactions).
* The miner node creates and sends the micro blocks (which contain transactions just as in normal blocks with a reference to previous micro blocks or key blocks) with a mining time interval of three seconds.
* Miners will mine those micro blocks and propagate them directly to the network until the next new key block appears with a reference to the liquid block.

All of the transactions are part of the same block and are contributed all together. In between blocks, the traditional Bitcoin system appears idle to an onlooker, as miners are working to discover the next block, but without apparent progress on the consensus front.
In contradiction, in DecentralChain-M5, the key-blocks can be small because they need to contain only the coinbase transaction, which defines the public key that the miner will be using to sign microblocks.
Because a key-block requires proof of stake, miners can not just produce one and expropriate the leadership at will.
Following the key-block, the lead miner can quickly issue microblocks, simply by signing them with the private key corresponding to the public key named in the key-block’s coinbase (Figure 4).

.. image:: _static/image.jpg

Figure 4: Key-blocks and Micro-blocks signing process.

:strong:`Leader Blocks`

They’re also called "Key Blocks", these blocks are generated with proof of stake but do not contain transactions.
They serve as a leader election mechanism and contain a public key that identifies the chosen leader.
Each block has a header that contains, among other fields, the unique reference of its predecessor which is a cryptographic hash of the predecessor header (either a key block or a microblock).

:strong:`Micro Blocks`

Once a node generates a key block it becomes the leader. As a leader, the node is allowed to generate microblocks at a set rate smaller than a predefined maximum.
These micro blocks will contain the ledger entries with no requirement for any Proof of Stake and they're generated by the elected leader in every block-generation cycle.
This block-generation cycle is initiated by a leader block.
The only requirement is to sign the micro blocks with the elected leader's private key.
The micro blocks can be generated at a very high speed by the elected leader(miner), thus resulting in increased performance and transaction speed.

For a microblock to be valid, all its entries must be valid according to the specification of the state machine, and the signature has to be valid. Figure 5 illustrates the structure.
Note that microblocks do not affect the weight of the chain, as they do not contain proof of stake.
When all micro blocks have been validated, they will be merged with their key block into one block.

DecentralChain-M5 reward mechanisms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remuneration consists of two parts. First, each key block entitles its generator a set amount. Second, each ledger entry carries a fee.
This fee is split by the leader that places this entry in a microblock and the subsequent leader that generates the next key block.

In order to motivate participants to follow the protocol, DecentralChain-M5 uses the following mechanisms:
Each transaction pays a fee to the system, but unlike Bitcoin, this fee is distributed, with :math:`40\%` to the leader, and :math:`60\%` to the subsequent leader.
Finally, if a leader forks the chain by generating two microblocks with the same parent, it is punished by revoking the subsidy revenue; whoever detects the fraud wins a nominal fee, (Figure 5).

.. image:: _static/image.jpg

Figure 5: chain structure of the DecentralChain-M5 Protocol. Microblocks (circles) are signed with the private key matching with the public key in the last key block (squares). The fee is distributed  :math:`40\%` to the leader and :math:`60\%` to the next one.

In practice, the remuneration is implemented by having each key block contain a single coinbase transaction that mints new coins and deposits the funds to the current and previous leaders.
As in Bitcoin, this transaction can only be spent after a maturity period of :math:`100` key blocks, to avoid non-mergeable transactions following a fork.

Fair Proof of Stake
===================

In this model, the choice of account that has the right to generate the next block and receive the corresponding transaction fees is based on the number of tokens in the account. The more tokens that are held in the account, the greater the chance that account will earn the right to generate a block.

In DecentralChain, we are convinced that each participant in the blockchain should participate in the block generation process proportionally to his stake: we have decided to correct the PoS formula. At the moment we do not have the goal of completely changing the algorithm, since there is no need; we simply want to make some adjustments.
We presented an improved PoS algorithm that makes the choice of block creator fair and reduces vulnerability to the multi-branching attacks, in accordance with the shortcomings of the current algorithm. 

We analyzed the model of the new algorithm for its correspondence to the stake share and the share of blocks, and the results were positive. Also, the algorithm was analyzed for vulnerability to attacks, and results obtained with the new model were better than with the old one. The attacks’ results for the attacker were not so successful in terms of the profits gained. The number of forks and their length decreased.

Blockchain Data Types
=====================

The blockchain data types are the data types that are used to describe 02_intermediate of blockchain entities. Here’s a list of blockchain data types:

.. csv-table:: Blockchain Data Types
  :file: _static/02_intermediate/tables/034_Blockchain-Data-Types.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 4 2

Binary Format
=============

* :ref:`Address binary format <02_intermediate:Address Binary Format>`
* :ref:`Alias binary format <02_intermediate:Alias Binary Format>`
* :ref:`Block binary format <02_intermediate:Block Binary Format>`
* :ref:`Network message binary format <02_intermediate:Network Message Binary Format>`

  * :ref:`Block message binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Checkpoint message binary format <02_intermediate:Checkpoint Message Binary Format>`
  * :ref:`Get block message binary format <02_intermediate:Get Block Message Binary Format>`
  * :ref:`Get peers message binary format <02_intermediate:Get Peers Message Binary Format>`
  * :ref:`Get signatures message binary format <02_intermediate:Get Signatures Message Binary Format>`
  * :ref:`Handshake message binary format <02_intermediate:Handshake Message Binary Format>`
  * :ref:`Peers message binary format <02_intermediate:Peers Message Binary Format>`
  * :ref:`Score message binary format <02_intermediate:Score Message Binary Format>`
  * :ref:`Signatures message binary format <02_intermediate:Signatures Message Binary Format>`
  * :ref:`Transaction message binary format <02_intermediate:Transaction Message Binary Format>`

* :ref:`Order binary format <02_intermediate:Order Binary Format>`
* :ref:`Transaction binary format <02_intermediate:Transaction Binary Format>`

  * :ref:`Burn transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Create alias transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Data transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Exchange transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Genesis transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Invoke script transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Issue transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Lease cancel transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Lease transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Mass transfer transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Reissue transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Set asset script transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Set script transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Sponsor fee transaction binary format <02_intermediate:Block Message Binary Format>`
  * :ref:`Transfer transaction binary format <02_intermediate:Block Message Binary Format>`

* :ref:`Transaction proofs binary format <02_intermediate:Transaction Proofs Binary Format>`

Address Binary Format
---------------------

Learn more about :ref:`address <02_intermediate:Address>`.

.. csv-table:: Address Binary Format
  :file: _static/02_intermediate/tables/035_Address-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 1 4

Alias Binary Format
--------------------

Learn more about :ref:`alias <02_intermediate:Alias>`.

.. csv-table:: Alias Binary Format
  :file: _static/02_intermediate/tables/036_Alias-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 2 4

Block Binary Format
-------------------

Learn more about :ref:`block <02_intermediate:Block>`.

Blocks are stored on the blockchain in a binary format (byte representation). :ref:`Node extensions <documentation:placeholder>` such as :ref:`gRPC server <documentation:placeholder>` can work directly with data in binary format.

:strong:`Version 5`

.. code-block:: none

  message Block {
    message Header {
      int32 chain_id = 1;
      bytes reference = 2;
      int64 base_target = 3;
      bytes generation_signature = 4;
      repeated uint32 feature_votes = 5;
      int64 timestamp = 6;
      int32 version = 7;
      bytes generator = 8;
      int64 reward_vote = 9;
      bytes transactions_root = 10;
    }

    Header header = 1;
    bytes signature = 2;
    repeated SignedTransaction transactions = 3;
  }

.. csv-table:: Block Binary Format Version 5
  :file: _static/02_intermediate/tables/037_Block-Binary-Format-V5.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

:strong:`Version 4`

.. csv-table:: Block Binary Format Version 4
  :file: _static/02_intermediate/tables/038_Block-Binary-Format-V4.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 2 2

:strong:`Version 3`

.. csv-table:: Block Binary Format Version 3
  :file: _static/02_intermediate/tables/039_Block-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 2 2

Network Message Binary Format	
-----------------------------

* :ref:`Block message binary format <02_intermediate:Block Message Binary Format>`
* :ref:`Checkpoint message binary format <02_intermediate:Checkpoint Message Binary Format>`
* :ref:`Get block message binary format <02_intermediate:Get Block Message Binary Format>`
* :ref:`Get peers message binary format <02_intermediate:Get Peers Message Binary Format>`
* :ref:`Get signatures message binary format <02_intermediate:Get Signatures Message Binary Format>`
* :ref:`Handshake message binary format <02_intermediate:Handshake Message Binary Format>`
* :ref:`Peers message binary format <02_intermediate:Peers Message Binary Format>`
* :ref:`Score message binary format <02_intermediate:Score Message Binary Format>`
* :ref:`Signatures message binary format <02_intermediate:Signatures Message Binary Format>`
* :ref:`Transaction message binary format <02_intermediate:Transaction Message Binary Format>`

Block Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Block message is a reply to GetBlock message.

.. csv-table:: Block Message Binary Format
  :file: _static/02_intermediate/tables/040_Block-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Checkpoint Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Checkpoint Message Binary Format
  :file: _static/02_intermediate/tables/041_Checkpoint-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Get Block Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Get Block Message Binary Format
  :file: _static/02_intermediate/tables/042_Get-Block-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Get Peers Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get peers message is sent when one sending node wants to know about other nodes on the network.

.. csv-table:: Get Peers Message Binary Format
  :file: _static/02_intermediate/tables/043_Get-Peers-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Get Signatures Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Get Signatures Message Binary Format
  :file: _static/02_intermediate/tables/044_Get-Signatures-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Handshake Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Handshake is used to start communication between two nodes.

.. csv-table:: Handshake Message Binary Format
  :file: _static/02_intermediate/tables/045_Handshake-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 1 1

Peers Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Peers message is a response to get peers message.

.. csv-table:: Peers Message Binary Format
  :file: _static/02_intermediate/tables/046_Peers-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Score Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Score Message Binary Format
  :file: _static/02_intermediate/tables/047_Score-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Signatures Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Signatures Message Binary Format
  :file: _static/02_intermediate/tables/048_Signatures-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Transaction Message Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Transaction Message Binary Format
  :file: _static/02_intermediate/tables/049_Transaction-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Order Binary Format
-------------------

Learn more about :ref:`order <02_intermediate:Order>`.

* An exchange transaction of version 3 can accept orders of versions 1–4.
* An exchange transaction of version 2 can accept orders of versions 1–3.
* An exchange transaction of version 1 can accept orders of version 1 only.

:strong:`Version 4`

.. code-block:: none

  message AssetPair {
      bytes amount_asset_id = 1;
      bytes price_asset_id = 2;
  };

  message Order {
    enum Side {
      BUY = 0;
      SELL = 1;
    };

    int32 chain_id = 1;
    bytes sender_public_key = 2;
    bytes matcher_public_key = 3;
    AssetPair asset_pair = 4;
    Side order_side = 5;
    int64 amount = 6;
    int64 price = 7;
    int64 timestamp = 8;
    int64 expiration = 9;
    Amount matcher_fee = 10;
    int32 version = 11;
    repeated bytes proofs = 12;
  };

  message Amount {
    bytes asset_id = 1;
    int64 amount = 2;
  };

.. csv-table:: Order Binary Format Version 4
  :file: _static/02_intermediate/tables/050_Order-Binary-Format-V4.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 4

:strong:`Version 3`

.. csv-table:: Order Binary Format Version 3
  :file: _static/02_intermediate/tables/051_Order-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 1 2 1 3

JSON Representation of Order Version 3

.. code-block:: none

  {
    "version": 3,
    "senderPublicKey": "FMc1iASTGwTC1tDwiKtrVHtdMkrVJ1S3rEBQifEdHnT2",
    "matcherPublicKey": "7kPFrHDiGw1rCm7LPszuECwWYL3dMf6iMifLRDJQZMzy",
    "assetPair": {
      "amountAsset": "BrjUWjndUanm5VsJkbUip8VRYy6LWJePtxya3FNv4TQa",
      "priceAsset": null
    },
    "orderType": "buy",
    "amount": 150000000,
    "timestamp": 1548660872383,
    "expiration": 1551252872383,
    "matcherFee": 300000,
    "proofs": [
      "YNPdPqEUGRW42bFyGqJ8VLHHBYnpukna3NSin26ERZargGEboAhjygenY67gKNgvP5nm5ZV8VGZW3bNtejSKGEa"
    ],
    "id": "Ho6Y16AKDrySs5VTa983kjg3yCx32iDzDHpDJ5iabXka",
    "sender": "3PEFvFmyyZC1n4sfNWq6iwAVhzUT87RTFcA",
    "price": 1799925005, 
  }

:strong:`Version 2`

.. csv-table:: Order Binary Format Version 2
  :file: _static/02_intermediate/tables/052_Order-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 3 2

:strong:`Version 1`

.. csv-table:: Order Binary Format Version 1
  :file: _static/02_intermediate/tables/053_Order-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 3 2

The price listed for amount asset in price asset :math:`* 10^8`. Expiration is order time to live, timestamp in future, max :math:`= 30` days in future. The signature is calculated from the following bytes:

.. csv-table:: Order Binary Format Version 1 Bytes
  :file: _static/02_intermediate/tables/054_Order-Binary-Format-V1-Bytes.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 3 2

Transaction Binary Format
-------------------------

Learn more about :ref:`transaction <02_intermediate:Transaction>`.

Transactions are stored on the blockchain in a binary format (byte representation). :ref:`Node extensions <documentation:placeholder>` such as :ref:`gRPC server <documentation:placeholder>` can work directly with data in binary format.
The transaction signature and ID are also formed on the basis of the binary format, namely the transaction body bytes. The contents of transaction body bytes is given in the description of the binary format of each type and version of the transaction. Normally the transaction body bytes include all transaction fields, with the exception of the following fields:

* Transaction ID (it is not stored on the blockchain),
* Version flag,
* Proofs or signature, depending on the version of the transaction.

The guideline for generating a signature and ID is given in the :ref:`cryptographic practical details <02_intermediate:Cryptographic Practical Details>` article. All strings are UTF-8 encoded.

Protobuf
^^^^^^^^

Protobuf facilitates the development of client libraries for the DecentralChain blockchain, as it avoids serialization errors and streamlines the creation of a correctly signed transaction. How to generate a transaction signature using protobuf:

* Download the `protocol buffers package <https://github.com/protocolbuffers/protobuf/releases/>`_ for your programming language. Generate the Transaction class on the basis of transaction.proto.
* Fill in the transaction fields.

   * Asset IDs should be specified in the binary format.
   * Addresses should be specified in the shortened binary format (without the first two and the last four bytes). See the :ref:`address binary format <02_intermediate:Address Binary Format>`) article.

* Serialize the transaction object to get transaction body bytes. Detailed instructions for various programming languages are provided in `protocol buffers tutorials <https://developers.google.com/protocol-buffers/docs/tutorials>`_.
* Generate the signature for the transaction body bytes with the Curve25519 function using sender private key bytes.

The byte representation of a transaction based on the protobuf schema must not contain default values. Make sure that your protocol buffers compiler does not write the field value when serializing if it is equal to the default value for this data type, otherwise the transaction signature will be invalid. Send the signed transaction to a node:

* If you use your own node and :ref:`gRPC server <documentation:placeholder>`, send the SignedTransaction object.
* If you use :ref:`Node REST API <documentation:placeholder>`, compose the JSON representation of the transaction and add the base58-encoded signature to the proof array. Send the transaction to a node using POST /transactions/broadcast method.

.. code-block:: none

  message SignedTransaction {
    Transaction transaction = 1;
    repeated bytes proofs = 2;
  }

  message Transaction {
    int32 chain_id = 1;
    bytes sender_public_key = 2;
    Amount fee = 3;
    int64 timestamp = 4;
    int32 version = 5;

    oneof data {
      GenesisTransactionData genesis = 101;
      PaymentTransactionData payment = 102;
      IssueTransactionData issue = 103;
      TransferTransactionData transfer = 104;
      ReissueTransactionData reissue = 105;
      BurnTransactionData burn = 106;
      ExchangeTransactionData exchange = 107;
      LeaseTransactionData lease = 108;
      LeaseCancelTransactionData lease_cancel = 109;
      CreateAliasTransactionData create_alias = 110;
      MassTransferTransactionData mass_transfer = 111;
      DataTransactionData data_transaction = 112;
      SetScriptTransactionData set_script = 113;
      SponsorFeeTransactionData sponsor_fee = 114;
      SetAssetScriptTransactionData set_asset_script = 115;
      InvokeScriptTransactionData invoke_script = 116;
      UpdateAssetInfoTransactionData update_asset_info = 117;
    };
  };

  message Amount {
    bytes asset_id = 1;
    int64 amount = 2;
  };

.. csv-table:: Transaction Binary Format
  :file: _static/02_intermediate/tables/055_Transaction-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 3

The fields that depend on the type of transaction are described in the following articles:

* :ref:`Burn transaction binary format <02_intermediate:Burn Transaction Binary Format>`
* :ref:`Create alias transaction binary format <02_intermediate:Create Alias Transaction Binary Format>`
* :ref:`Data transaction binary format <02_intermediate:Data Transaction Binary Format>`
* :ref:`Exchange transaction binary format <02_intermediate:Exchange Transaction Binary Format>`
* :ref:`Genesis transaction binary format <02_intermediate:Genesis Transaction Binary Format>`
* :ref:`Invoke script transaction binary format <02_intermediate:Invoke Script Transaction Binary Format>`
* :ref:`Issue transaction binary format <02_intermediate:Issue Transaction Binary Format>`
* :ref:`Lease cancel transaction binary format <02_intermediate:Lease Cancel Transaction Binary Format>`
* :ref:`Lease transaction binary format <02_intermediate:Lease Transaction Binary Format>`
* :ref:`Mass transfer transaction binary format <02_intermediate:Mass Transfer Transaction Binary Format>`
* :ref:`Reissue transaction binary format <02_intermediate:Reissue Transaction Binary Format>`
* :ref:`Set asset script transaction binary format <02_intermediate:Set Asset Script Transaction Binary Format>`
* :ref:`Set script transaction binary format <02_intermediate:Set Script Transaction Binary Format>`
* :ref:`Sponsor fee transaction binary format <02_intermediate:Sponsor Fee Transaction Binary Format>`
* :ref:`Transfer transaction binary format <02_intermediate:Transfer Transaction Binary Format>`
* :ref:`Update asset info transaction binary format <02_intermediate:Update Asset Info Transaction Binary Format>`

Burn Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`burn transaction <02_intermediate:Burn Transaction>`.

:strong:`Version 3`

.. code-block:: none

  message BurnTransactionData {
    Amount asset_amount = 1;
  };

  message Amount {
    bytes asset_id = 1;
    int64 amount = 2;
  };

.. csv-table:: Burn Transaction Binary Format Version 3
  :file: _static/02_intermediate/tables/056_Burn-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 2 1 3

:strong:`Version 2`

.. csv-table:: Burn Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/057_Burn-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The fields :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8` and :math:`9` are the transaction body bytes.

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":6,
    "id":"csr25XQHT1c965Fg7cY2vJ7XHYVsudPYrUbdaFqgaqL",
    "sender":"3P9QZNrHbyxXj8P9VrJZmVu2euodNtA11UW",
    "senderPublicKey":"9GaQj7gktEiiS1TTTjGbVjU9bva3AbCiawZ11qFZenBX",
    "fee":100000,
    "feeAssetId":null,
    "timestamp":1548660675277,
    "proofs": [
      "61jCivdv3KTuTY6QHgxt4jaGrXcszWg3vb9TmUR26xv7mjWWwjyqs7X5VDUs9c2ksndaPogmdunHDdjWCuG1GGhh"
    ],
    "version":2,
    "assetId":"FVxhjrxZYTFCa9Bd4JYhRqXTjwKuhYbSAbD2DWhsGidQ",
    "amount":9999,
    "chainId":87,
    "height":1370971
  }

:strong:`Version 1`

.. csv-table:: Burn Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/058_Burn-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 1 1

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5` and :math:`6` are the transaction body bytes.

Create Alias Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`create alias transaction <02_intermediate:Create Alias Transaction>`.

:strong:`Version 3`

.. code-block:: none

  message CreateAliasTransactionData {
    string alias = 1;
  };

.. csv-table:: Create Alias Transaction Binary Format Version 3
  :file: _static/02_intermediate/tables/059_Create-Alias-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1

:strong:`Version 2`

.. csv-table:: Create Alias Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/060_Create-Alias-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The fields :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7` and :math:`8` are the transaction body bytes.   

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":10,
    "id":"5CZV9RouJs7uaRkZY741WDy9zV69npX1FTZqxo5fsryL",
    "sender":"3PNaua1fMrQm4TArqeTuakmY1u985CgMRk6",
    "senderPublicKey":"B3f8VFh6T2NGT26U7rHk2grAxn5zi9iLkg4V9uxG6C8q",
    "fee":100000,
    "feeAssetId":null,
    "timestamp":1548666019772,
    "proofs": [
      "3cUM8Eq5KfmbS6q1qHDfzhX98YzER1ocnVjVAHG9HSkQdw86zjqxUfmsUPVwnVgwu5zatt3ETLnNFteobRMyR8bY"
    ],
    "version":2,
    "alias":"2.1.0a",
    "height":1371063
  }

:strong:`Version 1`

.. csv-table:: Create Alias Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/061_Create-Alias-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 2 2

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5` and :math:`6` are the transaction body bytes.

Data Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`data transaction <02_intermediate:Data Transaction>`.

:strong:`Version 2`

.. csv-table:: Data Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/062_Data-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

The maximum number of entries is :math:`100`. The maximum data size (keys + values) is :math:`165,890` bytes.

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":12,
    "id":"EByjQAWDRGrmc8uy7xRGy2zsQXZQq59bav7h8oTTJyHC",
    "sender":"3PLZcCJyYQnfWfzhKXRA4rteCQC9J1ewf5K",
    "senderPublicKey":"BQMVwAHwf2WEEwRsCxtMVcSLrXUhJ3XtCLmSptLx2e6L",
    "fee":600000,
    "feeAssetId":null,
    "timestamp":1532116120299,
    "proofs": [
      "PZiAGq2ssi1ojh2Cc9dWrzmbuw9nJif2omsQ4dvonU31oiwsJQGbZiio3LG28otatFfFbHPfcX1JVCHwP5i4mKy"
    ],
    "version":1,
    "data": [
      {"key":"4900","type":"integer","value":24010000},{"key":"4901","type":"integer","value":24019801},
      {"key":"4902","type":"integer","value":24029604},{"key":"4903","type":"integer","value":24039409},
      {"key":"4904","type":"integer","value":24049216},{"key":"4905","type":"integer","value":24059025},
      {"key":"4906","type":"integer","value":24068836},{"key":"4907","type":"integer","value":24078649},
      {"key":"4908","type":"integer","value":24088464},{"key":"4909","type":"integer","value":24098281},
      {"key":"4910","type":"integer","value":24108100},{"key":"4911","type":"integer","value":24117921},
      {"key":"4912","type":"integer","value":24127744},{"key":"4913","type":"integer","value":24137569},
      {"key":"4914","type":"integer","value":24147396},{"key":"4915","type":"integer","value":24157225},
      {"key":"4916","type":"integer","value":24167056},{"key":"4917","type":"integer","value":24176889},
      {"key":"4918","type":"integer","value":24186724},{"key":"4919","type":"integer","value":24196561},
      {"key":"4920","type":"integer","value":24206400},{"key":"4921","type":"integer","value":24216241},
      {"key":"4922","type":"integer","value":24226084},{"key":"4923","type":"integer","value":24235929},
      {"key":"4924","type":"integer","value":24245776},{"key":"4925","type":"integer","value":24255625},
      {"key":"4926","type":"integer","value":24265476},{"key":"4927","type":"integer","value":24275329},
      {"key":"4928","type":"integer","value":24285184},{"key":"4929","type":"integer","value":24295041},
      {"key":"4930","type":"integer","value":24304900},{"key":"4931","type":"integer","value":24314761},
      {"key":"4932","type":"integer","value":24324624},{"key":"4933","type":"integer","value":24334489},
      {"key":"4934","type":"integer","value":24344356},{"key":"4935","type":"integer","value":24354225},
      {"key":"4936","type":"integer","value":24364096},{"key":"4937","type":"integer","value":24373969},
      {"key":"4938","type":"integer","value":24383844},{"key":"4939","type":"integer","value":24393721},
      {"key":"4940","type":"integer","value":24403600},{"key":"4941","type":"integer","value":24413481},
      {"key":"4942","type":"integer","value":24423364},{"key":"4943","type":"integer","value":24433249},
      {"key":"4944","type":"integer","value":24443136},{"key":"4945","type":"integer","value":24453025},
      {"key":"4946","type":"integer","value":24462916},{"key":"4947","type":"integer","value":24472809},
      {"key":"4948","type":"integer","value":24482704},{"key":"4949","type":"integer","value":24492601},
      {"key":"4950","type":"integer","value":24502500},{"key":"4951","type":"integer","value":24512401},
      {"key":"4952","type":"integer","value":24522304},{"key":"4953","type":"integer","value":24532209},
      {"key":"4954","type":"integer","value":24542116},{"key":"4955","type":"integer","value":24552025},
      {"key":"4956","type":"integer","value":24561936},{"key":"4957","type":"integer","value":24571849},
      {"key":"4958","type":"integer","value":24581764},{"key":"4959","type":"integer","value":24591681},
      {"key":"4960","type":"integer","value":24601600},{"key":"4961","type":"integer","value":24611521},
      {"key":"4962","type":"integer","value":24621444},{"key":"4963","type":"integer","value":24631369},
      {"key":"4964","type":"integer","value":24641296},{"key":"4965","type":"integer","value":24651225},
      {"key":"4966","type":"integer","value":24661156},{"key":"4967","type":"integer","value":24671089},
      {"key":"4968","type":"integer","value":24681024},{"key":"4969","type":"integer","value":24690961},
      {"key":"4970","type":"integer","value":24700900},{"key":"4971","type":"integer","value":24710841},
      {"key":"4972","type":"integer","value":24720784},{"key":"4973","type":"integer","value":24730729},
      {"key":"4974","type":"integer","value":24740676},{"key":"4975","type":"integer","value":24750625},
      {"key":"4976","type":"integer","value":24760576},{"key":"4977","type":"integer","value":24770529},
      {"key":"4978","type":"integer","value":24780484},{"key":"4979","type":"integer","value":24790441},
      {"key":"4980","type":"integer","value":24800400},{"key":"4981","type":"integer","value":24810361},
      {"key":"4982","type":"integer","value":24820324},{"key":"4983","type":"integer","value":24830289},
      {"key":"4984","type":"integer","value":24840256},{"key":"4985","type":"integer","value":24850225},
      {"key":"4986","type":"integer","value":24860196},{"key":"4987","type":"integer","value":24870169},
      {"key":"4988","type":"integer","value":24880144},{"key":"4989","type":"integer","value":24890121},
      {"key":"4990","type":"integer","value":24900100},{"key":"4991","type":"integer","value":24910081},
      {"key":"4992","type":"integer","value":24920064},{"key":"4993","type":"integer","value":24930049},
      {"key":"4994","type":"integer","value":24940036},{"key":"4995","type":"integer","value":24950025},
      {"key":"4996","type":"integer","value":24960016},{"key":"4997","type":"integer","value":24970009},
      {"key":"4998","type":"integer","value":24980004},{"key":"4999","type":"integer","value":24990001}
    ],
    "height":1091300
  }

:strong:`Version 1`

.. csv-table:: Data Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/063_Data-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6.1`, :math:`6.2`, :math:`6.3`, :math:`6.4`, :math:`6.5`, :math:`6.6`, :math:`6.7`, :math:`6.8`, :math:`6.9`, :math:`6.10`, :math:`6.[5 × N - 4]`, :math:`6.[5 × N - 3]`, :math:`6.[5 × N - 2]`, :math:`6.[5 × N - 1]`, :math:`6.[5 × N]`, :math:`7` and :math:`8` are the transaction body bytes. The maximum number of records is :math:`100`. The maximum size of transaction body bytes is  :math:`153,600` bytes.

Exchange Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`exchange transaction <02_intermediate:Exchange Transaction>`.

:strong:`Version 3`

Exchange transaction of version 3 can accept orders of versions 1 –4.

.. code-block:: none

  message ExchangeTransactionData {
    int64 amount = 1;
    int64 price = 2;
    int64 buy_matcher_fee = 3;
    int64 sell_matcher_fee = 4;
    repeated Order orders = 5;
  };

.. csv-table:: Exchange Transaction Binary Format Version 3
  :file: _static/02_intermediate/tables/064_Exchange-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

:strong:`Version 2`

Transaction version 2 can accept orders of version 1, 2 and 3.

.. csv-table:: Exchange Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/065_Exchange-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4.1`, :math:`4.2`, :math:`4.3`, :math:`5.1`, :math:`5.2`, :math:`5.3`, :math:`6`, :math:`6.6`, :math:`7`, :math:`8`, :math:`9`, :math:`10` and :math:`11` are the transaction body bytes. 

:strong:`JSON Representation of Transaction`

.. code-block:: none

 {
    "type":6,
    "id":"csr25XQHT1c965Fg7cY2vJ7XHYVsudPYrUbdaFqgaqL",
    "sender":"3P9QZNrHbyxXj8P9VrJZmVu2euodNtA11UW",
    "senderPublicKey":"9GaQj7gktEiiS1TTTjGbVjU9bva3AbCiawZ11qFZenBX",
    "fee":100000,
    "feeAssetId":null,
    "timestamp":1548660675277,
    "proofs": [
      "61jCivdv3KTuTY6QHgxt4jaGrXcszWg3vb9TmUR26xv7mjWWwjyqs7X5VDUs9c2ksndaPogmdunHDdjWCuG1GGhh"
    ],
    "version":2,
    "assetId":"FVxhjrxZYTFCa9Bd4JYhRqXTjwKuhYbSAbD2DWhsGidQ",
    "amount":9999,
    "chainId":87,
    "height":1370971
  }

:strong:`Version 1`

Transaction version 1 can accept orders of version 1 only.

.. csv-table:: Exchange Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/066_Exchange-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 3

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8`, :math:`9`, :math:`10` and :math:`11` are the transaction body bytes. 

Genesis Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`genesis transaction <02_intermediate:Genesis Transaction>`.

.. csv-table:: Genesis Transaction Binary Format
  :file: _static/02_intermediate/tables/067_Genesis-Transaction-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1 1 2

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":1,
    "id":"2DVtfgXjpMeFf2PQCqvwxAiaGbiDsxDjSdNQkc5JQ74eWxjWFYgwvqzC4dn7iB1AhuM32WxEiVi1SGijsBtYQwn8",
    "fee":0,
    "timestamp":1465742577614,
    "signature":"2DVtfgXjpMeFf2PQCqvwxAiaGbiDsxDjSdNQkc5JQ74eWxjWFYgwvqzC4dn7iB1AhuM32WxEiVi1SGijsBtYQwn8",
    "recipient":"3PAWwWa6GbwcJaFzwqXQN5KQm7H96Y7SHTQ",
    "amount":9999999500000000,
    "height":1
  }

Invoke Script Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>`.

:strong:`Version 2`

.. code-block:: none

  message InvokeScriptTransactionData {
    Recipient d_app = 1;
    bytes function_call = 2;
    repeated Amount payments = 3;
  };

  message Recipient {
    oneof recipient {
      bytes public_key_hash = 1;
      string alias = 2;
    };
  };

  message Amount {
    bytes asset_id = 1;
    int64 amount = 2;
  };

.. csv-table:: Invoke Script Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/068_Invoke-Script-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

The maximum size of d_app + function_call + payments is :math:`5120` bytes.

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":16,
    "id":"7CVjf5KGRRYj6UyTC2Etuu4cUxx9qQnCJox8vw9Gy9yq",
    "sender":"3P5rWeMzoaGBrXJDMifQDDjCMKWJGKTiVJU",
    "senderPublicKey":"4kKN9G7cZXGQujLQm9ss5gqB7TKX4A9jtFGt7DnHUoQ6",
    "fee":500000,
    "feeAssetId":null,
    "timestamp":1565537422938,
    "proofs": [
      "28s21sisoa7yHWWmmX8U78fbNHW4KXAS9GHD8XmaN77gJxbnP2Q3DssNWpmSQ6hBq6xS985W4YiTmgvENhfWPNt5"
    ],
    "version":1,
    "dApp":"3PJbknfXMsJzZmksmsKSMz56tVdDqF5GdNM",
    "payment":[],
    "call": {
      "function":"returnSellVST",
      "args": [
        {
          "type":"string",
          "value":"GiEBRfGhEeGqhPmLCjwJcYuakyvaz2GHGCfCzuinSKD"
        }
      ]
    },
    "height":1656369,
    "stateChanges": {
      "data": [
        {
          "key":"sell_GiEBRfGhEeGqhPmLCjwJcYuakyvaz2GHGCfCzuinSKD_spent",
          "type":"integer",
          "value":10000000000
        }
      ],
      "transfers": [
        {
          "address":"3P5rWeMzoaGBrXJDMifQDDjCMKWJGKTiVJU",
          "asset":"4LHHvYGNKJUg5hj65aGD5vgScvCBmLpdRFtjokvCjSL8",
          "amount":10000000000
        }
      ],
      "issues":[],
      "reissues":[],
      "burns":[],
      "sponsorFees":[],
      "leases":[],
      "leaseCancels":[],
      "invokes":[]
    }
  }

:strong:`Version 1`

.. csv-table:: Invoke Script Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/069_Invoke-Script-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The maximum number of payments is :math:`10`.  The maximum size of transaction including proofs is :math:`5120` bytes.

Issue Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`issue transaction <02_intermediate:Issue Transaction>`.

:strong:`Version 3`

.. code-block:: none

  message IssueTransactionData {
    string name = 1;
    string description = 2;
    int64 amount = 3;
    int32 decimals = 4;
    bool reissuable = 5;
    bytes script = 6;
  };

.. csv-table:: Issue Transaction Binary Format Version 3
  :file: _static/02_intermediate/tables/070_Issue-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

:strong:`Version 2`

.. csv-table:: Issue Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/071_Issue-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The fields :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6.1`, :math:`6.2`, :math:`7.1`, :math:`7.2`, :math:`8`, :math:`9`, :math:`10`, :math:`11`, :math:`12`, :math:`13.1`, :math:`13.2` and :math:`13.3` are the transaction body bytes. 

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":3,
    "id":"FTQvw9zdYirRksUFCKDvor3hiu2NiUjXEPTDEcircqti",
    "sender":"3PPP59J1pToCk7fPs4d5EK5PoHJMeQRJCTb",
    "senderPublicKey":"E8Y8ywedRS9usVvvcuczn9hsSg1SNkQVBMcNeQEnjDTP",
    "fee":100000000,
    "feeAssetId":null,
    "timestamp":1548666518362,
    "proofs": [
      "3X7GpKW1ztto1aJN5tQNByaGZ9jGkaxZNo4BT268obZckbXuNQHGKjAUxtqcSEes5aZNMaQi2JYBGeKpcaPTxpSC"
    ],
    "version":2,
    "assetId":"FTQvw9zdYirRksUFCKDvor3hiu2NiUjXEPTDEcircqti",
    "name":"DCVN",
    "quantity":990000000000000000,
    "reissuable":false,
    "decimals":8,
    "description":"Tài chính cho nền dân chủ",
    "script":null,
    "chainId":87,
    "height":1371069
  }

:strong:`Version 1`

.. csv-table:: Issue Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/072_Issue-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1 1

The fields :math:`3`, :math:`4`, :math:`5.1`, :math:`5.2`, :math:`6.1`, :math:`6.2`, :math:`7`, :math:`8`, :math:`9`, :math:`10` and :math:`11` are the transaction body bytes. 

Lease Cancel Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`lease cancel transaction <02_intermediate:Lease Cancel Transaction>`

:strong:`Version 3`

.. code-block:: none

  message LeaseCancelTransactionData {
    bytes lease_id = 1;
  };
 
.. csv-table:: Lease Cancel Transaction Binary Format Version 3
  :file: _static/02_intermediate/tables/073_Lease-Cancel-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1

:strong:`Version 2`

.. csv-table:: Lease Cancel Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/074_Lease-Cancel-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The fields :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, and :math:`8` are the transaction body bytes. 

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":9,
    "id":"7siEtrJAvmVzM1WDX6v9RN4qkiCtk7qQEeD5ZhE6955E",
    "sender":"3PMBXG13f89pq3WyJHHKX2m5zN6kt2CEkHQ",
    "senderPublicKey":"BEPNBjo9Pi9hJ3hVtxpwyEfXCW3qWUNk5dMD7aFdiHsa",
    "fee":100000,
    "feeAssetId":null,
    "timestamp":1548660629957,
    "proofs": [
      "3cqVVsaEDzBz367KTBFGgMXEYJ2r3yLWd4Ha8r3GzmAFsm2CZ3GeNW22wqxfK4LNRFgsM5kCWRVhf6gu2Nv6zVqW"
    ],
    "version":2,
    "leaseId":"BggRaeNCVmzuFGohzF4dQeYXSWr8i5zNSnGtdKc5eGrY",
    "chainId":87,
    "height":1370970,
    "lease": {
      "id":"BggRaeNCVmzuFGohzF4dQeYXSWr8i5zNSnGtdKc5eGrY",
      "originTransactionId":"BggRaeNCVmzuFGohzF4dQeYXSWr8i5zNSnGtdKc5eGrY",
      "sender":"3PMBXG13f89pq3WyJHHKX2m5zN6kt2CEkHQ",
      "recipient":"3PMWRsRDy882VR2viKPrXhtjAQx7ygQcnea",
      "amount":406813214,
      "height":1363095,
      "status":"canceled",
      "cancelHeight":1370970,
      "cancelTransactionId":"7siEtrJAvmVzM1WDX6v9RN4qkiCtk7qQEeD5ZhE6955E"
    }
  }

:strong:`Version 1`

.. csv-table:: Lease Cancel Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/075_Lease-Cancel-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 1 1 2

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, and :math:`5` are the transaction body bytes. 

Lease Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`lease transaction <02_intermediate:Lease Transaction>`.

:strong:`Version 3`

.. code-block:: none

  message LeaseTransactionData {
    Recipient recipient = 1;
    int64 amount = 2;
  };
  
  message Recipient {
    oneof recipient {
      bytes public_key_hash = 1;
      string alias = 2;
    };
  };
 
.. csv-table:: Lease Transaction Binary Format Version 3
  :file: _static/02_intermediate/tables/076_Lease-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

:strong:`Version 2`

.. csv-table:: Lease Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/077_Lease-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The fields :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8` and :math:`9` are the transaction body bytes. 

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":8,
    "id":"J6jZCzLpWJX8EDVhopKFx1mcbFizLGHVb44dvqPzH4QS",
    "sender":"3PMYNm8hshzCNjZ8GpPta5SyN7qBTEzS7Kw",
    "senderPublicKey":"GNswAY61mER5ZyUFeDBo1UyKGkPSSmmnd6yj7axN2n8f",
    "fee":100000,
    "feeAssetId":null,
    "timestamp":1548660916755,
    "proofs": [
      "2opTj7mGKXLRajkJ78wN4ctSWqTeWtvisHaR8BnL2amqJ2KB313BbcpDYJKcqr7o7EpYjL5tppMz2pGjUMWbJe9b"
    ],
    "version":2,
    "amount":14000000000,
    "recipient":"3PMWRsRDy882VR2viKPrXhtjAQx7ygQcnea",
    "height":1370973,
    "status":"canceled"
  }

:strong:`Version 1`

.. csv-table:: Lease Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/078_Lease-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 1 3 

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5` and :math:`6` are the transaction body bytes. 

Mass Transfer Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`mass transfer transaction <02_intermediate:Mass Transfer Transaction>`.

:strong:`Version 2`

.. code-block:: none

  message MassTransferTransactionData {
    message Transfer {
      Recipient recipient = 1;
      int64 amount = 2;
    };
    bytes asset_id = 1;
    repeated Transfer transfers = 2;
    bytes attachment = 3;
  };

  message Recipient {
    oneof recipient {
      bytes public_key_hash = 1;
      string alias = 2;
    };
  }
 
.. csv-table:: Mass Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/079_Mass-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3 

The maximim number of transfers is :math:`100`.

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":11,
    "id":"3LRfudet7avpQcW1AdauiBGb8SSRAaoCugDzngDPLVcv",
    "sender":"3P2rvn2Hpz6pJcH8oPNrwLsetvYP852QQ2m",
    "senderPublicKey":"5DphrhGy6MM4N3yxfB2uR2oFUkp2MNMpSzhZ4uJEm3U1",
    "fee":5100000,
    "feeAssetId":null,
    "timestamp":1528973951321,
    "proofs": [
      "FmGBaWABAy5bif7Qia2LWQ5B4KNmBnbXETL1mE6XEy4AAMjftt3FrxAa8x2pZ9ux391oY5c2c6ZSDEM4nzrvJDo"
    ],
    "version":1,
    "assetId":"Fx2rhWK36H1nfXsiD4orNpBm2QG1JrMhx3eUcPVcoZm2",
    "attachment":"xZBWqm9Ddt5BJVFvHUaQwB7Dsj78UQ5HatQjD8VQKj4CHG48WswJxUUeHEDZJkHgt9LycUpHBFc8ENu8TF8vvnDJCgfy1NeKaUNydqy9vkACLZjSqaVmvfaM3NQB",
    "transferCount":6,
    "totalAmount":500000000000,
    "transfers": [
      {"recipient":"3PHnjQrdK389SbzwPEJHYKzhCqWvaoy3GQB","amount":5000000000},
      {"recipient":"3PGNLwUG2GPpw74teTAxXFLxgFt3T2uQJsF","amount":5000000000},
      {"recipient":"3P5kQneM9EdpVUbFLgefD385LLYTXY5J32c","amount":5000000000},
      {"recipient":"3P2j9FZyygnVDCQvmSc41VCAKwwCQm8QUhA","amount":5000000000},
      {"recipient":"3PNBZutLvMpjzxGAiQGqQuDyanhWyLi2Fhi","amount":5000000000},
      {"recipient":"3P84vdYxzDPFbS5zj9J6yCkmKKA2QMo1DKA","amount":5000000000},
    ],
    "height":1041197
  }

:strong:`Version 1`

.. csv-table:: Mass Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/080_Mass-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3 

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4.1`, :math:`4.2`, :math:`5.1`, :math:`5.2`, :math:`5.3`, :math:`5.4`, :math:`5.5`, :math:`5.[2 × N]`, :math:`5.[2 × N + 1]`, :math:`6`, :math:`7`, :math:`8.1` and :math:`8.2` are the transaction body bytes. 

Reissue Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`reissue transaction <02_intermediate:Reissue Transaction>`.

:strong:`Version 3`

.. code-block:: none

  message ReissueTransactionData {
    Amount asset_amount = 1;
    bool reissuable = 2;
  };

  message Amount {
    bytes asset_id = 1;
    int64 amount = 2;
  };

.. csv-table:: Reissue Transaction Binary Format Version 3
  :file: _static/02_intermediate/tables/081_Reissue-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

:strong:`Version 2`

.. csv-table:: Reissue Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/082_Reissue-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1 1 3 


The fields :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8`, :math:`9` and :math:`10` are the transaction body bytes. 

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":5,
    "id":"27ETigYaHym2Zbdp4x1gnXnZPF1VJCqQpXmhszC35Qac",
    "sender":"3PLJciboJqgKsZWLj7k1VariHgre6uu4S2T",
    "senderPublicKey":"DjYEAb3NsQiB6QdmVAzkwJh7iLgUs3yDLf7oFEeuZjfM",
    "fee":100000000,
    "feeAssetId":null,
    "timestamp":1548521785933,
    "proofs": [
      "5mEveeUwBdBqe8naNoV5eAe5vj6fk8U743eHGkhxhs3v9PMsb3agHqpe4EtzpUFdpASJegXyjrGSbynZg557cnSq"
    ],
    "version":2,
    "assetId":"GA4gB3Lf3AQdF1vBCbqGMTeDrkUxY7L83xskRx6Z7kEH",
    "quantity":200000,
    "reissuable":true,
    "chainId":87,
    "height":1368623
  }

:strong:`Version 1`

 .. csv-table:: Reissue Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/083_Reissue-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 1 3 

The fields :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8` and :math:`9` are the transaction body bytes. 

Set Asset Script Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`set asset script transaction <02_intermediate:Set Asset Script Transaction>`.

:strong:`Version 2`

.. code-block:: none

  message SetAssetScriptTransactionData {
    bytes asset_id = 1;
    bytes script = 2;
  };

.. csv-table:: Set Asset Script Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/084_Set-Asset-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 2

The maximim number of transfers is :math:`100`.

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":15,
    "id":"FwYSpmVDbWQ2BA5NCBZ9z5GSjY39PSyfNZzBayDiMA88",
    "sender":"3P67JUW8Djit7hMjKhADmn6CWvKPbRuh2sQ",
    "senderPublicKey":"AwQYJRHZNd9bvF7C13uwnPiLQfTzvDFJe7DTUXxzrGQS",
    "fee":100000000,
    "feeAssetId":null,
    "timestamp":1547201038106,
    "proofs": [
      "nzYhVKmRmd7BiFDDfrFVnY6Yo98xDGsKrBLWentF7ibe4P9cGWg4RtomHum2NEMBhuyZb5yjThcW7vsCLg7F8NQ"
    ],
    "version":1,
    "assetId":"7qJUQFxniMQx45wk12UdZwknEW9cDgvfoHuAvwDNVjYv",
    "script":"base64:AQa3b8tH",
    "chainId":87,
    "height":1346345
  }

:strong:`Version 1`

 .. csv-table:: Set Asset Script Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/085_Set-Asset-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1 1 3

The fields :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8`, :math:`9.1`, :math:`9.2` and :math:`9.3` are the transaction body bytes. 

Set Script Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`set script transaction <02_intermediate:Set Script Transaction>`.

:strong:`Version 2`

.. code-block:: none

  message SetScriptTransactionData {
    bytes script = 1;
  };
 
.. csv-table:: Set Script Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/086_Set-Script-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":13,
    "id":"8Nwjd2tcQWff3S9WAhBa7vLRNpNnigWqrTbahvyfMVrU",
    "sender":"3PBSduYkK7GQxVFWkKWMq8GQkVdAGX71hTx",
    "senderPublicKey":"3LZmDK7vuSBsDmFLxJ4qihZynUz8JF9e88dNu5fsus5p",
    "fee":2082496,
    "feeAssetId":null,
    "timestamp":1537973512182,
    "proofs": [
      "V45jPG1nuEnwaYb9jTKQCJpRskJQvtkBcnZ45WjZUbVdNTi1KijVikJkDfMNcEdSBF8oGDYZiWpVTdLSn76mV57"
    ],
    "version":1,
    "script":"base64:AQQAAAAEaW5hbAIAAAAESW5hbAQAAAAFZWxlbmECAAAAB0xlbnVza2EEAAAABGxvdmUCAAAAC0luYWxMZW51c2thCQAAAAAAAAIJAAEsAAAAAgUAAAAEaW5hbAUAAAAFZWxlbmEFAAAABGxvdmV4ZFt5",
    "chainId":87,
    "height":1190001
  }

:strong:`Version 1`

.. csv-table:: Set Script Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/087_Set-Script-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3 

Sponsor Fee Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`sponsor fee transaction <02_intermediate:Sponsor Fee Transaction>`.

:strong:`Version 2`

.. code-block:: none

  message SponsorFeeTransactionData {
    Amount min_fee = 1;
  };

  message Amount {
    bytes asset_id = 1;
    int64 amount = 2;
  };
 
.. csv-table:: Sponsor Fee Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/088_Sponsor-Fee-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":14,
    "id":"7EL2XEGP1By427BeLcHPYeVnBzGsXen4egMAwQpWGBVR",
    "sender":"3PHrS6VNPRtUD8MHkfkmELavL8JnGtSq5sx",
    "senderPublicKey":"5v5D5pqzKGBejtvtEeyDJXG28iQwMViu1uuetEcyQp9v",
    "fee":100000000,
    "feeAssetId":null,
    "timestamp":1534448057070,
    "proofs": [
      "3Q4JS4ujrGxAqp8LMXR9zZJC4tJ7YHiTo4SvMgrPhufo2UtR5x9JAaCGDjEr7qWXFDPJk7vWL8eapQkS45Dx1kcb"
    ],
    "version":1,
    "assetId":"FN76goSi7hQn6gQ8aezKVwyDvhkWx5ekXbP3sNLWqavN",
    "minSponsoredAssetFee":10,
    "height":1130205
  }

:strong:`Version 1`

.. csv-table:: Sponsor Fee Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/089_Sponsor-Fee-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3 

The fields :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8`, :math:`9` and :math:`10` are the transaction body bytes. 

Transfer Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`transfer transaction <02_intermediate:Transfer Transaction>`.

:strong:`Version 3`

.. code-block:: none

  message TransferTransactionData {
    Recipient recipient = 1;
    Amount amount = 2;
    bytes attachment = 3;
  };

  message Recipient {
    oneof recipient {
      bytes public_key_hash = 1;
      string alias = 2;
    };

  message Amount {
    bytes asset_id = 1;
    int64 amount = 2;
  };

.. csv-table:: Transfer Transaction Binary Format Version 3
  :file: _static/02_intermediate/tables/090_Transfer-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3 

:strong:`Version 2`

.. csv-table:: Transfer Transaction Binary Format Version 2
  :file: _static/02_intermediate/tables/091_Transfer-Transaction-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3 

:strong:`JSON Representation of Transaction`

.. code-block:: none

  {
    "type":4,
    "id":"2UMEGNXwiRzyGykG8voDgxnwHA7w5aX5gmxdcf9DZZjL",
    "sender":"3PCeQD3nAyHmzDSYBUnSPDWf9qxqzVU2sjh",
    "senderPublicKey":"6kn1XPDh2XUjVAgznxNousHq3EnKKLx7BRWyJzVFU76J",
    "fee":100000,
    "feeAssetId":null,
    "timestamp":1583160322998,
    "proofs": [
      "2z5fnoigbsCBqRPWqTDeDmGJF6qJwnm2WLspen6c6qziTc73sBh9Kh81kPhUT9DGg7ANwqsXMxQauEvyw3RxNH7z"
    ],
    "version":2,
    "recipient":"3P45uRnyVygTnbEJNxc2CHLUiC4izQxbuuS",
    "assetId":"51LxAtwBXapvvTFSbbh4nLyWFxH6x8ocfNvrXxbTChze",
    "feeAsset":null,
    "amount":30077000000,
    "attachment":"2d6RhvQATwGbyv7dKT3L77758iJx",
    "height":1954598
  }

:strong:`Version 1`

.. csv-table:: Transfer Transaction Binary Format Version 1
  :file: _static/02_intermediate/tables/092_Transfer-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 3 

Update Asset Info Transaction Binary Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`update asset info transaction <02_intermediate:Update Asset Info Transaction>`.

:strong:`Version 1`

.. code-block:: none

  message UpdateAssetInfoTransactionData {
    bytes asset_id = 1;
    string name = 2;
    string description = 3;
  }

.. csv-table:: Update Asset Transaction Binary Format Version 1
 :file: _static/02_intermediate/tables/093_Update-Asset-Info-Transaction-Binary-Format-V1.csv
 :header-rows: 1 
 :class: longtable
 :widths: 1 1 1

Transaction Proofs Binary Format
--------------------------------

Tableholder

The maximum number of proofs is :math:`8`.

Validation Rules
================

Account Validation
------------------

Account is valid then it is a valid Base58 string and the length of the corresponding array is :math:`26` bytes. Version of address (1st byte) is equal to :math:`1`. The network byte (2nd byte) is equal to network ID. The checksum of address (last :math:`4` bytes) is correct.

Transactions Validation
-----------------------

Transfer Transaction Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfer transaction is valid then:

* Recipient address is valid. If not, InvalidAddress validation result will be returned.
* Size of attachment is less than or equals MaxAttachementSize(:math:`140` bytes). In other case TooBigArray validation result will be returned.
* Transaction's amount is more than :math:`0`, otherwise NegativeAmount validation result is returned.
* Transaction's fee is positive, otherwise InsufficientFee validation result is returned.
* Adding fee to amount does not lead to Long overflow. In case of Long overflow OverflowError validation result will be returned.
* Transaction's signature is valid, otherwise InvalidSignature validation result is returned.

Issue Transaction Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Issue transaction is valid then:

* Sender's address is valid. If not, InvalidAddress validation result will be returned.
* Quantity of asset is positive, otherwise NegativeAmount validation result is returned.
* Transaction's fee is more than or equals MinFee(:math:`100000000` Decentralites = :math:`1` DecentralCoin), in other case InsufficientFee validation result is returned.
* Size of description is less than or equals MaxDescriptionLength(:math:`1000` bytes), otherwise TooBigArray is returned.
* Size of name is more than or equals MinAssetNameLength and less or equals MaxAssetNameLength, in other case InvalidName validation result will be returned.
* Decimals is positive and less than or equals MaxDecimals, in other case TooBigArray is returned.
* Transaction's signature is valid, otherwise InvalidSignature validation result is returned.

Reissue Transaction Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reissue transaction is valid then:

* Sender's account is valid. Otherwise InvalidAddress validation result is returned.
* Quantity is positive, in other case NegativeAmount validation result will be returned.
* Transaction's fee is positive, in other case InsufficientFee result will be returned.
* Transaction's signature is valid, otherwise InvalidSignature validation result is returned.

Block Validations
-----------------

Block is valid then:

* Block chain contains referenced blocks.
* Block's signature is valid.
* Block's consensus data is valid.
* Block's transactions are valid.

Consensus Data Validation
^^^^^^^^^^^^^^^^^^^^^^^^^

Block's consensus data is valid then:

* Block creation time is no more than MaxTimeDrift(:math:`15` seconds) in future.
* Block's transactions are sorted. This rule works only after :math:`1477958400000` on Testnet and :math:`1479168000000` on Mainnet.
* Block chain contains parent block or block chain height is equal :math:`1`.
* Block's base target is valid.
* Block's generator signature is valid.
* Generator's balance is more than or equals MinimalEffectiveBalanceForGeneration(:math:`1000000000000` Decentralites). This rule always works on Testnet and works only after :math:`1479168000000` on Mainnet.
* Block's hit is less than calculated block's target.
* Voted features are sorted in ascending order and are not repeated.

Transactions Data Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Block's transactions are valid then:

* Creation time of every transaction in block is less than block's creation time no more than on MaxTxAndBlockDiff(:math:`2` hours).
* All transactions are valid against state.

Transaction validation against state. Transactions are valid then:

* Transaction is valid by transaction validation rules.
* Transaction creation time more than block's creation time no more than on MaxTimeForUnconfirmed(:math:`90` minutes). This limitation works always on Testnet and only after :math:`1479168000000` on Mainnet.
* Application of transaction to accounts should not lead to temporary negative balance. This rule works after :math:`1479168000000` on Mainnet and after :math:`1477958400000` on Testnet.
* Changes made by transaction should be sorted by their amount. This rule works on both Mainnet and Testnet after :math:`1479416400000`.
* Application of transaction's amount to current balance should not lead to Long overflow.
* After application of all block's transactions affected balances should not be negative.

Unconfirmed Transactions Pool Validation
----------------------------------------

Transaction could be inserted in unconfirmed transactions pool then:

* Transaction is valid by transaction validation rules.
* If transaction's fee is more than or equals minimum fee that was set by the owner of a node.
* There is a space for a new transaction if unconfirmed transactions pool. By default the pool is limited by :math:`1000` transactions.
* unconfirmed transactions pool does not contain transaction with the same ID.
* Transaction created not later than MaxTimeForUncofimed(:math:`90` minutes) after the last block was created.
* Transaction creation time is no more than MaxTimeDrift(:math:`15` seconds) in future.
* Transaction is valid against state.

********
Glossary
********

A
=

.. glossary::

  Account

    An account is a cryptographically connected pair of :term:`public<Public Key>` and on the :term:`private key<Private Key>`. Accounts uniquely correlate :term:`transactions<Transaction>` and :term:`orders<Order>` with their senders.

  Account Data Storage

    An account data storage is the store of data records in the key-value format associated with the :term:`account<Account>`. Each account has single data storage. The size of the account data storage is unlimited.

  Account Script

    An account script is a :term:`Ride<Ride>` :term:`script<Script>` that has the following directives:

    .. code-block:: none

      {-# CONTENT_TYPE EXPRESSION #-}
      {-# SCRIPT_TYPE ACCOUNT #-}

    The account script is attached to the :term:`account<Account>` using the set script transaction. Only one script can be attached to an account. An account with an account script attached is called a :term:`smart account<Smart Account>`.

  Address

    An address is a unique :term:`account<Account>` identifier. The address can be represented as an alphanumeric string.

  Airdrop

    An airdrop is a simultaneous sending of :term:`tokens<Token>` to multiple :term:`addresses<Address>`. As a rule, the airdrop is used as an incentive for holders of a certain token as part of a marketing campaign to promote a project, increase its recognition, and attract investors.

  Alias

    An alias is a short, easy-to-remember :term:`address<Address>` name. There cannot be two aliases with the same name. A single address can have multiple aliases.

  Asset

    An asset is a synonym for the :term:`token<Token>`.

  Asset Script

    An asset script is a :term:`Ride<Ride>` :term:`script<Script>` that has the following directives:

    .. code-block:: none

      {-# CONTENT_TYPE EXPRESSION #-}
      {-# SCRIPT_TYPE ASSET #-}

    The asset script is attached to the asset using the set asset script transaction. You can attach a script to an asset only at the time of the asset creation. However, you can change the script later, if needed. An asset with a script attached to it is called a :term:`smart asset<Smart Asset>`.

B
=

.. glossary::

  Block

    A block is a unit of the :term:`blockchain<Blockchain>` chain. The block contains :term:`transactions<Transaction>`: from :math:`0` to :math:`6000` inclusive. The maximum block size is :math:`1` MB.

  Blockchain

    A blockchain is a continuous sequential chain of :term:`blocks<Block>` that are linked using cryptography. The blockchain has its own :term:`blockchain height<Blockchain Height>`.

  Block Height

    A block height is the :term:`block’s<Block>` sequence number in the :term:`blockchain<Blockchain>`.

  Blockchain Height

    A blockchain height is a sequence number of the last :term:`block<Block>` in the :term:`blockchain<Blockchain>`.

  Blockchain Network

    A blockchain network is a computer network that consists of :term:`node<Node>`.

  Block Signature

    A block signature is a :term:`hash<Hash>` that the :term:`mining node<Mining Node>` receives when it signs the generated :term:`block<Block>` with the :term:`private key<Private Key>` of the :term:`mining account<Mining Account>`.

C
=

.. glossary::

  Consensus

    The consensus is a set of rules in accordance with which :term:`blockchain<Blockchain>` operates. DecentralChain uses the :term:`LPoS consensus<LPoS>`.

  Cryptocurrency

    A cryptocurrency is a type of digital currency, the creation and control of which is based on cryptographic methods.

D
=

.. glossary::

  dApp

    A dApp is an :term:`account<Account>` with the :term:`dApp script<dApp Script>` attached.

  dApp Script

    A dApp script is a Ride script used to create dApp. The dApp script has the following directive:

    .. code-block:: none

      {-# CONTENT_TYPE DAPP #-}

    dApp Script can be attached to the :term:`account<Account>` using the set script transaction, and, as a result, the dApp will be created.

  Decentralized Application

    A decentralized application is an application that is stored and executed on the :term:`blockchain<Blockchain>` network.

E
=

.. glossary::

  Explorer

    Explorer (or `DecentralChain Explorer <https://decentralscan.com/>`_) is an online service that displays DecentralChain blockchain data in a human-readable form.

F
=

.. glossary::

  Faucet

    A test network faucet (or faucet) is a `DecentralChain Explorer <https://decentralscan.com/>`_ tool that refills the :term:`test network<Test Network>` accounts with the DecentralCoins test :term:`tokens<Token>`. For one recharge, the user receives :math:`10` testnet DecentralCoins.

G
=

.. glossary::

  Gateway

    Gateway is a centralized payment solution that allows transferring :term:`cryptocurrencies<Cryptocurrency>` from one :term:`blockchain<Blockchain>` to another and vice versa; as well as transferring fiat money to and out of the blockchain.

  Genesis Block

    The genesis block (or genesis) is the very first :term:`block<Block>` of the :term:`blockchain<Blockchain>`. The genesis block contains one or several genesis transactions.

  Genesis Transaction

    Genesis transaction is a :term:`genesis block<Genesis Block>` transaction that charges DecentralCoins to an :term:`account<Account>`. The genesis transactions define the initial distribution of DecentralCoins between accounts during the creation of the :term:`blockchain<Blockchain>`.

H
=

.. glossary::

  Hash

    A hash is a result of applying a :term:`hash function<Hash Function>`.

  Hash Function

    A hash function (or fold function) is a function that converts an array of input data of arbitrary length into a bit string of a fixed length, performed by a certain algorithm.

I
=

J
=

K
=

L
=

.. glossary::

  Leasing

    Leasing is a temporary reversible transfer of DecentralCoins from one account to another to increase the stability and security of the network, as well as potentially get mining reward. Note that the DecentralCoin :term:`tokens<Token>` are not actually being transferred to another account, they remain on the sender's balance, however, they are 'frozen' and cannot participate in the buying and selling operations, as well as they cannot be sent to another account. The leased tokens provide the leasing recipient with a greater chance of :term:`mining<Mining>` a :term:`block<Block>`. The recipient of the lease can share the income from mining with the one who leased DecentralCoins to him. However, the DecentralChain protocol does not regulate the payment process for :term:`LPoS<LPoS>` mining, this remains at the discretion of the :term:`miner<Miner>`. At any time, the sender can 'unfreeze' tokens by invoking the Lease Cancel transaction.

  LPoS

    LPoS (or Leased Proof-of-Stake) is a :term:`consensus<Consensus>` algorithm in which the probability of generating the next :term:`block<Block>` by the participant is proportional to the share of :term:`cryptocurrencies<Cryptocurrency>` belonging to this participant or leased to this participant from their total supply. In other words, the more :term:`tokens<Token>` on the :term:`account<Account>` of the :term:`miner<Miner>` (own and leased to them), the higher the probability of generating the next block.

M
=

.. glossary::

  Mainnet

    The mainnet (or main network) is the main DecentralChain :term:`blockchain<Blockchain>` network.

  Matcher

    Matcher is a service that executes :term:`orders<Order>` on the exchange.
  
  Matcher Fee

    A matcher fee is a fee that :term:`matcher<Matcher>` takes from both :term:`accounts<Account>` that participate in the exchange of the pair of :term:`tokens<Token>`.

  Miner

    A miner is the owner of the :term:`mining node<Mining Node>`.

  Mining

    Mining is the process of generating a :term:`block<Block>` by a :term:`mining node<Mining Node>`, as a result of which a new block is added to the :term:`blockchain<Blockchain>` and DecentralCoin :term:`tokens<Token>` are issued. For block generation, :term:`miners<Miner>` receive a reward for mining, as well as transaction fees, according to the rules of the DecentralChain-M5 protocol.

  Mining Account

    A mining account is an :term:`account<Account>` that the :term:`mining node<Mining Node>` uses to :term:`block<Block Signature>` the generated :term:`blocks<Block>`.

  Mining Node

    A mining node is a :term:`node<Node>` that can perform :term:`mining<Mining>`. Each mining node is a validating node :term:`node<Node>`.

  Multisignature

    Multisignature is an implementation of an electronic signature that requires the use of several  :term:`private key<Private Key>` as a condition for  :term:`transactions<Transaction>` execution.

N
=

.. glossary::

  NFT

    NFT (Non-Fungible Token) is a :term:`tokens<Token>` with unique ID. Two 'regular' tokens can not be distinguished from each other — they are the same, i.e. fungible. Each NFT is unique; there cannot be two identical NFTs. Most often NFTs are used in games.

  Node

    A node is a host that is connected to the :term:`blockchain<Blockchain>` network using the DecentralChain node application. The node stores :term:`blocks<Block>`, sends and validates :term:`transactions<Transaction>`.

O
=

.. glossary::

  Oracle

    Oracle is a provider of data from the outside world to the :term:`blockchain<Blockchain>`.

  Oracle Card

    An oracle card is a public description of the :term:`oracle<Oracle>` in the :term:`blockchain<Blockchain>` according to a standardized protocol in the form of a data transaction.

  Order

    Order (or exchange order) is an instruction to buy or sell a :term:`tokens<Token>` on the exchange.

P
=

.. glossary::

  PoS

    PoS (Proof-of-Stake) is a :term:`consensus<Consensus>` algorithm in which the probability of generating the next :term:`block<Block>` is proportional to the share of :term:`cryptocurrencies<Cryptocurrency>` belonging to this participant from their total supply. In other words, the more :term:`tokens<Token>` on the :term:`account<Account>` of a :term:`miner<Miner>`, the higher the probability of generating the next block.

  PoW

    PoW (Proof-of-Work) is a :term:`consensus<Consensus>` algorithm in which it is required to perform a complex calculation in order to generate a new :term:`block<Block>`. That is, the higher the performance of the :term:`miner's<Miner>` equipment, the higher the probability of generating the next block.

  Private Key

    The private key is one of a pair of :term:`account<Account>` keys. The account owner signs the :term:`transaction<Transaction>` with the private key before sending it, and, as a result, gets the digital signature of the transaction.

  Public Key

    An account script is a Ride script that has the following directives:

Q
=

R
=

.. glossary::

  Ride

    The Ride is a functional expression-based programming language. Ride is used to write :term:`scripts<Script>`. The language has strong static typing, it is case sensitive, has no loops and goto-like expressions, and therefore it is Turing-incomplete

S
=

.. glossary::

  Script

    A script is the source code on the :term:`Ride<Ride>` language. There are three types of scripts: :term:`dApp script<dApp Script>`, :term:`account script<Account Script>`, :term:`asset script<Asset Script>`.

  Secret Phrase

    Secret phrase (or Seed) is a set of characters (usually, it is 15 English words with spaces between them) that allows you to access your DecentralChain :term:`address<Address>` and, accordingly, the funds on your :term:`account<Account>`. When registering an account, you are asked to keep your secret phrase safe.

  Smart Account

    A smart account is an :term:`account<Account>` with an account script attached. Only one script can be attached to an account. The account script is attached to the account using the set script transaction.

  Smart Asset

    A smart asset is a :term:`tokens<Token>` with an :term:`asset script<Asset Script>` attached.

  Stagenet

    Stagenet (or staging network) is the DecentralChain :term:`blockchain<Blockchain>` network, which is used for experiments, intermediate testing of new functionality, as well as providing access for the DecentralChain community to intermediate releases. It is important to consider that this network is unstable, a frequent rollback of blockchain data to the N-th height in the past is possible.

T
=

.. glossary::

  Test Network

    Test network (or testnet) is a DecentralChain :term:`blockchain<Blockchain>` test network, which is used by developers to test their products, and by users to get acquainted with the blockchain.

  Token

    A token is a :term:`blockchain<Blockchain>` object that represents another object from the physical or virtual world or an abstract concept.

  Transaction

    Transaction is an action on the :term:`blockchain<Blockchain>` on behalf of the :term:`account<Account>`. Transactions can be sent only from the account — thus, any transaction can be correlated with a certain account.

  Transaction Body Bytes

    An account script is a Ride script that has the following directives:

U
=

.. glossary::

  UTX pool

    UTX pool (or Unconfirmed Transactions pool) is a pool of unconfirmed :term:`node<Node>` :term:`transactions<Transaction>` that are waiting for validation.

V
=

.. glossary::

  Validating Node

    A validating node is a :term:`node<Node>` that validates :term:`transactions<Transaction>`.

W
=

.. glossary::


  Decentralites

    One Decentralite is 1/100 000 000 DecentralCoin. 1 Decentralite is the minimum number of DecentralCoins that you can work with within the DecentralChain :term:`blockchain<Blockchain>`.

  DecentralCoins

    DecentralCoin is the main token of the DecentralChain blockchain. 1 DecentralCoin equals 100,000,000 Decentralites. 
    
  WCT

    An account script is a Ride script that has the following directives:

X
=

Y
=

Z
=
