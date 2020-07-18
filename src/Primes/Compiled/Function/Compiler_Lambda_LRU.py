from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Compiled.Function.Lambda_LRU", ["Primes/Compiled/Function/Lambda_LRU.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
