**********
Structures
**********

All structures in Ride are built-in — you cannot create your own structures. All structures have constructors.

Let's see an example of a code that creates an instance of the IntegerEntry structure and reads its key and value:

.. code-block:: none

 let data = IntegerEntry("Age", 33)
 let key  = data.key
 let val = data.value

Script Actions
==============

Script actions are executed, that is, they make changes on the blockchain only if they are included in the resulting expression of the callable function. See more details in the :ref:`callable function <03_ride-language/03_functions:Callable Functions>` article.

.. csv-table:: Script Actions
  :file: ../_static/03_ride-language/tables/163_Script-Actions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

Available script actions depend on the standard library version used.

BinaryEntry
-----------

BinaryEntry is a structure that sets key and value of binary entry :ref:`account data storage <02_decentralchain/01_account:Account Data Storage>`. Adding or changing an entry is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.

:strong:`Constructor`

.. code-block:: none

 BinaryEntry(key: String, value: ByteVector)

:strong:`Fields`

.. csv-table:: BinaryEntry Fields
  :file: ../_static/03_ride-language/tables/164_BinaryEntry-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

BooleanEntry
------------

BooleanEntry is a structure that sets the key and value of the :ref:`account data storage <02_decentralchain/01_account:Account Data Storage>` boolean entry. Adding or changing an entry is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.

:strong:`Constructor`

.. code-block:: none

 BooleanEntry(key: String, value: Boolean)

:strong:`Fields`

.. csv-table:: BooleanEntry Fields
  :file: ../_static/03_ride-language/tables/165_BooleanEntry-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Burn
----

Burn is a structure that sets the parameters of the token burning. The token burning is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.
If the token is a smart asset, the asset script verifies the Burn action as if it were :ref:`BurnTransaction <03_ride-language/05_structures:BurnTransaction>` with the fee of :math:`0` and the version of :math:`0`. If the asset script denies the action, then the transaction that invoked the dApp script is either denied or saved on the blockchain as failed, see the :ref:`transaction validation <02_decentralchain/03_transaction:Transaction Validation>`.

:strong:`Constructor`

.. code-block:: none

 Burn(assetId: ByteVector, quantity: Int)

:strong:`Fields`

.. csv-table:: Burn Fields
  :file: ../_static/03_ride-language/tables/166_Burn-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

DeleteEntry
-----------

DeleteEntry is a structure that sets the parameters of deletion of entry from the :ref:`account data storage <02_decentralchain/01_account:Account Data Storage>`. Deleting an entry is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.

:strong:`Constructor`

.. code-block:: none

 DeleteEntry(key: String)

:strong:`Fields`

.. csv-table:: DeleteEntry Fields
  :file: ../_static/03_ride-language/tables/167_DeleteEntry-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# SCRIPT_TYPE ACCOUNT #-}
    
 @Callable(inv)
 func default() = {
  (
    [
      DeleteEntry(inv.caller.toString())
    ],
    unit
  )
 }

IntegerEntry
------------

IntegerEntry is a structure that sets the key and value of :ref:`account data storage <02_decentralchain/01_account:Account Data Storage>` integer entry. Adding or changing an entry is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.

:strong:`Constructor`

.. code-block:: none

 IntegerEntry(key: String, value: Int)

:strong:`Fields`

.. csv-table:: IntegerEntry Fields
  :file: ../_static/03_ride-language/tables/168_IntegerEntry-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Issue
-----

Issue is a structure that sets the parameters of the token issue. The token issue is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.
The minimum fee for an invoke script transaction is increased by :math:`1` DecentralCoin for each issued asset that is not :ref:`NFT <02_decentralchain/02_token(asset):Non-Fungible Token>`.
You can get the ID of the issued token using the :ref:`calculateAssetId <03_ride-language/03_functions:Blockchain Functions>` function.

:strong:`Constructor`

.. code-block:: none

 Issue(name: String, description: String, quantity: Int, decimals: Int, isReissuable: Boolean, compiledScript: Script|Unit, nonce: Int)

or

.. code-block:: none

 Issue(name: String, description: String, quantity: Int, decimals: Int, isReissuable: Boolean) 

In the second case, compiledScript = unit and nonce = 0 values are inserted automatically.

:strong:`Fields`

.. csv-table:: Issue Fields
  :file: ../_static/03_ride-language/tables/169_Issue-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

:strong:`Regular Token Issue`

.. code-block:: none

 Issue("RegularToken", "This is an ordinary token", 10000, 2, true)

The structure sets the following parameters of token:

* Name: RegularToken
* Description: This is an ordinary token
* Amount of tokens to issue: :math:`100` (value of :math:`10 000` is specified in the minimum fraction — “cents”)
* Amount of decimals: :math:`2`
* Reissue ability: yes

:strong:`Multiple Token Issue`

.. code-block:: none

 (
  [
    Issue("RegularToken", "This is an ordinary token", 10000, 2, true, unit, 0),
    Issue("RegularToken", "This is an ordinary token", 10000, 2, true, unit, 1)
  ],
  unit
 )

:strong:`NFT Issue`

.. code-block:: none

 Issue("UberToken", "The ultimate token.", 1, 0, false)

The structure sets the following parameters of token:

* Name: UberToken
* Description: The ultimate token. 
* Amount of tokens to issue: :math:`1`
* Amount of decimals: :math:`0`
* Reissue ability: no

Lease
-----

Lease is a structure that sets the lease parameters. The lease is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`. More about :ref:`lease <02_decentralchain/05_node:Leased Proof of Stake>`.
You can get the lease ID using the :ref:`calculateLeaseId <03_ride-language/03_functions:Blockchain Functions>` function.

:strong:`Constructor`

.. code-block:: none

 Lease(recipient: Address|Alias, amount: Int, nonce: Int)

or

.. code-block:: none

 Lease(recipient: Address|Alias, amount: Int) 

In the second case, nonce = :math:`0` is inserted automatically.

:strong:`Fields`

.. csv-table:: Lease Fields
  :file: ../_static/03_ride-language/tables/170_Lease-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}
  
 @Callable(i)
 func foo() = {
  let lease = Lease(Alias("merry"),100000000)
  let id = calculateLeaseId(lease)
  (
    [
      lease,
      BinaryEntry("lease", id)
    ],
    unit
  )
 }

LeaseCancel
-----------

LeaseCancel is a structure that sets the lease cancellation parameters. The lease cancellation is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.


:strong:`Constructor`

.. code-block:: none

 LeaseCancel(leaseId: ByteVector)

:strong:`Fields`

.. csv-table:: LeaseCancel Fields
  :file: ../_static/03_ride-language/tables/171_LeaseCancel-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Reissue
-------

Reissue is a structure that sets the parameters of the token reissue. The token reissue is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.
The token reissue is only available for an asset that is issued by a dApp account.
If the token is a smart asset, the asset script verifies the Reissue action as if it were :ref:`ReissueTransaction <03_ride-language/05_structures:ReissueTransaction>` with the fee of 0 and the version of 0. If the asset script denies the action, then the transaction that invoked the dApp script is either denied or saved on the blockchain as failed, see the :ref:`transaction validation <02_decentralchain/03_transaction:Transaction Validation>`.

:strong:`Constructor`

.. code-block:: none

 Reissue(assetId: ByteVector, quantity: Int, isReissuable: Boolean)

:strong:`Fields`

.. csv-table:: Reissue Fields
  :file: ../_static/03_ride-language/tables/172_Reissue-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

ScriptTransfer
--------------

ScriptTransfer is a structure that sets the parameters of the token transfer. The token transfer is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.
If the token is a smart asset, the asset script verifies the ScriptTransfer action as if it were :ref:`TransferTransaction <03_ride-language/05_structures:TransferTransaction>` with the fee of :math:`0` and the version of :math:`0`. If the asset script denies the action, then the transaction that invoked the dApp script is either denied or saved on the blockchain as failed, see the :ref:`transaction validation <02_decentralchain/03_transaction:Transaction Validation>`. 

:strong:`Constructor`

.. code-block:: none

 ScriptTransfer(recipient: Address|Alias, amount: Int, asset: ByteVector|Unit)

:strong:`Fields`

.. csv-table:: ScriptTransfer Fields
  :file: ../_static/03_ride-language/tables/173_ScriptTransfer-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

SponsorFee
----------

SponsorFee is a structure that sets up sponsorship. For information about sponsorship, see the :ref:`sponsored fee <02_decentralchain/03_transaction:Sponsored Fees>` article. The sponsorship setup is performed only if the structure is included in the resulting expression of the callable function. See details in the :ref:`callable function <03_ride-language/03_functions:Callable Functions>` article.
The sponsorship setup is only available if the asset is issued by a dApp account (by the same script invocation as well) and is not a smart asset.

:strong:`Constructor`

.. code-block:: none

 SponsorFee(assetId: ByteVector, minSponsoredAssetFee: Int|Unit)

:strong:`Fields`

.. csv-table:: SponsorFee Fields
  :file: ../_static/03_ride-language/tables/174_SponsorFee-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}
  
 @Callable(i)
 func issueAndSponsor() = {
  let issue = Issue("Spring", "", 100000, 2, true, unit, 0)
  let id = calculateAssetId(issue)
  (
    [
      issue,
      SponsorFee(id, 300)
    ],
    unit
  )
 }

The issueAndSponsor callable function issues an asset and enables sponsorship. The minimum fee in sponsored assets is :math:`3` Spring.

StringEntry
-----------

StringEntry is a structure that sets key and value of :ref:`account data storage <02_decentralchain/01_account:Account Data Storage>` string entry. Adding or changing an entry is performed only if the structure is included in the :ref:`callable function result <03_ride-language/03_functions:Callable Functions>`>`.

:strong:`Constructor`

.. code-block:: none

 BinaryEntry(key: String, value: String)

:strong:`Fields`

.. csv-table:: StringEntry Fields
  :file: ../_static/03_ride-language/tables/175_StringEntry-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Common Structures
=================

.. csv-table:: Common Structures
  :file: ../_static/03_ride-language/tables/176_Common-Structures.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

Address
-------

Structure of an :ref:`address <02_decentralchain/01_account:Address>`.

:strong:`Constructor`

.. code-block:: none

 Address(bytes: ByteVector)

:strong:`Fields`

.. csv-table:: Address Fields
  :file: ../_static/03_ride-language/tables/177_Address-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

Get all types of balance in DecentralCoins for the current account (in a dApp script or an account script):

.. code-block:: none

 decentralchainBalance(this)

For any account:

.. code-block:: none

 let address=base58'3N4iKL6ikwxiL7yNvWQmw7rg3wGna8uL6LU'
 decentralchainBalance(Address(address))

Get an entry value by key from the account data storage:

.. code-block:: none

 let address2=base58'3N6dFJ6XBQsWz1VV1i5aW4CyYpVKc39MUGZ'
 getBoolean(Address(address2),"allow_orders")

Convert the address that invoked the function to a base58 string:

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

 @Callable(i)
 func foo(question: String) = {
  let callerAddress = toBase58String(i.caller.bytes)
  ...
 }

Check the recipient's address in the transfer transaction:

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE EXPRESSION #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

 # Bank dApp address
 let BANK = base58'3MpFRn3X9ZqcLimFoqNeZwPBnwP7Br5Fmgs'

 match (tx) {
  case t: TransferTransaction => addressFromRecipient(t.recipient).bytes == BANK
  case _ => false
 }

Alias
-----

Structure of an :ref:`alias <02_decentralchain/01_account:Alias>`.

:strong:`Constructor`

.. code-block:: none

 Alias(alias: String)

:strong:`Fields`

.. csv-table:: Alias Fields
  :file: ../_static/03_ride-language/tables/178_Alias-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

.. code-block:: none

 let alias = Alias("merry")
 addressFromRecipient(alias)

Asset
-----

Structure of a :ref:`token <02_decentralchain/02_token(asset):Token (Asset)>`. The structure is returned by the  :ref:`assetInfo <03_ride-language/03_functions:Blockchain Functions>` built-in function.

:strong:`Constructor`

.. code-block:: none

 Asset(id: ByteVector, quantity: Int, decimals: Int, issuer: Address, issuerPublicKey: ByteVector, reissuable: Boolean, scripted: Boolean, minSponsoredFee: Int|Unit, name: String, description: String)

:strong:`Fields`

.. csv-table:: Asset Fields
  :file: ../_static/03_ride-language/tables/179_Asset-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

Get the account balance in a given asset:

.. code-block:: none

 let address=base58'3Mw48B85LvkBUhhDDmUvLhF9koAzfsPekDb'
 let assetId=base58'GpxmxorKXLz1V7xootrvGyFgqP2tTTBib5HEm8QGZTHX'
 assetBalance(Address(address), assetId)

AssetPair
---------

Structure of a pair of :ref:`tokens <02_decentralchain/02_token(asset):Token (Asset)>` of an order within the :ref:`Order <03_ride-language/05_structures:Order>` structure.

:strong:`Constructor`

.. code-block:: none

 AssetPair(amountAsset: ByteVector|Unit, priceAsset: ByteVector|Unit)

:strong:`Fields`

.. csv-table:: AssetPair Fields
  :file: ../_static/03_ride-language/tables/180_AssetPair-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

Get the account balance in a given asset:

.. code-block:: none

 let address=base58'3Mw48B85LvkBUhhDDmUvLhF9koAzfsPekDb'
 let assetId=base58'GpxmxorKXLz1V7xootrvGyFgqP2tTTBib5HEm8QGZTHX'
 assetBalance(Address(address), assetId)

AttachedPayment
---------------

Structure of a payment attached to the script invocation and available to the :ref:`callable function <03_ride-language/03_functions:Callable Functions>`. The structure is used in:

* :ref:`Invocation <03_ride-language/05_structures:Invocation>` structure.
* :ref:`InvokeScriptTransaction <03_ride-language/05_structures:InvokeScriptTransaction>` structure.
* :ref:`Invoke <03_ride-language/03_functions:dApp-to-dApp Invocation Functions>` and :ref:`reentrantInvoke <03_ride-language/03_functions:dApp-to-dApp Invocation Functions>` functions.

:strong:`Constructor`

.. code-block:: none

 AttachedPayment(assetId: ByteVector|Unit, amount: Int)

:strong:`Fields`

.. csv-table:: AttachedPayment Fields
  :file: ../_static/03_ride-language/tables/181_AttachedPayment-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

BalanceDetails
--------------

Structure that contains DecentralCoins balances of account. The structure is returned by the decentralchainBalance built-in function. For description of balance types, see the :ref:`account balance <02_decentralchain/01_account:Account Balance>` article.

:strong:`Constructor`

.. code-block:: none

 BalanceDetails(available: Int, regular: Int, generating: Int, effective: Int)

:strong:`Fields`

.. csv-table:: BalanceDetails Fields
  :file: ../_static/03_ride-language/tables/182_BalanceDetails-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

All balances are given in Decentralites.

BlockInfo
---------

Structure containing block headers. The structure is returned by the blockInfoByHeight built-in function.

:strong:`Constructor`

.. code-block:: none

 BlockInfo(timestamp: Int, height: Int, baseTarget: Int, generationSignature: ByteVector, generator: Address, generatorPublicKey: ByteVector, vrf: ByteVector|Unit)

:strong:`Fields`

.. csv-table:: BlockInfo Fields
  :file: ../_static/03_ride-language/tables/183_BlockInfo-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Invocation
----------

Structure that contains the fields of the script invocation that the :ref:`callable function <03_ride-language/03_functions:Callable Functions>` can use.

:strong:`Constructor`

.. code-block:: none

 Invocation(caller: Address, callerPublicKey: ByteVector, originCaller: Address, originCallerPublicKey: ByteVector, payments: List[AttachedPayment], transactionId: ByteVector, fee: Int, feeAssetId: ByteVector|Unit)

:strong:`Fields`

The field values depend on how the callable function is invoked. If the callable function is invoked by an :ref:`invoke script transaction <02_decentralchain/03_transaction:Invoke Script Transaction>`:

.. csv-table:: Invocation Fields 1
  :file: ../_static/03_ride-language/tables/184_Invocation-Fields-1.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

If the callable function is invoked by the invoke or reentrantInvoke function (see the :ref:`dApp-to-dApp invocation <03_ride-language/07_dapp-to-app-invocation:dApp-to-App Invocation>` article):

.. csv-table:: Invocation Fields 2
  :file: ../_static/03_ride-language/tables/185_Invocation-Fields-2.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

The originCaller, originCallerPublicKey, transactionId, fee, and feeAssetId values are the same for all dApp-to-dApp invocations within a single Invoke Script transaction.

:strong:`Example`

The following function checks that the first payment in the Invoke Script transaction is at least 1 DecentralCoin or 5 in the specified asset.

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

 func isPaymentOk(i: Invocation) = {
  let acceptableAssetId = base58'3JmaWyFqWo8YSA8x3DXCBUW7veesxacvKx19dMv7wTMg'
  if (size(i.payments) == 0) then {
    throw("Payment not attached")
  } else {
    let p = i.payments[0]
    match p.assetId {
      case assetId: ByteVector => assetId == acceptableAssetId && p.amount >= 500000000
      case _ => p.amount >= 100000000
    }
  }
 }

 @Callable(i)
 func foo() = {
  if isPaymentOk(i) then ([],unit) else throw("Wrong payment amount or asset")
 }

Order
-----

Structure of an order :ref:`dApp-to-dApp invocation <03_ride-language/07_dapp-to-app-invocation:dApp-to-App Invocation>`. The structure is used:

* When checking an outgoing order by the :ref:`account script <03_ride-language/04_script-types:Account Script>` or the verifier function of the :ref:`dApp script <03_ride-language/04_script-types:dApp Script>`.
* In the :ref:`InvokeScriptTransaction <03_ride-language/05_structures:InvokeScriptTransaction>` structure.

:strong:`Constructor`

.. code-block:: none

 Order(id: ByteVector, matcherPublicKey: ByteVector, assetPair: AssetPair, orderType: Buy|Sell, price: Int, amount: Int, timestamp: Int, expiration: Int, matcherFee: Int, matcherFeeAssetId: ByteVector|Unit, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: Order Fields
  :file: ../_static/03_ride-language/tables/186_Order-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

The script below enables buying from a sender's account:

* Only the specified asset.
* Only at a given price.
* Only for DecentralCoins.

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE EXPRESSION #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

 let myAssetId = base58'8LLpj6yQLUu37KUt3rVo1S69j2gWMbgbM6qqgt2ac1Vb'

 match tx {
   case o: Order =>
    let isDecentralChainPriceAsset = !isDefined(o.assetPair.priceAsset)
    let rightPair = (o.assetPair.amountAsset == myAssetId) && isDecentralChainPriceAsset
    sigVerify(o.bodyBytes, o.proofs[0], o.senderPublicKey)
    && rightPair
    && o.price == 500000
    && o.orderType == Buy
   case _ => false
 }

Transfer
--------

Structure of a single transfer within the :ref:`MassTransferTransaction <03_ride-language/05_structures:MassTransferTransaction>` structure.

:strong:`Constructor`

.. code-block:: none

 Transfer(recipient: Address|Alias, amount: Int)

:strong:`Fields`

.. csv-table:: Transfer Fields
  :file: ../_static/03_ride-language/tables/187_Transfer-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Transaction Structures
======================

Tokenization
------------

.. csv-table:: Tokenization
  :file: ../_static/03_ride-language/tables/188_Tokenization.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 5

IssueTransaction
^^^^^^^^^^^^^^^^

Structure of an :ref:`issue transaction <02_decentralchain/03_transaction:Issue Transaction>`.

:strong:`Constructor`

.. code-block:: none

 IssueTransaction(quantity: Int, name: String, description: String, reissuable: Boolean, decimals: Int, script: ByteVector|Unit, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: IssueTransaction Fields
  :file: ../_static/03_ride-language/tables/189_IssueTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

ReissueTransaction
^^^^^^^^^^^^^^^^^^

Structure of a :ref:`reissue transaction <02_decentralchain/03_transaction:Reissue Transaction>`.

:strong:`Constructor`

.. code-block:: none

 ReissueTransaction(quantity: Int, assetId: ByteVector, reissuable: Boolean, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: ReissueTransaction Fields
  :file: ../_static/03_ride-language/tables/190_ReissueTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

BurnTransaction
^^^^^^^^^^^^^^^

Structure of an :ref:`burn transaction <02_decentralchain/03_transaction:Burn Transaction>`.

:strong:`Constructor`

.. code-block:: none

 BurnTransaction(quantity: Int, assetId: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: BurnTransaction Fields
  :file: ../_static/03_ride-language/tables/191_BurnTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

SetAssetScriptTransaction
^^^^^^^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`set asset script transaction <02_decentralchain/03_transaction:Set Asset Script Transaction>`.

:strong:`Constructor`

.. code-block:: none

 SetAssetScriptTransaction(script: ByteVector|Unit, assetId: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: SetAssetScriptTransaction Fields
  :file: ../_static/03_ride-language/tables/192_SetAssetScriptTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

UpdateAssetInfoTransaction
^^^^^^^^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`update asset info transaction <02_decentralchain/03_transaction:Update Asset Info Transaction>`.

:strong:`Constructor`

.. code-block:: none

 UpdateAssetInfoTransaction(name: String, assetId: ByteVector, description: String, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: UpdateAssetInfoTransaction Fields
  :file: ../_static/03_ride-language/tables/193_UpdateAssetInfoTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Usage
-----

.. csv-table:: Usage
  :file: ../_static/03_ride-language/tables/194_Usage.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 5

TransferTransaction
^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`transfer transaction <02_decentralchain/03_transaction:Transfer Transaction>`.

:strong:`Constructor`

.. code-block:: none

 TransferTransaction(feeAssetId: ByteVector|Unit, amount: Int, assetId: ByteVector|Unit, recipient: Address|Alias, attachment: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: TransferTransaction Fields
  :file: ../_static/03_ride-language/tables/195_TransferTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

ExchangeTransaction
^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`exchange transaction <02_decentralchain/03_transaction:Exchange Transaction>`.

:strong:`Constructor`

.. code-block:: none

 ExchangeTransaction(buyOrder: Order, sellOrder: Order, price: Int, amount: Int, buyMatcherFee: Int, sellMatcherFee: Int, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: ExchangeTransaction Fields
  :file: ../_static/03_ride-language/tables/196_ExchangeTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

CreateAliasTransaction
^^^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`create alias transaction <02_decentralchain/03_transaction:Create Alias Transaction>`.

:strong:`Constructor`

.. code-block:: none

 CreateAliasTransaction(alias: String, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: CreateAliasTransaction Fields
  :file: ../_static/03_ride-language/tables/197_CreateAliasTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

MassTransferTransaction
^^^^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`mass transfer transaction <02_decentralchain/03_transaction:Mass Transfer Transaction>`.

:strong:`Constructor`

.. code-block:: none

 MassTransferTransaction(assetId: ByteVector|Unit, totalAmount: Int, transfers: List[Transfer], transferCount: Int, attachment: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: MassTransferTransaction Fields
  :file: ../_static/03_ride-language/tables/198_MassTransferTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

DataTransaction
^^^^^^^^^^^^^^^

Structure of a :ref:`data transaction <02_decentralchain/03_transaction:Data Transaction>`.

:strong:`Constructor`

.. code-block:: none

 DataTransaction(data: List[BinaryEntry|BooleanEntry|DeleteEntry|IntegerEntry|StringEntry], id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: DataTransaction Fields
  :file: ../_static/03_ride-language/tables/199_DataTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

SetScriptTransaction
^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`set script transaction <02_decentralchain/03_transaction:Set Script Transaction>`.

:strong:`Constructor`

.. code-block:: none

 SetScriptTransaction(script: ByteVector|Unit, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: SetScriptTransaction Fields
  :file: ../_static/03_ride-language/tables/200_SetScriptTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

InvokeScriptTransaction
^^^^^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`invoke script transaction <02_decentralchain/03_transaction:Invoke Script Transaction>`.

:strong:`Constructor`

.. code-block:: none

 InvokeScriptTransaction(dApp: Address|Alias, payments: List[AttachedPayments], feeAssetId: ByteVector|Unit, function: String, args: List[Boolean|ByteVector|Int|String|List[Boolean|ByteVector|Int|String]], id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: InvokeScriptTransaction Fields
  :file: ../_static/03_ride-language/tables/201_InvokeScriptTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Network
-------

.. csv-table:: Network
  :file: ../_static/03_ride-language/tables/202_Network.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 5

LeaseTransaction
^^^^^^^^^^^^^^^^

Structure of a :ref:`lease transaction <02_decentralchain/03_transaction:Lease Transaction>`.

:strong:`Constructor`

.. code-block:: none

 LeaseTransaction(amount: Int, recipient: Address|Alias, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: LeaseTransaction Fields
  :file: ../_static/03_ride-language/tables/203_LeaseTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

LeaseCancelTransaction
^^^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`lease cancel transaction <02_decentralchain/03_transaction:Lease Cancel Transaction>`.

:strong:`Constructor`

.. code-block:: none

 LeaseCancelTransaction(leaseId: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: LeaseCancelTransaction Fields
  :file: ../_static/03_ride-language/tables/204_LeaseCancelTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

SponsorFeeTransaction
^^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`sponsor fee transaction <02_decentralchain/03_transaction:Sponsor Fee Transaction>`.

:strong:`Constructor`

.. code-block:: none

 SponsorFeeTransaction(assetId: ByteVector, minSponsoredAssetFee: Int|Unit, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: SponsorFeeTransaction Fields
  :file: ../_static/03_ride-language/tables/205_SponsorFeeTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Genesis
-------

.. csv-table:: Genesis
  :file: ../_static/03_ride-language/tables/206_Genesis.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 5

GenesisTransaction
^^^^^^^^^^^^^^^^^^

Structure of a :ref:`genesis transaction <02_decentralchain/03_transaction:Genesis Transaction>`.

:strong:`Constructor`

.. code-block:: none

 GenesisTransaction(amount: Int, recipient: Address|Alias, id: ByteVector, fee: Int, timestamp: Int, version: Int)

:strong:`Fields`

.. csv-table:: GenesisTransaction Fields
  :file: ../_static/03_ride-language/tables/207_GenesisTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5