from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("Find_Nth_Prime_Compiled_Ext.pyx",language_level=3),
)
