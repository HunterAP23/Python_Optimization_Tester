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

echo Done.
pause