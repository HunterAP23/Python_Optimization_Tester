from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [Extension("Primes.Compiled.Function.LRU", ["src/Primes/Interpreted/Function/LRU.py"])]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
