from setuptools import setup
from Cython.Build import cythonize
import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

setup(
    name = "fib",
    ext_modules = cythonize('fib.pyx', compiler_directives={'embedsignature': True}),
)
