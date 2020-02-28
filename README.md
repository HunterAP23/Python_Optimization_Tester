# Cython_test_multiprocess
  Runtime comparison of different implementations of calculating Prime numbers.

- [Setup](#setup)
- [Tests](#tests)
  - [Default Test](#default-test)
  - [N / 2 Bounding Test](#half-of-n-bounding-test)
  - [sqrt(N) Bounding Test](#square-root-of-n-bounding-test)
- [Implementations](#implementations)
  - [CPython Variants](#cpython-variants)
    - [Default](#cpython)
    - [Lambdas](#cpython-with-lambdas)
    - [LRU Caching](#cpython-with-lru-caching)
    - [Numpy Arrays](#cpython-with-numpy-arrays)
    - [Numpy Arrays & Lambdas](#cpython-with-numpy-arrays-and-lambdas)
    - [Numpy Arrays & LRU Caching](#cpython-with-numpy-arrays-and-lru-caching)
    - [Cython](#cpython-cython)
    - [Cython w/ Lambdas](#cpython-cython-with-lambdas)
    - [Cython w/ LRU Caching](#cpython-cython-with-lru-caching)
    - [Cython w/ Numpy Arrays](#cpython-cython-with-numpy-arrays)
    - [Cython w/ Numpy Arrays & Lambdas](#cpython-cython-with-numpy-arrays-and-lambdas)
    - [Cython w/ Numpy Arrays & LRU Caching](#cpython-cython-with-numpy-arrays-and-lru-caching)
    - [Cython Optimized](#cpython-optimized-cython)
    - [Cython Optimized w/ Lambdas](#cpython-optimized-cython-with-lambdas)
    - [Cython Optimized w/ LRU Caching](#cpython-optimized-cython-with-lru-caching)
    - [Cython Optimized w/ Numpy Arrays](#cpython-optimized-cython-with-numpy-arrays)
    - [Cython Optimized w/ Numpy Arrays & Lambdas](#cpython-optimized-cython-with-numpy-arrays-and-lambdas)
    - [Cython Optimized w/ Numpy Arrays & LRU Caching](#cpython-optimized-cython-with-numpy-arrays-and-lru-caching)
  - [Anaconda Variants](#anaconda-variants)
  - [PyPy Variants](#pypy-variants)

## Setup
1. Download the newest version of PyPy (skip if you're not planning on using PyPy).
2. Download the newest version of Anaconda (skip if you're not planning on using Anaconda).
3. Download or clone the repository.
4. Install the pip requirements with `pip install requirements.txt`
5. Run the program! I included the related `.bat` and `.sh` files for running
the different runtimes as needed.
  * <b>Windows</b>:
    * [Clean.bat](Clean.bat): Deletes all compiled Python files
    (`*.c`, `*.pyc`, `*.pyd`, `*.so`) including the `__pycache__` folder, and delete any text files including the `files_runs` and `files_compile` folders.
    * [Compile_Python.py](Compile_Python.py): Runs [Clean.bat](Clean.bat), then
    recompiles all `*.py` files using the `py_compile` module, then uses Cython
    to compile all `*.pyx` files.
    * [Compile_Conda.py](Compile_Conda.py): Same as [Compile_Python.py](Compile_Python.py),
    but uses the Anaconda runtime. This will ask you to create an environment,
    which will use Python 3.7 and install cython and numpy automatically.

## Tests
  Each one of these programs has three different versions of calculating primes.<br>
  For variable `N` as the number checked in the primality test:

#### Default Test
  * Check divisibility of `N` by each number less than `N`.

#### Half of N Bounding Test
  * Check divisibility of `N` by each number less than `math.floor((N / 2))`:
  * This method should theoretically be 2x as fast as the
  [default test method](#default).

#### Square Root of N Bounding Test
  * Check divisibility of `N` by each number less than `math.floor(sqrt(N))`:
  * This method should theoretically be log(N) as fast as the
  [default test method](#default).

# Implementations
### Cpython Variants
#### CPython
  * Defined in [Find_Nth_Prime_Python.py](Find_Nth_Prime_Python.py)
  * Loops over all numbers from `0` to `max_num` as variable `N`, calls
  the test method functions for each of those numbers.
  * Since we're calling the each test method functions `N` times each, this means
  we have function call overhead of `max_num` calls per test method.

#### CPython with Lambdas
  * Defined in [Find_Nth_Prime_Python_Lambda.py](Find_Nth_Prime_Python_Lambda.py)
  * Only calls the calculation function once with a `max_num` as a parameter.
  * The calculation function handles all the logic that `Find_Nth_Prime_Python.py`'s the calculation functions have, but all using a single lambda function inside the calculation function.
  * This reduces the function call overhead, which can lead to significant time
  savings.

#### CPython with LRU Caching
  * Defined in [Find_Nth_Prime_Python_LRU.py](Find_Nth_Prime_Python_LRU.py)
  * Similar to the [Python](#cpython) in that the
  test method functions are each called `max_num` amount of times, but this
  implementation caches the results of previous function calls to speed up the
  calculation of the current function call.
  * Despite the supposed function call overhead

#### CPython with Numpy Arrays
  * Defined in [Find_Nth_Prime_Python_Numpy.py](Find_Nth_Prime_Python_Numpy.py)
  * Same as [Python](#cpython), but uses Numpy arrays instead of Python lists.

#### CPython with Numpy Arrays and Lambdas
  * Defined in [Find_Nth_Prime_Python_Numpy_Lambdas.py](Find_Nth_Prime_Python_Numpy_Lambdas.py)
  * Same as [Python with Lambdas](#cpython-with-lambdas), but uses Numpy arrays
  instead of Python lists.

#### CPython with Numpy Arrays and LRU Caching
  * Defined in [Find_Nth_Prime_Python_Numpy_LRU.py](Find_Nth_Prime_Python_Numpy_LRU.py)
  * Same as [Python with Lambdas](#cpython-with-lambdas), but uses Numpy arrays
  instead of Python lists.

#### CPython Cython
  * Defined in [Find_Nth_Prime_Cython.pyx](Find_Nth_Prime_Cython.pyx)
  * Same as [Python](#cpython), but compiled using Cython.

#### CPython Cython with Lambdas
  * Defined in [Find_Nth_Prime_Cython_Lambda.pyx](Find_Nth_Prime_Cython_Lambda.pyx)
  * Same as [Python with Lambdas](#cpython-with-lambdas), but compiled using Cython.

#### CPython Cython with LRU Caching
  * Defined in [Find_Nth_Prime_Cython_LRU.pyx](Find_Nth_Prime_Cython_LRU.pyx)
  * Same as [Python with LRU Caching](#cpython-with-lru-caching), but compiled using Cython.

#### CPython Cython with Numpy Arrays
  * Defined in [Find_Nth_Prime_Cython_Numpy.pyx](Find_Nth_Prime_Cython_Numpy.pyx)
  * Same as [Cython](#cython), but uses Numpy arrays instead of Python lists.

#### CPython Cython with Numpy Arrays and Lambdas
  * Defined in [Find_Nth_Prime_Cython_Numpy_Lambda.pyx](Find_Nth_Prime_Cython_Numpy_Lambda.pyx)
  * Same as [Cython with Lambdas](#cython-with-lambdas), but uses Numpy arrays
  instead of Python lists.

#### CPython Cython with Numpy Arrays and LRU Caching
  * Defined in [Find_Nth_Prime_Cython_Numpy_LRU.pyx](Find_Nth_Prime_Cython_Numpy_LRU.pyx)
  * Same as [Cython with Lambdas](#cython-with-lambdas), but uses Numpy arrays
    instead of Python lists.

#### CPython Optimized Cython
  * Defined in [Find_Nth_Prime_Optimized.pyx](Find_Nth_Prime_Optimized.pyx)
  * Uses manual static typing for variables for slightly better performance.

#### CPython Optimized Cython with Lambdas
  * Defined in [Find_Nth_Prime_Optimized_Lambda.pyx](Find_Nth_Prime_Optimized_Lambda.pyx)
  * Uses manual static typing for variables for slightly better performance.

#### CPython Optimized Cython with LRU Caching
  * Defined in [Find_Nth_Prime_Optimized_LRU.pyx](Find_Nth_Prime_Optimized_LRU.pyx)
  * Uses manual static typing for variables for slightly better performance.

#### CPython Optimized Cython with Numpy Arrays
  * Defined in [Find_Nth_Prime_Optimized_Numpy.pyx](Find_Nth_Prime_Optimized_Numpy.pyx)
  * Uses manual static typing for variables for slightly better performance.

#### CPython Optimized Cython with Numpy Arrays and Lambdas
  * Defined in [Find_Nth_Prime_Optimized_Numpy_Lambda.pyx](Find_Nth_Prime_Optimized_Numpy_Lambda.pyx)
  * Uses manual static typing for variables for slightly better performance.

#### CPython Optimized Cython with Numpy Arrays and LRU Caching
  * Defined in [Find_Nth_Prime_Optimized_Numpy_LRU.pyx](Find_Nth_Prime_Optimized_Numpy_LRU.pyx)
  * Uses manual static typing for variables for slightly better performance.

### Anaconda Variants
There are no differences in the code between these implementations and the CPython ones.
The only difference is that the exact same CPython tests were run with the
Anaconda Python runtime rather than the default CPython runtime.
* <b>Anaconda</b>: [CPython](#cpython)
* <b>Anaconda with Lambdas</b>: [CPython w/ Lambdas](#cpython-with-lambdas),
* <b>Anaconda with LRU Caching</b>: [CPython w/ LRU Caching](#cpython-with-lru-caching)
* <b>Anaconda with Numpy Arrays</b>: [CPython w/ Numpy Arrays](#cpython-with-numpy-arrays)
* <b>Anaconda with Numpy Arrays and Lambdas</b>: [CPython w/ Numpy Arrays & Lambdas](#cpython-with-numpy-arrays-and-lambdas)
* <b>Anaconda Cython</b>: [CPython Cython](#cpython-cython)
* <b>Anaconda Cython with Lambdas</b>: [CPython Cython w/ Lambdas](#cpython-cython-with-lambdas)
* <b>Anaconda Cython with LRU Caching</b>: [CPython Cython w/ LRU Caching](#cpython-cython-with-lru-caching)
* <b>Anaconda Cython with Numpy Arrays</b>: [CPython Cython w/ Numpy Arrays](#cpython-cython-with-numpy-arrays)
* <b>Anaconda Cython with Numpy Arrays and Lambdas</b>: [CPython Cython w/ Numpy Arrays & Lambdas](#cpython-cython-with-numpy-arrays-and-lambdas)
* <b>Anaconda Optimized Cython</b>: [CPython Cython Optimized](#cpython-optimized-cython)
* <b>Anaconda Optimized Cython with Lambdas</b>: [CPython Cython Optimized w/ Lambdas](#cpython-optimized-cython-with-lambdas)
* <b>Anaconda Optimized Cython with LRU Caching</b>: [CPython Cython Optimized w/ LRU Caching](#cpython-optimized-cython-with-lru-caching)
* <b>Anaconda Optimized with Numpy Arrays</b>: [CPython Cython Optimized w/ Numpy Arrays](#cpython-optimized-cython-with-numpy-arrays)
* <b>Anaconda Optimized with Numpy Arrays and Lambdas</b>: [CPython Cython Optimized w/ Numpy Arrays & Lambdas](#cpython-optimized-cython-with-numpy-arrays-and-lambdas)
* <b>Anaconda Optimized with Numpy Arrays and LRU Caching</b>: [CPython Cython Optimized w/ Numpy Arrays & LRU Caching](#cpython-optimized-cython-with-numpy-arrays-and-lru-caching)


## Related Files:
#### Compiling
  * [Compiler_Cython.py](Compiler_Cython.py): Used by Cython to compile the
  * [Compiler_Cython_Lambda.py](Compiler_Cython_Lambda.py): Used by Cython to compile the
  * [Threader.py](Threader.py):<br>
    * Python wrapper for calling the programs.
    * It's handles the multiprocessing/threading of the other programs,
    which involves creating a process for each one of the different tests
    and running those tests simultaneously.
    * Each program's runtime is measured, and is both displayed to the user
    inside the console as well as saved to files under the `files_runs` folder.
