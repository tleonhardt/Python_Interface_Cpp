#!/usr/bin/env python
""" Python wrapper to time the Cython implementation for computing the nth fibonacci number
in a non-recursive fashion.
"""
from fib_python import compute_fibonacci
from cyfib import compute_fibonacci_wrapper

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

    fib_py = compute_fibonacci(n)
    fib_cy = compute_fibonacci_wrapper(n)
    if fib_py != fib_cy:
        raise(ValueError(fib_cy))

    py_tot = timeit.timeit("compute_fibonacci({})".format(n),
                           setup="from fib_python import compute_fibonacci",
                           number=number_of_times)
    cy_tot = timeit.timeit("compute_fibonacci_wrapper({})".format(n),
                           setup="from cyfib import compute_fibonacci_wrapper",
                           number=number_of_times)
    py_avg = py_tot / number_of_times
    cy_avg = cy_tot / number_of_times

    print("fib({}) = {}".format(n, fib_py))
    print("Python average time:  {0:.2g}".format(py_avg))
    print("Cython Wrapper average time:  {0:.2g}".format(cy_avg))
    print("Cython Wrapper speedup: {0:.2g} times".format(py_avg/cy_avg))
