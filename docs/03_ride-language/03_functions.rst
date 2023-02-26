*********
Functions
*********

Functions in Ride are declared with func, function must be declared above the place of its usage. 
When declaring a function to the right of the "=" sign must be an :ref:`expression <03_ride-language/01_syntax-basics:Expressions>`. The value of the function is the expression result.
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
===========

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
==================

The functions with the @Callable annotation become callable functions, since they can be called (or invoked) from other accounts: by an Invoke Script transaction or by a dApp.
A callable function can perform actions: write data to the dApp data storage, transfer tokens from the dApp to other accounts, issue/release/burn tokens, and others. The result of a callable function is a tuple of two elements: a list of structures describing script actions and a value passed to the parent function in case of the :ref:`dApp-to-dApp invocation <03_ride-language/07_dapp-to-app-invocation:dApp-to-App Invocation>`.

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
==================

A built-in function is a function of the standard library .

Account Data Storage Functions
------------------------------

Learn more about :ref:`account data storage <02_decentralchain/01_account:Account Data Storage>`.

.. csv-table:: Account Data Storage Functions
  :file: ../_static/03_ride-language/tables/012_Account-Data-Storage-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

getBinary(Address|Alias, String): ByteVector|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an array of bytes by key.

.. code-block:: none

 getBinary(addressOrAlias: Address|Alias, key: String): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/013_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinary(String): ByteVector|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an array of bytes by key from the dApp's own data storage.

.. code-block:: none

 getBinary(key: String): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/014_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinaryValue(Address|Alias, String): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an array of bytes by key. Fails if there is no data.

.. code-block:: none

 getBinaryValue(addressOrAlias: Address|Alias, key: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/015_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinaryValue(String): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an array of bytes by key from the dApp's own data storage.

.. code-block:: none

 getBinaryValue(key: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/016_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBoolean(Address|Alias, String): Boolean|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a boolean value by key.

.. code-block:: none

 getBoolean(addressOrAlias: Address|Alias, key: String): Boolean|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/017_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBoolean(String): Boolean|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a boolean value by key by key from the dApp's own data storage.

.. code-block:: none

 getBoolean(key: String): Boolean|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/018_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBooleanValue(Address|Alias, String): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a boolean value by key. Fails if there is no data.

.. code-block:: none

 getBooleanValue(addressOrAlias: Address|Alias, key: String): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/019_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBooleanValue(String): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a boolean value by key from the dApp's own data storage.

.. code-block:: none

 getBooleanValue(key: String): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/020_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getInteger(Address|Alias, String): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an integer by key.

.. code-block:: none

 getInteger(addressOrAlias: Address|Alias, key: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/021_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getInteger(String): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an integer by key from the dApp's own data storage.

.. code-block:: none

 getInteger(key: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/022_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getIntegerValue(Address|Alias, String): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an integer by key. Fails if there is no data.

.. code-block:: none

 getIntegerValue(addressOrAlias: Address|Alias, key: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/023_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getIntegerValue(String): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an integer by key from the dApp's own data storage.

.. code-block:: none

 getIntegerValue(key: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/024_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getString(Address|Alias, String): String|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a string by key.

.. code-block:: none

 getString(addressOrAlias: Address|Alias, key: String): String|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/025_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getString(String): String|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a string by key from the dApp's own data storage.

.. code-block:: none

 getString(key: String): String|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/026_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getStringValue(Address|Alias, String): String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a string by key. Fails if there is no data.

.. code-block:: none

 getStringValue(addressOrAlias: Address|Alias, key: String): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/027_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getStringValue(String): String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a string by key from the dApp's own data storage.

.. code-block:: none

 getString(key: String): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/028_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

isDataStorageUntouched(Address|Alias): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if the data storage of a given account never contained any entries. Returns false if there was at least one entry in the account data storage even if the entry was deleted.

.. code-block:: none

 isDataStorageUntouched(addressOrAlias: Address|Alias): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/029_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let addr = Address(base58'3N4iKL6ikwxiL7yNvWQmw7rg3wGna8uL6LU')
 isDataStorageUntouched(addr) # Returns false

Blockchain Functions
--------------------

.. csv-table:: Blockchain Functions
  :file: ../_static/03_ride-language/tables/030_Blockchain-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

addressFromRecipient(Address|Alias): Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the corresponding :ref:`address <02_decentralchain/01_account:Address>` of the :ref:`alias <02_decentralchain/01_account:Alias>`.

.. code-block:: none

 addressFromRecipient(AddressOrAlias: Address|Alias): Address

For a description of the return value, see the :ref:`Address <03_ride-language/05_structures:Address>` structure article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/031_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let address = Address(base58'3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF')
 addressFromRecipient(address)

assetBalance(Address|Alias, ByteVector): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets account balance by token ID.

.. code-block:: none

 assetBalance(addressOrAlias: Address|Alias, assetId: ByteVector): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/032_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

assetInfo(ByteVector): Asset|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the information about a :ref:`token (asset) <02_decentralchain/02_token(asset):Token (Asset)>`.

.. code-block:: none

 assetInfo(id: ByteVector): Asset|Unit

For a description of the return value, see the :ref:`BlockInfo <03_ride-language/05_structures:BlockInfo>` structure article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/033_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the information about a :ref:`block <02_decentralchain/04_block:Block>` by the :ref:`block height <02_decentralchain/04_block:Block Height>`.

.. code-block:: none

 blockInfoByHeight(height: Int): BlockInfo|Unit

For a description of the return value, see the :ref:`BlockInfo <03_ride-language/05_structures:BlockInfo>` structure article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/034_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calculates ID of the token formed by the :ref:`Issue <03_ride-language/05_structures:Issue>` structure when executing the :ref:`callable function <03_ride-language/03_functions:Callable Functions>`.

.. code-block:: none

 calculateAssetId(issue: Issue): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/035_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calculates ID of the lease formed by the :ref:`Lease <03_ride-language/05_structures:Lease>` structure when executing the :ref:`callable function <03_ride-language/03_functions:Callable Functions>`.

.. code-block:: none

 calculateLeaseId(lease: Lease): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/036_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns BLAKE2b-256 hash of the script assigned to a given account. Returns unit if there is no script. The function can be used to verify that the script is exactly the same as expected.

.. code-block:: none

 scriptHash(addressOrAlias: Address|Alias): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/037_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let addr = Address(base58'3MxBZbnN8Z8sbYjjL5N3oG5C8nWq9NMeCEm')
 scriptHash(addr) # Returns base58'G6ihnWN5mMedauCgNa8TDrSKWACPJKGQyYagmMQhPuja'

transactionHeightById(ByteVector): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the :ref:`block height <02_decentralchain/04_block:Block Height>` of a transaction.

.. code-block:: none

 transactionHeightById(id: ByteVector): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/038_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the data of a :ref:`transfer transaction <02_decentralchain/03_transaction:Transfer Transaction>`.

.. code-block:: none

 transferTransactionById(id: ByteVector): TransferTransaction|Unit

For a description of the return value, see the :ref:`TransferTransaction <03_ride-language/05_structures:TransferTransaction>` structure article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/039_Parameters.csv
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

decentralchainBalance(Address|Alias): BalanceDetails
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets all types of :ref:`DecentralCoin <02_decentralchain/02_token(asset):DecentralCoin>` balances. For description of balance types, see the :ref:`account balance <02_decentralchain/01_account:Account Balance>` article.

.. code-block:: none

 decentralchainBalance(addressOrAlias: Address|Alias): BalanceDetails

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/040_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Byte Array Functions
--------------------

.. csv-table:: Byte Array Functions
  :file: ../_static/03_ride-language/tables/041_Byte-Array-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

drop(ByteVector, Int): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the byte array without the first N bytes.

.. code-block:: none

 drop(xs: ByteVector, number: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/042_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the byte array without the last N bytes.

.. code-block:: none

 dropRight(xs: ByteVector, number: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/043_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^

Returns the number of bytes in the byte array.

.. code-block:: none

 size(byteVector: ByteVector): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/044_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the first N bytes of the byte array.

.. code-block:: none

 take(xs: ByteVector, number: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/045_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the last N bytes of the byte array.

.. code-block:: none

 takeRight(xs: ByteVector, number: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/046_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 takeRight(base58'37BPKA', 2) # Returns the last 2 bytes of the byte array

Converting Functions
--------------------

.. csv-table:: Converting Functions
  :file: ../_static/03_ride-language/tables/047_Converting-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

addressFromPublicKey(ByteVector): Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the corresponding :ref:`address <02_decentralchain/01_account:Address>` of the account public key.

.. code-block:: none

 addressFromPublicKey(publicKey: ByteVector): Address

For a description of the return value, see the :ref:`Address <03_ride-language/05_structures:Address>` structure article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/048_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let address = addressFromPublicKey(base58'J1t6NBs5Hd588Dn7mAPytqkhgeBshzv3zecScfFJWE2D')

parseBigInt(String): BigInt|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts the string representation of a number to its :ref:`big integer <03_ride-language/02_data-types:BigInt>` equivalent.

.. code-block:: none

 parseBigInt(str: String): BigInt|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/049_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

parseBigIntValue(String): BigInt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts the string representation of a number to its :ref:`big integer <03_ride-language/02_data-types:BigInt>` equivalent. Fails if the string cannot be parsed.

.. code-block:: none

 parseBigIntValue(str: String): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/050_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

parseInt(String): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts the string representation of a number to its integer equivalent.

.. code-block:: none

 parseInt(str: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/051_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts the string representation of a number to its integer equivalent. Fails if the string cannot be parsed.

.. code-block:: none

 parseIntValue(str: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/052_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts an array of bytes to a :ref:`big integer <03_ride-language/02_data-types:BigInt>` using the big-endian byte order.

.. code-block:: none

 toBigInt(bin: ByteVector): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/053_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

toBigInt(ByteVector, Int, Int): BigInt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts an array of bytes starting from a certain index to a :ref:`big integer <03_ride-language/02_data-types:BigInt>` using the big-endian byte order.

.. code-block:: none

 toBigInt(bin: ByteVector, offset: Int, size: Int): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/054_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

toBigInt(Int): BigInt
^^^^^^^^^^^^^^^^^^^^^

Converts an integer to a :ref:`big integer <03_ride-language/02_data-types:BigInt>`.

.. code-block:: none

 toBigInt(n: Int): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/055_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

toBytes(Boolean): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a boolean value to an array of bytes.

.. code-block:: none

 toBytes(b: Boolean): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/056_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 toBytes(true) # Returns base58'2'
 toBytes(false) # Returns base58'1'

toBytes(Int): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^

Converts an integer to an array of bytes using the big-endian byte order.

.. code-block:: none

 toBytes(n: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/057_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBytes(10) # Returns base58'1111111B'

toBytes(String): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a string to an array of bytes.

.. code-block:: none

 toBytes(s: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/058_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBytes("Ride") # Returns base58'37BPKA'

toBytes(BigInt): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a :ref:`big integer <03_ride-language/02_data-types:BigInt>` to an array of bytes using the big-endian byte order.

.. code-block:: none

 toBytes(n: BigInt): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/059_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1


toInt(BigInt): Int
^^^^^^^^^^^^^^^^^^

Converts a :ref:`big integer <03_ride-language/02_data-types:BigInt>` to an integer. Fails if the number cannot be converted.

.. code-block:: none

 toInt(n: BigInt): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/060_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

toInt(ByteVector): Int
^^^^^^^^^^^^^^^^^^^^^^

Converts an array of bytes to an integer using the big-endian byte order.

.. code-block:: none

 toInt(bin: ByteVector) : Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/061_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toInt(base58'1111111B') # Returns 10

toInt(ByteVector, Int): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts an array of bytes to an integer starting from a certain index using the big-endian byte order.

.. code-block:: none

 toInt(bin: ByteVector, offset: Int): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/062_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = toBytes("Ride")
 toInt(bytes, 2) # Returns 7234224039401641825
 toInt(bytes, 6) # Index out of bounds

toString(Address): String
^^^^^^^^^^^^^^^^^^^^^^^^^

Converts an array of bytes of an :ref:`address <02_decentralchain/01_account:Address>` to a string.

.. code-block:: none

 toString(addr: Address): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/063_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let address = Address(base58'3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF')
 toString(address) # Returns "3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF"

toString(Boolean): String
^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a boolean value to a string.

.. code-block:: none

 toString(b: Boolean): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/064_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toString(true) # Returns "true"
 toString(false) # Returns "false"

toString(Int): String
^^^^^^^^^^^^^^^^^^^^^

Converts an integer to a string.

.. code-block:: none

 toString(n: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/065_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toString(10) # Returns "10"

toString(BigInt): String
^^^^^^^^^^^^^^^^^^^^^^^^

Converts a :ref:`big integer <03_ride-language/02_data-types:BigInt>` to a string.

.. code-block:: none

 toString(n: BigInt): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/066_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

toUtf8String(ByteVector): String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts an array of bytes to a UTF-8 string. Fails if the array of bytes cotains an invalid UTF-8 sequence.

.. code-block:: none

 toUtf8String(u: ByteVector): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/067_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = toBytes("Ride")
 toUtf8String(bytes) # Returns "Ride"

transferTransactionFromProto(ByteVector): TransferTransaction|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deserializes transfer transaction: converts protobuf-encoded :ref:`binary format <02_decentralchain/10_binary-format:Transfer Transaction Binary Format>` specified in transaction.proto to a TransferTransaction structure. Returns unit if deserialization failed.

.. code-block:: none

 transferTransactionFromProto(b: ByteVector): TransferTransaction|Unit

For a description of the return value, see the :ref:`TransferTransaction <03_ride-language/05_structures:TransferTransaction>` structure article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/068_Parameters.csv
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
---------------------------------

.. csv-table:: dApp-to-dApp Invocation Functions
  :file: ../_static/03_ride-language/tables/069_dApp-to-dApp-Invocation-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

invoke(Address|Alias, String, List[Any], List[AttachedPayments]): Any
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Invokes a dApp :ref:`callable function <03_ride-language/03_functions:Callable Functions>`, with reentrancy restriction.

.. code-block:: none

 invoke(dApp: Address|Alias, function: String, arguments: List[Any], payments: List[AttachedPayments]): Any

Any means any valid type. You can extract a particular type from it using as[T] and exactAs[T] macros or the match ... case operator, see the :ref:`any <03_ride-language/02_data-types:Any>` article.

The invoke function can be used by a callable function of a :ref:`dApp script <03_ride-language/04_script-types:dApp Script>`, but not by a verifier function, :ref:`account script <03_ride-language/04_script-types:Account Script>` or :ref:`asset script <03_ride-language/04_script-types:Asset Script>`.

Via the invoke function, the callable function can invoke a callable function of another dApp, or another callable function of the same dApp, or even itself, and then use the invocation results in subsequent operations. For details, see the :ref:`dApp-to-dApp invocation <03_ride-language/07_dapp-to-app-invocation:dApp-to-App Invocation>` article.

To ensure executing callable functions and applying their actions in the right order, initialize a :ref:`strict variable <03_ride-language/01_syntax-basics:Strict Variables>` by the return value of an invoke function.

The invocation can contain payments that will be transferred from the balance of the parent dApp to the balance of the invoked dApp. Payments are forbidden if the dApp invokes itself.

If a payment token is a smart asset, the asset script verifies the invoke as if it was :ref:`InvokeScriptTransaction <03_ride-language/05_structures:InvokeScriptTransaction>` structure with the following fields:

* DApp, payments, function, args indicated in the invoke function.
* Sender, senderPublicKey of the dApp that performs the invocation.
* Id, timestamp, fee, feeAssetId indicated in the original invoke script transaction.
* Version = 0;
  
If the asset script denies the action, the Invoke Script transaction is either discarded or saved on the blockchain as failed, see the :ref:`transaction validation <02_decentralchain/03_transaction:Transaction Validation>` article.

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
  :file: ../_static/03_ride-language/tables/070_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

A user sends an invoke script transaction that invokes the callable function foo of dApp1. The foo function invokes the bar function of dApp2 passing the number a and attaching a payment of 1 USDN. The bar function transfers :math:`1` :ref:`DecentralCoin <02_decentralchain/02_token(asset):DecentralCoin>` to dApp1 and returns the doubled number a. The foo function writes to dApp1 data storage:

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
          IntegerEntry(key2, decentralchainBalance(addressFromStringValue(dapp2)).regular)
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Invokes a dApp :ref:`callable function <03_ride-language/03_functions:Callable Functions>`. The only difference from the invoke function above is that there is no reentrancy restriction for the parent dApp that uses reentrantInvoke. However, if the parent dApp is invoked again and this time uses the invoke function, the parent dApp cannot be invoked again in this invocation stack.

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
--------------------------

The functions listed below retrieve data by key from the :ref:`DataTransaction <03_ride-language/05_structures:DataTransaction>` structure or from any list of data entries.

.. csv-table:: Data Transaction Functions
  :file: ../_static/03_ride-language/tables/071_Data-Transaction-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

getBinary(List[], String): ByteVector|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a binary value from a list of data entires by key.

.. code-block:: none

 getBinary(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/072_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinary(List[], Int): ByteVector|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a binary value from a list of data entires by index.

.. code-block:: none

 getBinary(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): ByteVector|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/073_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinaryValue(List[], String): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a binary value from a list of data entires by key. Fails if there is no data.

.. code-block:: none

 getBinaryValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/074_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBinaryValue(List[], Int): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a binary value from a list of data entires by index. Fails if there is no data.

.. code-block:: none

 getBinaryValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/075_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBoolean(List[], String): Boolean|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a boolean value from a list of data entires by key.

.. code-block:: none

 getBoolean(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): Boolean|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/076_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBoolean(List[], Int): Boolean|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a boolean value from a list of data entires by index.

.. code-block:: none

 getBoolean(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): Boolean|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/077_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBooleanValue(List[], String): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a boolean value from a list of data entires by key. Fails if there is no data.

.. code-block:: none

 getBooleanValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/078_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getBooleanValue(List[], Int): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a boolean value from a list of data entires by index. Fails if there is no data.

.. code-block:: none

 getBooleanValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/079_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getInteger(List[], String): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets integer from a list of data entires by key.

.. code-block:: none

 getInteger(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/080_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getInteger(List[], Int): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an integer value from a list of data entires by index.

.. code-block:: none

 getInteger(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/081_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getIntegerValue(List[], String): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an integer value from a list of data entires by key. Fails if there is no data.

.. code-block:: none

 getIntegerValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/082_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getIntegerValue(List[], Int): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets an integer value from a list of data entires by index. Fails if there is no data.

.. code-block:: none

 getIntegerValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/083_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getString(List[], String): String|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a string value from a list of data entires by key.

.. code-block:: none

 getString(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): String|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/084_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getString(List[], Int): String|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a string value from a list of data entires by key.

.. code-block:: none

 getString(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): String|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/085_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getStringValue(List[], String): String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a string value from a list of data entires by key. Fails if there is no data.

.. code-block:: none

 getStringValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], key: String): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/086_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getStringValue(List[], Int): String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a string value from a list of data entires by index. Fails if there is no data.

.. code-block:: none

 getStringValue(data: List[BinaryEntry|BooleanEntry|IntegerEntry|StringEntry], index: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/087_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Decoding Functions
------------------

.. csv-table:: Decoding Functions
  :file: ../_static/03_ride-language/tables/088_Decoding-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

addressFromString(String): Address|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decodes address from base58 string.

.. code-block:: none

 addressFromString(string: String): Address|Unit

For a description of the return value, see the :ref:`Address <03_ride-language/05_structures:Address>` structure article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/089_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let address = addressFromString("3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF")

addressFromStringValue(String): Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decodes address from base58 string. Fails if the address cannot be decoded.

.. code-block:: none

 addressFromStringValue(string: String): Address

For a description of the return value, see the :ref:`Address <03_ride-language/05_structures:Address>` structure article.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/090_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let address = addressFromStringValue("3NADPfTVhGvVvvRZuqQjhSU4trVqYHwnqjF")

fromBase16String(String): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decodes a base16 string to an array of bytes.

.. code-block:: none

 fromBase16String(str: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/091_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = fromBase16String("52696465")

fromBase58String(String): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decodes a base58 string to an array of bytes.

.. code-block:: none

 fromBase58String(str: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/092_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = fromBase58String("37BPKA")

fromBase64String(String): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decodes a base64 string to an array of bytes.

.. code-block:: none

 fromBase64String(str: String): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/093_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 let bytes = fromBase64String("UmlkZQ==")

Encoding Functions
------------------

.. csv-table:: Encoding Functions
  :file: ../_static/03_ride-language/tables/094_Encoding-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

toBase16String(ByteVector): String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encodes an array of bytes to a base16 string.

.. code-block:: none

 toBase16String(bytes: ByteVector): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/095_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBase16String("Ride".toBytes()) # Returns "52696465"
 toBase16String(base16'52696465') # Returns "52696465"

toBase58String(ByteVector): String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encodes an array of bytes to a base58 string.

.. code-block:: none

 toBase58String(bytes: ByteVector): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/096_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBase58String("Ride".toBytes()) # Returns "37BPKA"
 toBase58String(base58'37BPKA')  # Returns "37BPKA

toBase64String(ByteVector): String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encodes an array of bytes to a base64 string.

.. code-block:: none

 toBase64String(bytes: ByteVector): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/097_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 toBase64String("Ride".toBytes()) # Returns "UmlkZQ=="
 toBase64String(base64'UmlkZQ==') # Returns "UmlkZQ=="

Exception Functions
-------------------

.. csv-table:: Exception Functions
  :file: ../_static/03_ride-language/tables/098_Exception-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

The return type of throw is nothing. There is no exception handling in Ride: after an exception has been thrown, the script execution fails. The transaction can be either discarded or saved on the blockchain as failed, see the :ref:`transaction validation <02_decentralchain/03_transaction:Transaction Validation>` article for details.

throw()
^^^^^^^

Raises an exception.

throw(String)
^^^^^^^^^^^^^

Raises an exception with a message.

.. code-block:: none

 throw(err: String)

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/099_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Hashing Functions
-----------------

.. csv-table:: Hashing Functions
  :file: ../_static/03_ride-language/tables/100_Hashing-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

blake2b256(ByteVector): ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Range of functions that hash an array of bytes using BLAKE2b-256.

.. csv-table:: blake2b256
  :file: ../_static/03_ride-language/tables/101_blake2b256.csv
  :header-rows: 1 
  :class: longtable
  :widths: 4 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/102_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Range of functions that hash an array of bytes using Keccak-256.

.. csv-table:: keccak256
  :file: ../_static/03_ride-language/tables/103_keccak256.csv
  :header-rows: 1 
  :class: longtable
  :widths: 4 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/104_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Range of functions that hash an array of bytes using SHA-256.

.. csv-table:: sha256
  :file: ../_static/03_ride-language/tables/105_sha256.csv
  :header-rows: 1 
  :class: longtable
  :widths: 4 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/106_Parameters.csv
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
--------------

.. csv-table:: List Functions
  :file: ../_static/03_ride-language/tables/107_List-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

A, B, T means any valid type.

cons(A, List[B]): List[A|B]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inserts element to the beginning of the :ref:`list <03_ride-language/02_data-types:List>`.

.. code-block:: none

 cons(head:T, tail: List[T]): List[T]

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/108_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none
  
 cons("Hello", ["World", "."]) # Returns ["Hello", "World", "."]
 cons(1, [2, 3, 4, 5]) # Returns [1, 2, 3, 4, 5]

containsElement(List[T], T): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if the element is in the :ref:`list <03_ride-language/02_data-types:List>`.

.. code-block:: none

 containsElement(list: List[T], element: T): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/109_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

getElement(List[T], Int): T
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the element from the :ref:`list <03_ride-language/02_data-types:List>` by index.

.. code-block:: none

 getElement(arr: List[T], pos: Int): T

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/110_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 getElement(["Hello", "World", "."], 0)  # Returns "Hello"
 getElement([false, true], 1) # Returns true 

indexOf(List[T], T): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the index of the first occurrence of the element in the :ref:`list <03_ride-language/02_data-types:List>` or unit if the element is missing.

.. code-block:: none

 indexOf(list: List[T], element: T): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/111_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let stringList = ["a","b","a","c"]
 indexOf("a", stringList) # Returns 0

lastIndexOf(List[T], T): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the index of the last occurrence of the element in the :ref:`list <03_ride-language/02_data-types:List>` or unit if the element is missing.

.. code-block:: none

 lastIndexOf(list: List[T], element: T): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/112_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 let stringList = ["a","b","a","c"]
 lastIndexOf("a", stringList) # Returns 2

max(List[Int]): Int
^^^^^^^^^^^^^^^^^^^

Returns the largest element in the :ref:`list <03_ride-language/02_data-types:List>` of integers. Fails if the list is empty.

.. code-block:: none

 max(List[Int]): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/113_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

max(List[BigInt]): BigInt
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the largest element in the list of :ref:`big integers <03_ride-language/02_data-types:BigInt>`. Fails if the list is empty.

.. code-block:: none

 max(List[BigInt]): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/114_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

min(List[Int]): Int
^^^^^^^^^^^^^^^^^^^

Returns the smallest element in the :ref:`list <03_ride-language/02_data-types:List>` of integers. Fails if the list is empty.

.. code-block:: none

 min(List[Int]): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/115_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

min(List[BigInt]): BigInt
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the smallest element in the list of :ref:`big integers <03_ride-language/02_data-types:BigInt>`. Fails if the list is empty.

.. code-block:: none

 min(List[BigInt]): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/116_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

removeByIndex(List[T], Int): List[T]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes an element from the :ref:`list <03_ride-language/02_data-types:List>` by index.

.. code-block:: none

 removeByIndex(list: List[T], index: Int): List[T]

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/117_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 removeByIndex(["Ride", 42, true], 1) # Returns ["Ride", true]

size(List[T]): Int
^^^^^^^^^^^^^^^^^^

Returns the size of the :ref:`list <03_ride-language/02_data-types:List>`.

.. code-block:: none

 size(arr: List[T]): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/118_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 size(["Hello", "World", "."]) # Returns 3

Math Functions
--------------

.. csv-table:: Math Functions
  :file: ../_static/03_ride-language/tables/119_Math-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

fraction(Int, Int, Int): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multiplies :ref:`integers <03_ride-language/02_data-types:Int>` :math:`a`, :math:`b` and divides the result by the integer :math:`c` to avoid overflow.

Fraction :math:`a × b / c` should not exceed the maximum value of the integer type :math:`9,223,372,036,854,755,807`.

The rounding method is DOWN, see rounding variables below.

.. code-block:: none

 fraction(a: Int, b: Int, c: Int): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/120_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

Lets assume that:

:math:`a = 100,000,000,000`,

:math:`b = 50,000,000,000,000`,

:math:`c = 2,500,000`.

The following formula, with :ref:`operators <03_ride-language/01_syntax-basics:Operators>` \* and /, fails due to overflow:

.. code-block:: none

 a * b / c #  overflow, because a × b exceeds max integer value

The fraction function with no overflow:

.. code-block:: none

 fraction(a, b, c) # Result: 2,000,000,000,000,000,000

fraction(Int, Int, Int, Union): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multiplies :ref:`integers <03_ride-language/02_data-types:Int>` :math:`a`, :math:`b` and divides the result by the integer :math:`c` to avoid overflow, applying the specified rounding method.

Fraction :math:`a × b / c` should not exceed the maximum value of the integer type :math:`9,223,372,036,854,755,807`.

.. code-block:: none

 fraction(a: Int, b: Int, c: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/121_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

fraction(BigInt, BigInt, BigInt): BigInt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multiplies :ref:`integers <03_ride-language/02_data-types:Int>` :math:`a`, :math:`b` and divides the result by the integer :math:`c` to avoid overflow, applying the specified rounding method.

Fraction :math:`a × b / c` should not exceed the maximum value of the integer type :math:`9,223,372,036,854,755,807`.

.. code-block:: none

 fraction(a: BigInt, b: BigInt, c: BigInt): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/122_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

fraction(BigInt, BigInt, BigInt, Union): BigInt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multiplies :ref:`integers <03_ride-language/02_data-types:Int>` :math:`a`, :math:`b` and divides the result by the integer :math:`c` to avoid overflow, applying the specified rounding method.

Fraction :math:`a × b / c` should not exceed the maximum value of the integer type :math:`9,223,372,036,854,755,807`.

.. code-block:: none

 fraction(a: BigInt, b: BigInt, c: BigInt, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/123_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

log(Int, Int, Int, Int, Int, Union): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calculates :math:`\log_b a`.

.. code-block:: none

 log(value: Int, vp: Int, base: Int, bp: Int, rp: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): Int

In Ride, there is no :ref:`data type <03_ride-language/02_data-types:Data Types>` with the floating point. That is why, for example, when you need to calculate :math:`\log_{2.7} 16.25` then the number value :math:`= 1625`, vp :math:`= 2` and the base :math:`= 27`, bp :math:`= 1`.

If the log function returns, for example, :math:`2807035420964590265`, and the parameter rp :math:`= 18`, then the result is :math:`2.807035420964590265`; in the number :math:`2807035420964590265` the last :math:`18` digits is a fractional part.

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/124_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calculates :math:`\log_b a` with high accuracy.

.. code-block:: none

 log(value: BigInt, ep: Int, base: BigInt, bp: Int, rp: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/125_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

median(List[Int]): Int
^^^^^^^^^^^^^^^^^^^^^^

Returns the median of the :ref:`list <03_ride-language/02_data-types:List>` of integers. Fails if the list is empty.

.. code-block:: none

 median(arr: List[Int]): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/126_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 median([1, 2, 3])         # Returns 2
 median([2, 4, 9, 20])     # Returns 6
 median([-2, -4, -9, -20]) # Returns -7

median(List[BigInt]): BigInt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the median of a :ref:`list <03_ride-language/02_data-types:List>` of :ref:`big integers <03_ride-language/02_data-types:BigInt>`. Fails if the list is empty or contains more than :math:`100` elements.

.. code-block:: none

 median(arr: List[BigInt]): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/127_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

pow(Int, Int, Int, Int, Int, Union): Int
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calculates :math:`a^{b}`.

.. code-block:: none

 pow(base: Int, bp: Int, exponent: Int, ep: Int, rp: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/128_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

:strong:`Example`

:math:`16.25^{2.7} = 1859,1057168...`

.. code-block:: none

 pow(1625, 2, 27, 1, 2, HALFUP) # function returns 185911, so the result is: 1859.11
 pow(1625, 2, 27, 1, 5, HALFUP) # function returns 185910572, so, the result is: 1859.10572

pow(BigInt, Int, BigInt, Int, Int, Union): BigInt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calculates :math:`a^{b}` with high accuracy.

.. code-block:: none

 pow(base: BigInt, bp: Int, exponent: BigInt, ep: Int, rp: Int, round: DOWN|CEILING|FLOOR|HALFUP|HALFEVEN): BigInt

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/129_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 2 1

Rounding Variables
^^^^^^^^^^^^^^^^^^

Below is the list of built-in rounding variables. The rounding variables are only used as the parameters of functions fraction, log, pow.

:strong:`Parameters`

.. csv-table:: Rounding Variables
  :file: ../_static/03_ride-language/tables/130_Rounding-Variables.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 3

:strong:`Example`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/131_Example.csv
  :header-rows: 1 
  :class: longtable
  :widths: 3 1 1 1 1 1

String Functions
----------------

.. csv-table:: String Functions
  :file: ../_static/03_ride-language/tables/132_String-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

contains(String, String): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the string contains substring.

.. code-block:: none

 contains(haystack: String, needle: String): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/133_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 "hello".contains("hell") # Returns true
 "hello".contains("world") # Returns false

drop(String, Int): String
^^^^^^^^^^^^^^^^^^^^^^^^^

Drops the first n characters of a string.

.. code-block:: none

 drop(xs: String, number: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/134_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Drops the last n characters of a string.

.. code-block:: none

 dropRight(xs: String, number: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/135_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the index of the first occurrence of a substring.

.. code-block:: none

 indexOf(str: String, substr: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/136_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 indexOf("Apple","ple") # Returns 3
 indexOf("Apple","le") # Returns 4
 indexOf("Apple","e") # Returns 5

indexOf(String, String, Int): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the index of the first occurrence of a substring after a certain index.

.. code-block:: none

 indexOf(str: String, substr: String, offset: Int): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/137_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 indexOf("Apple","ple", 1) # Returns 2
 indexOf("Apple","le", 2) # Returns 3
 indexOf("Apple","e", 3) # Returns 4

lastIndexOf(String, String): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the index of the last occurrence of a substring.

.. code-block:: none

 lastIndexOf(str: String, substr: String): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/138_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 lastIndexOf("Apple","pp") # Returns 1
 lastIndexOf("Apple","p") # Returns 2
 lastIndexOf("Apple","s") # Returns unit

lastIndexOf(String, String, Int): Int|Unit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the index of the last occurrence of a substring before a certain index.

.. code-block:: none

 lastIndexOf(str: String, substr: String, offset: Int): Int|Unit

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/139_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 lastIndexOf("mamamama","ma",4) # Returns 4
 lastIndexOf("mamamama","ma",3) # Returns 2

makeString(List[String], String): String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Concatenates list strings adding a separator.

.. code-block:: none

 makeString(arr: List[String], separator: String): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/140_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 makeString(["Apple","Orange","Mango"], " & ") # Returns "Apple & Orange & Mango"

size(String): Int
^^^^^^^^^^^^^^^^^

Returns the size of a string.

.. code-block:: none

 size(xs: String): Int

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/141_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 size("Ap") # Returns 2
 size("Appl") # Returns 4
 size("Apple") # Returns 5

split(String, String): List[String]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Splits a string delimited by a separator into a list of substrings.

.. code-block:: none

 split(str: String, separator: String): List[String]

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/142_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^

Takes the first n characters from a string.

.. code-block:: none

 take(xs: String, number: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/143_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Takes the last n characters from a string.

.. code-block:: none

 takeRight(xs: String, number: Int): String

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/144_Parameters.csv
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
---------------

.. csv-table:: Union Functions
  :file: ../_static/03_ride-language/tables/145_Union-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

isDefined(T|Unit): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if an argument is not unit.

.. code-block:: none

 isDefined(a: T|Unit): Boolean

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/146_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

value(T|Unit): T
^^^^^^^^^^^^^^^^

Gets a value from a :ref:`union <03_ride-language/02_data-types:Union>` type argument. Fails if it is :ref:`unit <03_ride-language/02_data-types:Unit>`.

.. code-block:: none

 value(a: T|Unit): T

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/147_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

valueOrElse(T|Unit, T): T
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a value from a :ref:`union <03_ride-language/02_data-types:Union>` type argument if it's not :ref:`unit <03_ride-language/02_data-types:Unit>`. Otherwise, returns the second argument.

.. code-block:: none

 valueOrElse(t: T|Unit, t0: T): T

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/148_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

valueOrErrorMessage(T|Unit, String): T
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a value from a :ref:`union <03_ride-language/02_data-types:Union>` type argument if it's not :ref:`unit <03_ride-language/02_data-types:Unit>`. Otherwise, fails with the message specified in the second argument.

.. code-block:: none

 valueOrErrorMessage(a: T|Unit, msg: String): T

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/149_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

Verification Functions
----------------------

.. csv-table:: Verification Functions
  :file: ../_static/03_ride-language/tables/150_Verification-Functions.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 4 1

bn256groth16Verify(ByteVector, ByteVector, ByteVector): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Range of functions. Check zk-SNARK by groth16 protocol on the bn254 curve. (Although the curve is called bn254 in the scientific literature, it is commonly referred to as bn256 in the code.)

.. csv-table:: bn256groth16Verify
  :file: ../_static/03_ride-language/tables/151_bn256groth16Verify.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/152_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

createMerkleRoot(List[ByteVector], ByteVector, Int) : ByteVector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calculates the Merkle root hash for transactions of block on the basis of the transaction hash and the sibling hashes of the Merkle tree. BLAKE2b-256 algorithm is used for hashing. To check for the transaction in the block, you need to compare the calculated hash with the transactionsRoot field in the block header. For more informtion see the :ref:`transactions root hash <02_decentralchain/04_block:Transactions Root Hash>`.

.. code-block:: none

 createMerkleRoot(merkleProofs: List[ByteVector], valueBytes: ByteVector, index: Int): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/153_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

ecrecover(messageHash: ByteVector, signature: ByteVector)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recovers public key from the message hash and the ECDSA digital signature based on the secp256k1 elliptic curve. Fails if the recovery failed. The public key is returned in uncompressed format (64 bytes). The function can be used to verify the digital signature of a message by comparing the recovered public key with the sender’s key.

.. code-block:: none

 ecrecover(messageHash: ByteVector, signature: ByteVector): ByteVector

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/154_Parameters.csv
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Range of functions. Check zk-SNARK by groth16 protocol.

.. csv-table:: groth16Verify
  :file: ../_static/03_ride-language/tables/155_groth16Verify.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/156_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

:strong:`Example`

.. code-block:: none

 groth16Verify(vk, proof, inputs) 

rsaVerify(digestAlgorithmType, ByteVector, ByteVector, ByteVector): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Range of functions. Check that the RSA digital signature is valid, i.e. it was created by the owner of the public key.

.. csv-table:: rsaVerify
  :file: ../_static/03_ride-language/tables/157_rsaVerify.csv
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
  :file: ../_static/03_ride-language/tables/158_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1

sigVerify(ByteVector, ByteVector, ByteVector): Boolean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Range of functions. Check that the Curve25519 digital signature is valid, i.e. it was created by the owner of the public key.

.. csv-table:: sigVerify
  :file: ../_static/03_ride-language/tables/159_sigVerify.csv
  :header-rows: 1 
  :class: longtable
  :widths: 5 1 1

:strong:`Parameters`

.. csv-table:: Parameters
  :file: ../_static/03_ride-language/tables/160_Parameters.csv
  :header-rows: 1 
  :class: longtable
  :widths: 1 1