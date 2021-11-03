########
Advanced
########

********
Overview
********

Ride is a straightforward, developer-friendly functional programming language for smart contracts and decentralized applications (dApps) on the DecentralChain blockchain.
Ride is a strong statically-typed, lazy, functional, expression-based compiled programming language. It is designed for building developer-friendly decentralized applications (dApps).

Scripts
=======

DecentralChain smart contracts are scripts written in Ride. Scripts can be assigned to accounts or tokens (assets). An account with a script assigned to it becomes a :ref:`dApp <documentation:placeholder>` or :ref:`smart account <documentation:placeholder>`. An asset with a script assigned to it becomes a :ref:`smart asset <documentation:placeholder>`.

Script functionality depends on its :ref:`type <03_advanced:Script Types>`:

* :ref:`dApp script <03_advanced:dApp Script>` enables you to define сallable functions that can perform various actions on the blockchain and a verifier function that allows or denies transactions and orders that are sent on behalf of the dApp account.
* :ref:`Account script <03_advanced:Account Script>` allows or denies transactions and orders that are sent on behalf of the account.
* :ref:`Asset script <03_advanced:Asset Script>` allows or denies transactions involving the asset.

Not Turing Complete
===================

Ride is NOT Turing Complete and its execution engine (virtual machine) doesn’t have any concept of loops. Also, there are a number of limitations by design, helping to ensure execution is secure and straightforward. 
Because of the lack of loops it's not always possible to implement the necessary logic within a single script call. However, Ride recognizes that iterations are necessary and has implemented them as FOLD macros. It is still possible to perform Turing-complete computations if the algorithm is split into several functions (or even several smart contracts) and invoked sequentially using several transactions.

Blockchain Operation
====================

Ride is created specifically for execution within a blockchain environment and optimized for this purpose. Since the blockchain is a distributed ledger, located on many computers all around the world, there is no way to access the filesystem or display anything in the console. Instead, Ride functions can read data from the blockchain:

* Entries in account data storages (both dApp or smart account and any other account).
* Balances of accounts.
* Parameters of tokens.
* The current blockchain height.
* Headers of blocks.
* Transfer transactions (by transaction ID).

Predictable Computational Cost
==============================

The complexity is defined for each Ride function and operator. The complexities of the used functions and operators make up the script complexity. There are no loops in Ride, so the script complexity can be calculated in advance. The maximum script complexity is limited. Due to these limitations, DecentralChain has low and predictable fees for script execution.

Try it yourself
===============

You can try out Ride in REPL both online at `https://waves-ide.com/ <https://waves-ide.com/>`_. 

*****************************
Getting Started/Syntax Basics
*****************************

* Directives 
* :ref:`Definitions <03_advanced:Definitions>`
* :ref:`Expressions <03_advanced:Expressions>`
* :ref:`Constants <03_advanced:Constants>`
* :ref:`Data Types <03_advanced:Data Types>`
* :ref:`Variables <03_advanced:Variables>`
* :ref:`Operators <03_advanced:Operators>`
* :ref:`Functions <03_advanced:Functions>`
* :ref:`Exceptions <03_advanced:Exceptions>`
* :ref:`Comments <03_advanced:Comments>`

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

Examples
--------

For a :ref:`dApp script <03_advanced:dApp Script>`:

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

For an :ref:`account script <03_advanced:Account Script>`:

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE EXPRESSION #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

For an :ref:`asset script <03_advanced:Asset Script>`:

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

A definition is a linking of the name to the value or to the :ref:`function <03_advanced:Functions>` body.

Examples
--------

Linking the name to the value.

.. code-block:: none

 let x = 5 + 5

Linking the name to the :ref:`function <03_advanced:Functions>` body.

.. code-block:: none

 func f(x: Int) = {
  x + 5
 }

Expressions
===========

An expression is a combination of one or more :ref:`constants <03_advanced:Constants>`, :ref:`variables <03_advanced:Variables>`, :ref:`operators <03_advanced:Operators>` and :ref:`function <03_advanced:Functions>` calls.

Expression Result
-----------------

An expression result is a value, which is obtained by the fold of the syntactic tree of the expression.
Ride interprets the expression and calculates its result.

Expression Type
---------------

An expression type is a :ref:`data type <03_advanced:Data Types>` of the expression result.

Examples
--------

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

Data Types
==========

.. csv-table:: Data Types
  :file: _static/03_advanced/tables/001_Data-Types.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

For each value, depending on the data type, the weight is determined. The weight is used in limitations on creating and comparing values. For more information see the :ref:`data weight <03_advanced:Data Weight>`.

Any
---

Any is an arbitrary data type. It is a common supertype of all types: an Any type value can be a string, a number, unit, a structure, a list, a tuple, etc.

.. code-block:: none

 func findString(a: Any) = {
  match a {
    case a: String => a
    case a: List[Any] =>
      match a[0] {
        case b: String => b
        case _ => throw("Data is not a string")
      }
    case _ => throw("Data is not a string")
  }
 }

BigInt
------

BigInt is a special numeric :ref:`data type <03_advanced:Data Types>` designed to handle values outside the range of :ref:`Int <03_advanced:Int>` and to perform high accuracy calculations.
BigInt variable has a size of :math:`64` bytes (:math:`512` bits) and contains an integer between :math:`–2511` to :math:`2511–1`, inclusive. The weight of the value is :math:`64`.
A BigInt variable can only be used inside a script. A :ref:`callable function <03_advanced:Callable Function>` does not accept arguments of BigInt type and does not return a value of BigInt type. You can pass a big integer value as a string, then use the parseBigInt or parseBigIntValue functions.

BigInt Operations
^^^^^^^^^^^^^^^^^

The following operators support BigInt values:

* Arithmetic operators: +, -, \*, /, %, unary minus.
* Comparison operators: <, >, <=, and >=.
* Equality operators: == and !=.

BigInt Functions
^^^^^^^^^^^^^^^^

The following functions operate BinInt values:

* :ref:`fraction(BigInt, BigInt, BigInt): BigInt <03_advanced:fraction(BigInt, BigInt, BigInt): BigInt>`
* :ref:`fraction(BigInt, BigInt, BigInt, Union): BigInt <03_advanced:fraction(BigInt, BigInt, BigInt, Union): BigInt>`
* :ref:`log(BigInt, Int, BigInt, Int, Int, Union): BigInt <03_advanced:log(BigInt, Int, BigInt, Int, Int, Union): BigInt>`
* :ref:`max(List[BigInt]): BigInt <03_advanced:max(List[BigInt]): BigInt>`
* :ref:`median(List[BigInt]): BigInt <03_advanced:median(List[BigInt]): BigInt>`
* :ref:`min(List[BigInt]): BigInt <03_advanced:min(List[BigInt]): BigInt>`
* :ref:`pow(BigInt, Int, BigInt, Int, Int, Union): BigInt <03_advanced:pow(BigInt, Int, BigInt, Int, Int, Union): BigInt>`
* :ref:`parseBigInt(String): BigInt|Unit <03_advanced:parseBigInt(String): BigInt|Unit>`
* :ref:`parseBigIntValue(String): BigInt <03_advanced:parseBigIntValue(String): BigInt>`
* :ref:`toBigInt(ByteVector): BigInt <03_advanced:toBigInt(ByteVector): BigInt>`
* :ref:`toBigInt(ByteVector, Int, Int): BigInt <03_advanced:toBigInt(ByteVector, Int, Int): BigInt>`
* :ref:`toInt(BigInt): Int <03_advanced:toInt(BigInt): Int>`
* :ref:`toString(BigInt): String <03_advanced:toString(BigInt): String>`

Boolean
-------

Boolean is a :ref:`data type <03_advanced:Data Types>` that can have only the values true or false.

ByteVector
----------

ByteVector is a :ref:`data type <03_advanced:Data Types>` for byte array.

To assign a value to a ByteVector variable, you can use a string in Base16, Base58, or Base64 with the appropriate prefix:

.. code-block:: none

 let a = base16'52696465'
 let b = base58'8t38fWQhrYJsqxXtPpiRCEk1g5RJdq9bG5Rkr2N7mDFC'
 let c = base64'UmlkZQ=='

This method, unlike the fromBase16String, fromBase58String, and fromBase64String functions, does not increase the complexity of the script, since decoding is performed by the compiler.
To convert :ref:`integer <03_advanced:Int>`, :ref:`boolean <03_advanced:Boolean>`, :ref:`boolean <03_advanced:Boolean>` and :ref:`string <03_advanced:String>` values to a byte array use toBytes function:

.. code-block:: none

 let a = 42.toBytes()
 let b = true.toBytes()
 let c = "Ride".toBytes()

For more byte array functions, see the :ref:`Built-in Functions <03_advanced:Built-in Functions>`.

ByteVector Limitations
^^^^^^^^^^^^^^^^^^^^^^

The maximum size of a ByteVector variable is :math:`32,767` bytes. Exception: the bodyBytes field of :ref:`transaction structure <03_advanced:Transaction Structures>`. You can pass this value as an argument to the rsaVerify и sigVerify :ref:`verification functions <03_advanced:Verification Functions>` (but cannot concatenate with other byte arrays in case the limit is exceeded).

Int
---

Int is an integer :ref:`data type <03_advanced:Data Types>`. The integer variable has the size of 8 bytes and stores an integer from :math:`-9,223,372,036,854,775,808` to :math:`9,223,372,036,854,775,807` inclusive.

.. code-block:: none

 let age = 42
 let length = size("hello")

String
------

Strings are denoted only using double quotes. They are immutable, and for that reason, the substring function is very efficient: no copying is performed and no extra allocations are required. Strings are  UTF-8 encoded.

.. code-block:: none

 let name = "Bob"   # use "double" quotes only

String Limitations
^^^^^^^^^^^^^^^^^^

The maximum size of a String variable is :math:`32,767` (:math:`1` character can take up to :math:`4` bytes).

String Functions
^^^^^^^^^^^^^^^^

The built-in functions for working with strings are presented in the following articles:

* String Functions
* Converting Functions

Unit
----

Unit is an empty value data type. The empty value data type is similar to unit in Scala or to null in C#. Usually, built-in functions return unit value of type unit instead of null.

.. code-block:: none

 "String".indexOf("substring") == unit # true

Nothing
-------

Nothing is the 'bottom type' of Ride’s type system. No value can be of type nothing, but an expression of type nothing can be used everywhere. In functional languages, this is essential for support for throwing an exception:

.. code-block:: none

 2 + throw() # the expression compiles because
    # there's a defined function +(Int, Int).
      # The type of the second operand is Nothing, 
      # which complies to any required type

List
----

The list data type may contain elements of various types, including nested lists. The maximum number of list items is :math:`1000`. The nesting depth is not limited. 
A list doesn't have any fields, but there are functions and operators in the Standard library that make it easier to work with fields.

* To prepend an element to an existing list, use the cons function or :: operator
* To append an element, use the :+ operator
* To concatenate :math:`2` lists, use the ++ operator

.. code-block:: none
   
 let list = [16, 10, 1997, "birthday"]
 let last = list[(list.size() - 1)] # "birthday", postfix call of size() function

 let initList = [16, 10]                   # init value
 let newList = cons(1997, initList)        # [1997, 16, 10]
 let newList2 = 1997 :: initList           # [1997, 16, 10]
 let newList2 = initList :+ 1              # [16, 10, 1]
 let newList2 = [4, 8, 15, 16] ++ [23, 42]     # [4 8 15 16 23 42]

List Operations
^^^^^^^^^^^^^^^

Lists support concatenation as well as adding items to the beginning and the end.

.. csv-table:: List Operations
  :file: _static/03_advanced/tables/002_List-Operations.csv
  :header-rows: 1 
  :class: longtable
  :widths: 4 1 1

Operation to be used:

.. code-block:: none
  
 nil :+ 1 :+ 2 :+ 3

Result: [1, 2, 3]

Operation to be used:

.. code-block:: none

 1 :: 2 :: 3 :: nil

Result: [1, 2, 3]

Operation to be used:

.. code-block:: none

 let intList  = [1, 2]             # List[Int]
 let strList  = ["3", "4"]         # List[String]
 let joined   = intList ++ strList # List[Int|String]
 joined

Result: [1, 2, "3", "4"]

Operation to be used:

.. code-block:: none

 let appended = joined :+ true     # List[Boolean|Int|String]
 appended

Result: [1, 2, "3", "4", true]

Operation to be used:

.. code-block:: none

 let nested = intList :: joined  # List[Int|List[Int]|String]
 nested

Result: [[1, 2], 1, 2, "3", "4"]

List Functions
^^^^^^^^^^^^^^

The built-in list functions are presented in the list functions article. Operations on a list can be implemented via the FOLD macro. The size of the list must be known in advance.

List as Function Argument
^^^^^^^^^^^^^^^^^^^^^^^^^

A list, including nested one, can be a function argument:

.. code-block:: none

 func foo(arg: List[String|Unit]) = {
 ...
 }

 foo(["Ride","DecentralCoins",unit])

.. code-block:: none

 func bar(arg: List[List[Int]]) = {
 ...
 }

 bar([[1],[],[5,7]])

A callable function can take a list as an argument, but nested lists are not allowed. Here’s an example:

.. code-block:: none

 @Callable(i)
 func join(strings: List[String|Int]) = {
  let a = match strings[0] {
    case n:Int => toString(n)
    case s:String => s
  }
  let b = match strings[1] {
    case n:Int => toString(n)
    case s:String => s
  }
  let c = match strings[2] {
    case n:Int => toString(n)
    case t:String => t
  } 
  [
    StringEntry(toBase58String(i.caller.bytes), a + "_" + b + "_" + c)
  ]
 }

Invoke Script transaction example:

.. code-block:: none

 {
  "type": 16,
  ...
  "call": {
    "function": "join",
    "args": [
     {
      "type": "list",
      "value": [
      {
        "type": "string",
        "value": "Ride"
      },
      {
        "type": "integer",
        "value": 5
      },
      {
        "type": "string",
        "value": "DecentralCoins"
      }
      ]
     }
    ]
  },
  ...
 }

Tuple
------

A tuple is an ordered collection of elements. Elements can be of any type. The tuple can contain from :math:`2` to :math:`22` elements.

Let's see some tuples:

.. code-block:: none

 let x=("Hello DecentralChain",42,true)
 x._2

Result: :math:`42`

And this one also:

.. code-block:: none

 let (a,b,c)=x
 c

Result: true

Union
-----

Union is a data type that unites :math:`2` or more data types. Union can combine primitive types, :ref:`lists <03_advanced:List>`, :ref:`tuples <03_advanced:Tuple>`, :ref:`structures <03_advanced:Structures>`. This type is a very convenient way to work with abstractions. Union(String | Unit) shows that the value is an intersection of these types.

To get a value of a particular type from a Union, you can use:

* :ref:`Union functions <03_advanced:Union Functions>`
* :ref:`match-case operator <03_advanced:Match-Case>`

.. code-block:: none

  let valueFromBlockchain = getString("3PHHD7dsVqBFnZfUuDPLwbayJiQudQJ9Ngf", "someKey") # Union(String | Unit)

The simplest example of Union types is given below (please bear in mind that defining custom user types in dApp code will be supported in future versions):

.. code-block:: none

 type Human : { firstName: String, lastName: String, age: Int}
 type Cat : {name: String, age: Int }

Let's see anoter example where each element of a List[Int|String] is a string or an integer.

.. code-block:: none

 let aList   = [1, 2, "DecentralCoins"]               # List[Int|String]
 let bList   = [true,false]                  # List[Boolean]
 let joined  = aList ++ bList                # List[Boolean|Int|String]

Pattern Matching
----------------

Let’s revisit the example above:

.. code-block:: none

 type Human : { firstName: String, lastName: String, age: Int}
 type Cat : {name: String, age: Int }

 Union(Human | Cat) is an object with one field, age, but we can use pattern matching like this:

.. code-block:: none

  Human | Cat => { age: Int }

This is designed to check a value against value type:

.. code-block:: none

 let t = ...               # Cat | Human
 t.age                     # OK
 t.name                    # Compiler error
 let name = match t {      # OK
  case h: Human => h.firstName
  case c: Cat   => c.name
 }

Type matching
-------------

This is a mechanism for knowing the type of a transaction:

.. code-block:: none

 let amount = match tx {              # tx is a current outgoing transaction
  case t: TransferTransaction => t.amount
  case m: MassTransferTransaction => m.totalAmount
  case _ => 0
 }

There are different types of transactions, if a transaction is TransferTransaction or MassTransferTransaction we use the corresponding field, while in all other cases, we will get :math:`0`.

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
Strict variables are suitable for :ref:`dApp-to-dApp invocation <03_advanced:dApp-to-App Invocation>` as they ensure executing callable functions and applying their actions in the right order. Let's see an example:

.. code-block:: none

 func foo() = {
   ...
   strict balanceBefore = wavesBalance(this).regular
   strict z = invoke(dapp2,"bar",args,[AttachedPayment(unit,100000000)])
   strict balanceAfter = wavesBalance(this).regular

   if(balanceAfter < balanceBefore) then ... else...
 }

In this example,  balanceBefore and balanceAfter may differ because payments to dApp2 and actions performed by the bar callable function can affect the balance.

Built-in Variables
------------------

The Standard library defines built-in variables that can be used in scripts.

.. csv-table:: Built-in Variables
  :file: _static/03_advanced/tables/003_Built-in-Variables.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 6

Operators
=========

Arithmetic Operators
--------------------

.. csv-table:: Arithmetic Operators
  :file: _static/03_advanced/tables/004_Arithmetic-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

The / operator uses the FLOOR rounding method.

Comparison Operators
--------------------

.. csv-table:: Comparison Operators
  :file: _static/03_advanced/tables/005_Comparison-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Equality Operators
------------------

.. csv-table:: Equality Operators
  :file: _static/03_advanced/tables/006_Equality-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Local Definition Operators
--------------------------

.. csv-table:: Local Definition Operators
  :file: _static/03_advanced/tables/007_Local-Definition-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Conditional Operators
---------------------

.. csv-table:: Conditional Operators
  :file: _static/03_advanced/tables/008_Conditional-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

List Operators
--------------

.. csv-table:: List Operators
  :file: _static/03_advanced/tables/009_List-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

See examples of the :ref:`list <03_advanced:List>` article.

Unary Operators
---------------

.. csv-table:: Unary Operators
  :file: _static/03_advanced/tables/010_Unary-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Logical Operators
-----------------

.. csv-table:: Logical Operators
  :file: _static/03_advanced/tables/011_Logical-Operators.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Match-Case
----------

match-case operator is used to spot a certain type from :ref:`union <03_advanced:Union>` or :ref:`any <03_advanced:Any>` type . The spotting is required to perform certain operations. Let's review the following example.

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

Functions in Ride are declared with func, function must be declared above the place of its usage. 
When declaring a function to the right of the "=" sign must be an :ref:`expression <03_advanced:Expressions>`. The value of the function is the expression result.
Definition of the function with no parameters that returns an integer:

.. code-block:: none

 func main() = {
  3
 }

Definition of a function with two parameters:

.. code-block:: none

 func main(amount: Int, name: String) = {
   throw()
 }

Functions do have return types, this is inferred automatically by the compiler, so you don't have to declare them. There is no return statement in the language because Ride is expression-based (everything is an expression), and the last statement is a result of the function. 

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
Functions can be invoked in prefix and postfix order:

.. code-block:: none

 let list = [1, 2, 3]
 let a1 = list.size()
 let a2 = size(list)

 let b1 = getInteger(this, "key")
 let b2 = this.getInteger("key")

Annotations
-----------

Functions can be without annotations, but they can also be with @Callable or @Verifier annotations. Annotated functions are used only in scripts of type DAPP.
Here’s an example of @Callable:

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

 func getPayment(i: Invocation) = {
  if (size(i.payments) == 0)
    then throw("Payment must be attached")
    else {
      let pmt = i.payments[0]
      if (isDefined(pmt.assetId))
        then throw("This function accepts DecentralCoin tokens only")
        else pmt.amount
    }
 }

 @Callable(i)
 func pay() = {
  let amount = getPayment(i)
  (
    [
      IntegerEntry(toBase58String(i.caller.bytes), amount)
    ],
    unit
  )
 }  

Annotations can bind some values to the function. In the example above, variable i was bound to the function pay and stored some fields of the invocation (the caller’s public key, address, payments attached to the invocation, fee, transaction ID etc.).
Functions without annotations are not available from the outside. You can call them only inside other functions.

Here’s an example of @Verifier:

.. code-block:: none

 @Verifier(tx)
 func verifier() = {
  match tx {
    case m: TransferTransaction => tx.amount <= 100 # can send up to 100 tokens
    case _ => false
  }
 }

A function with the @Verifier annotation sets the rules for outgoing transactions of a decentralized application (dApp). Verifier functions cannot be called from the outside, but they are executed every time an attempt is made to send a transaction from a dApp.
Verifier functions should always return a Boolean value as a result, depending on whether a transaction will be recorded to the blockchain or not.

Expression scripts (with directive {-# CONTENT_TYPE EXPRESSION  #-} along with functions annotated by @Verifier should always return a boolean value. Depending on that value the transaction will be accepted (in case of true) or rejected (in case of false) by the blockchain.

.. code-block:: none

 @Verifier(tx)
 func verifier() = {
  sigVerify(tx.bodyBytes, tx.proofs[0], tx.senderPublicKey)
 }

The Verifier function binds variable tx, which is an object with all fields of the current outgoing transaction.
A maximum of one @Verifier() function can be defined in each dApp script.

Callable Functions
------------------

The functions with the @Callable annotation become callable functions, since they can be called (or invoked) from other accounts: by an Invoke Script transaction or by a dApp.
A callable function can perform actions: write data to the dApp data storage, transfer tokens from the dApp to other accounts, issue/release/burn tokens, and others. The result of a callable function is a tuple of two elements: a list of structures describing script actions and a value passed to the parent function in case of the :ref:`dApp-to-dApp invocation <03_advanced:dApp-to-App Invocation>`.

.. code-block:: none

 @Callable(i)
 func giveAway(age: Int) = {
  (
    [
      ScriptTransfer(i.caller, age, unit),
      IntegerEntry(toBase58String(i.caller.bytes), age)
    ],
    unit
  )
 } 

Every caller of giveAway function will receive as many Decentralites as their age. The ScriptTransfer structure sets the parameters of the token transfer. dApp also will store information about the fact of the transfer in its data storage. The IntegerEntry structure sets the parameters of the entry: key and value.

Built-in Functions
------------------

A built-in function is a :ref:`function <03_advanced:Functions>` of the standard library .

Account Data Storage Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learn more about :ref:`account data storage <02_intermediate:Account Data Storage>`.

.. csv-table:: Account Data Storage Functions
  :file: _static/03_advanced/tables/012_Account-Data-Storage-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

getBinary(Address|Alias, String): ByteVector|Unit
"""""""""""""""""""""""""""""""""""""""""""""""""

Gets an array of bytes by key.

.. code-block:: none

 getBinary(addressOrAlias: Address|Alias, key: String): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/013_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinary(String): ByteVector|Unit
""""""""""""""""""""""""""""""""""

Gets an array of bytes by key from the dApp's own data storage.

.. code-block:: none

 getBinary(key: String): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/014_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinaryValue(Address|Alias, String): ByteVector
"""""""""""""""""""""""""""""""""""""""""""""""""

Gets an array of bytes by key. Fails if there is no data.

.. code-block:: none

 getBinaryValue(addressOrAlias: Address|Alias, key: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/015_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinaryValue(String): ByteVector
""""""""""""""""""""""""""""""""""

Gets an array of bytes by key from the dApp's own data storage.

.. code-block:: none

 getBinaryValue(key: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/016_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBoolean(Address|Alias, String): Boolean|Unit
"""""""""""""""""""""""""""""""""""""""""""""""

Gets a boolean value by key.

.. code-block:: none

 getBoolean(addressOrAlias: Address|Alias, key: String): Boolean|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/017_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBoolean(String): Boolean|Unit
""""""""""""""""""""""""""""""""

Gets a boolean value by key by key from the dApp's own data storage.

.. code-block:: none

 getBoolean(key: String): Boolean|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/018_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBooleanValue(Address|Alias, String): Boolean
"""""""""""""""""""""""""""""""""""""""""""""""

Gets a boolean value by key. Fails if there is no data.

.. code-block:: none

 getBooleanValue(addressOrAlias: Address|Alias, key: String): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/019_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBooleanValue(String): Boolean
""""""""""""""""""""""""""""""""

Gets a boolean value by key from the dApp's own data storage.

.. code-block:: none

 getBooleanValue(key: String): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/020_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getInteger(Address|Alias, String): Int|Unit
"""""""""""""""""""""""""""""""""""""""""""

Gets an integer by key.

.. code-block:: none

 getInteger(addressOrAlias: Address|Alias, key: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/021_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getInteger(String): Int|Unit
""""""""""""""""""""""""""""

Gets an integer by key from the dApp's own data storage.

.. code-block:: none

 getInteger(key: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/022_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getIntegerValue(Address|Alias, String): Int
"""""""""""""""""""""""""""""""""""""""""""

Gets an integer by key. Fails if there is no data.

.. code-block:: none

 getIntegerValue(addressOrAlias: Address|Alias, key: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/023_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getIntegerValue(String): Int
""""""""""""""""""""""""""""

Gets an integer by key from the dApp's own data storage.

.. code-block:: none

 getIntegerValue(key: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/024_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getString(Address|Alias, String): String|Unit
"""""""""""""""""""""""""""""""""""""""""""""

Gets a string by key.

.. code-block:: none

 getString(addressOrAlias: Address|Alias, key: String): String|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/025_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getString(String): String|Unit
""""""""""""""""""""""""""""""

Gets a string by key from the dApp's own data storage.

.. code-block:: none

 getString(key: String): String|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/026_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getStringValue(Address|Alias, String): String
"""""""""""""""""""""""""""""""""""""""""""""

Gets a string by key. Fails if there is no data.

.. code-block:: none

 getStringValue(addressOrAlias: Address|Alias, key: String): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/027_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getStringValue(String): String
""""""""""""""""""""""""""""""

Gets a string by key from the dApp's own data storage.

.. code-block:: none

 getString(key: String): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/028_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

isDataStorageUntouched(Address|Alias): Boolean
""""""""""""""""""""""""""""""""""""""""""""""

Checks if the data storage of a given account never contained any entries. Returns false if there was at least one entry in the account data storage even if the entry was deleted.

.. code-block:: none

 isDataStorageUntouched(addressOrAlias: Address|Alias): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/029_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let addr = Address(base58'3N4iKL6ikwxiL7yNvWQmw7rg3wGna8uL6LU')
 isDataStorageUntouched(addr) # Returns false

Blockchain Functions
^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Blockchain Functions
  :file: _static/03_advanced/tables/030_Blockchain-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

addressFromRecipient(Address|Alias): Address
""""""""""""""""""""""""""""""""""""""""""""

Gets the corresponding :ref:`address <02_intermediate:Address>` of the :ref:`alias <02_intermediate:Alias>`.

.. code-block:: none

 addressFromRecipient(AddressOrAlias: Address|Alias): Address

For a description of the return value, see the :ref:`address <03_advanced:Address>` article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/031_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let address = Address(base58'3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF')
 addressFromRecipient(address)

assetBalance(Address|Alias, ByteVector): Int
""""""""""""""""""""""""""""""""""""""""""""

Gets account balance by token ID.

.. code-block:: none

 assetBalance(addressOrAlias: Address|Alias, assetId: ByteVector): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/032_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

assetInfo(ByteVector): Asset|Unit
"""""""""""""""""""""""""""""""""

Gets the information about a :ref:`token (asset) <02_intermediate:Token (Asset)>`.

.. code-block:: none

 assetInfo(id: ByteVector): Asset|Unit

For a description of the return value, see the :ref:`BlockInfo <03_advanced:BlockInfo>` article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/033_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let bitcoinId = base58'8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS'
 let x = match assetInfo(bitcoinId) {
  case asset:Asset =>
    asset.decimals # 8
  case _ => throw("Can't find asset")
 }

blockInfoByHeight(Int): BlockInfo|Unit
""""""""""""""""""""""""""""""""""""""

Gets the information about a :ref:`block <02_intermediate:Block>` by the :ref:`block height <02_intermediate:Block Height>`.

.. code-block:: none

 blockInfoByHeight(height: Int): BlockInfo|Unit

For a description of the return value, see the :ref:`BlockInfo <03_advanced:BlockInfo>` article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/034_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let x = match blockInfoByHeight(1234567) {
  case block:BlockInfo =>
    block.generator.toString() # "3P38Z9aMhGKAWnCiyMW4T3PcHcRaTAmTztH"
  case _ => throw("Can't find block")
 }

calculateAssetId(Issue): ByteVector
"""""""""""""""""""""""""""""""""""

Calculates ID of the token formed by the :ref:`issue structure <03_advanced:Issue>` when executing the :ref:`callable function <03_advanced:Callable Functions>`.

.. code-block:: none

 calculateAssetId(issue: Issue): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/035_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

:strong:`Example`

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}
  
 @Callable(inv)
 func issueAndId() = {
  let issue = Issue("CryptoRouble", "Description", 1000, 2, true)
  let id = calculateAssetId(issue)
  (
    [
      issue,
      BinaryEntry("id", id)
    ],
    unit
  )
 }

calculateLeaseId(Lease): ByteVector
"""""""""""""""""""""""""""""""""""

Calculates ID of the lease formed by the :ref:`lease structure <03_advanced:Lease>` when executing the :ref:`callable function <03_advanced:Callable Functions>`.

.. code-block:: none

 calculateLeaseId(lease: Lease): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/036_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

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

scriptHash(Address|Alias): ByteVector|Unit
""""""""""""""""""""""""""""""""""""""""""

Returns BLAKE2b-256 hash of the script assigned to a given account. Returns unit if there is no script. The function can be used to verify that the script is exactly the same as expected.

.. code-block:: none

 scriptHash(addressOrAlias: Address|Alias): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/037_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let addr = Address(base58'3MxBZbnN8Z8sbYjjL5N3oG5C8nWq9NMeCEm')
 scriptHash(addr) # Returns base58'G6ihnWN5mMedauCgNa8TDrSKWACPJKGQyYagmMQhPuja'

transactionHeightById(ByteVector): Int|Unit
"""""""""""""""""""""""""""""""""""""""""""

Gets the :ref:`block height <02_intermediate:Block Height>` of a transaction.

.. code-block:: none

 transactionHeightById(id: ByteVector): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/038_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let bitcoinId = base58'8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS'
 let x = match transactionHeightById(bitcoinId) {
  case h:Int => h # 257457
  case _ => throw("Can't find transaction")
 }

transferTransactionById(ByteVector): TransferTransaction|Unit
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Gets the data of a :ref:`transfer transaction <02_intermediate:Transfer Transaction>`.

.. code-block:: none

 transferTransactionById(id: ByteVector): TransferTransaction|Unit

For a description of the return value, see the :ref:`TransferTransaction <03_advanced:TransferTransaction>` article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/039_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let transferId = base58'J2rcMzCWCZ1P3SFZzvz9PR2NtBjomDh57HTcqptaAJHK'
 let x = match transferTransactionById(transferId) {
  case ttx:TransferTransaction =>
    ttx.amount # 3500000000
  case _ => throw("Can't find transaction")
 }

wavesBalance(Address|Alias): BalanceDetails
"""""""""""""""""""""""""""""""""""""""""""

Gets all types of :ref:`DecentralCoin <02_intermediate:DecentralCoin>` balances. For description of balance types, see the :ref:`account balance <02_intermediate:Account Balance>` article.

.. code-block:: none

 wavesBalance(addressOrAlias: Address|Alias): BalanceDetails

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/040_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Byte Array Functions
^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Byte Array Functions
  :file: _static/03_advanced/tables/041_Byte-Array-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

drop(ByteVector, Int): ByteVector
"""""""""""""""""""""""""""""""""

Returns the byte array without the first N bytes.

.. code-block:: none

 drop(xs: ByteVector, number: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/042_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 drop("Ride".toBytes(), 2)   # Returns the byte array without the first 2 bytes
 drop(125.toBytes(), 2)      # Returns the byte array without the first 2 bytes
 drop(base16'52696465', 3)   # Returns the byte array without the first 3 bytes
 drop(base58'37BPKA', 3)     # Returns the byte array without the first 3 bytes
 drop(base64'UmlkZQ==', 3)   # Returns the byte array without the first 3 bytes

dropRight(ByteVector, Int): ByteVector
""""""""""""""""""""""""""""""""""""""

Returns the byte array without the last N bytes.

.. code-block:: none

 dropRight(xs: ByteVector, number: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/043_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 dropRight("Ride".toBytes(), 2)  # Returns the byte array without the last 2 bytes
 dropRight(125.toBytes(), 2)     # Returns the byte array without the last 2 bytes
 dropRight(base16'52696465', 3)  # Returns the byte array without the last 3 bytes
 dropRight(base58'37BPKA', 3)    # Returns the byte array without the last 3 bytes
 dropRight(base64'UmlkZQ==', 3)  # Returns the byte array without the last 3 bytes

size(ByteVector): Int
"""""""""""""""""""""

Returns the number of bytes in the byte array.

.. code-block:: none

 size(byteVector: ByteVector): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/044_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 size("Hello".toBytes())         # Returns 5
 size("Hello world".toBytes())   # Returns 11
 size(64.toBytes())              # Returns 8 because all integers in Ride take 8 bytes
 size(200000.toBytes())          # Returns 8 because all integers in Ride take 8 bytes
 size(base58'37BPKA')            # Returns 4

take(ByteVector, Int): ByteVector
"""""""""""""""""""""""""""""""""

Returns the first N bytes of the byte array.

.. code-block:: none

 take(xs: ByteVector, number: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/045_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 take(base58'37BPKA', 0) # Returns the empty byte array
 take(base58'37BPKA', 1) # Returns the byte array consisting of first byte of initial byte array
 take(base58'37BPKA', 15) # Returns whole byte array
 take(base58'37BPKA', -10) # Returns the empty byte array

takeRight(ByteVector, Int): ByteVector
""""""""""""""""""""""""""""""""""""""

Returns the last N bytes of the byte array.

.. code-block:: none

 takeRight(xs: ByteVector, number: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/046_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 takeRight(base58'37BPKA', 2) # Returns the last 2 bytes of the byte array

Converting Functions
^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Converting Functions
  :file: _static/03_advanced/tables/047_Converting-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

addressFromPublicKey(ByteVector): Address
"""""""""""""""""""""""""""""""""""""""""

Gets the corresponding :ref:`address <02_intermediate:Address>` of the account public key.

.. code-block:: none

 addressFromPublicKey(publicKey: ByteVector): Address

For a description of the return value, see the :ref:`address <03_advanced:Address>` article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/048_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let address = addressFromPublicKey(base58'J1t6NBs5Hd588Dn7mAPytqkhgeBshzv3zecScfFJWE2D')

parseBigInt(String): BigInt|Unit
""""""""""""""""""""""""""""""""

Converts the string representation of a number to its :ref:`big integer <03_advanced:BigInt>` equivalent.

.. code-block:: none

 parseBigInt(str: String): BigInt|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/049_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

parseBigIntValue(String): BigInt
""""""""""""""""""""""""""""""""

Converts the string representation of a number to its :ref:`big integer <03_advanced:BigInt>` equivalent. Fails if the string cannot be parsed.

.. code-block:: none

 parseBigIntValue(str: String): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/050_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

parseInt(String): Int|Unit
""""""""""""""""""""""""""

Converts the string representation of a number to its integer equivalent.

.. code-block:: none

 parseInt(str: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/051_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 parseInt("10") # Returns 10
 parseInt("010") # Returns 10
 parseInt("Ride") # Returns Unit
 parseInt("10.30") # Returns Unit

parseIntValue(String): Int
""""""""""""""""""""""""""

Converts the string representation of a number to its integer equivalent. Fails if the string cannot be parsed.

.. code-block:: none

 parseIntValue(str: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/052_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 parseIntValue("10") # Returns 10
 parseIntValue("010") # Returns 10
 parseIntValue("Ride") # Error while parsing string to integer
 parseIntValue("10.30") # Error while parsing string to integer
 parseIntValue("20 DecentralCoins") # Error while parsing string to integer

toBigInt(ByteVector): BigInt
""""""""""""""""""""""""""""

Converts an array of bytes to a :ref:`big integer <03_advanced:BigInt>` using the big-endian byte order.

.. code-block:: none

 toBigInt(bin: ByteVector): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/053_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

toBigInt(ByteVector, Int, Int): BigInt
""""""""""""""""""""""""""""""""""""""

Converts an array of bytes starting from a certain index to a :ref:`big integer <03_advanced:BigInt>` using the big-endian byte order.

.. code-block:: none

 toBigInt(bin: ByteVector, offset: Int, size: Int): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/054_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

toBigInt(Int): BigInt
"""""""""""""""""""""

Converts an integer to a :ref:`big integer <03_advanced:BigInt>`.

.. code-block:: none

 toBigInt(n: Int): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/055_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

toBytes(Boolean): ByteVector
""""""""""""""""""""""""""""

Converts a boolean value to an array of bytes.

.. code-block:: none

 toBytes(b: Boolean): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/056_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 toBytes(true) # Returns base58'2'
 toBytes(false) # Returns base58'1'

toBytes(Int): ByteVector
""""""""""""""""""""""""

Converts an integer to an array of bytes using the big-endian byte order.

.. code-block:: none

 toBytes(n: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/057_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBytes(10) # Returns base58'1111111B'

toBytes(String): ByteVector
"""""""""""""""""""""""""""

Converts a string to an array of bytes.

.. code-block:: none

 toBytes(s: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/058_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBytes("Ride") # Returns base58'37BPKA'

toBytes(BigInt): ByteVector
"""""""""""""""""""""""""""

Converts a :ref:`big integer <03_advanced:BigInt>` to an array of bytes using the big-endian byte order.

.. code-block:: none

 toBytes(n: BigInt): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/059_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1


toInt(BigInt): Int
""""""""""""""""""

Converts a :ref:`big integer <03_advanced:BigInt>` to an integer. Fails if the number cannot be converted.

.. code-block:: none

 toInt(n: BigInt): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/060_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

toInt(ByteVector): Int
""""""""""""""""""""""

Converts an array of bytes to an integer using the big-endian byte order.

.. code-block:: none

 toInt(bin: ByteVector) : Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/061_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toInt(base58'1111111B') # Returns 10

toInt(ByteVector, Int): Int
"""""""""""""""""""""""""""

Converts an array of bytes to an integer starting from a certain index using the big-endian byte order.

.. code-block:: none

 toInt(bin: ByteVector, offset: Int): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/062_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = toBytes("Ride")
 toInt(bytes, 2) # Returns 7234224039401641825
 toInt(bytes, 6) # Index out of bounds

toString(Address): String
"""""""""""""""""""""""""

Converts an array of bytes of an :ref:`address <02_intermediate:Address>` to a string.

.. code-block:: none

 toString(addr: Address): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/063_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let address = Address(base58'3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF')
 toString(address) # Returns "3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF"

toString(Boolean): String
"""""""""""""""""""""""""

Converts a boolean value to a string.

.. code-block:: none

 toString(b: Boolean): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/064_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toString(true) # Returns "true"
 toString(false) # Returns "false"

toString(Int): String
"""""""""""""""""""""

Converts an integer to a string.

.. code-block:: none

 toString(n: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/065_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toString(10) # Returns "10"

toString(BigInt): String
""""""""""""""""""""""""

Converts a :ref:`big integer <03_advanced:BigInt>` to a string.

.. code-block:: none

 toString(n: BigInt): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/066_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

toUtf8String(ByteVector): String
""""""""""""""""""""""""""""""""

Converts an array of bytes to a UTF-8 string. Fails if the array of bytes cotains an invalid UTF-8 sequence.

.. code-block:: none

 toUtf8String(u: ByteVector): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/067_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = toBytes("Ride")
 toUtf8String(bytes) # Returns "Ride"

transferTransactionFromProto(ByteVector): TransferTransaction|Unit
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Deserializes transfer transaction: converts protobuf-encoded :ref:`binary format <02_intermediate:Transfer Transaction Binary Format>` specified in transaction.proto to a TransferTransaction structure. Returns unit if deserialization failed.

.. code-block:: none

 transferTransactionFromProto(b: ByteVector): TransferTransaction|Unit

For a description of the return value, see the :ref:`TransferTransaction <03_advanced:TransferTransaction>` article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/068_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

:strong:`Example`

.. code-block:: none
  
 let transfer = base64'Cr4BCFQSIA7SdnwUqEBY+k4jUf9sCV5+xj0Ry/GYuwmDMCdKTdl3GgQQoI0GIPLIyqL6LSgDwgaHAQoWChT+/s+ZWeOWzh1eRnhdRL3Qh9bxGRIkCiBO/wEBhwH/f/+bAWBRMv+A2yiAOUeBc9rY+UR/a4DxKBBkGkcaRYCcAQAB//9/AX9//0695P8EiICAfxgBgIkefwHYuDmA//83/4ABJgEBAf8d9N+8AAERyo1/j3kAGn/SAb7YIH8y/4CAXg=='
 let x = match transferTransactionFromProto(transfer) {
  case ttx:TransferTransaction =>
    ttx.amount # 3500000000
  case _ => throw("Can't find transaction")
 }

dApp-to-dApp Invocation Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: dApp-to-dApp Invocation Functions
  :file: _static/03_advanced/tables/069_dApp-to-dApp-Invocation-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

invoke(Address|Alias, String, List[Any], List[AttachedPayments]): Any
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Invokes a dApp :ref:`callable function <03_advanced:Callable Functions>`, with reentrancy restriction.

.. code-block:: none

 invoke(dApp: Address|Alias, function: String, arguments: List[Any], payments: List[AttachedPayments]): Any

Any means any valid type. You can extract a particular type from it using as[T] and exactAs[T] macros or the match ... case operator, see the :ref:`any <03_advanced:Any>` article.

The invoke function can be used by a callable function of a :ref:`dApp script <03_advanced:dApp Script>`, but not by a verifier function, :ref:`account script <03_advanced:Account Script>` or :ref:`asset script <03_advanced:Asset Script>`.

Via the invoke function, the callable function can invoke a callable function of another dApp, or another callable function of the same dApp, or even itself, and then use the invocation results in subsequent operations. For details, see the :ref:`dApp-to-dApp invocation <03_advanced:dApp-to-App Invocation>` article.

To ensure executing callable functions and applying their actions in the right order, initialize a :ref:`strict variable <03_advanced:Strict Variables>` by the return value of an invoke function.

The invocation can contain payments that will be transferred from the balance of the parent dApp to the balance of the invoked dApp. Payments are forbidden if the dApp invokes itself.

If a payment token is a smart asset, the asset script verifies the invoke as if it was :ref:`InvokeScriptTransaction <03_advanced:InvokeScriptTransaction>` with the following fields:

* DApp, payments, function, args indicated in the invoke function.
* Sender, senderPublicKey of the dApp that performs the invocation.
* Id, timestamp, fee, feeAssetId indicated in the original invoke script transaction.
* Version = 0;
  
If the asset script denies the action, the Invoke Script transaction is either discarded or saved on the blockchain as failed, see the :ref:`transaction validation <02_intermediate:Transaction Validation>` article.

:strong:`Reentrancy Restriction`

The invocation stack generated by the invoke function must not contain invocations of the parent dApp after invocation of another dApp. Let the parent dApp A invokes dApp B using the invoke function. Regardless of whether dApp B uses invoke or reentrantInvoke, the following invocation stacks will fail:

.. code-block:: none

 → dApp A
   → dapp B
       → dApp A

.. code-block:: none

 → dApp A
   → dapp B
      → dApp C
         → dApp A

The following invocation stacks are valid:

.. code-block:: none

 → dApp A
   → dapp A
      → dapp A

.. code-block:: none

 → dApp N
   → dapp A
   → dApp A

.. code-block:: none

 → dapp N
   → dapp A
      → dapp B
   → dapp B
      → dapp A
      → dapp C

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/070_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

A user sends an invoke script transaction that invokes the callable function foo of dApp1. The foo function invokes the bar function of dApp2 passing the number a and attaching a payment of 1 USDN. The bar function transfers :math:`1` :ref:`DecentralCoin <02_intermediate:DecentralCoin>` to dApp1 and returns the doubled number a. The foo function writes to dApp1 data storage:

* The value returned by bar.
* The new balance of dApp2 (reduced by :math:`1` DecentralCoin transferred to dApp1).

dApp1:

.. code-block:: none
  
 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

 @Callable(i)
 func foo(dapp2: String, a: Int, key1: String, key2: String) = {
   strict res = invoke(addressFromStringValue(dapp2),"bar",[a],[AttachedPayment(base58'DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p',1000000)])
   match res {
     case r : Int => 
      (
        [
          IntegerEntry(key1, r),
          IntegerEntry(key2, wavesBalance(addressFromStringValue(dapp2)).regular)
        ],
        unit
      )
     case _ => throw("Incorrect invoke result") 
   }
 }

dApp2:
  
.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

 @Callable(i)
 func bar(a: Int) = {
  (
    [
        ScriptTransfer(i.caller, 100000000, unit)
    ],
    a*2
  )
 }

reentrantInvoke(Address|Alias, String, List[Any], List[AttachedPayments]): Any
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Invokes a dApp :ref:`callable function <03_advanced:Callable Functions>`. The only difference from the invoke function above is that there is no reentrancy restriction for the parent dApp that uses reentrantInvoke. However, if the parent dApp is invoked again and this time uses the invoke function, the parent dApp cannot be invoked again in this invocation stack.

For example, the invocation stack:

.. code-block:: none

 → dApp A
   → dapp B
      → dApp A
         → dApp C
            → dApp A

* Is valid if dApp A invokes both dApp B and dApp C via the reentrantInvoke function;
* Fails if dApp A invokes dApp B via the reentrantInvoke function and invokes dApp C via the invoke function.

.. code-block:: none

 reentrantInvoke(dApp: Address|Alias, function: String, arguments: List[Any], payments: List[AttachedPayments]): Any

Data Transaction Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

The functions listed below retrieve data by key from the :ref:`data transaction structure <03_advanced:DataTransaction>` or from any list of data entries.

.. csv-table:: Data Transaction Functions
  :file: _static/03_advanced/tables/071_Data-Transaction-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

getBinary(List[], String): ByteVector|Unit
""""""""""""""""""""""""""""""""""""""""""

Gets a binary value from a list of data entires by key.

.. code-block:: none

 getBinary(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/072_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinary(List[], Int): ByteVector|Unit
"""""""""""""""""""""""""""""""""""""""

Gets a binary value from a list of data entires by index.

.. code-block:: none

 getBinary(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/073_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinaryValue(List[], String): ByteVector
""""""""""""""""""""""""""""""""""""""""""

Gets a binary value from a list of data entires by key. Fails if there is no data.

.. code-block:: none

 getBinaryValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/074_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinaryValue(List[], Int): ByteVector
"""""""""""""""""""""""""""""""""""""""

Gets a binary value from a list of data entires by index. Fails if there is no data.

.. code-block:: none

 getBinaryValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/075_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBoolean(List[], String): Boolean|Unit
""""""""""""""""""""""""""""""""""""""""

Gets a boolean value from a list of data entires by key.

.. code-block:: none

 getBoolean(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): Boolean|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/076_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBoolean(List[], Int): Boolean|Unit
"""""""""""""""""""""""""""""""""""""

Gets a boolean value from a list of data entires by index.

.. code-block:: none

 getBoolean(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): Boolean|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/077_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBooleanValue(List[], String): Boolean
""""""""""""""""""""""""""""""""""""""""

Gets a boolean value from a list of data entires by key. Fails if there is no data.

.. code-block:: none

 getBooleanValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/078_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBooleanValue(List[], Int): Boolean
"""""""""""""""""""""""""""""""""""""

Gets a boolean value from a list of data entires by index. Fails if there is no data.

.. code-block:: none

 getBooleanValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/079_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getInteger(List[], String): Int|Unit
""""""""""""""""""""""""""""""""""""

Gets integer from a list of data entires by key.

.. code-block:: none

 getInteger(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/080_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getInteger(List[], Int): Int|Unit
"""""""""""""""""""""""""""""""""

Gets an integer value from a list of data entires by index.

.. code-block:: none

 getInteger(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/081_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getIntegerValue(List[], String): Int
""""""""""""""""""""""""""""""""""""

Gets an integer value from a list of data entires by key. Fails if there is no data.

.. code-block:: none

 getIntegerValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/082_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getIntegerValue(List[], Int): Int
"""""""""""""""""""""""""""""""""

Gets an integer value from a list of data entires by index. Fails if there is no data.

.. code-block:: none

 getIntegerValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/083_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getString(List[], String): String|Unit
""""""""""""""""""""""""""""""""""""""

Gets a string value from a list of data entires by key.

.. code-block:: none

 getString(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): String|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/084_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getString(List[], Int): String|Unit
"""""""""""""""""""""""""""""""""""

Gets a string value from a list of data entires by key.

.. code-block:: none

 getString(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): String|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/085_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getStringValue(List[], String): String
""""""""""""""""""""""""""""""""""""""

Gets a string value from a list of data entires by key. Fails if there is no data.

.. code-block:: none

 getStringValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/086_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getStringValue(List[], Int): String
"""""""""""""""""""""""""""""""""""

Gets a string value from a list of data entires by index. Fails if there is no data.

.. code-block:: none

 getStringValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/087_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Decoding Functions
^^^^^^^^^^^^^^^^^^

.. csv-table:: Decoding Functions
  :file: _static/03_advanced/tables/088_Decoding-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

addressFromString(String): Address|Unit
"""""""""""""""""""""""""""""""""""""""

Decodes address from base58 string.

.. code-block:: none

 addressFromString(string: String): Address|Unit

For a description of the return value, see the :ref:`address <03_advanced:Address>` article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/089_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let address = addressFromString("3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF")

addressFromStringValue(String): Address
"""""""""""""""""""""""""""""""""""""""

Decodes address from base58 string. Fails if the address cannot be decoded.

.. code-block:: none

 addressFromStringValue(string: String): Address

For a description of the return value, see the :ref:`address <03_advanced:Address>` article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/090_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let address = addressFromStringValue("3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF")

fromBase16String(String): ByteVector
""""""""""""""""""""""""""""""""""""

Decodes a base16 string to an array of bytes.

.. code-block:: none

 fromBase16String(str: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/091_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = fromBase16String("52696465")

fromBase58String(String): ByteVector
""""""""""""""""""""""""""""""""""""

Decodes a base58 string to an array of bytes.

.. code-block:: none

 fromBase58String(str: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/092_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = fromBase58String("37BPKA")

fromBase64String(String): ByteVector
""""""""""""""""""""""""""""""""""""

Decodes a base64 string to an array of bytes.

.. code-block:: none

 fromBase64String(str: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/093_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = fromBase64String("UmlkZQ==")

Encoding Functions
^^^^^^^^^^^^^^^^^^

.. csv-table:: Encoding Functions
  :file: _static/03_advanced/tables/094_Encoding-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

toBase16String(ByteVector): String
""""""""""""""""""""""""""""""""""

Encodes an array of bytes to a base16 string.

.. code-block:: none

 toBase16String(bytes: ByteVector): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/095_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBase16String("Ride".toBytes()) # Returns "52696465"
 toBase16String(base16'52696465') # Returns "52696465"

toBase58String(ByteVector): String
""""""""""""""""""""""""""""""""""

Encodes an array of bytes to a base58 string.

.. code-block:: none

 toBase58String(bytes: ByteVector): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/096_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBase58String("Ride".toBytes()) # Returns "37BPKA"
 toBase58String(base58'37BPKA')  # Returns "37BPKA

toBase64String(ByteVector): String
""""""""""""""""""""""""""""""""""

Encodes an array of bytes to a base64 string.

.. code-block:: none

 toBase64String(bytes: ByteVector): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/097_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBase64String("Ride".toBytes()) # Returns "UmlkZQ=="
 toBase64String(base64'UmlkZQ==') # Returns "UmlkZQ=="

Exception Functions
^^^^^^^^^^^^^^^^^^^

.. csv-table:: Exception Functions
  :file: _static/03_advanced/tables/098_Exception-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

The return type of throw is nothing. There is no exception handling in Ride: after an exception has been thrown, the script execution fails. The transaction can be either discarded or saved on the blockchain as failed, see the :ref:`transaction validation <02_intermediate:Transaction Validation>` article for details.

throw()
"""""""

Raises an exception.

throw(String)
"""""""""""""

Raises an exception with a message.

.. code-block:: none

 throw(err: String)

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/099_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Hashing Functions
^^^^^^^^^^^^^^^^^

.. csv-table:: Hashing Functions
  :file: _static/03_advanced/tables/100_Hashing-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

blake2b256(ByteVector): ByteVector
""""""""""""""""""""""""""""""""""

Range of functions that hash an array of bytes using BLAKE2b-256.

.. csv-table:: blake2b256
  :file: _static/03_advanced/tables/101_blake2b256.csv
  :header-rows: 1 
  :class: longtable
  :widths: 4 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/102_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

:strong:`Example`

.. code-block:: none
  
 blake2b256("Ride".toBytes())        # Returns 6NSWRz5XthhFVm9uVQHuisdaseQJfc4WMGajN435v3f4
 blake2b256(125.toBytes())            # Returns H9emWhyMuyyjDmNkgx7jAfHRuy9icXK3uYJuVw6R1uuK
 blake2b256(base16'52696465')   # Returns 6NSWRz5XthhFVm9uVQHuisdaseQJfc4WMGajN435v3f4
 blake2b256(base58'37BPKA')       # Returns 6NSWRz5XthhFVm9uVQHuisdaseQJfc4WMGajN435v3f4
 blake2b256(base64'UmlkZQ==')  # Returns 6NSWRz5XthhFVm9uVQHuisdaseQJfc4WMGajN435v3f4

keccak256(ByteVector): ByteVector
"""""""""""""""""""""""""""""""""

Range of functions that hash an array of bytes using Keccak-256.

.. csv-table:: keccak256
  :file: _static/03_advanced/tables/103_keccak256.csv
  :header-rows: 1 
  :class: longtable
  :widths: 4 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/104_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

:strong:`Example`

.. code-block:: none
  
 keccak256("Ride".toBytes())        # Returns 4qa5wNk4961VwJAjCKBzXiEvBQ2gBJoqDcLFRJTiSKpv
 keccak256(125.toBytes())            # Returns 5UUkcH6Fp2E3mk7NSqSTs3JBP33zL3SB3yg4b2sR5gpF
 keccak256(base16'52696465')   # Returns 4qa5wNk4961VwJAjCKBzXiEvBQ2gBJoqDcLFRJTiSKpv
 keccak256(base58'37BPKA')       # Returns 4qa5wNk4961VwJAjCKBzXiEvBQ2gBJoqDcLFRJTiSKpv
 keccak256(base64'UmlkZQ==')  # Returns 4qa5wNk4961VwJAjCKBzXiEvBQ2gBJoqDcLFRJTiSKpv

sha256(ByteVector): ByteVector
""""""""""""""""""""""""""""""

Range of functions that hash an array of bytes using SHA-256.

.. csv-table:: sha256
  :file: _static/03_advanced/tables/105_sha256.csv
  :header-rows: 1 
  :class: longtable
  :widths: 4 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/106_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

:strong:`Example`

.. code-block:: none
  
 sha256("Ride".toBytes())        # Returns 5YxvrKsjJtq4G325gRVxbXpkox1sWdHUGVJLnRFqTWD3
 sha256(125.toBytes())            # Returns A56kbJjy7A4B9Pa5tUgRNvtCHSsZ7pZVJuPsLT2vtPSU
 sha256(base16'52696465')   # Returns 5YxvrKsjJtq4G325gRVxbXpkox1sWdHUGVJLnRFqTWD3
 sha256(base58'37BPKA')       # Returns 5YxvrKsjJtq4G325gRVxbXpkox1sWdHUGVJLnRFqTWD3
 sha256(base64'UmlkZQ==')  # Returns 5YxvrKsjJtq4G325gRVxbXpkox1sWdHUGVJLnRFqTWD3

List Functions
^^^^^^^^^^^^^^

.. csv-table:: List Functions
  :file: _static/03_advanced/tables/107_List-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

A, B, T means any valid type.

cons(A, List[B]): List[A|B]
"""""""""""""""""""""""""""

Inserts element to the beginning of the :ref:`list <03_advanced:List>`.

.. code-block:: none

 cons(head:T, tail: List[T]): List[T]

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/108_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 cons("Hello", ["World", "."]) # Returns ["Hello", "World", "."]
 cons(1, [2, 3, 4, 5]) # Returns [1, 2, 3, 4, 5]

containsElement(List[T], T): Boolean
""""""""""""""""""""""""""""""""""""

Check if the element is in the :ref:`list <03_advanced:List>`.

.. code-block:: none

 containsElement(list: List[T], element: T): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/109_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getElement(List[T], Int): T
"""""""""""""""""""""""""""

Gets the element from the :ref:`list <03_advanced:List>` by index.

.. code-block:: none

 getElement(arr: List[T], pos: Int): T

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/110_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 getElement(["Hello", "World", "."], 0)  # Returns "Hello"
 getElement([false, true], 1) # Returns true 

indexOf(List[T], T): Int|Unit
"""""""""""""""""""""""""""""

Returns the index of the first occurrence of the element in the :ref:`list <03_advanced:List>` or unit if the element is missing.

.. code-block:: none

 indexOf(list: List[T], element: T): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/111_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let stringList = ["a","b","a","c"]
 indexOf("a", stringList) # Returns 0

lastIndexOf(List[T], T): Int|Unit
"""""""""""""""""""""""""""""""""

Returns the index of the last occurrence of the element in the :ref:`list <03_advanced:List>` or unit if the element is missing.

.. code-block:: none

 lastIndexOf(list: List[T], element: T): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/112_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let stringList = ["a","b","a","c"]
 lastIndexOf("a", stringList) # Returns 2

max(List[Int]): Int
"""""""""""""""""""

Returns the largest element in the :ref:`list <03_advanced:List>` of integers. Fails if the list is empty.

.. code-block:: none

 max(List[Int]): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/113_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

max(List[BigInt]): BigInt
"""""""""""""""""""""""""

Returns the largest element in the list of :ref:`big integers <03_advanced:BigInt>`. Fails if the list is empty.

.. code-block:: none

 max(List[BigInt]): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/114_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

min(List[Int]): Int
"""""""""""""""""""

Returns the smallest element in the :ref:`list <03_advanced:List>` of integers. Fails if the list is empty.

.. code-block:: none

 min(List[Int]): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/115_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

min(List[BigInt]): BigInt
"""""""""""""""""""""""""

Returns the smallest element in the list of :ref:`big integers <03_advanced:BigInt>`. Fails if the list is empty.

.. code-block:: none

 min(List[BigInt]): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/116_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

removeByIndex(List[T], Int): List[T]
""""""""""""""""""""""""""""""""""""

Removes an element from the :ref:`list <03_advanced:List>` by index.

.. code-block:: none

 removeByIndex(list: List[T], index: Int): List[T]

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/117_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 removeByIndex(["Ride", 42, true], 1) # Returns ["Ride", true]

size(List[T]): Int
""""""""""""""""""

Returns the size of the :ref:`list <03_advanced:List>`.

.. code-block:: none

 size(arr: List[T]): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/118_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 size(["Hello", "World", "."]) # Returns 3

Math Functions
^^^^^^^^^^^^^^

.. csv-table:: Math Functions
  :file: _static/03_advanced/tables/119_Math-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

fraction(Int, Int, Int): Int
""""""""""""""""""""""""""""

Multiplies :ref:`integers <03_advanced:Int>` :math:`a`, :math:`b` and divides the result by the integer :math:`c` to avoid overflow.

Fraction :math:`a × b / c` should not exceed the maximum value of the integer type :math:`9,223,372,036,854,755,807`.

The rounding method is DOWN, see rounding variables below.

.. code-block:: none

 fraction(a: Int, b: Int, c: Int): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/120_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

Lets assume that:

:math:`a = 100,000,000,000`,

:math:`b = 50,000,000,000,000`,

:math:`c = 2,500,000`.

The following formula, with :ref:`operators <03_advanced:Operators>` \* and /, fails due to overflow:

.. code-block:: none

 a * b / c #  overflow, because a × b exceeds max integer value

The fraction function with no overflow:

.. code-block:: none

 fraction(a, b, c) # Result: 2,000,000,000,000,000,000

fraction(Int, Int, Int, Union): Int
"""""""""""""""""""""""""""""""""""

Multiplies :ref:`integers <03_advanced:Int>` :math:`a`, :math:`b` and divides the result by the integer :math:`c` to avoid overflow, applying the specified rounding method.

Fraction :math:`a × b / c` should not exceed the maximum value of the integer type :math:`9,223,372,036,854,755,807`.

.. code-block:: none

 fraction(a: Int, b: Int, c: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/121_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

fraction(BigInt, BigInt, BigInt): BigInt
""""""""""""""""""""""""""""""""""""""""

Multiplies :ref:`integers <03_advanced:Int>` :math:`a`, :math:`b` and divides the result by the integer :math:`c` to avoid overflow, applying the specified rounding method.

Fraction :math:`a × b / c` should not exceed the maximum value of the integer type :math:`9,223,372,036,854,755,807`.

.. code-block:: none

 fraction(a: BigInt, b: BigInt, c: BigInt): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/122_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

fraction(BigInt, BigInt, BigInt, Union): BigInt
"""""""""""""""""""""""""""""""""""""""""""""""

Multiplies :ref:`integers <03_advanced:Int>` :math:`a`, :math:`b` and divides the result by the integer :math:`c` to avoid overflow, applying the specified rounding method.

Fraction :math:`a × b / c` should not exceed the maximum value of the integer type :math:`9,223,372,036,854,755,807`.

.. code-block:: none

 fraction(a: BigInt, b: BigInt, c: BigInt, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/123_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

log(Int, Int, Int, Int, Int, Union): Int
""""""""""""""""""""""""""""""""""""""""

Calculates :math:`\log_b a`.

.. code-block:: none

 log(value: Int, vp: Int, base: Int, bp: Int, rp: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): Int

In Ride, there is no :ref:`data type <03_advanced:Data Types>` with the floating point. That is why, for example, when you need to calculate :math:`\log_{2.7} 16.25` then the number value :math:`= 1625`, vp :math:`= 2` and the base :math:`= 27`, bp :math:`= 1`.

If the log function returns, for example, :math:`2807035420964590265`, and the parameter rp :math:`= 18`, then the result is :math:`2.807035420964590265`; in the number :math:`2807035420964590265` the last :math:`18` digits is a fractional part.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/124_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

:strong:`Example`

:math:`\log_{2.7} 16.25 = 2.807035421...`

.. code-block:: none

 log(1625, 2, 27, 1, 2, HALFUP) # Function returns 281, so the result is: 2.81
 log(1625, 2, 27, 1, 5, HALFUP) # Function returns 280703542, so the result is: 2.80704
 log(0, 0, 2, 0, 0, HALFUP)     # Result: -Infinity

log(BigInt, Int, BigInt, Int, Int, Union): BigInt
"""""""""""""""""""""""""""""""""""""""""""""""""

Calculates :math:`\log_b a` with high accuracy.

.. code-block:: none

 log(value: BigInt, ep: Int, base: BigInt, bp: Int, rp: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/125_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

median(List[Int]): Int
""""""""""""""""""""""

Returns the median of the :ref:`list <03_advanced:List>` of integers. Fails if the list is empty.

.. code-block:: none

 median(arr: List[Int]): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/126_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 median([1, 2, 3])         # Returns 2
 median([2, 4, 9, 20])     # Returns 6
 median([-2, -4, -9, -20]) # Returns -7

median(List[BigInt]): BigInt
""""""""""""""""""""""""""""

Returns the median of a :ref:`list <03_advanced:List>` of :ref:`big integers <03_advanced:BigInt>`. Fails if the list is empty or contains more than :math:`100` elements.

.. code-block:: none

 median(arr: List[BigInt]): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/127_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

pow(Int, Int, Int, Int, Int, Union): Int
""""""""""""""""""""""""""""""""""""""""

Calculates :math:`a^{b}`.

.. code-block:: none

 pow(base: Int, bp: Int, exponent: Int, ep: Int, rp: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/128_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

:strong:`Example`

:math:`16.25^{2.7} = 1859,1057168...`

.. code-block:: none

 pow(1625, 2, 27, 1, 2, HALFUP) # function returns 185911, so the result is: 1859.11
 pow(1625, 2, 27, 1, 5, HALFUP) # function returns 185910572, so, the result is: 1859.10572

pow(BigInt, Int, BigInt, Int, Int, Union): BigInt
"""""""""""""""""""""""""""""""""""""""""""""""""

Calculates :math:`a^{b}` with high accuracy.

.. code-block:: none

 pow(base: BigInt, bp: Int, exponent: BigInt, ep: Int, rp: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/129_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

Rounding Variables
""""""""""""""""""

Below is the list of built-in rounding variables. The rounding variables are only used as the parameters of functions fraction, log, pow.

:strong:`Parameters`

.. csv-table:: Rounding Variables
  :file: _static/03_advanced/tables/130_Rounding-Variables.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

:strong:`Example`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/131_Example.csv
  :header-rows: 1 
  :class: longtable
  :widths: 3 1 1 1 1 1

String Functions
^^^^^^^^^^^^^^^^

.. csv-table:: String Functions
  :file: _static/03_advanced/tables/132_String-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

contains(String, String): Boolean
"""""""""""""""""""""""""""""""""

Checks whether the string contains substring.

.. code-block:: none

 contains(haystack: String, needle: String): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/133_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 "hello".contains("hell") # Returns true
 "hello".contains("world") # Returns false

drop(String, Int): String
"""""""""""""""""""""""""

Drops the first n characters of a string.

.. code-block:: none

 drop(xs: String, number: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/134_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 drop("Apple", 0) # Returns "Apple"
 drop("Apple", 1) # Returns "pple"
 drop("Apple", 3) # Returns "le"
 drop("Apple", 5) # Returns an empty string
 drop("Apple", 15) # Returns an empty string

dropRight(String, Int): String
""""""""""""""""""""""""""""""

Drops the last n characters of a string.

.. code-block:: none

 dropRight(xs: String, number: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/135_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 dropRight("Apple", 0) # Returns "Apple"
 dropRight("Apple", 1) # Returns "Appl"
 dropRight("Apple", 3) # Returns "Ap"
 dropRight("Apple", 5) # Returns an empty string
 dropRight("Apple", 15) # Returns an empty string

indexOf(String, String): Int|Unit
"""""""""""""""""""""""""""""""""

Returns the index of the first occurrence of a substring.

.. code-block:: none

 indexOf(str: String, substr: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/136_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 indexOf("Apple","ple") # Returns 3
 indexOf("Apple","le") # Returns 4
 indexOf("Apple","e") # Returns 5

indexOf(String, String, Int): Int|Unit
""""""""""""""""""""""""""""""""""""""

Returns the index of the first occurrence of a substring after a certain index.

.. code-block:: none

 indexOf(str: String, substr: String, offset: Int): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/137_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 indexOf("Apple","ple", 1) # Returns 2
 indexOf("Apple","le", 2) # Returns 3
 indexOf("Apple","e", 3) # Returns 4

lastIndexOf(String, String): Int|Unit
"""""""""""""""""""""""""""""""""""""

Returns the index of the last occurrence of a substring.

.. code-block:: none

 lastIndexOf(str: String, substr: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/138_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 lastIndexOf("Apple","pp") # Returns 1
 lastIndexOf("Apple","p") # Returns 2
 lastIndexOf("Apple","s") # Returns unit

lastIndexOf(String, String, Int): Int|Unit
""""""""""""""""""""""""""""""""""""""""""

Returns the index of the last occurrence of a substring before a certain index.

.. code-block:: none

 lastIndexOf(str: String, substr: String, offset: Int): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/139_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 lastIndexOf("mamamama","ma",4) # Returns 4
 lastIndexOf("mamamama","ma",3) # Returns 2

makeString(List[String], String): String
""""""""""""""""""""""""""""""""""""""""

Concatenates list strings adding a separator.

.. code-block:: none

 makeString(arr: List[String], separator: String): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/140_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 makeString(["Apple","Orange","Mango"], " & ") # Returns "Apple & Orange & Mango"

size(String): Int
"""""""""""""""""

Returns the size of a string.

.. code-block:: none

 size(xs: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/141_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 size("Ap") # Returns 2
 size("Appl") # Returns 4
 size("Apple") # Returns 5

split(String, String): List[String]
"""""""""""""""""""""""""""""""""""

Splits a string delimited by a separator into a list of substrings.

.. code-block:: none

 split(str: String, separator: String): List[String]

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/142_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 split("A.p.p.l.e", ".") # Returns ["A", "p", "p", "l", "e"]
 split("Apple", ".") # Returns ["Apple"]
 split("Apple", "") # Returns ["A", "p", "p", "l", "e"]
 split("Ap.ple", ".") # Returns ["Ap","ple"]

take(String, Int): String
"""""""""""""""""""""""""

Takes the first n characters from a string.

.. code-block:: none

 take(xs: String, number: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/143_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 take("Apple", 0) # Returns an empty string
 take("Apple", 1) # Returns "A"
 take("Apple", 3) # Returns "App"
 take("Apple", 5) # Returns "Apple"
 take("Apple", 15) # Returns "Apple"
 take("Apple", -10) # Returns an empty string

takeRight(String, Int): String
""""""""""""""""""""""""""""""

Takes the last n characters from a string.

.. code-block:: none

 takeRight(xs: String, number: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/144_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 takeRight("Apple", 0) # Returns an empty string
 takeRight("Apple", 1) # Returns "A"
 takeRight("Apple", 3) # Returns "ple"
 takeRight("Apple", 5) # Returns "Apple"
 takeRight("Apple", 15) # Returns "Apple"

Union Functions
^^^^^^^^^^^^^^^

.. csv-table:: Union Functions
  :file: _static/03_advanced/tables/145_Union-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

isDefined(T|Unit): Boolean
""""""""""""""""""""""""""

Checks if an argument is not unit.

.. code-block:: none

 isDefined(a: T|Unit): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/146_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

value(T|Unit): T
""""""""""""""""

Gets a value from a :ref:`union <03_advanced:Union>` type argument. Fails if it is :ref:`unit <03_advanced:Unit>`.

.. code-block:: none

 value(a: T|Unit): T

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/147_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

valueOrElse(T|Unit, T): T
"""""""""""""""""""""""""

Returns a value from a :ref:`union <03_advanced:Union>` type argument if it's not :ref:`unit <03_advanced:Unit>`. Otherwise, returns the second argument.

.. code-block:: none

 valueOrElse(t: T|Unit, t0: T): T

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/148_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

valueOrErrorMessage(T|Unit, String): T
""""""""""""""""""""""""""""""""""""""

Returns a value from a :ref:`union <03_advanced:Union>` type argument if it's not :ref:`unit <03_advanced:Unit>`. Otherwise, fails with the message specified in the second argument.

.. code-block:: none

 valueOrErrorMessage(a: T|Unit, msg: String): T

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/149_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Verification Functions
^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Verification Functions
  :file: _static/03_advanced/tables/150_Verification-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

bn256groth16Verify(ByteVector, ByteVector, ByteVector): Boolean
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Range of functions. Check zk-SNARK by groth16 protocol on the bn254 curve. (Although the curve is called bn254 in the scientific literature, it is commonly referred to as bn256 in the code.)

.. csv-table:: bn256groth16Verify
  :file: _static/03_advanced/tables/151_bn256groth16Verify.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/152_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

createMerkleRoot(List[ByteVector], ByteVector, Int) : ByteVector
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Calculates the Merkle root hash for transactions of block on the basis of the transaction hash and the sibling hashes of the Merkle tree. BLAKE2b-256 algorithm is used for hashing. To check for the transaction in the block, you need to compare the calculated hash with the transactionsRoot field in the block header. For more informtion see the :ref:`transactions root hash <02_intermediate:Transactions Root Hash>`.

.. code-block:: none

 createMerkleRoot(merkleProofs: List[ByteVector], valueBytes: ByteVector, index: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/153_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

ecrecover(messageHash: ByteVector, signature: ByteVector)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Recovers public key from the message hash and the ECDSA digital signature based on the secp256k1 elliptic curve. Fails if the recovery failed. The public key is returned in uncompressed format (64 bytes). The function can be used to verify the digital signature of a message by comparing the recovered public key with the sender’s key.

.. code-block:: none

 ecrecover(messageHash: ByteVector, signature: ByteVector): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/154_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

Verify the transaction of the Ethereum blockchain using the following data:

* The transaction.
* The signature that is generated by the ecsign functions (r, s, and v bytes concatenation).
* Sender public key.

.. code-block:: none

 func check(t: ByteVector, signature: ByteVector, publicKey: ByteVector) = {
  ecrecover(keccak256(t), signature) == publicKey
 } 

groth16Verify(ByteVector, ByteVector, ByteVector): Boolean
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Range of functions. Check zk-SNARK by groth16 protocol.

.. csv-table:: groth16Verify
  :file: _static/03_advanced/tables/155_groth16Verify.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/156_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 groth16Verify(vk, proof, inputs) 

rsaVerify(digestAlgorithmType, ByteVector, ByteVector, ByteVector): Boolean
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Range of functions. Check that the RSA digital signature is valid, i.e. it was created by the owner of the public key.

.. csv-table:: rsaVerify
  :file: _static/03_advanced/tables/157_rsaVerify.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 1 1

The recommended RSA key module length is at least 2048 bits. Data can be hashed before signing using one of the following algorithms:

* MD5
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512
* SHA3-224
* SHA3-256
* SHA3-384
* SHA3-512

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/158_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

sigVerify(ByteVector, ByteVector, ByteVector): Boolean
""""""""""""""""""""""""""""""""""""""""""""""""""""""

Range of functions. Check that the Curve25519 digital signature is valid, i.e. it was created by the owner of the public key.

.. csv-table:: sigVerify
  :file: _static/03_advanced/tables/159_sigVerify.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: _static/03_advanced/tables/160_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Exceptions
==========

There is no exception handling in Ride: after an exception has been thrown, the script execution fails. The transaction can be either discarded or saved on the blockchain as failed, see the :ref:`transaction validation <02_intermediate:Transaction Validation>` article for details
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

************
Script Types
************

There are three types of scripts:

* :ref:`dApp script <03_advanced:dApp Script>` enables you to define :ref:`сallable functions <03_advanced:Callable Functions>` that can be called from other accounts, accept payments to the dApp, and perform various actions on the blockchain. Also dApp script can comprise a verifier function that allows or denies transactions and orders that are sent on behalf of the dApp account.
* :ref:`Account script <03_advanced:Account Script>` allows or denies transactions and orders that are sent on behalf of the account (like a verifier function of a dApp script).
* :ref:`Asset script <03_advanced:Asset Script>` allows or denies transactions involving the asset.

Features of each script type are described in the table.

.. csv-table:: Script Types
  :file: _static/03_advanced/tables/161_Script-Types.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4 2 2

dApp Script
===========

dApp script enables you to define callable functions that can be called from other accounts by sending an :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>` or by a :ref:`dApp-to-dApp invocation <03_advanced:dApp-to-App Invocation>`.
Callable functions can accept payments to the dApp and perform various actions on the blockchain. Also dApp script can comprise a verifier function that allows or denies transactions and orders that are sent on behalf of the dApp account. An account with a dApp script assigned to it is called a dApp. 

dApp Script Format
------------------

The script code is composed of the following parts:

* Directives
* Auxiliary definitions
* Callable function
* Verifier function

.. image:: _static/02_intermediate/images/image.jpg

Directives
^^^^^^^^^^

The dApp script should start with directives:

.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

The above directives tell the compiler that:

* The script uses the standard library version 5.
* The script contains a set of definitions.
* The script will be assigned to an account (not asset).

Auxiliary definitions
^^^^^^^^^^^^^^^^^^^^^

After the directives, you can define auxiliary variables and functions. These variables and functions are accessible within the entire script. Please note that functions without annotations cannot be called from other accounts. Let's see an exaxmple:

.. code-block:: none

 let someConstant = 42
 func doSomething() = {
  1+1
 }

Callable Functions (dApp Script)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The callable function should be marked with the @Callable(i) annotation, where i is an :ref:`invocation <03_advanced:Invocation>` structure that contains fields of the script invocation that are accessible to the callable function. The variable name in the annotation is required even if the function does not use it. 
Callable function result is a set of :ref:`script actions <03_advanced:Script Actions>` that are performed on the blockchain: adding/deleting/modifying entries to the account data storages, token transfers, issue/reissue/burning, and others. The result format and the available actions depend on the Standard library version used.
For a detailed description, see the :ref:`callable function <03_advanced:Callable Functions>` article.

In the example below the callable function transfers 1 DecentralCoin to an account that called it and records the request information in the account data storage. If the same account tries to call the function again, the callable function throws an exception.

.. code-block:: none

 @Callable(i)
 func faucet () = {
  let isKnownCaller =  match getBoolean(this, toBase58String(i.caller.bytes)) {
    case hist: Boolean =>
      hist
    case _ =>
      false
  }
  if (!isKnownCaller) then 
  (
    [
      BooleanEntry(toBase58String(i.caller.bytes), true),
      ScriptTransfer(i.caller, 100000000, unit)
    ],
    unit
  )
  else throw("Can be used only once")
 }

Verifier Function
^^^^^^^^^^^^^^^^^

Verifier function checks transactions and orders that are sent on behalf of the dApp account for compliance with the specified conditions (in other words it works similar to the account script).
The verifier function should be marked with the @Verifier(tx) annotation, where tx is the transaction or the order that the function is currently checking. The variable name in the annotation is required even if the function does not use it.
The verifier function has no arguments.Possible results of the verifier function are:

* True (the transaction or the order is allowed),
* False (the transaction or the order is denied),
* An error (the transaction or the order is denied).

For a detailed description, see verifier function the article.
Using the :ref:`match ... case <03_advanced:Match-Case>` operator, you can set up different conditions depending on the type of the transaction/order. For example, the following function allows :ref:`transfer transactions <02_intermediate:Transfer Transaction>` and denies orders and other types of transactions.

.. code-block:: none

 @Verifier(tx)
 func verify() = {
  match tx {
    case ttx:TransferTransaction => sigVerify(ttx.bodyBytes, ttx.proofs[0], ttx.senderPublicKey)
    case _ => false
  }
 }

dApp script that has no verifier function performs default verification, that is, checking that the transaction or the order is indeed signed by this account.

Failed Transactions
-------------------

If the callable function failed or threw an :ref:`exception <03_advanced:Exceptions>` when a block generator adds the transaction to a block, such a transaction is saved on the blockchain and marked with the attribute "applicationStatus": "script_execution_failed", provided that: There are two annotations: @Callable(i) and @Verifier(tx). The variable name in the annotation is required even if the function does not use it.
An annotated function cannot be called inside a dApp script.

* The :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>` passed the sender signature verification or the account script verification.
* The complexity of performed computations exceeded the :ref:`threshold for saving failed transactions <03_advanced:Limitations>`.

The transaction sender is charged a fee. The transaction doesn't entail any other changes on the blockchain.

Data Accessible to dApp Script
------------------------------

Data accessible to the callable function:

* Particular fields of the invocation, including payments, fee, sender address and public key. See the :ref:`invocation <03_advanced:Invocation>` article for the fields description. Proofs are inaccessible.
* Blockchain data: current height, account balances, entries in account data storages, parameters of tokens, etc.

Data accessible to the verifier function:

* Fields of the current verified transaction/order, including proofs. The built-in variable tx contains this transaction or order. The set of fields depends on the type of transaction/order, see the :ref:`transaction structures <03_advanced:Transaction Structures>` chapter and :ref:`order <03_advanced:Order>` article.
* Blockchain data: current height, account balances, entries in account data storages, parameters of tokens, etc.

Annotations
-----------

Annotation is a form of metadata that is added to a :ref:`function <03_advanced:Functions>` of a :ref:`dApp script <03_advanced:dApp Script>`. At the present moment, there are two annotations: @Callable(i) and @Verifier(tx). The variable name in the annotation is required even if the function does not use it.
An annotated function cannot be called inside a dApp script.

@Callable(i)
^^^^^^^^^^^^

Annotation of a :ref:`callable function <03_advanced:Callable Functions>`.
Variable i contains an :ref:`invocation <03_advanced:Invocation>` structure representing certain fields of the invocation.

@Verifier(tx)
^^^^^^^^^^^^^

Annotation of a verifier function.
Variable tx contains a structure of transaction or :ref:`order <03_advanced:Order>` sent from a dApp's account.

Callable Function
------------------

Callable function is a :ref:`dApp script <03_advanced:dApp Script>` function which can be invoked by a :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>` or an invoke or reentrantInvoke functions (see details in the :ref:`dApp-to-dApp invocation functions <03_advanced:dApp-to-dApp Invocation Functions>` article).

* Add, modify, delete dApp :ref:`account data storage <02_intermediate:Account Data Storage>` entries.
* Transfer tokens.
* Add, modify, delete dApp.
* Issue tokens on behalf of the dApp, reissue and burn tokens.
* Setup :ref:`sponsorship <02_intermediate:How to Enable Sponsorship>`.
* Lease, cancel lease.

The callable function can return a value that is passed to the invoking function in case of the :ref:`dApp-to-dApp invocation <03_advanced:dApp-to-App Invocation>`.
The invocation can contain payments to dApp. Tokens obtained in these payments can be used in script actions performed by the callable function and in payments attached to nested invocations.

Annotation
^^^^^^^^^^

The callable function should be marked with the @Callable(i) annotation, where i is an :ref:`invocation <03_advanced:Invocation>` structure that contains invocation fields that are available to the callable function. The variable name in the annotation is required even if the callable function does not use it.

Arguments
^^^^^^^^^

The callable function can have arguments of the following types:

* The script uses the standard library version 5.
* :ref:`Boolean <03_advanced:Boolean>`
* :ref:`ByteVector <03_advanced:ByteVector>`
* :ref:`Int <03_advanced:Int>`
* :ref:`String <03_advanced:String>`
* :ref:`Union <03_advanced:Union>` with elements having types listed above.
* :ref:`List <03_advanced:List>` with elements having types listed above.

Invocation Result
^^^^^^^^^^^^^^^^^

The callable function invocation result is a :ref:`tuple <03_advanced:Tuple>` of two elements:
List of script actions. Actions are executed in the same order as the elements in the list.
Return value that is passed to the invoking function in case of the :ref:`dApp-to-dApp invocation <03_advanced:dApp-to-App Invocation>`.

Let's see an example of invocation of an invocation result:

.. code-block:: none

  (
    [
      BooleanEntry("key1", true),
      IntegerEntry("key2", 42),
      StringEntry("key3", "some string"),
      BinaryEntry("key4", base58'encoded'),
      DeleteEntry("key5"),
      ScriptTransfer(Address(base58'3Ms8fSfAxBLDjKvNVgACRzQoBLCtCWxtawu'), 100, base58'someAssetid'),
      Issue("RegularToken", "This is an ordinary token", 10000, 2, true),
      Reissue("4ZzED8WJXsvuo2MEm2BmZ87Azw8Sx7TVC6ufSUA5LyTV", 1000, true),
      Burn("4ZzED8WJXsvuo2MEm2BmZ87Azw8Sx7TVC6ufSUA5LyTV", 1000)]
      SponsorFee("4ZzED8WJXsvuo2MEm2BmZ87Azw8Sx7TVC6ufSUA5LyTV", 300),
      Lease(Address(base58'3Mn5hzck8nYd52Ytd2ZjzoiQLVoMcn1VAs9',1000),
      LeaseCancel(base58'Pxaf8pGKHS5ufGhqjmwRRcHQtC9T3h4d1XaJMnkhR1Vt')
    ],
    42
  )

Script Actions (Callable Function)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Script actions performed by the callable function are set by Ride structures.

.. csv-table:: Script Actions (Callable Function)
  :file: _static/03_advanced/tables/162_Script-Actions-(Callable-Function).csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 5

Limitations  (Callable Function)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The maximum total number of Issue, Reissue, Burn, SponsorFee, ScriptTransfer, Lease, LeaseCancelscript actions executed by all callable functions in a single transaction is :math:`30`.
* The maximum total number of BinaryEntry, BooleanEntry, IntegerEntry, StringEntry, DeleteEntryscript actions executed by all callable functions in a single transaction is :math:`100`.
* The maximum number of the payments to dApp in invocation is :math:`10`.

See also the :ref:`limitations <03_advanced:Limitations>` article.

Example
^^^^^^^

The example listed below is a wallet application which allows sending DecentralCoins to a certain address and withdrawing them (withdrawing others' DecentralCoins is prevented). There are two callable functions in the example(deposit and withdraw):
 
.. code-block:: none

 {-# STDLIB_VERSION 5 #-}
 {-# CONTENT_TYPE DAPP #-}
 {-# SCRIPT_TYPE ACCOUNT #-}

 @Callable(i)
 func deposit() = {
  let pmt =
    if i.payments.size() == 1 then
      i.payments[0]
    else throw("Attached payment is required")
  if (isDefined(pmt.assetId))
    then throw("Works with DecentralCoins only")
    else {
      let currentKey = toBase58String(i.caller.bytes)
      let currentAmount = match getInteger(this, currentKey) {
        case a:Int => a
        case _ => 0
      }
      let newAmount = currentAmount + pmt.amount
      (
        [
          IntegerEntry(currentKey, newAmount)
        ],
        unit
      )
    }
 }

 @Callable(i)
 func withdraw(amount: Int) = {
  let currentKey = toBase58String(i.caller.bytes)
  let currentAmount = match getInteger(this, currentKey) {
    case a:Int => a
    case _ => 0
  }
  let newAmount = currentAmount - amount
  if (amount < 0)
    then throw("Can't withdraw negative amount")
    else if (newAmount < 0)
      then throw("Not enough balance")
      else (
        [
          IntegerEntry(currentKey, newAmount),
          ScriptTransfer(i.caller, amount, unit)
        ],
        unit
      )
 }

 @Verifier(tx)
 func verify() = false

Threshold for Saving Failed Transactions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Invoke Script transaction is saved on the blockchain and a fee is charged for it even if the dApp script or the asset script fails when a block generator adds the transaction to a block, provided that the sender's signature or account script verification passed.

However, if the callable function failed or :ref:`threw an exception <03_advanced:Exceptions>` before the :ref:`complexity <03_advanced:Script Complexity>` of performed calculations exceeded the :ref:`threshold for saving failed transactions <03_advanced:Limitations>`, the transaction is discarded and the fee is not charged.

Verifier Function
------------------

Verifier function is a function of :ref:`dApp script <03_advanced:dApp Script>` that is responsible for :ref:`verification of transactions <02_intermediate:Transaction Validation>` and orders sent from a :ref:`dApp <02_intermediate:dApp and Smart Account>` account. The verifier function does the same as an :ref:`account script <03_advanced:Account Script>`.
dApp script can have only one verifier function. The verifier function should be adorned with the @Verifier(tx) annotation, where tx: Transaction|Order is the transaction or the order that the function is currently checking.
Verifier function has no arguments.
Verifier function can have one of the following execution results:

* True (the transaction or the order is allowed).
* False (the transaction or the order is denied).
* an error (the transaction or the order is denied).

dApp that has no verifier function performs default verification, that is, checking that the first proof of the transaction/order has the correct sender's signature. The following function does the same as the default implementation:

.. code-block:: none

 @Verifier(tx)
 func verify() = {
  sigVerify(tx.bodyBytes, tx.proofs[0], tx.senderPublicKey)
 }

If the verifier function is defined, only verification by this function is performed, proofs are not checked additionally.

Example
^^^^^^^

dApp with the verifier function listed below only allows :ref:`transfer transaction <02_intermediate:Transfer Transaction>` with an amount of token lower than 100. Orders and other transactions are denied. The match operator is used to specify verification rules depending on the type of the transaction/order.
 
.. code-block:: none
  
 @Verifier(tx)
 func verify() = {
    match tx {
      case ttx:TransferTransaction => ttx.amount < 100 && sigVerify(ttx.bodyBytes, ttx.proofs[0], ttx.senderPublicKey)
      case _ => false
    }
 }

See available fields for each transaction type in the :ref:`transaction structures <03_advanced:Transaction Structures>` article.

Account Script
==============

Account script verifies transactions and orders that are sent on behalf of the account. That is, the account script allows or denies the transaction or the order depending on whether it meets the specified conditions.

Account Script Format
---------------------

The script code is composed of the following parts:

* Directives
* Auxiliary definitions
* Boolean expression

.. image:: _static/02_intermediate/images/image.jpg

Directives
^^^^^^^^^^

The account script should start with directives:

.. code-block:: none

 {- # STDLIB_VERSION 5 # -}
 {- # CONTENT_TYPE EXPRESSION # -}
 {- # SCRIPT_TYPE ACCOUNT # -}

The above directives tell the compiler that:

* The script uses the standard library version 5.
* The script contains a boolean expression.
* The script will be assigned to an account (not asset).


Auxiliary Definitions
^^^^^^^^^^^^^^^^^^^^^

After the directives, you can define auxiliary variables and functions. Let's see an example:

.. code-block:: none

 let someConstant = 42
 func doSomething () = {
  height + someConstant
 }

Boolean Expression
^^^^^^^^^^^^^^^^^^

The expression checks transactions and orders that are sent on behalf of the account for compliance with the specified conditions. If the conditions are not met, the transaction/order is denied. Possible results of evaluating the expression are:

* True (the transaction or the order is allowed),
* False (the transaction or the order is denied),
* An error (the transaction or the order is denied).

Using the :ref:`match ... case <03_advanced:Match-Case>`, you can set up different conditions depending on the type of the transaction/order. For example, the following expression prohibits sending orders and changing the account script, and allows other transactions, provided that the array of confirmations (proofs) contains the correct signature of the account at position :math:`0`:

.. code-block:: none

 match tx {
  case t: Order | SetScriptTransaction => false
  case _ => sigVerify (tx.bodyBytes, tx.proofs [0], tx.senderPublicKey)
 }

Data Accessible to Account Script
---------------------------------

The following data can be used for checks:

* Fields of the current verified transaction/order, including proofs. The built-in variable tx contains this transaction or order. The set of fields depends on the type of transaction/order, see the :ref:`transaction structures <03_advanced:Transaction Structures>` chapter and :ref:`order <03_advanced:Order>` article.
* Blockchain data: current height, account balances, entries in account data storages, parameters of tokens, etc.

Asset Script
============

Asset script verifies transactions within the :ref:`asset (token) <02_intermediate:Token (Asset)>`, that is, allows or denies the transaction depending on the specified conditions. Asset with a script assigned to it is called a :ref:`smart asset <02_intermediate:Smart Asset>`.
Keep the following in mind:

* The asset script can only verify transactions, but not orders.
* If a token is issued without a script, then the script cannot be added later.
* The script cannot be removed, so it is impossible to turn a smart asset into a regular one.
* Smart asset cannot be a sponsored asset.

Asset Script Format
-------------------

The script code is composed of the following parts:

* Directives
* Auxiliary definitions
* Boolean expression

.. image:: _static/02_intermediate/images/image.jpg

Directives
^^^^^^^^^^

The asset script should start with directives:

.. code-block:: none

 {- # STDLIB_VERSION 5 # -}
 {- # CONTENT_TYPE EXPRESSION # -}
 {- # SCRIPT_TYPE ACCOUNT # -}

The above directives tell the compiler that:

* The script uses the standard library version 5.
* The script contains a boolean expression.
* The script will be assigned to an asset.

Auxiliary Definitions
^^^^^^^^^^^^^^^^^^^^^

After the directives, you can define auxiliary variables and functions. Let's see an example:

.. code-block:: none

 let someConstant = 42
 func doSomething () = {
  height + someConstant
 }

Boolean Expression
^^^^^^^^^^^^^^^^^^

The expression checks transactions and orders that are sent on behalf of the account for compliance with the specified conditions. If the conditions are not met, the transaction/order is denied. Possible results of evaluating the expression are:

* True (the transaction or the order is allowed),
* False (the transaction or the order is denied),
* An error (the transaction or the order is denied).

Using the :ref:`match ... case <03_advanced:Match-Case>`, you can set up different conditions depending on the type of the transaction/order. For example, the following expression prohibits sending orders and changing the account script, and allows other transactions, provided that the array of confirmations (proofs) contains the correct signature of the account at position :math:`0`:

.. code-block:: none

 match tx {
  case t : SetAssetScriptTransaction => false
  case _ => true
 }

Failed Transactions
-------------------

If the asset script denies the Exchange transaction when a block generator adds the transaction to a block (provided that the sender signature verification or the account script verification passed), the transaction is saved on the blockchain but marked as failed ("applicationStatus": "script_execution_failed"). The sender of the transaction (matcher) is charged a fee. The transaction doesn't entail any other changes in balances, in particular, the order senders don't pay the matcher fee.

If the asset script denies the Invoke Script transaction when a block generator adds the transaction to a block (provided that the sender signature verification or the account script verification passed and the complexity of calculations performed by dApp script exceeded the :ref:`threshold for saving failed transactions <03_advanced:Limitations>`), the transaction is saved on the blockchain but marked as failed ("applicationStatus": script_execution_failed"). The transaction sender is charged a fee. The transaction doesn't entail any other changes on the blockchain.

Data Accessible to Asset Script
-------------------------------

The following data can be used for checks:

* Fields of the current verified transaction, excluding proofs. The built-in variable tx contains this transaction. The set of fields depends on the type of transaction, see the :ref:`transaction structures <03_advanced:Transaction Structures>` chapter.
* Blockchain data: current height, account balances, entries in account data storages, parameters of tokens, etc.

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

Script actions are executed, that is, they make changes on the blockchain only if they are included in the resulting expression of the callable function. See more details in the :ref:`callable function <03_advanced:Callable Functions>` article.

.. csv-table:: Script Actions
  :file: _static/03_advanced/tables/163_Script-Actions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 4

Available script actions depend on the standard library version used.

BinaryEntry
-----------

BinaryEntry is a structure that sets key and value of binary entry :ref:`account data storage <02_intermediate:Account Data Storage>`. Adding or changing an entry is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.

:strong:`Constructor`

.. code-block:: none

 BinaryEntry(key: String, value: ByteVector)

:strong:`Fields`

.. csv-table:: BinaryEntry Fields
  :file: _static/03_advanced/tables/164_BinaryEntry-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

BooleanEntry
------------

BooleanEntry is a structure that sets the key and value of the :ref:`account data storage <02_intermediate:Account Data Storage>` boolean entry. Adding or changing an entry is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.

:strong:`Constructor`

.. code-block:: none

 BooleanEntry(key: String, value: Boolean)

:strong:`Fields`

.. csv-table:: BooleanEntry Fields
  :file: _static/03_advanced/tables/165_BooleanEntry-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Burn
----

Burn is a structure that sets the parameters of the token burning. The token burning is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.
If the token is a smart asset, the asset script verifies the Burn action as if it were :ref:`BurnTransaction <03_advanced:BurnTransaction>` with the fee of :math:`0` and the version of :math:`0`. If the asset script denies the action, then the transaction that invoked the dApp script is either denied or saved on the blockchain as failed, see the :ref:`transaction validation <02_intermediate:Transaction Validation>`.

:strong:`Constructor`

.. code-block:: none

 Burn(assetId: ByteVector, quantity: Int)

:strong:`Fields`

.. csv-table:: Burn Fields
  :file: _static/03_advanced/tables/166_Burn-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

DeleteEntry
-----------

DeleteEntry is a structure that sets the parameters of deletion of entry from the :ref:`account data storage <02_intermediate:Account Data Storage>`. Deleting an entry is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.

:strong:`Constructor`

.. code-block:: none

 DeleteEntry(key: String)

:strong:`Fields`

.. csv-table:: DeleteEntry Fields
  :file: _static/03_advanced/tables/167_DeleteEntry-Fields.csv
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

IntegerEntry is a structure that sets the key and value of :ref:`account data storage <02_intermediate:Account Data Storage>` integer entry. Adding or changing an entry is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.

:strong:`Constructor`

.. code-block:: none

 IntegerEntry(key: String, value: Int)

:strong:`Fields`

.. csv-table:: IntegerEntry Fields
  :file: _static/03_advanced/tables/168_IntegerEntry-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Issue
-----

Issue is a structure that sets the parameters of the token issue. The token issue is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.
The minimum fee for an invoke script transaction is increased by :math:`1` DecentralCoin for each issued asset that is not :ref:`NFT <02_intermediate:Non-Fungible Token>`.
You can get the ID of the issued token using the :ref:`calculateAssetId <03_advanced:Blockchain Functions>` function.

:strong:`Constructor`

.. code-block:: none

 Issue(name: String, description: String, quantity: Int, decimals: Int, isReissuable: Boolean, compiledScript: Script|Unit, nonce: Int)

or

.. code-block:: none

 Issue(name: String, description: String, quantity: Int, decimals: Int, isReissuable: Boolean) 

In the second case, compiledScript = unit and nonce = 0 values are inserted automatically.

:strong:`Fields`

.. csv-table:: Issue Fields
  :file: _static/03_advanced/tables/169_Issue-Fields.csv
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

Lease is a structure that sets the lease parameters. The lease is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`. More about :ref:`lease <02_intermediate:Leased Proof of Stake>`.
You can get the lease ID using the :ref:`calculateLeaseId <03_advanced:Blockchain Functions>` function.

:strong:`Constructor`

.. code-block:: none

 Lease(recipient: Address|Alias, amount: Int, nonce: Int)

or

.. code-block:: none

 Lease(recipient: Address|Alias, amount: Int) 

In the second case, nonce = :math:`0` is inserted automatically.

:strong:`Fields`

.. csv-table:: Lease Fields
  :file: _static/03_advanced/tables/170_Lease-Fields.csv
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

LeaseCancel is a structure that sets the lease cancellation parameters. The lease cancellation is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.


:strong:`Constructor`

.. code-block:: none

 LeaseCancel(leaseId: ByteVector)

:strong:`Fields`

.. csv-table:: LeaseCancel Fields
  :file: _static/03_advanced/tables/171_LeaseCancel-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Reissue
-------

Reissue is a structure that sets the parameters of the token reissue. The token reissue is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.
The token reissue is only available for an asset that is issued by a dApp account.
If the token is a smart asset, the asset script verifies the Reissue action as if it were :ref:`ReissueTransaction <03_advanced:ReissueTransaction>` with the fee of 0 and the version of 0. If the asset script denies the action, then the transaction that invoked the dApp script is either denied or saved on the blockchain as failed, see the :ref:`transaction validation <02_intermediate:Transaction Validation>`.

:strong:`Constructor`

.. code-block:: none

 Reissue(assetId: ByteVector, quantity: Int, isReissuable: Boolean)

:strong:`Fields`

.. csv-table:: Reissue Fields
  :file: _static/03_advanced/tables/172_Reissue-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

ScriptTransfer
--------------

ScriptTransfer is a structure that sets the parameters of the token transfer. The token transfer is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.
If the token is a smart asset, the asset script verifies the ScriptTransfer action as if it were :ref:`TransferTransaction <03_advanced:TransferTransaction>` with the fee of :math:`0` and the version of :math:`0`. If the asset script denies the action, then the transaction that invoked the dApp script is either denied or saved on the blockchain as failed, see the :ref:`transaction validation <02_intermediate:Transaction Validation>`. 

:strong:`Constructor`

.. code-block:: none

 ScriptTransfer(recipient: Address|Alias, amount: Int, asset: ByteVector|Unit)

:strong:`Fields`

.. csv-table:: ScriptTransfer Fields
  :file: _static/03_advanced/tables/173_ScriptTransfer-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

SponsorFee
----------

SponsorFee is a structure that sets up sponsorship. For information about sponsorship, see the :ref:`sponsored fee <02_intermediate:Sponsored Fees>` article. The sponsorship setup is performed only if the structure is included in the resulting expression of the callable function. See details in the :ref:`callable function <03_advanced:Callable Functions>` article.
The sponsorship setup is only available if the asset is issued by a dApp account (by the same script invocation as well) and is not a smart asset.

:strong:`Constructor`

.. code-block:: none

 SponsorFee(assetId: ByteVector, minSponsoredAssetFee: Int|Unit)

:strong:`Fields`

.. csv-table:: SponsorFee Fields
  :file: _static/03_advanced/tables/174_SponsorFee-Fields.csv
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

StringEntry is a structure that sets key and value of :ref:`account data storage <02_intermediate:Account Data Storage>` string entry. Adding or changing an entry is performed only if the structure is included in the :ref:`callable function result <03_advanced:Invocation Result>`.

:strong:`Constructor`

.. code-block:: none

 BinaryEntry(key: String, value: String)

:strong:`Fields`

.. csv-table:: StringEntry Fields
  :file: _static/03_advanced/tables/175_StringEntry-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Common Structures
=================

.. csv-table:: Common Structures
  :file: _static/03_advanced/tables/176_Common-Structures.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

Address
-------

Structure of an :ref:`address <02_intermediate:Address>`.

:strong:`Constructor`

.. code-block:: none

 Address(bytes: ByteVector)

:strong:`Fields`

.. csv-table:: Address Fields
  :file: _static/03_advanced/tables/177_Address-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

Get all types of balance in DecentralCoins for the current account (in a dApp script or an account script):

.. code-block:: none

 wavesBalance(this)

For any account:

.. code-block:: none

 let address=base58'3N4iKL6ikwxiL7yNvWQmw7rg3wGna8uL6LU'
 wavesBalance(Address(address))

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

Structure of an :ref:`alias <02_intermediate:Alias>`.

:strong:`Constructor`

.. code-block:: none

 Alias(alias: String)

:strong:`Fields`

.. csv-table:: Alias Fields
  :file: _static/03_advanced/tables/178_Alias-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

:strong:`Example`

.. code-block:: none

 let alias = Alias("merry")
 addressFromRecipient(alias)

Asset
-----

Structure of a :ref:`token <02_intermediate:Token (Asset)>`. The structure is returned by the  :ref:`assetInfo <03_advanced:Blockchain Functions>` built-in function.

:strong:`Constructor`

.. code-block:: none

 Asset(id: ByteVector, quantity: Int, decimals: Int, issuer: Address, issuerPublicKey: ByteVector, reissuable: Boolean, scripted: Boolean, minSponsoredFee: Int|Unit, name: String, description: String)

:strong:`Fields`

.. csv-table:: Asset Fields
  :file: _static/03_advanced/tables/179_Asset-Fields.csv
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

Structure of a pair of :ref:`tokens <02_intermediate:Token (Asset)>` of an order within the :ref:`order <03_advanced:Order>` structure.

:strong:`Constructor`

.. code-block:: none

 AssetPair(amountAsset: ByteVector|Unit, priceAsset: ByteVector|Unit)

:strong:`Fields`

.. csv-table:: AssetPair Fields
  :file: _static/03_advanced/tables/180_AssetPair-Fields.csv
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

Structure of a payment attached to the script invocation and available to the :ref:`callable function <03_advanced:Callable Functions>`. The structure is used in:

* :ref:`Invocation <03_advanced:Invocation>` structure.
* :ref:`InvokeScriptTransaction <03_advanced:InvokeScriptTransaction>` structure.
* :ref:`Invoke <03_advanced:dApp-to-dApp Invocation Functions>` and :ref:`reentrantInvoke <03_advanced:dApp-to-dApp Invocation Functions>` functions.

:strong:`Constructor`

.. code-block:: none

 AttachedPayment(assetId: ByteVector|Unit, amount: Int)

:strong:`Fields`

.. csv-table:: AttachedPayment Fields
  :file: _static/03_advanced/tables/181_AttachedPayment-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

BalanceDetails
--------------

Structure that contains DecentralCoins balances of account. The structure is returned by the wavesBalance built-in function. For description of balance types, see the :ref:`account balance <02_intermediate:Account Balance>` article.

:strong:`Constructor`

.. code-block:: none

 BalanceDetails(available: Int, regular: Int, generating: Int, effective: Int)

:strong:`Fields`

.. csv-table:: BalanceDetails Fields
  :file: _static/03_advanced/tables/182_BalanceDetails-Fields.csv
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
  :file: _static/03_advanced/tables/183_BlockInfo-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Invocation
----------

Structure that contains the fields of the script invocation that the :ref:`callable function <03_advanced:Callable Functions>` can use.

:strong:`Constructor`

.. code-block:: none

 Invocation(caller: Address, callerPublicKey: ByteVector, originCaller: Address, originCallerPublicKey: ByteVector, payments: List[AttachedPayment], transactionId: ByteVector, fee: Int, feeAssetId: ByteVector|Unit)

:strong:`Fields`

The field values depend on how the callable function is invoked. If the callable function is invoked by an :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>`:

.. csv-table:: Invocation Fields 1
  :file: _static/03_advanced/tables/184_Invocation-Fields-1.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

If the callable function is invoked by the invoke or reentrantInvoke function (see the :ref:`dApp-to-dApp invocation <03_advanced:dApp-to-App Invocation>` article):

.. csv-table:: Invocation Fields 2
  :file: _static/03_advanced/tables/185_Invocation-Fields-2.csv
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

Structure of an order :ref:`dApp-to-dApp invocation <03_advanced:dApp-to-App Invocation>`. The structure is used:

* When checking an outgoing order by the :ref:`account script <03_advanced:Account Script>` or the verifier function of the :ref:`dApp script <03_advanced:dApp Script>`.
* In the :ref:`InvokeScriptTransaction <03_advanced:InvokeScriptTransaction>`.

:strong:`Constructor`

.. code-block:: none

 Order(id: ByteVector, matcherPublicKey: ByteVector, assetPair: AssetPair, orderType: Buy|Sell, price: Int, amount: Int, timestamp: Int, expiration: Int, matcherFee: Int, matcherFeeAssetId: ByteVector|Unit, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: Order Fields
  :file: _static/03_advanced/tables/186_Order-Fields.csv
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

Structure of a single transfer within the :ref:`MassTransferTransaction <03_advanced:MassTransferTransaction>` structure.

:strong:`Constructor`

.. code-block:: none

 Transfer(recipient: Address|Alias, amount: Int)

:strong:`Fields`

.. csv-table:: Transfer Fields
  :file: _static/03_advanced/tables/187_Transfer-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Transaction Structures
======================

Tokenization
------------

.. csv-table:: Tokenization
  :file: _static/03_advanced/tables/188_Tokenization.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 5

IssueTransaction
^^^^^^^^^^^^^^^^

Structure of an :ref:`issue transaction <02_intermediate:Issue Transaction>`.

:strong:`Constructor`

.. code-block:: none

 IssueTransaction(quantity: Int, name: String, description: String, reissuable: Boolean, decimals: Int, script: ByteVector|Unit, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: IssueTransaction Fields
  :file: _static/03_advanced/tables/189_IssueTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

ReissueTransaction
^^^^^^^^^^^^^^^^^^

Structure of a :ref:`reissue transaction <02_intermediate:Reissue Transaction>`.

:strong:`Constructor`

.. code-block:: none

 ReissueTransaction(quantity: Int, assetId: ByteVector, reissuable: Boolean, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: ReissueTransaction Fields
  :file: _static/03_advanced/tables/190_ReissueTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

BurnTransaction
^^^^^^^^^^^^^^^

Structure of an :ref:`burn transaction <02_intermediate:Burn Transaction>`.

:strong:`Constructor`

.. code-block:: none

 BurnTransaction(quantity: Int, assetId: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: BurnTransaction Fields
  :file: _static/03_advanced/tables/191_BurnTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

SetAssetScriptTransaction
^^^^^^^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`set asset script transaction <02_intermediate:Set Asset Script Transaction>`.

:strong:`Constructor`

.. code-block:: none

 SetAssetScriptTransaction(script: ByteVector|Unit, assetId: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: SetAssetScriptTransaction Fields
  :file: _static/03_advanced/tables/192_SetAssetScriptTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

UpdateAssetInfoTransaction
^^^^^^^^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`update asset info transaction <02_intermediate:Update Asset Info Transaction>`.

:strong:`Constructor`

.. code-block:: none

 UpdateAssetInfoTransaction(name: String, assetId: ByteVector, description: String, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: UpdateAssetInfoTransaction Fields
  :file: _static/03_advanced/tables/193_UpdateAssetInfoTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Usage
-----

.. csv-table:: Usage
  :file: _static/03_advanced/tables/194_Usage.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 5

TransferTransaction
^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`transfer transaction <02_intermediate:Transfer Transaction>`.

:strong:`Constructor`

.. code-block:: none

 TransferTransaction(feeAssetId: ByteVector|Unit, amount: Int, assetId: ByteVector|Unit, recipient: Address|Alias, attachment: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: TransferTransaction Fields
  :file: _static/03_advanced/tables/195_TransferTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

ExchangeTransaction
^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`exchange transaction <02_intermediate:Exchange Transaction>`.

:strong:`Constructor`

.. code-block:: none

 ExchangeTransaction(buyOrder: Order, sellOrder: Order, price: Int, amount: Int, buyMatcherFee: Int, sellMatcherFee: Int, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: ExchangeTransaction Fields
  :file: _static/03_advanced/tables/196_ExchangeTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

CreateAliasTransaction
^^^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`create alias transaction <02_intermediate:Create Alias Transaction>`.

:strong:`Constructor`

.. code-block:: none

 CreateAliasTransaction(alias: String, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: CreateAliasTransaction Fields
  :file: _static/03_advanced/tables/197_CreateAliasTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

MassTransferTransaction
^^^^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`mass transfer transaction <02_intermediate:Mass Transfer Transaction>`.

:strong:`Constructor`

.. code-block:: none

 MassTransferTransaction(assetId: ByteVector|Unit, totalAmount: Int, transfers: List[Transfer], transferCount: Int, attachment: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: MassTransferTransaction Fields
  :file: _static/03_advanced/tables/198_MassTransferTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

DataTransaction
^^^^^^^^^^^^^^^

Structure of a :ref:`data transaction <02_intermediate:Data Transaction>`.

:strong:`Constructor`

.. code-block:: none

 DataTransaction(data: List[BinaryEntry|BooleanEntry|DeleteEntry|IntegerEntry|StringEntry], id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: DataTransaction Fields
  :file: _static/03_advanced/tables/199_DataTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

SetScriptTransaction
^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`set script transaction <02_intermediate:Set Script Transaction>`.

:strong:`Constructor`

.. code-block:: none

 SetScriptTransaction(script: ByteVector|Unit, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: SetScriptTransaction Fields
  :file: _static/03_advanced/tables/200_SetScriptTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

InvokeScriptTransaction
^^^^^^^^^^^^^^^^^^^^^^^

Structure of an :ref:`invoke script transaction <02_intermediate:Invoke Script Transaction>`.

:strong:`Constructor`

.. code-block:: none

 InvokeScriptTransaction(dApp: Address|Alias, payments: List[AttachedPayments], feeAssetId: ByteVector|Unit, function: String, args: List[Boolean|ByteVector|Int|String|List[Boolean|ByteVector|Int|String]], id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: InvokeScriptTransaction Fields
  :file: _static/03_advanced/tables/201_InvokeScriptTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Network
-------

.. csv-table:: Network
  :file: _static/03_advanced/tables/202_Network.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 5

LeaseTransaction
^^^^^^^^^^^^^^^^

Structure of a :ref:`lease transaction <02_intermediate:Lease Transaction>`.

:strong:`Constructor`

.. code-block:: none

 LeaseTransaction(amount: Int, recipient: Address|Alias, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: LeaseTransaction Fields
  :file: _static/03_advanced/tables/203_LeaseTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

LeaseCancelTransaction
^^^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`lease cancel transaction <02_intermediate:Lease Cancel Transaction>`.

:strong:`Constructor`

.. code-block:: none

 LeaseCancelTransaction(leaseId: ByteVector, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: LeaseCancelTransaction Fields
  :file: _static/03_advanced/tables/204_LeaseCancelTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

SponsorFeeTransaction
^^^^^^^^^^^^^^^^^^^^^

Structure of a :ref:`sponsor fee transaction <02_intermediate:Sponsor Fee Transaction>`.

:strong:`Constructor`

.. code-block:: none

 SponsorFeeTransaction(assetId: ByteVector, minSponsoredAssetFee: Int|Unit, id: ByteVector, fee: Int, timestamp: Int, version: Int, sender: Address, senderPublicKey: ByteVector, bodyBytes: ByteVector, proofs: List[ByteVector])

:strong:`Fields`

.. csv-table:: SponsorFeeTransaction Fields
  :file: _static/03_advanced/tables/205_SponsorFeeTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Genesis
-------

.. csv-table:: Genesis
  :file: _static/03_advanced/tables/206_Genesis.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3 5

GenesisTransaction
^^^^^^^^^^^^^^^^^^

Structure of a :ref:`genesis transaction <02_intermediate:Genesis Transaction>`.

:strong:`Constructor`

.. code-block:: none

 GenesisTransaction(amount: Int, recipient: Address|Alias, id: ByteVector, fee: Int, timestamp: Int, version: Int)

:strong:`Fields`

.. csv-table:: GenesisTransaction Fields
  :file: _static/03_advanced/tables/207_GenesisTransaction-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

***********************
Iterations with FOLD<N>
***********************

FOLD<N> macro makes it possible to implement operations on a list of values such as sum, filter, map, zip, exists, etc. The macro behaves like the fold or reduce function in other programming languages.

.. code-block:: none

 FOLD<N>(list, start, foldFunc)

.. csv-table:: Iterations with FOLD
  :file: _static/03_advanced/tables/208_Iterations-with-FOLD.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 5

The combining function accepts two input parameters: the intermediate result and the next element of the list. Macro FOLD<N>(list, start, foldFunc) means:

* Execute up to N iterations.
* At each iteration: take the r-esult of the previous iteration (at the first iteration take the start value) and the next list item list, apply the foldFunc function to this pair.
* Return the final result.

The value of N must be known in advance. If there are more elements in the list than specified in FOLD, the script fails.
The complexity of FOLD<N> corresponds to the complexity of foldFunc multiplied by N plus extras.
The FOLD<N> macro is a syntactic sugar; it is unwrapped by the compiler. Therefore, in particular, the size of the script increases linearly with N.

Sum
===

.. code-block:: none

 func sum(accum: Int, next: Int) = accum + next
 let arr = [1,2,3,4,5]
 FOLD<5>(arr, 0, sum)    # Result: 15

The expression

.. code-block:: none

 FOLD<5>(arr, 0, sum)

after compiling and decompiling will look like this:

.. code-block:: none

 let $list = arr
 let $size = size($list)
 let $acc0 = 0
 if (($size == 0))
  then $acc0
  else {
    let $acc1 = sum($acc0, $list[0])
    if (($size == 1))
      then $acc1
      else {
        let $acc2 = sum($acc1, $list[1])
        if (($size == 2))
          then $acc2
          else {
            let $acc3 = sum($acc2, $list[2])
            if (($size == 3))
            then $acc3
              else {
                let $acc4 = sum($acc3, $list[3])
                if (($size == 4))
                  then $acc4
                  else {
                    let $acc5 = sum($acc4, $list[4])
                    if (($size == 5))
                      then $acc5
                      else {
                        let $acc6 = sum($acc5, $list[5])
                        throw("List size exceed 5")
                      }
                  }
              }
          }
      }
  }

Product
=======

.. code-block:: none
  
 func mult(accum: Int, next: Int) = accum * next
 let arr = [1,2,3,4,5]
 FOLD<5>(arr, 1, mult)    # Result: 1204]

Filter
======

The following code composes an array consisting only of even elements of the original array:

.. code-block:: none
  
 func filterEven(accum: List[Int], next: Int) =
  if (next % 2 == 0) then accum :+ next else accum
 let arr = [1,2,3,4,5]
 FOLD<5>(arr, [], filterEven)    # Result: [2, 4]

Map
===

The following code inverts the array, reducing each element by :math:`1`:

.. code-block:: none

 func map(accum: List[Int], next: Int) = (next - 1) :: accum
 let arr = [1, 2, 3, 4, 5]
 FOLD<5>(arr, [], map)    # Result: [4, 3, 2, 1, 0]

**********************
dApp-to-App Invocation
**********************

A dApp callable function can invoke a callable function of another dApp, or another callable function of the same dApp, or even itself. The invocation is synchronous. The invoked function returns a value that the invoking function can use.

dApp-to-dApp invocation is processed as follows:

* A user sends an Invoke Script transaction that invokes the callable function :math:`1`.
* The callable function :math:`1` invokes the callable function :math:`2` via a :ref:`strict variable <03_advanced:Strict Variable>` initialized by the :ref:`invoke or reentrantInvoke <03_advanced:dApp-to-App Invocation>` function.
* The callable function :math:`2` is executed; the script actions and return value are calculated.
* The :ref:`return value <03_advanced:Callable Function Result>` is assigned to the strict variable. The subsequent operations of callable function 1 are executed, taking into account script actions of callable function :math:`2` (as if the actions were applied to the blockchain state).
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
* The number of the :ref:`invoke or reentrantInvoke <03_advanced:dApp-to-App Invocation>` function calls is up to 100 within a single Invoke Script transaction.
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
  :file: _static/03_advanced/tables/209_Invoke-and-ReentrantInvoke-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 5

.. code-block:: none

 strict z = invoke(dapp,foo,args,[AttachedPayment(unit,100000000)])

The return value is of type Any, which means any valid type. You can extract a particular type from it using as[T] and exactAs[T] macros or the match ... case operator, see the :ref:`any <03_advanced:Any>` article.

The invoke and reentrantInvoke functions differ only in the reentrancy restriction. For details, see the :ref:`dApp-to-dApp invocation function <03_advanced:dApp-to-dApp Invocation Functions>` article.

Invocation Fields
=================

For dApp-to-dApp invocation, the fields of :ref:`invocation <03_advanced:Invocation>` structure used by the invoked function are filled with the following values:

.. csv-table:: Invocation Fields
  :file: _static/03_advanced/tables/210_Invocation-Fields.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 2 2 5

Callable Function Result
========================

In standard library version 5, a callable function result is a :ref:`tuple <03_advanced:Tuple>` of two elements:

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

For details, see the :ref:`callable function <03_advanced:Callable Functions>` article.

Updating Balance and Account Data Storage Entries
=================================================

If the callable function invoked by the invoke or reentrantInvoke function performs script actions, the results of those actions are available to the invoking function:

* If the invoked function adds an entry to the account's data storage, the invoking function can obtain the entry after the invocation.
* If the invoked function deletes an entry from the account's data storage, the invoking function cannot obtain the entry after the invocation.
* If the invoked function performs actions with tokens (transfer, issue/reissue/burn, and others) and the invoking function obtains balances after the invocation, it receives the updated balances.

Transaction Fail
================

If the callable function's execution fails or :ref:`throws an exception <03_advanced:Exception Functions>`, the Invoke Script transaction could be rejected or saved on the blockchain as failed. This depends on whether the complexity of performed computations has exceeded the :ref:`threshold for saving a failed transaction <03_advanced:Limitations>` (currently :math:`1000`). The complexity is summed up for all invocations.

Consider the example: callable function :math:`1` performs computations of 800 complexity, then invokes callable function :math:`2` which performs computations of 300 complexity and then fails. The complexity :math:`800 + 300` has exceeded the threshold, so the transaction is saved as failed, and the sender is charged a fee.

If the total complexity of executed callable functions and asset scripts exceeds the limit of :math:`26,000`, the transaction is saved as failed as well. For example, if the complexity of executed callable functions is :math:`25,000` in total, and there is a smart asset in script action whose script's complexity is :math:`1500`.

In case of failure, no payments and script actions are applied to the blockchain state, even if some of the invoked functions are executed completely. The only state change the failed transaction entails is charging the fee.

Known Issue
===========

If the invoke or reentrantInvoke function is called inside a function without annotation (that is, inside a function that cannot be invoked from outside the dApp), and the dApp script contains a verifier function, then an error occurs when trying to set such a script.

***********
Limitations
***********

.. csv-table:: Limitations
  :file: _static/03_advanced/tables/211_Limitations.csv
  :header-rows: 1 
  :class: longtable
  :widths: 6 2

Script Complexity
=================

Script complexity is a dimensionless quantity that estimates computational resources needed to execute a script. The complexity of a script is estimated based on complexities of all the operators and functions it consists of. The complexity of the built-in functions is listed in the built-in functions article.

Limitations on script complexity are given in the :ref:`limitations <03_advanced:Limitations>` article.

Data Weight
===========

The weight of each value approximately corresponds to its size in bytes. Weight is used in :ref:`limitations <03_advanced:Limitations>` on creating and comparing values.

Weight Calculation
------------------

.. csv-table:: Weight Calculation
  :file: _static/03_advanced/tables/212_Weight Calculation.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Weight of List
--------------

The weight of the list is calculated as follows:

:math:`W_{list} = 20 + 20 × Q + W_{elems}`

where:

* :math:`Q` is a number of elements.
* :math:`W_{elems}` is a total weight of elements.

Weight of Tuple or Structure
----------------------------

The weight of the tuple or structure is calculated as follows:

:math:`W_{struct} = 40 + 30 × Q + W_{fields}`

where:

* :math:`Q` is a number of fields.
* :math:`W_{fields}` is a total weight of fields.  

Weight Limitations
------------------

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

***************
Ride Components
***************

Parser
======

Parser checks the Ride script syntax, the presence of all the variables and functions used, and forms an abstract syntax tree that is used by compiler.

Compiler
========

Compiler generates executable script code based on an abstract syntax tree. The compiled script can be assigned to an account or asset.

Estimator
=========

Estimator calculates the :ref:`complexity <03_advanced:Script Complexity>` of the compiled script.

Evaluator
=========

Evaluator is a node component that executes the script in cases of sending a transaction from a smart account, an invoke script transaction, or transactions involving smart assets. Script execution is a part of :ref:`transaction validation <02_intermediate:Transaction Validation>` and transaction execution, that is, calculating new state of the blockchain as a result of transaction.

Decompiler
==========

Decompiler converts script code from executable format to Ride code. Decompiler is used in `DecentralChain Explorer <https://decentralscan.com/>`_ to view an account script, dApp script or asset script.