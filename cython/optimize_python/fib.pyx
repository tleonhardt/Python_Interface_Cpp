""" Cython implementation for computing the nth fibonacci number in a
non-recursive fashion.
"""

cpdef int compute_fibonacci_cython(int n):
    """ Compute the nth fibonacci number in a non-recursive fashion.
    """
    cdef int a, b, intermediate, x
    a, b = 1, 1
    for x in range(n):
        intermediate = a
        a = a + b
        b = intermediate
    return a
