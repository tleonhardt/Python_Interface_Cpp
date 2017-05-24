#!/usr/bin/env python
# coding=utf-8
""" Python wrapper to time the CFFI wrapper for computing the nth fibonacci number
in a non-recursive fashion and compare it to the pure Python implementation.
"""
import os

import cffi

import fib_python


if __name__ == '__main__':
    import sys
    import timeit

    n = 20
    try:
        n = int(sys.argv[1])
    except Exception:
        pass

    number_of_times = 100000
    try:
        number_of_times = int(sys.argv[2])
    except Exception:
        pass

    # The main top-level CFFI class that you instantiate once
    ffi = cffi.FFI()

    # Parses the given C source.  This registers all declared functions.
    ffi.cdef('int compute_fibonacci(int n);')

    # Load and return a dynamic library.  The standard C library can be loaded by passing None.
    libfib = ffi.dlopen(os.path.join('.', 'libfibonacci.so'))

    fib_py = fib_python.compute_fibonacci(n)
    fib_cffi = libfib.compute_fibonacci(n)
    if fib_py != fib_cffi:
        raise (ValueError(fib_cffi))

    py_tot = timeit.timeit("compute_fibonacci({})".format(n),
                           setup="from fib_python import compute_fibonacci",
                           number=number_of_times)
    cffi_tot = timeit.timeit("libfib.compute_fibonacci({})".format(n),
                             setup="""import cffi; ffi = cffi.FFI(); ffi.cdef('int compute_fibonacci(int n);'); libfib = ffi.dlopen('./libfibonacci.so')""",
                             number=number_of_times)
    py_avg = py_tot / number_of_times
    cffi_avg = cffi_tot / number_of_times

    print("fib({}) = {}".format(n, fib_py))
    print("Python average time:  {0:.2g}".format(py_avg))
    print("CFFI/C average time:  {0:.2g}".format(cffi_avg))
    print("CFFI/C speedup: {0:.2g} times".format(py_avg / cffi_avg))
