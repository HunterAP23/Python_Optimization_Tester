from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension("Primes.Optimized.Function.Tuple_LRU_Internal", ["src/Primes/Optimized/Function/Tuple_LRU_Internal.pyx"])
]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
