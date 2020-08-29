from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Compiled.Local.Generator", ["Primes/Compiled/Local/Generator.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
