from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Optimized.Function.Standard", ["Primes/Optimized/Function/Standard.pyx"])]

setup(
    ext_modules=cythonize(extensions, language_level=3),
)
