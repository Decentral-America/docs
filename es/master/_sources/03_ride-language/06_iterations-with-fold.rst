***********************
Iterations with FOLD<N>
***********************

FOLD<N> macro makes it possible to implement operations on a list of values such as sum, filter, map, zip, exists, etc. The macro behaves like the fold or reduce function in other programming languages.

.. code-block:: none

 FOLD<N>(list, start, foldFunc)

.. csv-table:: Iterations with FOLD
  :file: ../_static/03_ride-language/tables/208_Iterations-with-FOLD.csv
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
