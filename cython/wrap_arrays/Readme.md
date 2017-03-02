This code uses Cython to wrap C functions which take pointers to arrays as both IN and INOUT arguments.

# Wrapping existing C code using Cython
Example code for wrapping an existing C dynamic library in Python by using Cython.

## Building
Build the dynamic library and Cython wrapper using the following shell script:

    ./build_cython.sh

## Evaluating
Run pytest unit tests to verify everything is working as intended for the Cython wrapper:
    ./py.test -v

## Code Files
* C implementation
    * fastlz.h/.c
* Cython wrapper
    * Cython declaration
        * cfastlz.pxd
    * Cython wrapper
        * cyfastlz.pyx
    * Setuptools script
        * setup.py
    * pytest unit tests
        * test_cython_wrapper.py
