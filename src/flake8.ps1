flake8.exe --ignore E501 . | Where-Object { $_ -NotMatch "EK_Subprocess.py"} | Where-Object{ $_ -NotMatch "compare[0-9]*.py"} 

pause
