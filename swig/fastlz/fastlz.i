/* fastlz.i */
 %module fastlz
 %{
 /* Includes the header in the wrapper code */
 #include "fastlz.h"
 %}

/* Parse the header file to generate wrappers */
 %include "fastlz.h"
