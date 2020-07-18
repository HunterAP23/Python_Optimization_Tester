from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Compiled.Local.List", ["Primes/Compiled/Local/List.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
