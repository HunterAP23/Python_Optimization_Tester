from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Optimized.Local.Standard", ["Primes/Optimized/Local/Standard.pyx"])]

setup(
    ext_modules=cythonize(extensions, language_level=3),
)
