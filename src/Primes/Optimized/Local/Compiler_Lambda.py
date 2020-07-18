from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("Primes.Optimized.Local.Lambda", ["Primes/Optimized/Local/Lambda.pyx"])]

setup(
    ext_modules = cythonize(extensions, language_level=3),
)
