from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Optimized.Function_Separated.Lambda_LRU_Map", ["Primes/Optimized/Function_Separated/Lambda_LRU_Map.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
