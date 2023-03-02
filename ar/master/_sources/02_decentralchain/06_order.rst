*****
Order
*****

Order is the instruction from the :ref:`account <02_decentralchain/01_account:Account>` to matcher to buy or sell a :ref:`token <02_decentralchain/02_token(asset):Token (Asset)>` on the exchange. 

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
  :file: ../_static/02_decentralchain/tables/023_Asset-Pair-Fields.csv 
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

Order's Amount and Price
========================

In the user interface, the amount and price are usually presented as values with a fractional part (for example, :math:`0.74585728` DecentralCoins), i.e. in the denormalized form. The denormalized form is convenient for humans, but not for calculations. To solve the problem of calculation accuracy, the normalization is performed.

In the user interface, the amount and price are usually presented as values with a fractional part (for example, :math:`0.74585728` :ref:`DecentralCoins <02_decentralchain/02_token(asset):DecentralCoin>`), i.e. in the denormalized form. The denormalized form is convenient for humans, but not for calculations. To solve the problem of calculation accuracy, the normalization is performed, i.e. amount and price are represented as an integer. So, :math:`0.74585728` DecentralCoins is :math:`0.74585728 × 10^{8}` or :math:`74585728` Decentralites. In this case, the exponent is :math:`8`, because DecentralCoins has :math:`8` decimals after the decimal point. Other assets may have different amount of decimals. For example, TDX has 2 decimals.

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

See the :ref:`order binary format <02_decentralchain/10_binary-format:Order Binary Format>` page.
