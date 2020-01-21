from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("Find_Nth_Prime1_LRU.pyx",language_level=3),
)
