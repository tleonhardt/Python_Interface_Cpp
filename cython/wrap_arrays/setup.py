# coding=utf-8
from setuptools import setup
from Cython.Build import cythonize
import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

setup(
    name="cyfastlz",
    ext_modules=cythonize('cyfastlz.pyx', compiler_directives={'embedsignature': True}),
)
