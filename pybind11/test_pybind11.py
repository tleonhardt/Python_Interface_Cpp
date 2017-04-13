#!/usr/bin/env python
# coding=utf-8
""" Python wrapper to time the pybind11 wrapper for computing the nth fibonacci number
in a non-recursive fashion and compare it to the pure Python implementation.
"""
# import fibonacci
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

    fib_py = fib_python.compute_fibonacci(n)
    fib_pybind11 = fibonacci.compute_fibonacci(n)
    if fib_py != fib_pybind11:
        raise (ValueError(fib_pybind11))

    py_tot = timeit.timeit("compute_fibonacci({})".format(n),
                           setup="from fib_python import compute_fibonacci",
                           number=number_of_times)
    pybind11_tot = timeit.timeit("fibonacci.compute_fibonacci(n))".format(n),
                             setup="""import fibonacci""",
                             number=number_of_times)
    py_avg = py_tot / number_of_times
    pybind11_avg = pybind11_tot / number_of_times

    print("fib({}) = {}".format(n, fib_py))
    print("Python average time:  {0:.2g}".format(py_avg))
    print("pybind11 average time:  {0:.2g}".format(pybind11_avg))
    print("pybind11 speedup: {0:.2g} times".format(py_avg / pybind11_avg))
