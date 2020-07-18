from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Optimized.Local.List", ["Primes/Optimized/Local/List.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
