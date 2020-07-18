from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Compiled.Local.Lambda_LRU", ["Primes/Compiled/Local/Lambda_LRU.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
