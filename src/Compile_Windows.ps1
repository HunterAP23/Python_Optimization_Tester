Remove-Item -Path "./build" -Include *.pyd -Recurse -Force
Remove-Item -Path "./files_compile_windows" -Include *.txt -Recurse -Force
Remove-Item -Path "./files_runs_windows" -Include *.txt -Recurse -Force

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
Get-ChildItem -Path "." -File -Recurse -Filter *.txt | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

New-Item -path "." -name "files_compile_windows" -type directory
New-Item -path "." -name "files_runs_windows" -type directory

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
