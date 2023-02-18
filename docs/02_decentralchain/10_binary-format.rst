*************
Binary Format
*************

* :ref:`Address binary format <02_decentralchain/10_binary-format:Address Binary Format>`
* :ref:`Alias binary format <02_decentralchain/10_binary-format:Alias Binary Format>`
* :ref:`Block binary format <02_decentralchain/10_binary-format:Block Binary Format>`
* :ref:`Network message binary format <02_decentralchain/10_binary-format:Network Message Binary Format>`

  * :ref:`Block message binary format <02_decentralchain/10_binary-format:Block Message Binary Format>`
  * :ref:`Checkpoint message binary format <02_decentralchain/10_binary-format:Checkpoint Message Binary Format>`
  * :ref:`Get block message binary format <02_decentralchain/10_binary-format:Get Block Message Binary Format>`
  * :ref:`Get peers message binary format <02_decentralchain/10_binary-format:Get Peers Message Binary Format>`
  * :ref:`Get signatures message binary format <02_decentralchain/10_binary-format:Get Signatures Message Binary Format>`
  * :ref:`Handshake message binary format <02_decentralchain/10_binary-format:Handshake Message Binary Format>`
  * :ref:`Peers message binary format <02_decentralchain/10_binary-format:Peers Message Binary Format>`
  * :ref:`Score message binary format <02_decentralchain/10_binary-format:Score Message Binary Format>`
  * :ref:`Signatures message binary format <02_decentralchain/10_binary-format:Signatures Message Binary Format>`
  * :ref:`Transaction message binary format <02_decentralchain/10_binary-format:Transaction Message Binary Format>`

* :ref:`Order binary format <02_decentralchain/10_binary-format:Order Binary Format>`
* :ref:`Transaction binary format <02_decentralchain/10_binary-format:Transaction Binary Format>`

  * :ref:`Burn transaction binary format <02_decentralchain/10_binary-format:Burn Transaction Binary Format>`
  * :ref:`Create alias transaction binary format <02_decentralchain/10_binary-format:Create Alias Transaction Binary Format>`
  * :ref:`Data transaction binary format <02_decentralchain/10_binary-format:Data Transaction Binary Format>`
  * :ref:`Exchange transaction binary format <02_decentralchain/10_binary-format:Exchange Transaction Binary Format>`
  * :ref:`Genesis transaction binary format <02_decentralchain/10_binary-format:Genesis Transaction Binary Format>`
  * :ref:`Invoke script transaction binary format <02_decentralchain/10_binary-format:Invoke Script Transaction Binary Format>`
  * :ref:`Issue transaction binary format <02_decentralchain/10_binary-format:Issue Transaction Binary Format>`
  * :ref:`Lease cancel transaction binary format <02_decentralchain/10_binary-format:Lease Cancel Transaction Binary Format>`
  * :ref:`Lease transaction binary format <02_decentralchain/10_binary-format:Lease Transaction Binary Format>`
  * :ref:`Mass transfer transaction binary format <02_decentralchain/10_binary-format:Mass Transfer Transaction Binary Format>`
  * :ref:`Reissue transaction binary format <02_decentralchain/10_binary-format:Reissue Transaction Binary Format>`
  * :ref:`Set asset script transaction binary format <02_decentralchain/10_binary-format:Set Asset Script Transaction Binary Format>`
  * :ref:`Set script transaction binary format <02_decentralchain/10_binary-format:Set Script Transaction Binary Format>`
  * :ref:`Sponsor fee transaction binary format <02_decentralchain/10_binary-format:Sponsor Fee Transaction Binary Format>`
  * :ref:`Transfer transaction binary format <02_decentralchain/10_binary-format:Transfer Transaction Binary Format>`

* :ref:`Transaction proofs binary format <02_decentralchain/10_binary-format:Transaction Proofs Binary Format>`

Address Binary Format
=====================

Learn more about :ref:`address <02_decentralchain/01_account:Address>`.

.. csv-table:: Address Binary Format
  :file: ../_static/02_decentralchain/tables/035_Address-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 1 4

Alias Binary Format
===================

Learn more about :ref:`alias <02_decentralchain/01_account:Alias>`.

.. csv-table:: Alias Binary Format
  :file: ../_static/02_decentralchain/tables/036_Alias-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 2 4

Block Binary Format
===================

Learn more about :ref:`block <02_decentralchain/04_block:Block>`.

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
  :file: ../_static/02_decentralchain/tables/037_Block-Binary-Format-V5.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

:strong:`Version 4`

.. csv-table:: Block Binary Format Version 4
  :file: ../_static/02_decentralchain/tables/038_Block-Binary-Format-V4.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 2 2

:strong:`Version 3`

.. csv-table:: Block Binary Format Version 3
  :file: ../_static/02_decentralchain/tables/039_Block-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 2 2

Network Message Binary Format	
=============================

* :ref:`Block message binary format <02_decentralchain/10_binary-format:Block Message Binary Format>`
* :ref:`Checkpoint message binary format <02_decentralchain/10_binary-format:Checkpoint Message Binary Format>`
* :ref:`Get block message binary format <02_decentralchain/10_binary-format:Get Block Message Binary Format>`
* :ref:`Get peers message binary format <02_decentralchain/10_binary-format:Get Peers Message Binary Format>`
* :ref:`Get signatures message binary format <02_decentralchain/10_binary-format:Get Signatures Message Binary Format>`
* :ref:`Handshake message binary format <02_decentralchain/10_binary-format:Handshake Message Binary Format>`
* :ref:`Peers message binary format <02_decentralchain/10_binary-format:Peers Message Binary Format>`
* :ref:`Score message binary format <02_decentralchain/10_binary-format:Score Message Binary Format>`
* :ref:`Signatures message binary format <02_decentralchain/10_binary-format:Signatures Message Binary Format>`
* :ref:`Transaction message binary format <02_decentralchain/10_binary-format:Transaction Message Binary Format>`

Block Message Binary Format
---------------------------

Block message is a reply to GetBlock message.

.. csv-table:: Block Message Binary Format
  :file: ../_static/02_decentralchain/tables/040_Block-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Checkpoint Message Binary Format
--------------------------------

.. csv-table:: Checkpoint Message Binary Format
  :file: ../_static/02_decentralchain/tables/041_Checkpoint-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Get Block Message Binary Format
-------------------------------

.. csv-table:: Get Block Message Binary Format
  :file: ../_static/02_decentralchain/tables/042_Get-Block-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Get Peers Message Binary Format
-------------------------------

Get peers message is sent when one sending node wants to know about other nodes on the network.

.. csv-table:: Get Peers Message Binary Format
  :file: ../_static/02_decentralchain/tables/043_Get-Peers-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Get Signatures Message Binary Format
------------------------------------

.. csv-table:: Get Signatures Message Binary Format
  :file: ../_static/02_decentralchain/tables/044_Get-Signatures-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Handshake Message Binary Format
-------------------------------

Handshake is used to start communication between two nodes.

.. csv-table:: Handshake Message Binary Format
  :file: ../_static/02_decentralchain/tables/045_Handshake-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 1 1

Peers Message Binary Format
---------------------------

Peers message is a response to get peers message.

.. csv-table:: Peers Message Binary Format
  :file: ../_static/02_decentralchain/tables/046_Peers-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Score Message Binary Format
---------------------------

.. csv-table:: Score Message Binary Format
  :file: ../_static/02_decentralchain/tables/047_Score-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Signatures Message Binary Format
--------------------------------

.. csv-table:: Signatures Message Binary Format
  :file: ../_static/02_decentralchain/tables/048_Signatures-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Transaction Message Binary Format
---------------------------------

.. csv-table:: Transaction Message Binary Format
  :file: ../_static/02_decentralchain/tables/049_Transaction-Message-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1

Order Binary Format
===================

Learn more about :ref:`order <02_decentralchain/06_order:Order>`.

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
  :file: ../_static/02_decentralchain/tables/050_Order-Binary-Format-V4.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 4

:strong:`Version 3`

.. csv-table:: Order Binary Format Version 3
  :file: ../_static/02_decentralchain/tables/051_Order-Binary-Format-V3.csv 
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
  :file: ../_static/02_decentralchain/tables/052_Order-Binary-Format-V2.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 3 2

:strong:`Version 1`

.. csv-table:: Order Binary Format Version 1
  :file: ../_static/02_decentralchain/tables/053_Order-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 3 2

The price listed for amount asset in price asset :math:`* 10^8`. Expiration is order time to live, timestamp in future, max :math:`= 30` days in future. The signature is calculated from the following bytes:

.. csv-table:: Order Binary Format Version 1 Bytes
  :file: ../_static/02_decentralchain/tables/054_Order-Binary-Format-V1-Bytes.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 3 2

Transaction Binary Format
=========================

Learn more about :ref:`transaction <02_decentralchain/03_transaction:Transaction>`.

Transactions are stored on the blockchain in a binary format (byte representation). :ref:`Node extensions <documentation:placeholder>` such as :ref:`gRPC server <documentation:placeholder>` can work directly with data in binary format.
The transaction signature and ID are also formed on the basis of the binary format, namely the transaction body bytes. The contents of transaction body bytes is given in the description of the binary format of each type and version of the transaction. Normally the transaction body bytes include all transaction fields, with the exception of the following fields:

* Transaction ID (it is not stored on the blockchain),
* Version flag,
* Proofs or signature, depending on the version of the transaction.

The guideline for generating a signature and ID is given in the :ref:`cryptographic practical details <02_decentralchain/09_protocol:Cryptographic Practical Details>` article. All strings are UTF-8 encoded.

Protobuf
--------

Protobuf facilitates the development of client libraries for the DecentralChain blockchain, as it avoids serialization errors and streamlines the creation of a correctly signed transaction. How to generate a transaction signature using protobuf:

* Download the `protocol buffers package <https://github.com/protocolbuffers/protobuf/releases/>`_ for your programming language. Generate the Transaction class on the basis of transaction.proto.
* Fill in the transaction fields.

   * Asset IDs should be specified in the binary format.
   * Addresses should be specified in the shortened binary format (without the first two and the last four bytes). See the :ref:`address binary format <02_decentralchain/10_binary-format:Address Binary Format>`) article.

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
  :file: ../_static/02_decentralchain/tables/055_Transaction-Binary-Format.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 3

The fields that depend on the type of transaction are described in the following articles:

* :ref:`Burn transaction binary format <02_decentralchain/10_binary-format:Burn Transaction Binary Format>`
* :ref:`Create alias transaction binary format <02_decentralchain/10_binary-format:Create Alias Transaction Binary Format>`
* :ref:`Data transaction binary format <02_decentralchain/10_binary-format:Data Transaction Binary Format>`
* :ref:`Exchange transaction binary format <02_decentralchain/10_binary-format:Exchange Transaction Binary Format>`
* :ref:`Genesis transaction binary format <02_decentralchain/10_binary-format:Genesis Transaction Binary Format>`
* :ref:`Invoke script transaction binary format <02_decentralchain/10_binary-format:Invoke Script Transaction Binary Format>`
* :ref:`Issue transaction binary format <02_decentralchain/10_binary-format:Issue Transaction Binary Format>`
* :ref:`Lease cancel transaction binary format <02_decentralchain/10_binary-format:Lease Cancel Transaction Binary Format>`
* :ref:`Lease transaction binary format <02_decentralchain/10_binary-format:Lease Transaction Binary Format>`
* :ref:`Mass transfer transaction binary format <02_decentralchain/10_binary-format:Mass Transfer Transaction Binary Format>`
* :ref:`Reissue transaction binary format <02_decentralchain/10_binary-format:Reissue Transaction Binary Format>`
* :ref:`Set asset script transaction binary format <02_decentralchain/10_binary-format:Set Asset Script Transaction Binary Format>`
* :ref:`Set script transaction binary format <02_decentralchain/10_binary-format:Set Script Transaction Binary Format>`
* :ref:`Sponsor fee transaction binary format <02_decentralchain/10_binary-format:Sponsor Fee Transaction Binary Format>`
* :ref:`Transfer transaction binary format <02_decentralchain/10_binary-format:Transfer Transaction Binary Format>`
* :ref:`Update asset info transaction binary format <02_decentralchain/10_binary-format:Update Asset Info Transaction Binary Format>`

Burn Transaction Binary Format
------------------------------

Learn more about :ref:`burn transaction <02_decentralchain/03_transaction:Burn Transaction>`.

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
  :file: ../_static/02_decentralchain/tables/056_Burn-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 2 1 3

:strong:`Version 2`

.. csv-table:: Burn Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/057_Burn-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/058_Burn-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 1 1

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5` and :math:`6` are the transaction body bytes.

Create Alias Transaction Binary Format
--------------------------------------

Learn more about :ref:`create alias transaction <02_decentralchain/03_transaction:Create Alias Transaction>`.

:strong:`Version 3`

.. code-block:: none

  message CreateAliasTransactionData {
    string alias = 1;
  };

.. csv-table:: Create Alias Transaction Binary Format Version 3
  :file: ../_static/02_decentralchain/tables/059_Create-Alias-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1

:strong:`Version 2`

.. csv-table:: Create Alias Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/060_Create-Alias-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/061_Create-Alias-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 2 2

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5` and :math:`6` are the transaction body bytes.

Data Transaction Binary Format
------------------------------

Learn more about :ref:`data transaction <02_decentralchain/03_transaction:Data Transaction>`.

:strong:`Version 2`

.. csv-table:: Data Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/062_Data-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/063_Data-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6.1`, :math:`6.2`, :math:`6.3`, :math:`6.4`, :math:`6.5`, :math:`6.6`, :math:`6.7`, :math:`6.8`, :math:`6.9`, :math:`6.10`, :math:`6.[5 × N - 4]`, :math:`6.[5 × N - 3]`, :math:`6.[5 × N - 2]`, :math:`6.[5 × N - 1]`, :math:`6.[5 × N]`, :math:`7` and :math:`8` are the transaction body bytes. The maximum number of records is :math:`100`. The maximum size of transaction body bytes is  :math:`153,600` bytes.

Exchange Transaction Binary Format
----------------------------------

Learn more about :ref:`exchange transaction <02_decentralchain/03_transaction:Exchange Transaction>`.

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
  :file: ../_static/02_decentralchain/tables/064_Exchange-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

:strong:`Version 2`

Transaction version 2 can accept orders of version 1, 2 and 3.

.. csv-table:: Exchange Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/065_Exchange-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/066_Exchange-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 3

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8`, :math:`9`, :math:`10` and :math:`11` are the transaction body bytes. 

Genesis Transaction Binary Format
---------------------------------

Learn more about :ref:`genesis transaction <02_decentralchain/03_transaction:Genesis Transaction>`.

.. csv-table:: Genesis Transaction Binary Format
  :file: ../_static/02_decentralchain/tables/067_Genesis-Transaction-Binary-Format.csv 
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
---------------------------------------

Learn more about :ref:`invoke script transaction <02_decentralchain/03_transaction:Invoke Script Transaction>`.

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
  :file: ../_static/02_decentralchain/tables/068_Invoke-Script-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/069_Invoke-Script-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3

The maximum number of payments is :math:`10`.  The maximum size of transaction including proofs is :math:`5120` bytes.

Issue Transaction Binary Format
-------------------------------

Learn more about :ref:`issue transaction <02_decentralchain/03_transaction:Issue Transaction>`.

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
  :file: ../_static/02_decentralchain/tables/070_Issue-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

:strong:`Version 2`

.. csv-table:: Issue Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/071_Issue-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/072_Issue-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1 1

The fields :math:`3`, :math:`4`, :math:`5.1`, :math:`5.2`, :math:`6.1`, :math:`6.2`, :math:`7`, :math:`8`, :math:`9`, :math:`10` and :math:`11` are the transaction body bytes. 

Lease Cancel Transaction Binary Format
--------------------------------------

Learn more about :ref:`lease cancel transaction <02_decentralchain/03_transaction:Lease Cancel Transaction>`

:strong:`Version 3`

.. code-block:: none

  message LeaseCancelTransactionData {
    bytes lease_id = 1;
  };
 
.. csv-table:: Lease Cancel Transaction Binary Format Version 3
  :file: ../_static/02_decentralchain/tables/073_Lease-Cancel-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1

:strong:`Version 2`

.. csv-table:: Lease Cancel Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/074_Lease-Cancel-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/075_Lease-Cancel-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 1 1 2

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, and :math:`5` are the transaction body bytes. 

Lease Transaction Binary Format
-------------------------------

Learn more about :ref:`lease transaction <02_decentralchain/03_transaction:Lease Transaction>`.

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
  :file: ../_static/02_decentralchain/tables/076_Lease-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

:strong:`Version 2`

.. csv-table:: Lease Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/077_Lease-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/078_Lease-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 1 3 

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4`, :math:`5` and :math:`6` are the transaction body bytes. 

Mass Transfer Transaction Binary Format
---------------------------------------

Learn more about :ref:`mass transfer transaction <02_decentralchain/03_transaction:Mass Transfer Transaction>`.

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
  :file: ../_static/02_decentralchain/tables/079_Mass-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/080_Mass-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3 

The fields :math:`1`, :math:`2`, :math:`3`, :math:`4.1`, :math:`4.2`, :math:`5.1`, :math:`5.2`, :math:`5.3`, :math:`5.4`, :math:`5.5`, :math:`5.[2 × N]`, :math:`5.[2 × N + 1]`, :math:`6`, :math:`7`, :math:`8.1` and :math:`8.2` are the transaction body bytes. 

Reissue Transaction Binary Format
---------------------------------

Learn more about :ref:`reissue transaction <02_decentralchain/03_transaction:Reissue Transaction>`.

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
  :file: ../_static/02_decentralchain/tables/081_Reissue-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3

:strong:`Version 2`

.. csv-table:: Reissue Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/082_Reissue-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/083_Reissue-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 1 3 

The fields :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8` and :math:`9` are the transaction body bytes. 

Set Asset Script Transaction Binary Format
------------------------------------------

Learn more about :ref:`set asset script transaction <02_decentralchain/03_transaction:Set Asset Script Transaction>`.

:strong:`Version 2`

.. code-block:: none

  message SetAssetScriptTransactionData {
    bytes asset_id = 1;
    bytes script = 2;
  };

.. csv-table:: Set Asset Script Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/084_Set-Asset-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/085_Set-Asset-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 1 1 1 3

The fields :math:`2`, :math:`3`, :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8`, :math:`9.1`, :math:`9.2` and :math:`9.3` are the transaction body bytes. 

Set Script Transaction Binary Format
------------------------------------

Learn more about :ref:`set script transaction <02_decentralchain/03_transaction:Set Script Transaction>`.

:strong:`Version 2`

.. code-block:: none

  message SetScriptTransactionData {
    bytes script = 1;
  };
 
.. csv-table:: Set Script Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/086_Set-Script-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/087_Set-Script-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3 

Sponsor Fee Transaction Binary Format
-------------------------------------

Learn more about :ref:`sponsor fee transaction <02_decentralchain/03_transaction:Sponsor Fee Transaction>`.

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
  :file: ../_static/02_decentralchain/tables/088_Sponsor-Fee-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/089_Sponsor-Fee-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 1 3 

The fields :math:`4`, :math:`5`, :math:`6`, :math:`7`, :math:`8`, :math:`9` and :math:`10` are the transaction body bytes. 

Transfer Transaction Binary Format
----------------------------------

Learn more about :ref:`transfer transaction <02_decentralchain/03_transaction:Transfer Transaction>`.

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
  :file: ../_static/02_decentralchain/tables/090_Transfer-Transaction-Binary-Format-V3.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 3 

:strong:`Version 2`

.. csv-table:: Transfer Transaction Binary Format Version 2
  :file: ../_static/02_decentralchain/tables/091_Transfer-Transaction-Binary-Format-V2.csv 
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
  :file: ../_static/02_decentralchain/tables/092_Transfer-Transaction-Binary-Format-V1.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 1 1 1 3 

Update Asset Info Transaction Binary Format
-------------------------------------------

Learn more about :ref:`update asset info transaction <02_decentralchain/03_transaction:Update Asset Info Transaction>`.

:strong:`Version 1`

.. code-block:: none

  message UpdateAssetInfoTransactionData {
    bytes asset_id = 1;
    string name = 2;
    string description = 3;
  }

.. csv-table:: Update Asset Info Transaction Binary Format Version 1
 :file: ../_static/02_decentralchain/tables/093_Update-Asset-Info-Transaction-Binary-Format-V1.csv
 :header-rows: 1 
 :class: longtable
 :widths: 1 1 1

Transaction Proofs Binary Format
================================

.. csv-table:: Transaction Proofs Binary Format
 :file: ../_static/02_decentralchain/tables/094_Transaction-Proofs-Binary-Format.csv
 :header-rows: 1 
 :class: longtable
 :widths: 1 3 3 1 3

The maximum number of proofs is :math:`8`.
