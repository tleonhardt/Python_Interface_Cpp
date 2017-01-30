/* fibonacci.i */
 %module fibonacci
 %{
 /* Includes the header in the wrapper code */
 #include "fibonacci.h"
 %}

/* Parse the header file to generate wrappers */
 %include "fibonacci.h"
