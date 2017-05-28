# coding=utf-8
"""
Cython declaration file specifying what function(s) we are using from which external C header.
"""
from libc.stdint cimport uint8_t


cdef extern from "fastlz.h":
    # TODO: Copy function prototypes you want to wrap from the C header file here (without ending semicolon)

