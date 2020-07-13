Remove-Item –path ./flake8_report.txt
flake8.exe --ignore E501,E731 --output-file ./flake8_report.txt

pause
