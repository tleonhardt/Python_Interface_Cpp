# coding=utf-8
# distutils: libraries = "fibonacci"
# distutils: library_dirs = "."
cimport cfib

cpdef int compute_fibonacci_wrapper(int n):
    return cfib.compute_fibonacci(n)
