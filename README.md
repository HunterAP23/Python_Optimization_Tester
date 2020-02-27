# Cython_test_multiprocess
  Runtime comparison of different implementations of calculating Prime numbers.

- [Tests](#tests)
  - [Default Test](#default-test)
  - [Half of N Bounding Test](#half-of-n-bounding-test)
  - [Square Root of N Bounding Test](#square-root-of-n-bounding-test)
- [Implementations](#implementations)
  - [Cpython Variants](#cpython-variants)
    - [Default](#cpython)
    - [Lambdas](#cpython-with-lambdas)
    - [LRU Caching](#cpython-with-lru-caching)
    - [Numpy Arrays](#cpython-with-numpy-arrays)
    - [Numpy Arrays & Lambdas](#cpython-with-numpy-arrays-&-lambdas)
    - [Numpy Arrays & LRU Caching](#cpython-with-numpy-arrays-&-lru-caching)
    - [Cython](#cpython-cython)
    - [Cython w/ Lambdas](#cpython-cython-with-lambdas)
    - [Cython w/ LRU Caching](#cpython-cython-with-lru-caching)
    - [Cython w/ Numpy Arrays](#cpython-cython-with-numpy-arrays)
    - [Cython w/ Numpy Arrays & Lambdas](#cpython-cython-with-numpy-arrays-&-lambdas)
    - [Cython w/ Numpy Arrays & LRU Caching](#cpython-cython-with-numpy-arrays-&-lru-caching)
    - [Cython Optimized](#cpython-optimized-cython)
    - [Cython Optimized w/ Lambdas](#cpython-optimized-cython-with-lambdas)
    - [Cython Optimized w/ LRU Caching](#cpython-optimized-cython-with-lru-caching)
    - [Cython Optimized w/ Numpy Arrays](#cpython-optimized-cython-with-numpy-arrays)
    - [Cython Optimized w/ Numpy Arrays & Lambdas](#cpython-optimized-with-numpy-arrays-&-lambdas)
    - [Cython Optimized w/ Numpy Arrays & LRU Caching](#cpython-optimized-with-numpy-arrays-&-lru-caching)
  - [Anaconda Variants](#anaconda-variants)
    - [Default](#anaconda)
    - [Lambdas](#anaconda-with-lambdas)
    - [LRU Caching](#anaconda-with-lru-caching)
    - [Numpy Arrays](#anaconda-with-numpy-arrays)
    - [Numpy Arrays & Lambdas](#anaconda-with-numpy-arrays-&-lambdas)
    - [Numpy Arrays & LRU Caching](#anaconda-with-numpy-arrays-&-lru-caching)
    - [Cython](#anaconda-cython)
    - [Cython w/ Lambdas](#anaconda-cython-with-lambdas)
    - [Cython w/ LRU Caching](#anaconda-cython-with-lru-caching)
    - [Cython w/ Numpy Arrays](#anaconda-cython-numpy-arrays)
    - [Cython w/ Numpy Arrays & Lambdas](#anaconda-cython-with-numpy-arrays-&-lambdas)
    - [Cython w/ Numpy Arrays & LRU Caching](#anaconda-cython-with-numpy-arrays-&-lru-caching)
    - [Cython Optimized](#anaconda-optimized-cython)
    - [Cython Optimized w/ Lambdas](#anaconda-optimized-cython-with-lambdas)
    - [Cython Optimized w/ LRU Caching](#anaconda-optimized-cython-with-lru-caching)
    - [Cython Optimized w/ Numpy Arrays](#anaconda-optimized-cython-with-numpy-arrays)
    - [Cython Optimized w/ Numpy Arrays & Lambdas](#anaconda-optimized-with-numpy-arrays-&-lambdas)
    - [Cython Optimized w/ Numpy Arrays & LRU Caching](#anaconda-optimized-with-numpy-arrays)
  - [PyPy Variants](#pypy-variants)
    - [Default](#pypy)
    - [Lambdas](#pypy-with-lambdas)
    - [LRU Caching](#pypy-with-lru-caching)
    - [Numpy Arrays](#pypy-with-numpy-arrays)
    - [Numpy Arrays & Lambdas](#pypy-with-numpy-arrays-&-lambdas)
    - [Numpy Arrays & LRU Caching](#pypy-with-numpy-arrays-&-lru-caching)
    - [Cython](#pypy-cython)
    - [Cython w/ Lambdas](#pypy-cython-with-lambdas)
    - [Cython w/ LRU Caching](#pypy-cython-with-lru-caching)
    - [Cython w/ Numpy Arrays](#pypy-cython-numpy-arrays)
    - [Cython w/ Numpy Arrays & Lambdas](#pypy-cython-with-numpy-arrays-&-lambdas)
    - [Cython w/ Numpy Arrays & LRU Caching](#pypy-cython-with-numpy-arrays-&-lru-caching)
    - [Cython Optimized](#pypy-optimized-cython)
    - [Cython Optimized w/ Lambdas](#pypy-optimized-cython-with-lambdas)
    - [Cython Optimized w/ LRU Caching](#pypy-optimized-cython-with-lru-caching)
    - [Cython Optimized w/ Numpy Arrays](#pypy-optimized-cython-with-numpy-arrays)
    - [Cython Optimized w/ Numpy Arrays & Lambdas](#pypy-optimized-with-numpy-arrays-&-lambdas)
    - [Cython Optimized w/ Numpy Arrays & LRU Caching](#pypy-optimized-with-numpy_arrays)

# Tests
  Each one of these programs has three different versions of calculating primes.<br>
  For variable `N` as the number checked in the primality test:

## Default
  * Check divisibility of `N` by each number less than `N`.

## Half of N Bounding Test
  * Check divisibility of `N` by each number less than `math.floor((N / 2))`:
  * This method should theoretically be 2x as fast as the
  [default test method](#default).

## Square Root of N Bounding Test
  * Check divisibility of `N` by each number less than `math.floor(sqrt(N))`:
  * This method should theoretically be log(N) as fast as the
  [default test method](#default).

# Implementations
## Cpython Variants
### CPython
  * Defined in [Find_Nth_Prime_Python.py](Find_Nth_Prime_Python.py)
  * Loops over all numbers from `0` to `max_num` as variable `N`, calls
  the test method functions for each of those numbers.
  * Since we're calling the each test method functions `N` times each, this means
  we have function call overhead of `max_num` calls per test method.

### CPython with Lambdas
  * Defined in [Find_Nth_Prime_Python_Lambda.py](Find_Nth_Prime_Python_Lambda.py)
  * Only calls the calculation function once with a `max_num` as a parameter.
  * The calculation function handles all the logic that `Find_Nth_Prime_Python.py`'s the calculation functions have, but all using a single lambda function inside the calculation function.
  * This reduces the function call overhead, which can lead to significant time
  savings.

### CPython with LRU Caching
  * Defined in [Find_Nth_Prime_Python_LRU.py](Find_Nth_Prime_Python_LRU.py)
  * Similar to the [Python](#cpython) in that the
  test method functions are each called `max_num` amount of times, but this
  implementation caches the results of previous function calls to speed up the
  calculation of the current function call.
  * Despite the supposed function call overhead

### CPython with Numpy Arrays
  * Defined in [Find_Nth_Prime_Python_Numpy.py](Find_Nth_Prime_Python_Numpy.py)
  * Same as [Python](#cpython), but uses numpy
  arrays instead of Python lists.

### CPython with Numpy Arrays & Lambdas
  * Defined in [Find_Nth_Prime_Python_Numpy_Lambdas.py](Find_Nth_Prime_Python_Numpy_Lambdas.py)
  * Same as [Python with Lambdas](#cpython-with-lambdas),
  but uses numpy arrays instead of Python lists.

### CPython with Numpy Arrays & LRU Caching
  * Defined in [Find_Nth_Prime_Python_Numpy_LRU.py](Find_Nth_Prime_Python_Numpy_LRU.py)
  * Same as [Python with Lambdas](#cpython-with-lambdas),
  but uses numpy arrays instead of Python lists.

### CPython Cython
  * Defined in [Find_Nth_Prime_Cython.pyx](Find_Nth_Prime_Cython.pyx)
  * Same as [Python](#cpython), but compiled
  using Cython.

### Cython with Lambdas
  * Defined in [Find_Nth_Prime_Cython_Lambda.pyx](Find_Nth_Prime_Cython_Lambda.pyx)
  * Same as [Python with Lambdas](#cpython-with-lambdas), but compiled using Cython.

### Cython with LRU Caching
  * Defined in [Find_Nth_Prime_Cython_LRU.pyx](Find_Nth_Prime_Cython_LRU.pyx)
  * Same as [Python with LRU Caching](#cpython-with-lru-caching), but compiled using Cython.

### Cython with Numpy Arrays
  * Defined in [Find_Nth_Prime_Cython_Numpy.pyx](Find_Nth_Prime_Cython_Numpy.pyx)
  * Same as [Cython](#cython), but uses numpy
  arrays instead of Python lists.

### Cython with Numpy Arrays & Lambdas
  * Defined in [Find_Nth_Prime_Cython_Numpy.pyx](Find_Nth_Prime_Cython_Numpy.pyx)
  * Same as [Cython with Lambdas](#cython-with-lambdas),
  but uses numpy arrays instead of Python lists.

### Optimized Cython
  * Defined in [Find_Nth_Prime_Optimized.pyx](Find_Nth_Prime_Optimized.pyx)
  * Uses manual static typing for variables for slightly better performance.

### Optimized Cython with Lambdas
  * Defined in [Find_Nth_Prime_Optimized_Lambda.pyx](Find_Nth_Prime_Optimized_Lambda.pyx)
  * Uses manual static typing for variables for slightly better performance.

### Optimized Cython with LRU Caching
  * Defined in [Find_Nth_Prime_Optimized_LRU.pyx](Find_Nth_Prime_Optimized_LRU.pyx)
  * Uses manual static typing for variables for slightly better performance.

## Anaconda Variants


# Related Files:
## Compiling
  * [Compiler_Cython.py](Compiler_Cython.py): Used by Cython to compile the
  * [Compiler_Cython_LAmbda.py](Compiler_Cython_Lambda.py): Used by Cython to compile the
  * [Threader.py](Threader.py):<br>
    * Python wrapper for calling the programs.
    * It's handles the multiprocessing/threading of the other programs,
    which involves creating a process for each one of the different tests
    and running those tests simultaneously.
    * Each program's runtime is measured, and is both displayed to the user
    inside the console as well as saved to files under the `files_runs` folder.
