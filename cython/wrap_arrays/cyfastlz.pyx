# coding=utf-8
# distutils: libraries = "fastlz"
# distutils: library_dirs = "."
cimport cfastlz
from libc.stdint cimport uint8_t


cpdef bytes compress(bytes in_buf):
    cdef int N, M

    N = len(in_buf)

    # The minimum input buffer size is 16.
    if N < 16:
        return None

    # The output buffer must be at least 5% larger than the input buffer and can't be smaller than 66 bytes
    M = max(int(1.5*N), 66)

    # Create the output buffer
    output = bytearray(M)

    # TODO: Call cfastlz.fastlz_compress().  Make sure to get the return value and to cast Python array type to C type.

    # TODO: Check for invalid return value and return None if that occurs

    # TODO: Return the compressed data as a bytes object


cpdef bytes decompress(bytes in_buf):
    cdef int N, M

    N = len(in_buf)

    # Bounds check length, just make sure it is positive
    if N < 1:
        return None

    # Create an output buffer of sufficient size
    M = max(int(4*N), 66)
    output = bytearray(M)

    # TODO: Call cfastlz.fastlz_decompress().  Make sure to get the return value and to cast Python array type to C type.

    # TODO: Check for invalid return value and return None if that occurs

    # TODO: Return the uncompressed data as a bytes object
