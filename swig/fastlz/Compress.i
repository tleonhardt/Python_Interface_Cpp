/* Compress.i */
 %module Compress
 %{
 /* Includes the header in the wrapper code */
 #include "Compress.h"
 %}

// SWIG library file for ISO C99 types such as uint32_t
%include "stdint.i"

// Provide support for the C++ vector class in the STL
%include "std_vector.i"

// Instantiate a Python class called VectorUint8 which wraps a C++ vector<uint8_t> STL container of bytes
namespace std
{
    %template(VectorUint8) vector<uint8_t>;
}

/* Parse the header file to generate wrappers */
 %include "Compress.h"
