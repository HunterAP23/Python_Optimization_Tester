@echo off

for %%a in (*.c) do (
	del "%%a"
)

for %%b in (*.pyd) do (
	del "%%b"
)

for %%c in (*.txt) do (
	del "%%c"
)

"C:\Users\etgar\Downloads\CompTools\Media\ptime-10\ptime.exe" python.exe master1.py build_ext --inplace -cplus -3 >> compile_time1.txt

"C:\Users\etgar\Downloads\CompTools\Media\ptime-10\ptime.exe" python.exe master2.py build_ext --inplace -cplus -3 >> compile_time2.txt

python.exe tester.py