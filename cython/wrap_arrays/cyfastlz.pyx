# coding=utf-8
# distutils: libraries = "fastlz"
# distutils: library_dirs = "."
cimport cfastlz
import numpy as np
cimport numpy as np

cpdef compress(in_buf):
    N = len(in_buf)

    # The minimum input buffer size is 16.
    if N < 16:
        return None

    # The output buffer must be at least 5% larger than the input buffer and can't be smaller than 66 bytes
    M = max(int(1.5*N), 66)

    # Create the output buffer
    output = bytearray(M)

    # wrap np arrays to c arrays for the call
    fcret = cfastlz.fastlz_compress(<const unsigned char*>in_buf, N, <unsigned char*> output)

    if fcret <=0:
        return None

    # Return the compressed data as a numpy array
    return bytes(output[:fcret])

cpdef decompress(in_buf):
    N = len(in_buf)
    # Bounds check length, just make sure it is positive
    if N < 1:
        return None

    # Create an output buffer of sufficient size
    M = max(int(4*N), 66)
    output = bytearray(M)

    # wrap np arrays to c arrays for the call
    fcret = cfastlz.fastlz_decompress(<const unsigned char*> in_buf, N, <unsigned char*> output, M)

    # If error occurs, e.g. the compressed data is corrupted or the output buffer is not large enough, then 0 (zero)
    if fcret <=0:
        return None

    # Return the uncompressed data as a numpy array
    return bytes(output[:fcret])
