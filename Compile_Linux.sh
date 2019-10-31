#!/bin/bash

files_c=`ls -1 *.c`
files_so=`ls -1 *.so`
files_pyc=`ls -1 *.pyc`
file_txt=`ls -1 *.txt`

for c in $files_c; do
	rm $c
done

for so in $files_so; do
	rm $so
done

for pyc in $files_pyc; do
	rm $pyc
done

for txt in $files_txt; do
	rm $txt
done

printf "Building Variant: Compiled..."
time python3 master_compiled.py build_ext --inplace >> compile-time_compiled.txt
printf "Done\n"

printf "Building Variant: Compiled-External..."
time python3 master_compiled_ext.py build_ext --inplace >> compile-time_compiled-ext.txt
printf "Done\n"

printf "Building Variant: Optimized..."
time python3 master_optimized.py build_ext --inplace >> compile-time_optimized.txt
printf "Done\n"

printf "Building Variant: Optimized-External..."
time python3 master_optimized_ext.py build_ext --inplace >> compile-time_optimized-ext.txt
printf "Done\n"

read -p "Run tester.py script? (0=No, 1=Yes): " tester
if [[ $tester == 1 ]]; then
	echo "Running tester.py"
	python3 tester.py
else
	echo "Exiting."
fi
