from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Optimized.Function.Main", ["Primes/Optimized/Function/Main.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
