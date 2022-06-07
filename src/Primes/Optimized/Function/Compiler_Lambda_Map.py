from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [Extension("Primes.Optimized.Function.Lambda_Map", ["src/Primes/Optimized/Function/Lambda_Map.pyx"])]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
