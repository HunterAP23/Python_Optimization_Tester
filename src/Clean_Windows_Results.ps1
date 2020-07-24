Write-Output "Cleaning up *.txt objects in Compiled folder"

Remove-Item -Path "./files_runs" -Include *.txt -Recurse -Force
