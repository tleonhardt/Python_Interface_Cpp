This code uses SWIG to wrap C functions which take pointers to arrays as both IN and INOUT arguments.
But it does so by having the user create intermediate C++ wrapper functions which take and
return std::vector arguments.


# Interfacing with C code from Python using SWIG
Example code for interfacing with C code from Python using SWIG.

## Building
Build the SWIG wrapper using the following shell script:

    ./build_swig_python_wrapper.sh

## Evaluating
Compare the results of a pure Python implementation to that of the SWIG wrapper using:

    ./test_swig.py

## Code Files
* C implementation
    * fastlz.h/.c
* SWIG
    * Interface File
        * fastlz.i
    * Distutils script
        * setup.py
