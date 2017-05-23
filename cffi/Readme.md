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
    
    
## Troubleshooting
The ABI of the C API is generally not stable and may change between versions of Python. This can 
cause code which used to work to break when you upgrade either your version of Python or CFFI.
 
If you get a Python traceback from an exception that contains something like "ImportError: dlopen", 
then you may have a mismatch between your version of Python and your version of CFFI.  Try upgrading
one or both.  The **conda** package manager which ships with the Anaconda Python distro is convenient
for this.
