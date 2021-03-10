from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Optimized.Local.Generator", ["Primes/Optimized/Local/Generator.pyx"])]

setup(
    ext_modules=cythonize(extensions, language_level=3),
)
