from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension("Primes.Compiled.Function.Tuple_LRU_Internal", ["src/Primes/Interpreted/Function/Tuple_LRU_Internal.py"])
]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
