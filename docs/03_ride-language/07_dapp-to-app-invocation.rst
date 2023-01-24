**********************
dApp-to-App Invocation
**********************

A dApp callable function can invoke a callable function of another dApp, or another callable function of the same dApp, or even itself. The invocation is synchronous. The invoked function returns a value that the invoking function can use.

dApp-to-dApp invocation is processed as follows:

* A user sends an Invoke Script transaction that invokes the callable function :math:`1`.
* The callable function :math:`1` invokes the callable function :math:`2` via a :ref:`strict variable <03_ride-language/07_dapp-to-app-invocation:Strict Variable>` initialized by the :ref:`invoke or reentrantInvoke <03_ride-language/07_dapp-to-app-invocation:dApp-to-App Invocation>` function.
* The callable function :math:`2` is executed; the script actions and return value are calculated.
* The :ref:`return value <03_ride-language/07_dapp-to-app-invocation:Callable Function Result>` is assigned to the strict variable. The subsequent operations of callable function 1 are executed, taking into account script actions of callable function :math:`2` (as if the actions were applied to the blockchain state).
* Finally, the script actions of callable functions :math:`2` and :math:`1` are applied to the blockchain state.
  
Features
========

* dApp-to-dApp invocations can be nested.
* All invoked callable functions are executed within a single Invoke Script transaction.
* A dApp-to-dApp invocation can contain payments that are transferred from the balance of the parent dApp to the balance of the invoked dApp.
* Payments attached to a callable function invocation can be used in script actions and in payments attached to nested invocations.

Conditions
==========

* Both the parent and invoked dApp scripts use standard library version 5.
* If the dApp invokes itself, the invocation must not contain payments.
* The number of the :ref:`invoke or reentrantInvoke <03_ride-language/07_dapp-to-app-invocation:dApp-to-App Invocation>` function calls is up to 100 within a single Invoke Script transaction.
* The maximum total number of Issue, Reissue, Burn, SponsorFee, ScriptTransfer, Lease, LeaseCancel script actions executed by all callable functions in a single transaction is :math:`30`.
* The maximum total number of BinaryEntry, BooleanEntry, IntegerEntry, StringEntry, DeleteEntry script actions executed by all callable functions in a single transaction is :math:`100`.
* The total complexity is limited by :math:`26,000` for all callable functions and asset scripts of involved smart assets. The sender's account script complexity is not included in that limit.

Strict Variable
===============

strict keyword defines a variable with eager evaluation. Unlike lazy variables defined with let, a strict variable is evaluated immediately when script execution reaches it, that is, before the next expression.

Invoke and reentrantInvoke Functions
====================================

.. code-block:: none

 invoke(dApp: Address|Alias, function: String, arguments: List[Any], payments: List[AttachedPayments]): Any
 reentrantInvoke(dApp: Address|Alias, function: String, arguments: List[Any], payments: List[AttachedPayments]): Any

:strong:`Parameters:`

.. csv-table:: Invoke and ReentrantInvoke Functions
  :file: ../_static/03_ride-language/tables/209_Invoke-and-ReentrantInvoke-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 5

.. code-block:: none

 strict z = invoke(dapp,foo,args,[AttachedPayment(unit,100000000)])

The return value is of type Any, which means any valid type. You can extract a particular type from it using as[T] and exactAs[T] macros or the match ... case operator, see the :ref:`any <03_ride-language/02_data-types:Any>` article.

The invoke and reentrantInvoke functions differ only in the reentrancy restriction. For details, see the :ref:`dApp-to-dApp invocation function <03_ride-language/03_functions:dApp-to-dApp Invocation Functions>` article.

Invocation Fields
=================

For dApp-to-dApp invocation, the fields of :ref:`invocation <03_ride-language/05_structures:Invocation>` structure used by the invoked function are filled with the following values:

.. csv-table:: Invocation Fields
  :file: ../_static/03_ride-language/tables/210_Invocation-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Callable Function Result
========================

In standard library version 5, a callable function result is a :ref:`tuple <03_ride-language/02_data-types:Tuple>` of two elements:

* List of script actions.
* Return value that is passed to the invoking function.

Let's see an example:

.. code-block:: none

 (
   [
     ScriptTransfer(i.caller,100,unit)
   ],
   42
 )

In standard library version 4 or 3, there is no return value, so unit is implied.

For details, see the :ref:`callable function <03_ride-language/03_functions:Callable Functions>` article.

Updating Balance and Account Data Storage Entries
=================================================

If the callable function invoked by the invoke or reentrantInvoke function performs script actions, the results of those actions are available to the invoking function:

* If the invoked function adds an entry to the account's data storage, the invoking function can obtain the entry after the invocation.
* If the invoked function deletes an entry from the account's data storage, the invoking function cannot obtain the entry after the invocation.
* If the invoked function performs actions with tokens (transfer, issue/reissue/burn, and others) and the invoking function obtains balances after the invocation, it receives the updated balances.

Transaction Fail
================

If the callable function's execution fails or :ref:`throws an exception <03_ride-language/03_functions:Exception Functions>`, the Invoke Script transaction could be rejected or saved on the blockchain as failed. This depends on whether the complexity of performed computations has exceeded the :ref:`threshold for saving a failed transaction <03_ride-language/07_dapp-to-app-invocation:Limitations>` (currently :math:`1000`). The complexity is summed up for all invocations.

Consider the example: callable function :math:`1` performs computations of 800 complexity, then invokes callable function :math:`2` which performs computations of 300 complexity and then fails. The complexity :math:`800 + 300` has exceeded the threshold, so the transaction is saved as failed, and the sender is charged a fee.

If the total complexity of executed callable functions and asset scripts exceeds the limit of :math:`26,000`, the transaction is saved as failed as well. For example, if the complexity of executed callable functions is :math:`25,000` in total, and there is a smart asset in script action whose script's complexity is :math:`1500`.

In case of failure, no payments and script actions are applied to the blockchain state, even if some of the invoked functions are executed completely. The only state change the failed transaction entails is charging the fee.

Limitations
===========

.. csv-table:: Limitations
  :file: ../_static/03_ride-language/tables/211_Limitations.csv
  :header-rows: 1 
  :class: longtable
  :widths: 6 2

Script Complexity
-----------------

Script complexity is a dimensionless quantity that estimates computational resources needed to execute a script. The complexity of a script is estimated based on complexities of all the operators and functions it consists of. The complexity of the built-in functions is listed in the built-in functions article.

Limitations on script complexity are given in the :ref:`limitations <03_ride-language/07_dapp-to-app-invocation:Limitations>` article.

Data Weight
-----------

The weight of each value approximately corresponds to its size in bytes. Weight is used in :ref:`limitations <03_ride-language/07_dapp-to-app-invocation:Limitations>` on creating and comparing values.

Weight Calculation
^^^^^^^^^^^^^^^^^^

.. csv-table:: Weight Calculation
  :file: ../_static/03_ride-language/tables/212_Weight Calculation.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Weight of List
^^^^^^^^^^^^^^

The weight of the list is calculated as follows:

:math:`W_{list} = 20 + 20 × Q + W_{elems}`

where:

* :math:`Q` is a number of elements.
* :math:`W_{elems}` is a total weight of elements.

Weight of Tuple or Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The weight of the tuple or structure is calculated as follows:

:math:`W_{struct} = 40 + 30 × Q + W_{fields}`

where:

* :math:`Q` is a number of fields.
* :math:`W_{fields}` is a total weight of fields.  

Weight Limitations
^^^^^^^^^^^^^^^^^^

* The maximum weight of the value is :math:`307200`.
* A comparison of values is not allowed if the weight of each value exceeds :math:`13000`.

If the limitations are exceeded, the script fails.

Let's consider an example, using the AssetPair structure:

.. code-block:: none

 AssetPair(amountAsset: ByteVector|Unit, priceAsset: ByteVector|Unit)

An asset ID is a ByteVector of :math:`32` bytes, its weight is :math:`32`. If both assets in the pair are not DecentralCoins, then the weight of the AssetPair structure is:

:math:`W_{AssetPair} = 40 + 30 × 2 + (32 + 32) = 164`

If one of the assets is DecentralCoin, then the corresponding field is of type Unit and its weight is :math:`40`. Then the weight of the AssetPair structure is:

:math:`W_{AssetPair} = 40 + 30 × 2 + (32 + 40) = 172`
