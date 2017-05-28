#!/usr/bin/env python
# coding=utf-8
""" Python wrapper to time the Cython implementation versus the pure Python implementation.

This is for the example of numerical integration.
"""
from integrate import integrate_f as pyintegrate_f
from cyintegrate import integrate_f as cyintegrate_f
from math import pi, isclose

if __name__ == '__main__':
    import sys
    import timeit

    a = 0
    b = pi/2
    N = 10000
    try:
        N = int(sys.argv[1])
    except Exception:
        pass

    number_of_times = 100
    try:
        number_of_times = int(sys.argv[2])
    except Exception:
        pass

    int_py = pyintegrate_f(a, b, N)
    int_cy = cyintegrate_f(a, b, N)
    if not isclose(int_py, int_cy):
        raise(ValueError(int_cy))

    py_tot = timeit.timeit("integrate_f({}, {}, {})".format(a, b, N),
                           setup="from integrate import integrate_f",
                           number=number_of_times)
    cy_tot = timeit.timeit("integrate_f({}, {}, {})".format(a, b, N),
                           setup="from cyintegrate import integrate_f",
                           number=number_of_times)
    py_avg = py_tot / number_of_times
    cy_avg = cy_tot / number_of_times

    print("int({}, {}, {}) = {}".format(a, b, N, int_py))
    print("Python average time:  {0:.2g}".format(py_avg))
    print("Cython average time:  {0:.2g}".format(cy_avg))
    print("Cython speedup: {0:.2g} times".format(py_avg/cy_avg))
