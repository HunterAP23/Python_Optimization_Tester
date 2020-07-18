Write-Output "Cleaning up *.c objects"
Get-ChildItem -Path "." -File -Recurse -Filter *.c | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

Write-Output "Cleaning up *.pyd objects"
Get-ChildItem -Path "." -File -Recurse -Filter *.pyd | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

Write-Output "Cleaning up *.txt objects in Compiled folder"

Remove-Item -Path "./files_runs" -Include *.txt -Recurse -Force
