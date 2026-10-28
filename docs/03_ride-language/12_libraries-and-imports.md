# Libraries and Imports

```{note}
Verified against node-scala commit [`104ddc70e8`](https://github.com/Decentral-America/node-scala/tree/104ddc70e8007175e0d1306b6db527ad37bb1b1f): `ScriptPreprocessor.scala`, `DirectiveSet.scala` and `API.compile` in the `lang` module, and `compileWithImports` in the node's `UtilsApiRoute.scala`. Every example and error message below was compiled on the Testnet node.
```

Ride has no modules at run time. A script on the chain is self-contained: it cannot load code stored somewhere else. From version 5 it can invoke another dApp's callables, as covered in {doc}`dApp-to-App Invocation <07_dapp-to-app-invocation>`. What Ride does have is a compile-time import: the `IMPORT` directive pastes the declarations of one or more **library** files into a script before it is compiled.

## Writing a Library

A library is a Ride file with `{-# CONTENT_TYPE LIBRARY #-}`. It contains declarations only, `let` and `func`, with no final expression:

```none
{-# STDLIB_VERSION 6 #-}
{-# CONTENT_TYPE LIBRARY #-}
{-# SCRIPT_TYPE ACCOUNT #-}

func twice(x: Int) = x * 2
```

Three rules apply:

* **It must say `CONTENT_TYPE LIBRARY`.** Importing any other file fails with ``CONTENT_TYPE of `a.ride` is not LIBRARY``.
* **It cannot import.** A library with its own `IMPORT` directive fails with `Libraries should not contain imports`.
* **Its other directives are ignored.** The compiler strips every directive from a library before pasting it in, so the library compiles with the importing script's `STDLIB_VERSION`, `CONTENT_TYPE` and `SCRIPT_TYPE`. A library that calls `replaceAll`, which is new in version 9, fails to compile when imported into a version 4 script, whatever version the library itself declares. Write the library's directives to match the scripts that will import it, so you can compile the library on its own to check it.

## Importing a Library

List the libraries, separated by commas, in one `IMPORT` directive:

```none
{-# STDLIB_VERSION 6 #-}
{-# CONTENT_TYPE DAPP #-}
{-# SCRIPT_TYPE ACCOUNT #-}
{-# IMPORT lib/math.ride #-}

@Callable(i)
func double(x: Int) = [IntegerEntry("result", twice(x))]
```

The compiler replaces the `IMPORT` directive with the libraries' declarations and compiles the result as one script. The consequences:

* **Names are keys, not paths.** The node does not read files. Whoever compiles supplies a map from each name to its source, and an unknown name fails with ``Unresolved imports: `b.ride` ``.
* **Everything is pasted, used or not.** Every declaration of every imported library ends up in the compiled script and counts towards its {ref}`size limit <03_ride-language/10_limitations:Script Size>`. A function the script never calls still takes space, but it adds nothing to complexity.
* **Names share one scope.** A library declaration and a script declaration with the same name fail with `Value 'twice' can't be defined because function with this name is already defined`.
* **Keep libraries independent of each other.** With up to four libraries, they are pasted in the order the directive lists them, so one can call another that comes earlier. With five or more, the order is not preserved and such calls fail with `Can't find a function`.
* **Nothing records the import.** The chain stores only the compiled script, and decompiling it shows the library's functions as if they had been written inline.

## Compiling with Imports

The node's `POST /utils/script/compileCode` endpoint takes only a single file, and fails on any `IMPORT` with `Unresolved imports`. Use `POST /utils/script/compileWithImports` instead, sending the script and a map of library names to sources:

```bash
curl -X POST https://testnet-node.decentralchain.io/utils/script/compileWithImports \
  -H 'Content-Type: application/json' \
  -d '{
    "script": "{-# STDLIB_VERSION 6 #-}\n{-# CONTENT_TYPE DAPP #-}\n{-# SCRIPT_TYPE ACCOUNT #-}\n{-# IMPORT lib/math.ride #-}\n\n@Callable(i)\nfunc double(x: Int) = [IntegerEntry(\"result\", twice(x))]",
    "imports": {
      "lib/math.ride": "{-# STDLIB_VERSION 6 #-}\n{-# CONTENT_TYPE LIBRARY #-}\n{-# SCRIPT_TYPE ACCOUNT #-}\n\nfunc twice(x: Int) = x * 2"
    }
  }'
```

```json
{"script":"base64:BgIHCAISAwoBAQEBBXR3aWNlAQF4CQBoAgUBeAACAQFpAQZkb3VibGUBAXgJAMwIAgkBDEludGVnZXJFbnRyeQICBnJlc3VsdAkBBXR3aWNlAQUBeAUDbmlsAA4EH7k=","complexity":0,"extraFee":400000}
```

Its response is shorter than `compileCode`'s, and two of its fields mean something different:

* **`complexity`** is the verifier's complexity: the whole script's for an account or asset script, and the `@Verifier` function's for a dApp. A dApp without a verifier always reports 0, as here.
* **`extraFee`** is always 400,000 (0.004 DCC), whatever the verifier costs.

For the real values, send the compiled `script` to `POST /utils/script/estimate`. For the example above, it returns `"callableComplexities": {"double": 4}` and `"extraFee": 0`, because a dApp with no verifier costs nothing extra to transact from. The rule behind `extraFee` is under {ref}`Complexity <03_ride-language/10_limitations:Complexity>`.

A larger compiled script also means a higher Set Script fee wherever that fee is charged per kilobyte, so keep libraries small.
