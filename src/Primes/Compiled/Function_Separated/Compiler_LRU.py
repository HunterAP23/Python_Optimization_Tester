from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Compiled.Function_Separated.LRU", ["Primes/Compiled/Function_Separated/LRU.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
