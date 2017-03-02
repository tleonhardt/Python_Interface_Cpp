This code doesn't work yet.
This code uses SWIG to wrap C functions which take pointers to arrays as both IN and INOUT arguments.
The idea is to use the numpy.i typemaps and numpy to make it relatively easy.


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
