@echo off

for %%c in (*.txt) do (
	del "%%c"
)

for %%c in (*.pyd, *.c) do (
	del "%%c"
)

"C:\Users\etgar\Downloads\CompTools\Media\ptime-10\ptime.exe" python master1.py build_ext --inplace >> compile_time1.txt

"C:\Users\etgar\Downloads\CompTools\Media\ptime-10\ptime.exe" python master2.py build_ext --inplace >> compile_time2.txt

python "tester.py"

pause
