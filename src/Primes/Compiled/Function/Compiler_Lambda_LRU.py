from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [Extension("Primes.Compiled.Function.Lambda_LRU", ["src/Interpreted/Compiled/Function/Lambda_LRU.py"])]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
