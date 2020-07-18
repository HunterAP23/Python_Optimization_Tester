from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Compiled.Function_Separated.Main", ["Primes/Compiled/Function_Separated/Main.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
