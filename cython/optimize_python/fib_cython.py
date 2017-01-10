#!/usr/bin/env python
# coding=utf-8
""" Python wrapper to time the Cython implementation for computing the nth fibonacci number
in a non-recursive fashion and compare it to the pure Python implementation.
"""
from fib import compute_fibonacci_cython

if __name__ == '__main__':
    import sys
    import timeit

    n = 20
    try:
        n = int(sys.argv[1])
    except Exception:
        pass

    fib_n = compute_fibonacci_cython(n)

    number_of_times = 100000
    try:
        number_of_times = int(sys.argv[2])
    except Exception:
        pass

    total_time = timeit.timeit("compute_fibonacci_cython({})".format(n),
                               setup="from fib import compute_fibonacci_cython",
                               number=number_of_times)
    avg_time = total_time / number_of_times
    print("fib({0}) = {1}  [average execution time: {2:.2g} s]".format(n, fib_n, avg_time))
