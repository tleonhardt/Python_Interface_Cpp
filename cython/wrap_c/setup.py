from setuptools import setup
from Cython.Build import cythonize

setup(
    name = "cyfib",
    ext_modules = cythonize('cyfib.pyx', compiler_directives={'embedsignature': True}),
)
