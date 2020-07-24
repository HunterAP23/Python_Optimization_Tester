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

Write-Output "Cleaning up *.pyc objects"
Get-ChildItem -Path "." -File -Recurse -Filter *.pyc | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

Write-Output "Cleaning up *.so objects"
Get-ChildItem -Path "." -File -Recurse -Filter *.so | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}
