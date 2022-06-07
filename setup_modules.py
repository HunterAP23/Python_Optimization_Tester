from pathlib import Path

from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = []

for directory in Path(".venv/Lib/site-packages").iterdir():
    if directory.is_dir() and (
        "cython" not in str(directory.name).lower() and "pyinstaller" not in str(directory.name).lower()
    ):
        items = list(directory.glob("*[!__init__].py"))
        for i in list(directory.glob("*[!__init__].pxd")):
            items.append(i)
        if len(items) > 0:
            for i in range(len(items)):
                items[i] = str(items[i])
            extensions.append(
                Extension(
                    str(directory.name),
                    items,
                )
            )

setup(
    ext_modules=cythonize(
        extensions,
        language_level=3,
        exclude_failures=True,
    ),
)
total = "Total files: {}".format(len(extensions))
print(total)
