# Function Reference

One page per standard library version lists every built-in function and operator available at that version: its full signature, its complexity, and what it does. Each page is generated from node-scala's compiled standard library by `docs/scripts/generate_ride_reference.py` and records the node-scala commit it was generated from.

On each page:

* **Overloads have their own rows.** A function with several signatures, such as `toString` or `fraction`, has one row per signature, and each signature can have its own cost.
* **Notes mark what changed.** On the V9 page, for example, *New in V9.* marks a function added in version 9 and *Was 6 in V8.* a cost that changed from version 8, as for `drop` on a `ByteVector`. *dApp scripts only.* and *Not available in asset scripts.* mark the functions you can't call from every kind of script.
* **Costs are the node's.** They are what the node charges for one call at that version, so they can differ from the figures in the hand-written {doc}`Functions <../03_functions>` page, which was written for version 5.

For the cost of one function across versions 5 to 9 at a glance, see {doc}`Complexity Changes by Version <../09_complexity-changes>`. For everything else each version adds, such as new structures and fields, see {doc}`Standard Library Versions <../08_stdlib-versions>`. For versions 1 to 5, see {doc}`Previous Versions <../11_previous-versions>`.

```{toctree}
:maxdepth: 1

v9
v8
v7
v6
```
