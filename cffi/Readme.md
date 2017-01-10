# Interfacing with a dynamic library from Python using CFFI
Example code for interfacing with a C dynamic library from Python using CFFI.

## Building
Build the C dynamic library using the following shell script:

    ./build_c_dynamic_lib.sh

## Evaluating
Compare the results of a pure Python implementation to that of the CFFI wrapper using:

    ./test_cffi.py

## Code Files
* Pure Python implementation
    * fib_python.py
* C implementation
    * fibonacci.h/.c
* CFFI "wrapper" (there is no wrapper code, its all inline Python)
    * test_cffi.py
