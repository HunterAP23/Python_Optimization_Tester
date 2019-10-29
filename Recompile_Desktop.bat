@echo off

for %%c in (*.txt) do (
	del "%%c"
)

"D:\Downloads\CompTools\Media\ptime-10\ptime.exe" python.exe master1.py build_ext --inplace >> compile_time1.txt

"D:\Downloads\CompTools\Media\ptime-10\ptime.exe" python.exe master2.py build_ext --inplace >> compile_time2.txt

python.exe tester.py