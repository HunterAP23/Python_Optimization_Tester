from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("Primes/Compiled/Function/*.pyx", language_level=3),
)
