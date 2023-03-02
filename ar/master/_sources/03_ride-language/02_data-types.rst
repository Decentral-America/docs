**********
Data Types
**********

.. csv-table:: Data Types
  :file: ../_static/03_ride-language/tables/001_Data-Types.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

For each value, depending on the data type, the weight is determined. The weight is used in limitations on creating and comparing values. For more information see the :ref:`data weight <03_ride-language/07_dapp-to-app-invocation:Data Weight>`.

Any
===

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
======

BigInt is a special numeric :ref:`data type <03_ride-language/02_data-types:Data Types>` designed to handle values outside the range of :ref:`Int <03_ride-language/02_data-types:Int>` and to perform high accuracy calculations.
BigInt variable has a size of :math:`64` bytes (:math:`512` bits) and contains an integer between :math:`–2511` to :math:`2511–1`, inclusive. The weight of the value is :math:`64`.
A BigInt variable can only be used inside a script. A :ref:`callable function <03_ride-language/03_functions:Callable Functions>` does not accept arguments of BigInt type and does not return a value of BigInt type. You can pass a big integer value as a string, then use the parseBigInt or parseBigIntValue functions.

BigInt Operations
-----------------

The following operators support BigInt values:

* Arithmetic operators: +, -, \*, /, %, unary minus.
* Comparison operators: <, >, <=, and >=.
* Equality operators: == and !=.

BigInt Functions
----------------

The following functions operate BigInt values:

* :ref:`fraction(BigInt, BigInt, BigInt): BigInt <03_ride-language/03_functions:fraction(BigInt, BigInt, BigInt): BigInt>`
* :ref:`fraction(BigInt, BigInt, BigInt, Union): BigInt <03_ride-language/03_functions:fraction(BigInt, BigInt, BigInt, Union): BigInt>`
* :ref:`log(BigInt, Int, BigInt, Int, Int, Union): BigInt <03_ride-language/03_functions:log(BigInt, Int, BigInt, Int, Int, Union): BigInt>`
* :ref:`max(List[BigInt]): BigInt <03_ride-language/03_functions:max(List[BigInt]): BigInt>`
* :ref:`median(List[BigInt]): BigInt <03_ride-language/03_functions:median(List[BigInt]): BigInt>`
* :ref:`min(List[BigInt]): BigInt <03_ride-language/03_functions:min(List[BigInt]): BigInt>`
* :ref:`pow(BigInt, Int, BigInt, Int, Int, Union): BigInt <03_ride-language/03_functions:pow(BigInt, Int, BigInt, Int, Int, Union): BigInt>`
* :ref:`parseBigInt(String): BigInt|Unit <03_ride-language/03_functions:parseBigInt(String): BigInt|Unit>`
* :ref:`parseBigIntValue(String): BigInt <03_ride-language/03_functions:parseBigIntValue(String): BigInt>`
* :ref:`toBigInt(ByteVector): BigInt <03_ride-language/03_functions:toBigInt(ByteVector): BigInt>`
* :ref:`toBigInt(ByteVector, Int, Int): BigInt <03_ride-language/03_functions:toBigInt(ByteVector, Int, Int): BigInt>`
* :ref:`toInt(BigInt): Int <03_ride-language/03_functions:toInt(BigInt): Int>`
* :ref:`toString(BigInt): String <03_ride-language/03_functions:toString(BigInt): String>`

Boolean
=======

Boolean is a :ref:`data type <03_ride-language/02_data-types:Data Types>` that can have only the values true or false.

ByteVector
==========

ByteVector is a :ref:`data type <03_ride-language/02_data-types:Data Types>` for byte array.

To assign a value to a ByteVector variable, you can use a string in Base16, Base58, or Base64 with the appropriate prefix:

.. code-block:: none

 let a = base16'52696465'
 let b = base58'8t38fWQhrYJsqxXtPpiRCEk1g5RJdq9bG5Rkr2N7mDFC'
 let c = base64'UmlkZQ=='

This method, unlike the fromBase16String, fromBase58String, and fromBase64String functions, does not increase the complexity of the script, since decoding is performed by the compiler.
To convert :ref:`integer <03_ride-language/02_data-types:Int>`, :ref:`boolean <03_ride-language/02_data-types:Boolean>` and :ref:`string <03_ride-language/02_data-types:String>` values to a byte array use toBytes function:

.. code-block:: none

 let a = 42.toBytes()
 let b = true.toBytes()
 let c = "Ride".toBytes()

For more byte array functions, see the :ref:`Built-in Functions <03_ride-language/03_functions:Built-in Functions>`.

ByteVector Limitations
----------------------

The maximum size of a ByteVector variable is :math:`32,767` bytes. Exception: the bodyBytes field of :ref:`transaction structure <03_ride-language/05_structures:Transaction Structures>`. You can pass this value as an argument to the rsaVerify и sigVerify :ref:`verification functions <03_ride-language/03_functions:Verification Functions>` (but cannot concatenate with other byte arrays in case the limit is exceeded).

Int
===

Int is an integer :ref:`data type <03_ride-language/02_data-types:Data Types>`. The integer variable has the size of 8 bytes and stores an integer from :math:`-9,223,372,036,854,775,808` to :math:`9,223,372,036,854,775,807` inclusive.

.. code-block:: none

 let age = 42
 let length = size("hello")

String
======

Strings are denoted only using double quotes. They are immutable, and for that reason, the substring function is very efficient: no copying is performed and no extra allocations are required. Strings are  UTF-8 encoded.

.. code-block:: none

 let name = "Bob"   # use "double" quotes only

String Limitations
------------------

The maximum size of a String variable is :math:`32,767` (:math:`1` character can take up to :math:`4` bytes).

String Functions
----------------

The built-in functions for working with strings are presented in the following articles:

* String Functions
* Converting Functions

Unit
====

Unit is an empty value :ref:`data type <03_ride-language/02_data-types:Data Types>`. The empty value data type is similar to unit in Scala or to null in C#. Usually, built-in functions return unit value of type unit instead of null.

.. code-block:: none

 "String".indexOf("substring") == unit # true

Nothing
=======

Nothing is the 'bottom type' of Ride’s type system. No value can be of type nothing, but an expression of type nothing can be used everywhere. In functional languages, this is essential for support for throwing an exception:

.. code-block:: none

 2 + throw() # the expression compiles because
    # there's a defined function +(Int, Int).
      # The type of the second operand is Nothing, 
      # which complies to any required type

List
====

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
---------------

Lists support concatenation as well as adding items to the beginning and the end.

.. csv-table:: List Operations
  :file: ../_static/03_ride-language/tables/002_List-Operations.csv
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
--------------

The built-in list functions are presented in the list functions article. Operations on a list can be implemented via the FOLD macro. The size of the list must be known in advance.

List as Function Argument
-------------------------

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
=====

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
=====

Union is a data type that unites :math:`2` or more data types. Union can combine primitive types, :ref:`lists <03_ride-language/02_data-types:List>`, :ref:`tuples <03_ride-language/02_data-types:Tuple>`, :ref:`structures <03_ride-language/05_structures:Structures>`. This type is a very convenient way to work with abstractions. Union(String | Unit) shows that the value is an intersection of these types.

To get a value of a particular type from a Union, you can use:

* :ref:`Union functions <03_ride-language/03_functions:Union Functions>`
* :ref:`match-case operator <03_ride-language/01_syntax-basics:Match-Case>`

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
================

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
=============

This is a mechanism for knowing the type of a transaction:

.. code-block:: none

 let amount = match tx {              # tx is a current outgoing transaction
  case t: TransferTransaction => t.amount
  case m: MassTransferTransaction => m.totalAmount
  case _ => 0
 }

There are different types of transactions, if a transaction is TransferTransaction or MassTransferTransaction we use the corresponding field, while in all other cases, we will get :math:`0`.
