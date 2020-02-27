# Cython_test_multiprocess
  Runtime comparison of different implementations of calculating Prime numbers.

- [Tests](#tests)
  - [Default Test](#default-test)
  - [Half of N Bounding Test](#half-of-n-bounding-test)
  - [Square Root of N Bounding Test](#square-root-of-n-bounding-test)
- [Implementations](#implementations)
  - [Python Implementation](#python-implementation)
  - [Python Implementation with Lambdas](#python-implementation-with-lambdas)
  - [Python Implementation with LRU Caching](#python-implementation-with-lru-caching)
  - [Cython Implementation](#cython-implementation)
  - [Cython Implementation with Lambdas](#cython-implementation-with-lambdas)
  - [Cython Implementation with LRU Caching](#cython-implementation-with-lru-caching)
  - [Optimized Cython Implementation](#optimized-cython-implementation)
  - [Optimized Cython Implementation with Lambdas](#optimized-cython-implementation-with-lambdas)
  - [Optimized Cython Implementation with LRU Caching](#optimized-cython-implementation-with-lru-caching)

# Tests
  Each one of these programs has three different versions of calculating primes.<br>
  For variable `N` as the number checked in the primality test:

## Default
  Check divisibility of `N` by each number less than `N`.

## Half of N Bounding Test
  * Check divisibility of `N` by each number less than `math.floor((N / 2))`:
  * This method should theoretically be 2x as fast as the
  [default test method](#default).

## Square Root of N Bounding Test
  * Check divisibility of `N` by each number less than `math.floor(sqrt(N))`:
  * This method should theoretically be log(N) as fast as the
  [default test method](#default).

# Implementations
## Python Implementation
  * Defined in `Find_Nth_Prime_Python.py`
  * Loops over all numbers from `0` to `max_num` as variable `N`, calls
  the test method functions for each of those numbers.
  * Calling the test method functions for each value of `N` means we have function
  overhead of `max_num` calls.

## Python Implementation with Lambdas
  * Defined in [Find_Nth_Prime_Python_Lambda.py](Find_Nth_Prime_Python_Lambda.py)
  * Only calls the calculation function once with a `max_num` as a parameter.
  * The calculation function handles all the logic that `Find_Nth_Prime_Python.py`'s the calculation functions have, but all using a single lambda function inside the calculation function.
  * This reduces the function calling overhead, which can lead to significant time
  savings.

## Python Implementation with LRU Caching
  * Defined in  `Find_Nth_Prime_Python_LRU.py`
  * Similar to the [Python Implementation](#python-implementation) in that the
  test method functions

## Cython Implementation
  * Defined in `Find_Nth_Prime_Cython.py`

## Cython Implementation with Lambdas
  * Defined in `Find_Nth_Prime_Cython_Lambda.py`

## Cython Implementation with LRU Caching
  * Defined in `Find_Nth_Prime_Cython_LRU.py`

## Optimized Cython Implementation
  * Defined in `Find_Nth_Prime_Optimized.py`
  * Uses manual static typing for variables for slightly better performance.

## Optimized Cython Implementation with Lambdas
  * Defined in `Find_Nth_Prime_Optimized_Lambda.py`
  * Uses manual static typing for variables for slightly better performance.

## Optimized Cython Implementation with LRU Caching
  * Defined in `Find_Nth_Prime_Optimized_LRU.py`
  * Uses manual static typing for variables for slightly better performance.

# Related Files:
## master1.py
  Used by Cython to compile the Find_Nth_Prime1.pyx file.

## master2.py
  Used by Cython to compile the Find_Nth_Prime2.pyx file.

## tester.py
  Python wrapper for calling the programs.
  It's handles the multiprocessing/threading of the other programs,
  which involves creating a process for each one of the different tests
  and running those tests simultaneously.
  Each program's runtime is measured, and is both displayed to the user
  inside the console as well as saved to files under the `files_runs` folder.
