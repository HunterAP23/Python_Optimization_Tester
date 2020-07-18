from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("Primes/Compiled/Function_Separated/*.pyx", language_level=3),
)
