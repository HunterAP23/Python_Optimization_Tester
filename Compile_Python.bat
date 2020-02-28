@echo off

echo Cleaning...

del /Q __pycache__ 2>NUL
rmdir __pycache__ 2>NUL

del /Q files_compile 2>NUL
rmdir files_compile 2>NUL

del /Q files_runs 2>NUL
rmdir files_runs 2>NUL

for %%a in (*.c) do (
	del "%%a"
)

for %%a in (*.txt) do (
	del "%%a"
)

for %%a in (*.pyc) do (
	del "%%a"
)

for %%a in (*.pyd) do (
	del "%%a"
)

for %%a in (*.so) do (
	del "%%a"
)

for %%a in (*.py) do (
	echo Compiling CPython bytecode for %%a
	python -m py_compile "%%a"
)

mkdir files_compile

rem echo Cythonizing Cython
rem ptime.exe python.exe Compiler_Cython.py build_ext --inplace >> files_compile/compile_time_cython.txt

rem echo Cythonizing Cython Lambda
rem ptime.exe python.exe Compiler_Cython_Lambda.py build_ext --inplace >> files_compile/compile_time_cython_lambda.txt

rem echo Cythonizing Cython LRU
rem ptime.exe python.exe Compiler_Cython_LRU.py build_ext --inplace >> files_compile/compile_time_cython_LRU.txt

rem echo Cythonizing Optimized
rem ptime.exe python.exe Compiler_Optimized.py build_ext --inplace >> files_compile/compile_time_optimized.txt

rem echo Cythonizing Optimized Lambda
rem ptime.exe python.exe Compiler_Optimized_Lambda.py build_ext --inplace >> files_compile/compile_time_optimized_lambda.txt

rem echo Cythonizing Optimized LRU
rem ptime.exe python.exe Compiler_Optimized_LRU.py build_ext --inplace >> files_compile/compile_time_optimized_LRU.txt

python.exe Threader.py

pause
