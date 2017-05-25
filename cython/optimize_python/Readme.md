# Optimizing existing Python code using Cython
Example code for optimizing existing Python code by selectively compiling a portion of it to C using Cython.

## Building

### Mac OS X or Linux
Build the Cython extension using the following shell script:

    ./build_cython.sh
    
### Windows
Build the Cython extension using the following batch file:

    build_cython.bat

## Evaluating
Compare the results of a pure Python implementation to that of the Cython extension:

    ./cython_speedup.py

## Code Files
* Pure Python implementation
    * fib_python.py
* Cython implementation
    * Cython code
        * fib.pyx
    * Setuptools script
        * setup.py
