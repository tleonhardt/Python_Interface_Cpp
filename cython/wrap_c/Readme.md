# Wrapping existing C code using Cython
Example code for wrapping an existing C dynamic library in Python by using Cython.

## Building
Build the dynamic library and Cython wrapper using the following shell script:

    ./build_cython.sh

## Evaluating
Compare the results of a pure Python implementation to that of the Cython wrapper using:

    ./cython_wrapper_speedup.py

## Code Files
* Pure Python implementation
    * fib_python.py
* C implementation
    * fibonacci.h/.c
* Cython wrapper
    * Cython declaration
        * cfib.pxd
    * Cython wrapper
        * cyfib.pyx
    * Setuptools script
        * setup.py
