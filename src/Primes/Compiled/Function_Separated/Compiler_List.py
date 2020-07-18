from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Compiled.Function_Separated.List", ["Primes/Compiled/Function_Separated/List.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
