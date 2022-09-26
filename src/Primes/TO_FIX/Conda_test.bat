@echo off

echo Normal Python
ptime python.exe
echo.

echo After activating "tester" env
CALL C:\ProgramData\Anaconda3\condabin\activate.bat tester
ptime python
echo.
pause

echo After deactivating "tester" env
conda deactivate
python
echo.

echo Explicit python path call
CALL C:\ProgramData\Anaconda3\condabin\conda.bat

pause
