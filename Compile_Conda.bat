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

CALL C:\ProgramData\Anaconda3\condabin\activate.bat tester

for %%a in (*.py) do (
	echo Compiling Anaconda bytecode for %%a
	python -m py_compile "%%a"
)

mkdir files_compile

echo Cythonizing Anaconda Cython
ptime.exe python.exe Compiler_Cython.py build_ext --inplace >> files_compile/compile_time_conda_cython.txt

echo Cythonizing Anaconda Cython Lambda
ptime.exe python.exe Compiler_Cython_Lambda.py build_ext --inplace >> files_compile/compile_time_conda_cython_lambda.txt

echo Cythonizing Anaconda Cython LRU
ptime.exe python.exe Compiler_Cython_LRU.py build_ext --inplace >> files_compile/compile_time_conda_cython_LRU.txt

echo Cythonizing Anaconda Optimized
ptime.exe python.exe Compiler_Optimized.py build_ext --inplace >> files_compile/compile_time_conda_optimized.txt

echo Cythonizing Anaconda Optimized Lambda
ptime.exe python.exe Compiler_Optimized_Lambda.py build_ext --inplace >> files_compile/compile_time_conda_optimized_lambda.txt

echo Cythonizing Anaconda Optimized LRU
ptime.exe python.exe Compiler_Optimized_LRU.py build_ext --inplace >> files_compile/compile_time_conda_optimized_LRU.txt

C:\ProgramData\Anaconda3\python.exe Threader.py

pause
