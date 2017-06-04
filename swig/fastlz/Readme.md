# Wrapping C++ code using STL containers with SWIG
This code uses SWIG to wrap C++ functions which use STL container classes.  It demonstrates how to wrap
C++ code which uses STL container class and instantiate STL container wrappers in Python.  In the process 
it also demonstrates how to link SWIG wrapper code to dynamic libraries.

## Building
First build the fastlz C compression code into a dynamic library:

    ./build_fastlz_lib.sh
    
Then build the SWIG wrapper using the following shell script:

    ./build_swig_python_wrapper.sh

## Evaluating
Test a full round-trip compression and decompression using the wrapper with py.test

    py.test -v

## Code Files
* C compression code which gets built into a dynamic library
    * fastlz.h/.c
* C++ compression wrapper which wraps the C library and gets wrapped by SWIG
    * Compress.h/.cpp
* SWIG
    * Interface File
        * Compress.i
    * Distutils script
        * setup.py

## Exercise
Fill in the **TODO:** blocks present in **test_swig.py**
