*************
Token (Asset)
*************

Token is a digital asset on the blockchain. A token can be used:

* As a cryptocurrency to pay for goods and services within a project, as well as for crowdfunding;
* As an object or resource in games etc.

A token can represent a physical or an intangible object. The words “token” and “asset” are used interchangeably in the DecentralChain ecosystem.
DecentralCoin is the native token on the DecentralChain blockchain. :ref:`More about DecentralCoin <02_decentralchain/02_token(asset):DecentralCoin>`.

All other tokens are custom tokens issued on behalf of some account. Any account that has enough DecentralCoins to pay the fee can issue its own token. The new token is immediately available:

* For transfers between accounts,
* For trading on `Decentral.Exchange <https://decentral.exchange/>`_ (except for :ref:`NFTs <02_decentralchain/02_token(asset):Non-Fungible Token>`; :ref:`smart assets <02_decentralchain/02_token(asset):Smart Asset>` trading is temporarily unavailable),
* For payments attached to dApp :ref:`script invocation <02_decentralchain/03_transaction:Invoke Script Transaction>`.

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
  * :ref:`Smart asset <02_decentralchain/02_token(asset):Smart Asset>`: A smart asset is an asset with an attached script that places conditions on every transaction made for the asset in question.
  * Script (for issuing a smart asset).

* Before creating a new asset, carefully read the creation conditions. If necessary, change the name of the asset according to the conditions, then select the I understand... checkbox and click Generate.
* On the next screen double-check the entered data and if everything is correct click Send to finish the creation or click Go Back to make corrections..

The transaction fee is :math:`1` DecentralCoin for a regular token or :math:`0.001` DecentralCoins for a :ref:`non-fungible token (NFT) <02_decentralchain/02_token(asset):Non-Fungible Token>`.
Moreover, the token can be issued by the :ref:`dApp script <03_ride-language/04_script-types:dApp Script>` as a result of the :ref:`invoke script transaction <02_decentralchain/03_transaction:Invoke Script Transaction>` when the callable function result contains the :ref:`Issue <03_ride-language/05_structures:Issue>` action. The minimum fee for invoke script transaction is increased by :math:`1` DecentralCoin for each non-NFT token issued.

Token ID
========

Token ID is a byte array calculated as follows:

* If the token is issued by :ref:`issue transaction <02_decentralchain/03_transaction:Issue Transaction>`, the token ID is the same as the transaction ID.
* If the token is issued by :ref:`invoke script transaction <02_decentralchain/03_transaction:Invoke Script Transaction>` when the callable function of :ref:`dApp script <02_decentralchain/01_account:dApp and Smart Account>` performed the :ref:`Issue <03_ride-language/05_structures:Issue>` action, the token ID is calculated as the BLAKE2b-256 hash of the byte array containing transaction ID and the fields of the Issue structure.

In the :ref:`Node REST API <documentation:placeholder>`, the token identifier is encoded in base58. For example:

.. code-block:: none

 "assetId": "8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS"

The :ref:`DecentralCoin <02_decentralchain/02_token(asset):DecentralCoin>` token has no identifier. The Node REST API uses null for DecentralCoin.

Token Operations
================

* Transfer to another account

Can be done via a :ref:`transfer transaction <02_decentralchain/03_transaction:Transfer Transaction>` or a :ref:`mass transfer transaction <02_decentralchain/03_transaction:Mass Transfer Transaction>`.
A :ref:`dApp script <02_decentralchain/01_account:dApp and Smart Account>` can transfer the token via a :ref:`ScriptTransfer <03_ride-language/05_structures:ScriptTransfer>` script action as a result of an :ref:`invoke script transaction <02_decentralchain/03_transaction:Invoke Script Transaction>`.

* Exchange (trade deal)

Three accounts can participate in the exchange: one user creates an :ref:`order <02_decentralchain/06_order:Order>` to buy a token, the other creates an order to sell a token. The matcher combines buy and sell orders with suitable parameters and creates an :ref:`exchange transaction <02_decentralchain/03_transaction:Exchange Transaction>`.

* Burning

Decreases the amount of token on the account and thereby the total amount of the token on the blockchain. Any token owner can burn it, not only the issuer. It is impossible to burn :ref:`DecentralCoin <02_decentralchain/02_token(asset):DecentralCoin>`. Can be done via a :ref:`burn transaction <02_decentralchain/03_transaction:Burn Transaction>`.
A dApp script can burn the token via a :ref:`Burn <03_ride-language/05_structures:Burn>` script action as a result of the Invoke script transaction.

* Payment to :ref:`dApp <02_decentralchain/01_account:dApp and Smart Account>`

An :ref:`invoke script transaction <02_decentralchain/03_transaction:Invoke Script Transaction>` can contain up to two payments to the dApp. Payment amount and token are available to the callable function.

Operations Available Only to Issuer
-----------------------------------

The following token operations can only be performed by the account that issued the token:

* Sponsorship setup

The token issuer can enable sponsorship which allows all users to pay fees in this token (instead of DecentralCoins) for invoke script transactions and transfer transactions. :ref:`More about sponsorship <02_decentralchain/03_transaction:Sponsored Fees>`. Enabling or disabling sponsorship can be done via a :ref:`sponsor fee transaction <02_decentralchain/03_transaction:Sponsor Fee Transaction>`. A dApp script can set up sponsorship using a :ref:`SponsorFee <03_ride-language/05_structures:SponsorFee>` as a result of the invoke script transaction.

* Reissue

Increases the amount of token on the blockchain. The reissuable field of token determines whether the token can be reissued. Can be done via a :ref:`reissue transaction <02_decentralchain/03_transaction:Reissue Transaction>`.
A dApp script can reissue the token via a :ref:`Reissue <03_ride-language/05_structures:Reissue>` script action as a result of the invoke script transaction.

* Replacing the asset script

Can be done via a :ref:`set asset script transaction <02_decentralchain/03_transaction:Set Asset Script Transaction>`. If the token is not a smart asset, that is, the script was not attached when the token was issued, then it is impossible to attach the script later.

* Modifying the token name and / or description

Can be done via an :ref:`update asset info transaction <02_decentralchain/03_transaction:Update Asset Info Transaction>`.

Token Types
===========

Non-Fungible Token
------------------

Non-fungible token or NFT is a special type of a :ref:`token <02_decentralchain/02_token(asset):Token (Asset)>` that is issued with the following parameters:

* "quantity": :math:`1`
* "decimals": :math:`0`
* "reissuable": false

NFT is a singular entity that has a unique ID. This contrasts with a regular token, two coins of which (for example, two WBTC) cannot be distinguished from each other. NFTs can be used as in-game items, collectibles, certificates, or unique coupons. 

Issue of NFT
^^^^^^^^^^^^

NFT can be issued in the same ways as a regular token, see :ref:`token issue <02_decentralchain/02_token(asset):Token Issue>`. The minimum fee for an NFT issue is :math:`0.001` DecentralCoins, :math:`1000` times less than for a regular token.

Smart Asset
-----------

Smart asset is a :ref:`token <02_decentralchain/02_token(asset):Token (Asset)>` that has an :ref:`asset script <03_ride-language/04_script-types:Asset Script>` assigned to it.
By default, tokens on the DecentralChain blockchain are not smart contracts, and any transactions with them are allowed. The script endows a token with functionality that sets the rules for its circulation. Each transaction involving a smart asset is automatically checked against the conditions specified in the script. If the asset's script allows the transaction, it will be executed; if the script denies the transaction, it is either not put onto the blockchain at all or saved as failed (for details, see the :ref:`transaction validation <02_decentralchain/03_transaction:Transaction Validation>` article).

Using smart assets, you can implement various financial instruments on the blockchain (options, interval trading, taxation), game mechanics (allowing transactions only between characters with certain properties). Please note:

* If a token is issued without a script, then the script cannot be added later.
* The script cannot be removed, so it is impossible to turn a smart asset into a regular one.
* The asset script can be changed using the :ref:`set asset script transaction <02_decentralchain/03_transaction:Set Asset Script Transaction>`, unless prohibited by the asset script itself (as well as by the :ref:`dApp or account script <02_decentralchain/01_account:dApp and Smart Account>` assigned to the issuer account).
* The :ref:`minimum fee <02_decentralchain/03_transaction:Minimum Fee>` for transaction is increased by :math:`0.004` DecentralCoins for each smart asset involved, except for:

  * :ref:`Invoke script transactions <02_decentralchain/03_transaction:Invoke Script Transaction>`,
  * Smart assets used as matcher fee in :ref:`exchange transaction <02_decentralchain/03_transaction:Exchange Transaction>`.

Tokens of Other Blockchains
---------------------------

A token issued on another blockchain cannot be used directly on the DecentralChain blockchain. A new token representing the original one can be issued on the DecentralChain blockchain, and a gateway that pegs the two tokens :math:`1:1` can be deployed. 

DecentralCoin
==============

DecentralCoin is the native :ref:`token <02_decentralchain/02_token(asset):Token (Asset)>` of the DecentralChain blockchain. :ref:`Block generators <02_decentralchain/05_node:Generating Node>` receive :ref:`transaction fees <02_decentralchain/03_transaction:Transaction Fees>` and :ref:`block rewards <02_decentralchain/05_node:Block Reward>` in DecentralCoins, which encourages generators to maintain and develop the blockchain network infrastructure. The more DecentralCoins the generator holds (by ownership or lease), the greater its chance to add the next block is.

DecentralCoin Parameters
-------------------------

DecentralCoins are present on the blockchain since inception, there is no issue transaction for it, therefore the DecentralCoin token does not have an ID. The REST API uses null for DecentralCoins.
The number of decimal places (decimals) for DecentralCoins is :math:`8`. The atomic unit called Decentralite is :math:`\frac{1}{100,000,000}` DecentralCoins.

Leasing
-------

The owner of DecentralCoins can lease them via a :ref:`lease transaction <02_decentralchain/03_transaction:Lease Transaction>`. DecentralCoins received on lease are included in the :ref:`generating balance <02_decentralchain/01_account:Account Balance>`. Block generators send back different percentages as rewards to lessors. A lessor can cancel the lease at any time via a :ref:`lease cancel transaction <02_decentralchain/03_transaction:Lease Cancel Transaction>`. :ref:`More about leasing <02_decentralchain/05_node:Leased Proof of Stake>`.

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
  :file: ../_static/02_decentralchain/tables/001_Token-Custom-Parameters.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

Atomic Unit
-----------

The amount of token is displayed differently in UIs and in the :ref:`JSON representation <02_decentralchain/03_transaction:JSON Representation>` used by the :ref:`Node REST API <documentation:placeholder>`. In API requests and responses, amount values are integers indicated in atomic units to avoid precision issues in floating-point calculations. An atomic unit is the minimum fraction (“cent”) of a token, it is equal to :math:`10^{-decimals}`. The amount of token in JSON is the real quantity multiplied by :math:`10^{decimals}`.

For USD-N in the example above:

* decimals = :math:`6`,
* atomic unit is :math:`\frac{1}{1,000,000}` USD-N.
* "quantity": :math:`999999999471258900` corresponds to :math:`999,999,999,471.258900` USD-N in UIs, "minSponsoredAssetFee": :math:`7420` corresponds to :math:`0.007420` USD-N.