#!/usr/bin/env python
""" Pure Python implementation for computing the nth fibonacci number in a
non-recursive fashion.
"""

def compute_fibonacci(n):
    """
    Computes fibonacci sequence
    """
    a = 1
    b = 1
    intermediate = 0
    for x in range(n):
        intermediate = a
        a = a + b
        b = intermediate
    return a

if __name__ == '__main__':
    import sys
    import timeit

    n = 20
    try:
        n = int(sys.argv[1])
    except Exception:
        pass

    fib_n = compute_fibonacci(n)

    number_of_times = 100000
    try:
        number_of_times = int(sys.argv[2])
    except Exception:
        pass

    total_time = timeit.timeit("compute_fibonacci({})".format(n),
                        setup="from __main__ import compute_fibonacci",
                        number=number_of_times)
    avg_time = total_time / number_of_times
    print("fib({0}) = {1}  [average execution time: {2:.2g} s]".format(n, fib_n, avg_time))
