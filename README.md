# Python Performance Optimization Test Suite
  Runtime comparison of different implementations of calculating Prime numbers.

- [Setup](#setup)
- [Tests](#tests)
- [Optimizations](#optimizations)

## Setup
1. Download the newest version of PyPy (skip if you're not planning on using PyPy).
2. Download the newest version of Anaconda (skip if you're not planning on using Anaconda).
3. Download or clone the repository.
4. Install the pip requirements with `pip install -r requirements.txt -U`
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
|       Test       | Description                                           |
|------------------|-------------------------------------------------------|
|       Primes     |    Find every Prime Number up to a given integer      |
|     Fibonacci    | Calculate all Fibonacci numbers up to a given integer |
|  Database Usage  |          Run different database operations            |
| Image Processing |             Apply modifications to images             |
| Video Processing |             Apply modifications to videos             |
## Optimizations
- Python Runtimes:
  - __CPython__: The standard C-based Python runtime
  - __Pypy__: An alternative implementation of the CPython runtime, utilizing a JIT compiler, but lacks support for some CPython extensions
  - __Cinder__: Meta's internal CPython implementation, highly unsupported for external use cases
  - __Pyston__: Fork of the CPython 3.8 runtime with a claimed 30% performance improvement
- Compilation:
  - __Interpreted__: All code is interpreted by the Python runtime
  - __Compiled Cython__: Base code is compiled with Cython without any Cython optimizations
  - __Optimized Cython__: Base code is compiled with Cython and is modified to utilize Cython optimizations (such as static typing)
  - __Numba JIT__: Base code is compiled just-in-time with Numba
  - __Numba AOT__: Base code is compiled ahead-of-time with Numba
- Code Branching:
  - __Inline / Imperative__: Code is run within the main function
  - __Function__: Code is put into it's own function
- Caching:
  - __Least-Recently-Used Cache__: In-memory caching with Python built-ins `functools.lru_cache`
  - __JSON Cache__: File-based caching with JSON files
  - __SQLite Cache__: Database caching with local SQLite
  - __Redis Cache__: Database caching with in-memory Redis service
- Data Storage Objects:
  - __Lists__: Store results inside mutable Python lists
  - __Tuples__: Store results inside immutable Python tuples
  - __Numpy Arrays__: Store results inside mutable in-memory Numpy arrays
  - __Pandas DataFrames / Series__: Store results inside mutable Pandas DataFrames / Series
- Data Comprehension:
  - __For Loops__: The "standard" method of iterating over data.
  - __List Comprehension__: Create a mutable list directly from generators
  - __Tuple Comprehension__: Create an immutable tuple directly from generators
  - __Numpy Array Methods__: Apply functions to Numpy arrays
  - __Pandas DataFrame / Series Methods__: Apply functions to Pandas DataFrames / Series
- Miscellaneous Python Tricks:
  - __Generators__: Yield results as they come, rather than return an entire container of the results
  - __Lambdas__: Anonymous functions rather than defined named ones
  - __Maps__: Apply a function over an iterable rather than handle iterating manually

### Prime Number Tests
For some given number `N`, find every number below `N`<br>
Since this is a mathematical test, we can have some shortcuts.
For prime numbers, we already know the following:
* All prime numbers are odd numbers, except for 2.
* We only need to start with 2 as the first prime number, then loop from 3
  to `N`, incrementing by 2 for each iteration to test only odd numbers.
* Instead of checking every number up to `N` we can stop at `floor(N/2)`
* Instead of checking every number up to `floor(N/2)` we can stop at `floor(math.sqrt(N))`
* Instead of doing pure math, we can use bitshifting.

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
