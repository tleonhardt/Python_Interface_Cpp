/* fibonacci.i */
 %module fibonacci
 %{
 /* Includes the header in the wrapper code */
 #include "fibonacci.h"
 %}

// Include types such as uint32_t, uint8_t, etc.
 %include "stdint.i"

/* Parse the header file to generate wrappers */
 %include "fibonacci.h"
