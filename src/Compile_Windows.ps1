Write-Output "Clearing 'build' directory"
Remove-Item -Path "./build" -Include *.pyd -Recurse -Force
Write-Output "Deleting TXT files in the 'files_compile_windows' directory"
Remove-Item -Path "./files_compile_windows" -Include *.txt -Recurse -Force
Write-Output "Deleting TXT files in the 'files_runs_windows' directory"
Remove-Item -Path "./files_runs_windows" -Include *.txt -Recurse -Force

# Write-Output "Cleaning up *.c objects"
# Get-ChildItem -Path "." -File -Recurse -Filter *.c | Foreach-Object {
#     Write-Output $_.Name
#     rm $_.FullName
# }

# Write-Output "Cleaning up *.pyc objects"
# Get-ChildItem -Path "." -File -Recurse -Filter *.pyc | Foreach-Object {
#     Write-Output $_.Name
#     rm $_.FullName
# }

# Write-Output "Cleaning up *.pyd objects"
# Get-ChildItem -Path "." -File -Recurse -Filter *.pyd | Foreach-Object {
#     Write-Output $_.Name
#     rm $_.FullName
# }

# Write-Output "Cleaning up *.so objects"
# Get-ChildItem -Path "." -File -Recurse -Filter *.so | Foreach-Object {
#     Write-Output $_.Name
#     rm $_.FullName
# }

Write-Output "Cleaning up TXT files"
Get-ChildItem -Path "." -File -Recurse -Filter *.txt | Foreach-Object {
    Write-Output $_.Name
    rm $_.FullName
}

if ( -Not (Test-Path "build"))
{
     New-Item -path "." -name "build" -type directory -force
}

if ( -Not (Test-Path "files_compile_windows"))
{
     New-Item -path "." -name "files_compile_windows" -type directory -force
}

if ( -Not (Test-Path "files_runs_windows"))
{
     New-Item -path "." -name "files_runs_windows" -type directory -force
}

if ( -Not (Test-Path "package"))
{
     New-Item -path "." -name "package" -type directory -force
}

if ( -Not (Test-Path "package/Primes"))
{
     New-Item -path "." -name "package/Primes" -type directory -force
}

if ( -Not (Test-Path "package/Primes/Compiled"))
{
     New-Item -path "." -name "package/Primes/Compiled" -type directory -force
}

if ( -Not (Test-Path "package/Primes/Optimized"))
{
     New-Item -path "." -name "package/Primes/Optimized" -type directory -force
}

############# "Compiled" variations #############
# Check if the "Compiled" Function Primes scripts have relevant compilation scripts
Get-ChildItem -Path "src/Primes/Interpreted/Function" -File -Recurse -Filter *.py -exclude Compiler_* | Foreach-Object {
     $comp_name="src/Primes/Compiled/Function/Compiler_$($_.Basename).py"
     if ( -Not (Test-Path $comp_name)) {
          Write-Output "$comp_name does not exist"
          exit
     }
}

# Check if the "Compiled" Function Primes compilation scripts have relevant python scripts
Get-ChildItem -Path "src/Primes/Compiled/Function" -File -Recurse -Filter Compiler_*.py | Foreach-Object {
     $comp_name=$_.Basename.Replace("Compiler_", "")
     $comp_name="src/Primes/Interpreted/Function/" + $comp_name + ".py"
     if ( -Not (Test-Path $comp_name)) {
          Write-Output "$comp_name does not exist"
          exit
     }
}

# Check if the "Compiled" Inline Primes scripts have relevant compilation scripts
Get-ChildItem -Path "src/Primes/Interpreted/Inline" -File -Recurse -Filter *.py | Foreach-Object {
     $comp_name="src/Primes/Compiled/Inline/Compiler_$($_.Basename).py"
     if ( -Not (Test-Path $comp_name)) {
          Write-Output "$comp_name does not exist"
          exit
     }
}

# Check if the "Compiled" Inline Primes compilation scripts have relevant python scripts
Get-ChildItem -Path "src/Primes/Compiled/Inline" -File -Recurse -Filter Compiler_*.py | Foreach-Object {
     $comp_name=$_.Basename.Replace("Compiler_", "")
     $comp_name="src/Primes/Interpreted/Inline/" + $comp_name + ".py"
     if ( -Not (Test-Path $comp_name)) {
          Write-Output "$comp_name does not exist"
          exit
     }
}

############# "Optimized" variations #############
# Check if the "Optimized" Function Primes scripts have relevant compilation scripts
Get-ChildItem -Path "src/Primes/Optimized/Function" -File -Recurse -Filter *.pyx | Foreach-Object {
     $comp_name="src/Primes/Optimized/Function/Compiler_$($_.Basename).py"
     if ( -Not (Test-Path $comp_name)) {
          Write-Output "$comp_name does not exist"
          exit
     }
}

# Check if the "Optimized" Function Primes compilation scripts have relevant cython PYX scripts
Get-ChildItem -Path "src/Primes/Optimized/Function" -File -Recurse -Filter Compiler_*.py | Foreach-Object {
     $comp_name=$_.Basename.Replace("Compiler_", "")
     $comp_name="src/Primes/Optimized/Function/" + $comp_name + ".pyx"
     if ( -Not (Test-Path $comp_name)) {
          Write-Output "$comp_name does not exist"
          exit
     }
}

# Check if the "Optimized" Inline Primes scripts have relevant compilation scripts
Get-ChildItem -Path "src/Primes/Optimized/Inline" -File -Recurse -Filter *.pyx | Foreach-Object {
     $comp_name="src/Primes/Optimized/Inline/Compiler_$($_.Basename).py"
     if ( -Not (Test-Path $comp_name)) {
          Write-Output "$comp_name does not exist"
          exit
     }
}

# Check if the "Optimized" Inline Primes compilation scripts have relevant cython PYX scripts
Get-ChildItem -Path "src/Primes/Optimized/Inline" -File -Recurse -Filter Compiler_*.py | Foreach-Object {
     $comp_name=$_.Basename.Replace("Compiler_", "")
     $comp_name="src/Primes/Optimized/Inline/" + $comp_name + ".pyx"
     if ( -Not (Test-Path $comp_name)) {
          Write-Output "$comp_name does not exist"
          exit
     }
}
############# Actual compilation steps #############
# Compile interpreted code
Write-Output "Compiling Cython objects"
Get-ChildItem -Path "src/Primes/Compiled" -File -Recurse -Filter Compiler_*.py | Foreach-Object {
     Write-Output $_.FullName
     python $_.FullName build_ext
     if ($LastExitCode -ne 0) { break }
}

# Compile optimized code
Write-Output "Compiling Optimized objects"
Get-ChildItem -Path "src/Primes/Optimized" -File -Recurse -Filter Compiler_*.py | Foreach-Object {
     Write-Output $_.FullName
     python $_.FullName build_ext
     if ($LastExitCode -ne 0) { break }
}
