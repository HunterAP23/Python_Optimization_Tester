from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [Extension("Primes.Compiled.Inline.Lambda_LRU", ["src/Primes/Compiled/Inline/Lambda_LRU.pyx"])]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
