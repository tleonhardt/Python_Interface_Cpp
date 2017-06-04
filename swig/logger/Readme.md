# Cross-language polymorphism
This example demonstrates cross language polymorphism using SWIG directors.  

This allows you to define a base class in C++ which contains some virtual methods.  Then you can
derive from that class in Python.  Then you instantiate a C++ object from Python where this C++
object takes a pointer to the base class type.  Then you can call a virtual method from C++.

If a base class type was used, then it calls the C++ virtual method.  But if a Python derived class
is used, it calls the Python virtual method from C++!  If this doesn't blow your mind at least a 
little bit, then I don't think you understand what is going on, go through the example more
slowly until your mind is blown ;-)


## Building
Build the SWIG wrapper using the following shell script:

    ./build_swig.sh

## Evaluating
The **runme.py** example constructs the class first using a base class type as implemented in C++, then
using a derived class type as implemented in Python.

    ./runme.py

## Code Files
* C++ implementation
    * example.h/.cpp
* SWIG
    * Interface File
        * example.i
    * Distutils script
        * setup.py
* Test code to run it all
    * runme.py
    
## Exercise
Fill in the **TODO:** blocks present in **runme.py**.
