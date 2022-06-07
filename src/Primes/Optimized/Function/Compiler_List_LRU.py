from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [Extension("Primes.Optimized.Function.List_LRU", ["src/Primes/Optimized/Function/List_LRU.pyx"])]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
