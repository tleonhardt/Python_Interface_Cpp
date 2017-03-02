# coding=utf-8
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="cyfastlz",
    ext_modules=cythonize('cyfastlz.pyx', compiler_directives={'embedsignature': True}),
)
