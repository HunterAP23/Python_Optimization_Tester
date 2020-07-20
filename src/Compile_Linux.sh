#!/bin/bash

# for pyx in $(find "Primes/Compiled" | grep '.pyx'); do
#         echo $pyx
#         cythonize -3 -i $pyx
# done

for pyx in $(find "Primes/Compiled" | grep "Compiler_*.py"); do
     python3 $pyx build_ext --inplace
done

for pyx in $(find "Primes/Optimized" | grep "Compiler_*.py"); do
     python3 $pyx build_ext --inplace
done

python3 "Compiler_Tester.py" build_ext --inplace
