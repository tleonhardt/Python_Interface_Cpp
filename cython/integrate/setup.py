# coding=utf-8
from setuptools import setup
from Cython.Build import cythonize
import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

setup(
    name="cyintegrate",
    ext_modules=cythonize('cyintegrate.pyx', compiler_directives={'embedsignature': True}),
)
