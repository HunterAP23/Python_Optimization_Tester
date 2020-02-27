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

echo Compiling...

for %%a in (*.py) do (
	echo Compiling %%a
	python -m py_compile "%%a"
)

mkdir files_compile

echo Compiling
ptime.exe python.exe Compiler_Cython.py build_ext --inplace >> files_compile/compile_time_cython.txt

ptime.exe python.exe Compiler_Cython_LRU.py build_ext --inplace >> files_compile/compile_time_cython_LRU.txt

ptime.exe python.exe Compiler_Optimized.py build_ext --inplace >> files_compile/compile_time_optimized.txt

ptime.exe python.exe Compiler_Optimized_LRU.py build_ext --inplace >> files_compile/compile_time_optimized_LRU.txt

python.exe tester.py

pause
