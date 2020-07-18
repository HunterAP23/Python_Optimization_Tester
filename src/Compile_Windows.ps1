# Write-Output "Cleaning up *.c objects"
# Get-ChildItem -Path "." -File -Recurse -Filter *.c | Foreach-Object {
#     Write-Output $_.Name
#     rm $_.FullName
# }
#
# Write-Output "Cleaning up *.pyd objects"
# Get-ChildItem -Path "." -File -Recurse -Filter *.pyd | Foreach-Object {
#     Write-Output $_.Name
#     rm $_.FullName
# }

# Clean up
# Write-Output "Cleaning up *.txt objects in Compiled folder"
# Get-ChildItem -Path "Primes/Compiled" -File -Recurse -Filter *.txt | Foreach-Object {
#     Write-Output $_.Name
#     # rm $content
# }

# Write-Output "Cleaning up *.txt objects in Compiled folder"
# Get-ChildItem -Path "Primes/Optimized" -File -Recurse -Filter *.txt | Foreach-Object {
#     Write-Output $_.Name
#     # rm $content
# }

# Compile
Write-Output "Compiling Cython objects"
Get-ChildItem -Path "Primes/Compiled" -File -Recurse -Filter *.pyx | Foreach-Object {
    Write-Output $_.FullName
    # python3 -v $_.FullName build_ext --inplace
    # python3 "Primes/Compiled/Function/Compiler.py" build_ext --inplace
    cythonize -3 -i $_.FullName
}

# cythonize -3 -i "Primes/Compiled/**/*.pyx"

# python3 master2.py build_ext --inplace

# python3 Tester_Start.py
