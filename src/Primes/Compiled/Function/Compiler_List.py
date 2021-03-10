from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Compiled.Function.Generator", ["Primes/Compiled/Function/Generator.pyx"])]

setup(
    ext_modules=cythonize(extensions, language_level=3),
)
