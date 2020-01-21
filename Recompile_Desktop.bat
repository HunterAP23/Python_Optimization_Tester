@echo off

for /R %%c in (files_compile\*.txt files_runs\*.txt) do (
	del "%%c"
)

mkdir "files_compile" 2>nul

rem C:\Python37\python.exe
"D:\Downloads\CompTools\Media\ptime-10\ptime.exe" python.exe master1.py build_ext --inplace >> files_compile\compile_time1.txt

"D:\Downloads\CompTools\Media\ptime-10\ptime.exe" python.exe master1_LRU.py build_ext --inplace >> files_compile\compile_time1_LRU.txt

"D:\Downloads\CompTools\Media\ptime-10\ptime.exe" python.exe master2.py build_ext --inplace >> files_compile\compile_time2.txt

"D:\Downloads\CompTools\Media\ptime-10\ptime.exe" python.exe master2_LRU.py build_ext --inplace >> files_compile\compile_time2_LRU.txt

python.exe "tester.py"
