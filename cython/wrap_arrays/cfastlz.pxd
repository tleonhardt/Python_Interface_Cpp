# coding=utf-8
"""
Cython declaration file specifying what function(s) we are using from which external C header.
"""
from libc.stdint cimport uint8_t


cdef extern from "fastlz.h":
    int fastlz_compress(const uint8_t* inBuf, int length, uint8_t* output)
    int fastlz_decompress(const uint8_t* inBuf, int length, uint8_t* output, int maxout)
