@echo off

echo Cleaning...

del /Q __pycache__ 2>NUL
rmdir __pycache__ 2>NUL

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
	python -m py_compile "%%a"
)

echo Compiling...

ptime.exe python.exe master1.py build_ext --inplace >> compile_time1.txt

ptime.exe python.exe master2.py build_ext --inplace >> compile_time2.txt

python.exe tester.py

pause