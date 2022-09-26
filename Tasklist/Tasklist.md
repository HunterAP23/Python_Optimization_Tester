# Tasklist
List out different variables that factor into the combination calculation for these tests.

## Runtimes
What underlying runtimes are used to run (and possibly compile) the tests.

### CPython
- Standard runtime, considered as baseline for performance.
- Most widespread use among all Python runtimes.

### Pypy
- Higher performance runtime through thr use of a just-in-time (JIT) compiler.
- Is missing normal CPython extension support, limiting compatibility.
- Not as widespread in use as CPython or Anaconda.

### Anaconda
- High performance, data-science-driven runtime.
- Very widespread use.
- Requires separate package management through the `conda` application.

## Compilers
Tools used to compile Python source code into bytecode, or some other language for performance gains (such as C, C++, Rust, etc.)

### Cython
- A superset of Python (contains all the features of Python and adds more on top of them).
- Compiles source code into redistributable dynamically linked libraries.
- Can compile code into C or C++.
- Can use manual optimizations like static typing.

### Nuitka
- Compiles Python code to C.
- Relies on CPython, so it does not work with non-CPython runtimes.

## Packagers
Tools used to package Python projects into executables. These have no affect on performance.

### Pyinstaller
- Combines source code, dynamically-linked libraries, and Python runtime into a single executable.
- Not compatible with PyPy since Pypy lacks CPython functionality.

### Nuitka
- Also handles packaging of source code into executables.

## Inline VS Function
Whether the program's main actions occur within the main function, or if they are relegated to external functions.

### Inline
- Supposed decrease in overhead from having to call external functions.
- Adds complexity to main function, which can als decrease readability.

### Functions
- Supposed increase in overhead due to repeated calls to other locations in memory.
- Removes complexity from main function, and can improve code readability.

## Comprehension
What methods are used for handling the comprehension of data inside a data container.

### List
- Stores data in a mutable manner, allowing for easy push  pop / append / remove actions.
- Use slightly more memory than tuples

### Tuple
- Immutable storage containers, requiring complete recreation to add or remove elements
- Use slightly less memory than lists

### Generator
- Used similarly to list comprehension, but should be more memory efficient
- Generators can continue where they left off after the previous `yield` call, leading to possibly faster results if conditions are correct

