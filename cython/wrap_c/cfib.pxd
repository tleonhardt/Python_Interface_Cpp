# coding=utf-8
"""
Cython declaration file specifying what function(s) we are using from which external C header.
"""
cdef extern from "fibonacci.h":
    int compute_fibonacci(int n)
