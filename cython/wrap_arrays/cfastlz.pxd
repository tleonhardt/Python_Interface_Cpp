# coding=utf-8
"""
Cython declaration file specifying what function(s) we are using from which external C header.
"""
cdef extern from "fastlz.h":
    int fastlz_compress(const unsigned char* inBuf, int length, unsigned char* output)
    int fastlz_decompress(const unsigned char* inBuf, int length, unsigned char* output, int maxout)
