from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Optimized.Function.List", ["Primes/Optimized/Function/List.pyx"])]

setup(
    ext_modules=cythonize(extensions, language_level=3),
)
