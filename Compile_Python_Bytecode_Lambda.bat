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

ptime python.exe -B lambda_test.py

for %%a in (*.py) do (
	echo Compiling CPython bytecode for %%a
	python -m py_compile "%%a"
)

ptime python.exe lambda_test.py

pause
