# Interfacing with C++ from Python using pybind11
Example code for interfacing with C++ code from Python using pybind11.

## Building
Build the pybind11 Python wrapper using the following shell script:

    ./build_pybind11.sh

## Evaluating
Compare the results of a pure Python implementation to that of the pybind11 wrapper using:

    ./test_pybind11.py

## Code Files
* Pure Python implementation
    * fib_python.py
* C++ implementation
    * fibonacci.h/.cpp
* pybind11 wrapper
    * test_pybind11.py
