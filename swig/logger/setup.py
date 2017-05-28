# coding=utf-8
from distutils.core import setup, Extension

name = "example"  # name of the module
version = "1.0"   # the module's version number

setup(name=name, version=version,
      # distutils detects .i files and compiles them automatically
      ext_modules=[Extension(name='_{}'.format(name),  # SWIG requires _ as a prefix for the module name
                             sources=["example.i", "example.cpp"],
                             include_dirs=[],
                             extra_compile_args=["-std=c++11"],
                             swig_opts=['-c++'])
                   ])
