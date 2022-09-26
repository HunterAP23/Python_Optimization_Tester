from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension(
        "Primes.Compiled.Function.Lambda_LRU_External",
        ["src/Primes/Interpreted/Function/Lambda_LRU_External.py"],
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        language_level=3,
    ),
    options={"build": {"build_lib": "src/"}},
)
