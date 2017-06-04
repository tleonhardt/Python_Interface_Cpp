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
        
        
## Exercise
You need to fill in the **TODO:** blocks in **cfastlz.pxd** and **cyfastlz.pyx**

Some useful things to keep in mind:

1. Read the documentation in fastlz.h to understand how the compress() and decompress() functions work.
2. You can cast from a Python type to a C type using syntax like the following:

```python
<const uint8_t*>in_buf
```
3. In Python, you can use *slicing* to return a subarray, substring, etc using syntax similar to:

```python
my_array = range(10)
my_array[2:7]
[2, 3, 4, 5, 6]
```

The slice includes the starting index, but excludes the ending index.

You know you are done when the unit test passes.


### Solution
The solution is on the **solutions** branch.  Don't peak until you have given this an honest effort.
