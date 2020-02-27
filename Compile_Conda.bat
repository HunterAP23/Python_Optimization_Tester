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

ptime.exe C:\ProgramData\Anaconda3\python.exe master1.py build_ext --inplace >> files_compile/compile_time1.txt

ptime.exe C:\ProgramData\Anaconda3\python.exe master1_LRU.py build_ext --inplace >> files_compile/compile_time1_LRU.txt

ptime.exe C:\ProgramData\Anaconda3\python.exe master2.py build_ext --inplace >> files_compile/compile_time2.txt

ptime.exe C:\ProgramData\Anaconda3\python.exe master2_LRU.py build_ext --inplace >> files_compile/compile_time2_LRU.txt

C:\ProgramData\Anaconda3\python.exe tester.py

pause
