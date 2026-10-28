..
   The price-oracle example includes docs/_samples/oracle-publish.ts (typechecked
   in CI) and docs/_samples/ride/oracle-consumer.ride (compiled by
   docs/scripts/check_ride_samples.py). Both were run on the public Testnet on
   2026-10-27. The token verification format is @decentralchain/oracle-data's
   (packages/sdk/oracle-data/src/constants.ts in the DecentralChain monorepo).

******
Oracle
******

Oracle is a data provider from the outside world on the blockchain.

Sources of the Outside World
============================

Software oracles handle data accessible on the web. For example, the temperature, costs of products and merchandise, flight or train delays, etc. The information originates from online sources, e.g. API. The oracle extracts the required data and pushes it into the blockchain.

Hardware oracles track real-world objects with devices and sensors. For example, a video camera with an analytics function virtual line crossing tracks vehicles entering a specific zone. If an event is detected, the oracle writes about it on the blockchain. Based on the data of such oracle, some script of decentralized application on the blockchain may be triggered. In this case, for example, a fine and the write-off of tokens from the account of the vehicle owner. But it is not in oracle scope, it is in the scope of the script that is based on the data of such an oracle.

Human oracles imply that the data is entered by a human being.

Oracles Issue
=============

The oracle is a way of connecting the blockchain with the outside world. The major problem that is solved by the usage of oracles is the very point that blockchains can only access data that is stored on the blockchain. Here, in blockchain, the point is that it is important that decentralized applications can only access data that is stored on the blockchain so that every execution of the script leads to the same result at a given point in time. Therefore, decentralized applications are not able to access data from outside the blockchain, e.g., provided by web services or other external sources of data. Nevertheless, many interesting applications need access to the outside world, e.g., decentralized applications for insurances, decentralized betting systems, financial services and so forth.

Here, the solution is quite straightforward: if external data is necessary for the execution of a decentralized application, this data needs to be stored on the blockchain. To achieve this, there are usually small programs implemented that access the necessary data and write it to the blockchain. Those little programs are called oracles.

How an Oracle Works on DecentralChain
=====================================

On DecentralChain an oracle is an ordinary :ref:`account <02_decentralchain/01_account:Account>`. It publishes data by sending :ref:`Data transactions <02_decentralchain/03_transaction:Data Transaction>`, which write key-value entries into its :ref:`account data storage <02_decentralchain/01_account:Account Data Storage>`. A later Data transaction with the same key overwrites the entry, so each key always holds the oracle's latest value.

Anyone can read the entries:

* **Off-chain**, from any node: ``GET /addresses/data/{oracleAddress}`` returns every entry, ``?key=price_DCC_USD`` one or more entries by key, and ``GET /addresses/data/{oracleAddress}/{key}`` a single entry.
* **On-chain**, from a Ride script: ``getInteger(oracleAddress, key)``, ``getString``, ``getBoolean`` and ``getBinary`` return the value or ``unit`` when there is none, and the ``...Value`` variants (``getIntegerValue`` and so on) fail the script instead.

A script reads the state as of the block it runs in, so every node that validates the transaction gets the same value and the same result.

Data Format
===========

Each entry has a key and a typed value: ``integer`` (64-bit signed), ``boolean``, ``string`` (UTF-8) or ``binary`` (base64 in JSON). One Data transaction carries up to :math:`100` entries; a key is at most :math:`400` bytes and a value at most :math:`32,767` bytes. The fee is :math:`0.001` DCC per started kilobyte of data.

Ride has no floating-point numbers, so publish numbers as integers with a fixed scale that every reader knows, for example 8 decimal places: :math:`2.50` becomes ``250000000``. Publish the time of each observation too, so a script can refuse a value that is too old. Choose key names that say what the value is and in which unit, and don't change the meaning of a key once scripts depend on it: publish a new key instead.

Example: A Price Oracle
=======================

This script publishes a DCC/USD price and the time it was observed. A real oracle would run it on a schedule with a price from an exchange API:

.. literalinclude:: ../_samples/oracle-publish.ts
  :language: typescript
  :lines: 2-

The entries it wrote on the Testnet (transaction ``AntBkfvR2TZBfhvoEBXhTi81BSfkhnFzqfUZ5VruUG6v``)::

  [{"key": "price_DCC_USD", "type": "integer", "value": 250000000},
   {"key": "price_DCC_USD_timestamp", "type": "integer", "value": 1793150813445}]

This dApp sells a 10 USD voucher for DCC at the oracle's price, and refuses a price older than one hour:

.. literalinclude:: ../_samples/ride/oracle-consumer.ride
  :language: none
  :lines: 2-

On the Testnet, with a price of 2.50 USD, a ``buyVoucher`` call paying 1 DCC failed with ``Pay at least 400000000 Decentralites`` and a call paying 4 DCC succeeded (transaction ``B7nXy9ohWaHi4NyCjEPTdZWrpT9G6utWGaHgaRfNQmp4``). To deploy the dApp, see :doc:`Creating and Launching a dApp <../04_building-apps/08_creating-and-launching-a-dapp>`.

Token Verification Oracle
=========================

Wallets and explorers use an oracle to show which tokens are verified and to show their ticker, logo and description. The format is the one ``@decentralchain/oracle-data`` parses and writes. The oracle account describes itself with these entries:

.. list-table::
  :header-rows: 1
  :widths: 2 1 4

  * - Key
    - Type
    - Value
  * - ``data_provider_name``, ``data_provider_link``, ``data_provider_email``
    - string
    - Who runs the oracle
  * - ``data_provider_version``
    - integer
    - Format version, ``0``
  * - ``data_provider_lang_list``
    - string
    - Languages of the descriptions, comma-separated, for example ``en,es``
  * - ``data_provider_description_<en>``
    - string
    - The oracle's description in each language, with the language code in angle brackets

For each token it describes, it writes entries whose key ends in the token ID in angle brackets: ``status_<ASSET_ID>`` and ``version_<ASSET_ID>`` (integers), and ``ticker_``, ``link_``, ``email_``, ``logo_`` (a data URI) and ``description_<LANG>_`` strings. ``status`` is ``2`` verified, ``1`` detailed, ``0`` not verified, ``-1`` suspicious or ``-2`` scam. A verified or detailed token must have every field; the others need only the version and the status.

The Mainnet oracle that Decentral.Exchange uses is ``3DUM611HQFwQcCQDQnA5W92Xs219smEHaaP``. Its entries for CR Coin include::

  {"key": "status_<G9TVbwiiUZd5WxFxoY7Tb6ZPjGGLfynJK4a3aoC59cMo>", "type": "integer", "value": 2}
  {"key": "ticker_<G9TVbwiiUZd5WxFxoY7Tb6ZPjGGLfynJK4a3aoC59cMo>", "type": "string", "value": "CRC"}
  {"key": "link_<G9TVbwiiUZd5WxFxoY7Tb6ZPjGGLfynJK4a3aoC59cMo>", "type": "string", "value": "https://crcoin.io"}

``getProviderData`` and ``getProviderAssets`` in ``@decentralchain/oracle-data`` turn the entries back into objects, and ``getFields`` builds the entries for a Data transaction.

Consensus of Oracles
====================

One source may be unsafe if it does not have the authority or high rating. However, several oracles can be used to stay away from the monopoly and be safer. For example, get information from ten oracles and only if the data of :math:`6` out of :math:`10` oracles coincide, to accept them. This is the consensus of the oracles.

A dApp can apply this directly: read the same key from several oracle addresses, ignore the values that are missing or stale, and use the median of the rest. Whoever controls an oracle account controls what it publishes, so a dApp that trusts a single oracle trusts that account's owner.
