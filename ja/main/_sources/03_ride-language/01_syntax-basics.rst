*************
Syntax Basics
*************

* :ref:`Directives <03_ride-language/01_syntax-basics:Directives>`
* :ref:`Definitions <03_ride-language/01_syntax-basics:Definitions>`
* :ref:`Expressions <03_ride-language/01_syntax-basics:Expressions>`
* :ref:`Constants <03_ride-language/01_syntax-basics:Constants>`
* :ref:`Variables <03_ride-language/01_syntax-basics:Variables>`
* :ref:`Operators <03_ride-language/01_syntax-basics:Operators>`
* :ref:`Functions <03_ride-language/01_syntax-basics:Functions>`
* :ref:`Exceptions <03_ride-language/01_syntax-basics:Exceptions>`
* :ref:`Comments <03_ride-language/01_syntax-basics:Comments>`

Directives
==========

Every Ride script should start with directives for the compiler. The directives define the script format and available functions, structures and variables.
Directive format is as follows:

.. code-block:: none

 {-# DIRECTIVE_NAME VALUE #-}

Directive List
--------------

There are three types of directives, with different possible values.

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

{-# STDLIB_VERSION 5 #-} sets the version of the standard library. The latest version currently in production is 5.

{-# CONTENT_TYPE DAPP #-} sets the type of the file you're working on. There are different content types, DAPP and EXPRESSION. The DAPP type allows you to define functions and finish execution with certain actions which result in account balances, asset properties, and entries in the dApp account data storage. The EXPRESSION type should always return a boolean value, since it’s used as a predicate for transaction validation.

{-# SCRIPT_TYPE ACCOUNT #-} sets the entity type we want to add to the script to change its default behavior. Ride scripts can be attached to either an ACCOUNT or ASSET.

:strong:`Examples`

For a :ref:`dApp script <03_ride-language/04_script-types:dApp Script>`:

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

For an :ref:`account script <03_ride-language/04_script-types:Account Script>`:

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE EXPRESSION #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

For an :ref:`asset script <03_ride-language/04_script-types:Asset Script>`:

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE EXPRESSION #-}
 {-# SCRIPT_TYPE ASSET #-}

Not all combinations of directives are correct. The example below will not work, because DAPP content type is allowed only for accounts:

.. code-block:: none

 # Wrong example, will not work

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ASSET #-}

Definitions
===========

A definition is a linking of the name to the value or to the :ref:`function <03_ride-language/01_syntax-basics:Functions>` body.

:strong:`Examples`

Linking the name to the value.

.. code-block:: none

 let x = 5 + 5

Linking the name to the :ref:`function <03_ride-language/01_syntax-basics:Functions>` body.

.. code-block:: none

 func f(x: Int) = {
  x + 5
 }

Expressions
===========

An expression is a combination of one or more :ref:`constants <03_ride-language/01_syntax-basics:Constants>`, :ref:`variables <03_ride-language/01_syntax-basics:Variables>`, :ref:`operators <03_ride-language/01_syntax-basics:Operators>` and :ref:`function <03_ride-language/01_syntax-basics:Functions>` calls.

Expression Result
-----------------

An expression result is a value, which is obtained by the fold of the syntactic tree of the expression.
Ride interprets the expression and calculates its result.

Expression Type
---------------

An expression type is a :ref:`data type <03_ride-language/02_data-types:Data Types>` of the expression result.

:strong:`Examples`

The expression that consists of a single constant.

.. code-block:: none
 
 7

The expression that consists of a single variable.

.. code-block:: none
 
 7 + x * size("apple")  

The expression that consists of the constant :math:`7`, operators + and \*, variable x and the size function call.

.. code-block:: none

 7 + x * size("apple")

Constants
=========

A constant is a value that cannot be changed by the program during its execution.

Examples
--------

Below :math:`7` and "apple" are constants.

.. code-block:: none

 7 + x + size("apple")

Variables
=========

These are declared and initialized with the let keyword.

.. code-block:: none

 let a = "Bob"
 let b = 1

In Ride, you can only declare a variable along with a value assignment. The = sign must be followed by an expression. The value of the variable is the expression result.
Ride variables are immutable: the value of a variable cannot be changed after it is defined.
Ride is strongly typed and the variable's type is inferred from the value.
Ride allows you to define variables globally, inside any function, or even inside a variable definition.

.. code-block:: none

 func lazyIsGood() = {
  let a = "Bob"
  let b = {
     let x = 1
     "Alice"
    }  
  true
 }

Lazy Variables
--------------

Let keyword defines a variable with lazy evaluation: the value of a variable is evaluated the first time it is used. Let's see an example:

.. code-block:: none

 let a = 42                 # Integer variable definition
 let b = "Ride!"  # String variable definition

Ride allows you to define variables globally, inside any function, or even inside a variable definition.

.. code-block:: none

 func lazyIsGood() = {
  let c = {
     let d = 1
     true
    }  
  c
 }

The function above returns true, but variable d won't be initialized because unused lazy variables are not evaluated.
Since a function is a definition and not an expression, you can assign a function value to a variable but not the function itself.

.. code-block:: none

 let result = lazyIsGood()  # result is true

Strict Variables
----------------

The strict keyword defines a variable with strict (eager) evaluation. Unlike lazy variables defined with let, a strict variable is evaluated immediately when script execution reaches it, that is, before the next expression.
Strict variables can only be used inside another definition, for example, inside the body of a function. A strict variable will not be evaluated if it is defined inside another definition that is not used: for example, inside a function that has not been called.
Strict variables are suitable for :ref:`dApp-to-dApp invocation <03_ride-language/07_dapp-to-app-invocation:dApp-to-App Invocation>` as they ensure executing callable functions and applying their actions in the right order. Let's see an example:

.. code-block:: none

 func foo() = {
   ...
   strict balanceBefore = decentralchainBalance(this).regular
   strict z = invoke(dapp2,"bar",args,[AttachedPayment(unit,100000000)])
   strict balanceAfter = decentralchainBalance(this).regular

   if(balanceAfter < balanceBefore) then ... else...
 }

In this example,  balanceBefore and balanceAfter may differ because payments to dApp2 and actions performed by the bar callable function can affect the balance.

Built-in Variables
------------------

The Standard library defines built-in variables that can be used in scripts.

.. csv-table:: Built-in Variables
  :file: ../_static/03_ride-language/tables/003_Built-in-Variables.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 6

Operators
=========

Arithmetic Operators
--------------------

.. csv-table:: Arithmetic Operators
  :file: ../_static/03_ride-language/tables/004_Arithmetic-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

The / operator uses the FLOOR rounding method.

Comparison Operators
--------------------

.. csv-table:: Comparison Operators
  :file: ../_static/03_ride-language/tables/005_Comparison-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Equality Operators
------------------

.. csv-table:: Equality Operators
  :file: ../_static/03_ride-language/tables/006_Equality-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Local Definition Operators
--------------------------

.. csv-table:: Local Definition Operators
  :file: ../_static/03_ride-language/tables/007_Local-Definition-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Conditional Operators
---------------------

.. csv-table:: Conditional Operators
  :file: ../_static/03_ride-language/tables/008_Conditional-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

List Operators
--------------

.. csv-table:: List Operators
  :file: ../_static/03_ride-language/tables/009_List-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

See examples of the :ref:`list <03_ride-language/02_data-types:List>` article.

Unary Operators
---------------

.. csv-table:: Unary Operators
  :file: ../_static/03_ride-language/tables/010_Unary-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Logical Operators
-----------------

.. csv-table:: Logical Operators
  :file: ../_static/03_ride-language/tables/011_Logical-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Match-Case
----------

match-case operator is used to spot a certain type from :ref:`union <03_ride-language/02_data-types:Union>` or :ref:`any <03_ride-language/02_data-types:Any>` type . The spotting is required to perform certain operations. Let's review the following example.

.. code-block:: none

 match tx {
  case _: TransferTransaction|ExchangeTransaction => t.amount > 100 && sigVerify(tx.bodyBytes, tx.proofs[0], tx.senderPublicKey)
  case _ => false
 }

In this example, if:

* The type of transaction is transfer transaction or exchange transaction.
* Amount field value is greater than :math:`100`.

Then it will be sent to the blockchain. If the transaction has a different type and/or amount field value is lesser than 100, then it will be rejected.

Possible Issue
^^^^^^^^^^^^^^

Let's review the following code.

.. code-block:: none

 {-# STDLIB_VERSION 2 #-}
 {-# CONTENT_TYPE EXPRESSION #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

 match (tx) {
  case t: TransferTransaction|ExchangeTransaction|MassTransferTransaction|Order => false   # Prohibit any transfer of funds from the account

  case _ => sigVerify(...)
 }

In this example we are using version 2 of Ride standard library, STDLIB_VERSION 2, and we want to reject any funds transfer from our account. In order to do this, we are returning false for:

* TransferTransaction
* ExchangeTransaction
* MassTransferTransaction

Transactions of other types (for example transactions that do not transfer funds) are being sent to the blockchain. But Ride is developing rapidly, and  new transaction types are emerging. Features of invoke script transaction which is not supported by Ride v2 include attaching payments to transfer tokens to the account of the called dApp. This means that the InvokeScriptTransaction won't be caught by the first case. It will pass to the default branch case _ => and sent to blockchain. As a result, the funds could be transferred from the account instead of the transfers being prohibited like we wanted.

Solution
^^^^^^^^

To prevent the reviewed issue, it is recommended to return false inside of the default case. Then for the entities, not listed in previous branches, sending information to the blockchain will be prohibited.
Below is the sample of script which rejects any funds transfer from account, but allows all other transactions existing in Ride v2. Usage of case _ => false rejects any other transactions, not supported by the Ride v2 (i.e. invoke script transaction).

.. code-block:: none

 {-# STDLIB_VERSION 2 #-}
 {-# CONTENT_TYPE EXPRESSION #-}
 {-# SCRIPT_TYPE ACCOUNT #-}
  
 match tx {
  case t: TransferTransaction|ExchangeTransaction|MassTransferTransaction|Order => false   # Prohibit any transfer of funds from the account
  case _: Transaction => sigVerify(tx.bodyBytes, tx.proofs[0], tx.senderPublicKey) # Allow all other known transaction types as long as the signature is correct
  case _ => false  # Reject all other (new, unknown) entity types, since they are not in the version of the language used at the moment
 }

Functions
=========

Functions in Ride can only be used after they are declared.

.. code-block:: none
  
  func greet(name: String) = {
    "Hello, " + name
  }

  func add(a: Int, b: Int) = {
    func m(a:Int) = a
    m(a) + b
  }

The type (Int, String, etc) comes after the argument’s name.

As in many other languages, functions should not be overloaded. It helps to keep the code simple, readable and maintainable.

.. code-block:: none

  func calc() = {
    42
  }

  func do() = { 
    let a = calc()
    true
  }

The callable function will not be called either, because variable a is unused.

Unlike most languages, variable shadowing is not allowed. Declaring a variable with a name that is already used in a parent scope will result in a compilation error.

Functions should be defined before they are used. Functions can be invoked in prefix and postfix order:

.. code-block:: none

  let list = [1, 2, 3]
  let a1 = list.size()
  let a2 = size(list)

  let b1 = getInteger(this, “key”)
  let b2 = this.getInteger(“key”)
  
In these examples :math:`a1` is the same as :math:`a2` and :math:`b1` is the same as :math:`b2`.

Learn more about :ref:`functions <03_ride-language/03_functions:Functions>`.

Exceptions
==========

There is no exception handling in Ride: after an exception has been thrown, the script execution fails. The transaction can be either discarded or saved on the blockchain as failed, see the :ref:`transaction validation <02_decentralchain/03_transaction:Transaction Validation>` article for details
The throw function will terminate script execution immediately, with the provided text. There is no way to catch thrown exceptions.

.. code-block:: none

 throw("Here is exception text")

The idea of throw is to stop execution and send useful feedback to the user.

.. code-block:: none
 
 let a = 12
 if (a != 100) then
  throw ("a is not 100, actual value is " + a.toString())
  else throw("A is 100")

Comments
========

To write comments use the pound sign.

.. code-block:: none

 let month = 7 # Sets the month

There are no multi-line comments.