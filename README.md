# Cython_test_multiprocess
  Runtime comparison of different implementations of calculating Prime numbers.

  1. Python implementation
  2. Cython implementation
  3. Cython with manual static typing optimizations
  1. Python implementation with LRU Cache
  2. Cython implementation with LRU Cache
  3. Cython with manual static typing optimizations and LRU Cache

  Each one of these programs runs three different versions of calculating primes:
  For number N being tested as prime,
  and primes being a list of primes less than N,
  and for i being any number less than the length of the primes list:
  1. N % primes[i] == 0: if true, then N is not prime, otherwise N is appended
  the list of primes.
  2. (N / 2) % primes[i] == 0: if true, then N is not prime, otherwise N is
  appended the list of primes. This method should theoretically be 2x as fast
  as method #1.
  3. sqrt(N) % primes[i] == 0: if true, then N is not prime, otherwise N is
  appended the list of primes. This method should theoretically be log(N) as fast
  as method #1.

## Find_Nth_Prime.py
  Python implementation of the program.

## Find_Nth_Prime1.py
  Cython implementation of the program.

## Find_Nth_Prime1.py
  Cython implementation of the program, with manual optimizations
  like static typing of variables.

## Find_Nth_Prime_LRU.py
Python implementation of the program with LRU Cache for each calculating function.

## Find_Nth_Prime1_LRU.py
Cython implementation of the program with LRU Cache for each calculating function.

## Find_Nth_Prime1_LRU.py
Cython implementation of the program, with manual optimizations
like static typing of variables, and with LRU Cache for each calculating function.

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
