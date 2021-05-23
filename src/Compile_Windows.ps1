Write-Output "Cleaning up *.c objects"
Get-ChildItem -Path "." -File -Recurse -Filter *.c | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

Write-Output "Cleaning up *.pyc objects"
Get-ChildItem -Path "." -File -Recurse -Filter *.pyc | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

Write-Output "Cleaning up *.pyd objects"
Remove-Item -Path "./build" -Include *.pyd -Recurse -Force
Get-ChildItem -Path "." -File -Recurse -Filter *.pyd | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

Write-Output "Cleaning up *.so objects"
Get-ChildItem -Path "." -File -Recurse -Filter *.so | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

Write-Output "Cleaning up *.txt files"
Remove-Item -Path "./files_runs" -Include *.txt -Recurse -Force
Get-ChildItem -Path "." -File -Recurse -Filter *.txt | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

# Compile
Write-Output "Compiling Cython objects"
Get-ChildItem -Path "Primes/Compiled" -File -Recurse -Filter Compiler_*.py | Foreach-Object {
     Write-Output $_.FullName
     python $_.FullName build_ext --inplace
}

Write-Output "Compiling Optimized objects"
Get-ChildItem -Path "Primes/Optimized" -File -Recurse -Filter Compiler_*.py | Foreach-Object {
     Write-Output $_.FullName
     python $_.FullName build_ext --inplace
}

# python37 "Compiler_Tester.py" build_ext --inplace
