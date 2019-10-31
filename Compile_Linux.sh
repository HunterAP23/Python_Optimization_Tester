#!/bin/bash

rm *.c
rm *.so
rm *.pyc
rm *.txt

time python3 master1.py build_ext --inplace >> compile_time1.txt

time python3 master2.py build_ext --inplace >> compile_time2.txt

python3 tester.py
