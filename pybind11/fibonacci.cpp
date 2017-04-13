/* File : fibonacci.cpp
 *
 * Implementation of the algorithm in C++.
 *
 * For simplicity, we put both this function and the binding code into a single file.
 *
 * In practice, implementation and binding code will generally be located in separate files.
 */

#include <pybind11/pybind11.h>

int compute_fibonacci(int n)
{
    int temp;
    int a = 1;
    int b = 1;
    for (int x=0; x<n; x++)
    {
        temp = a;
        a += b;
        b = temp;
    }
    return a;
}

namespace py = pybind11;

// The PYBIND11_PLUGIN() macro creates a function that will be called when an import statement is issued within Python
PYBIND11_PLUGIN(fibonacci)
{
    // creates a module named fibonacci (with the supplied docstring)
    py::module m("fibonacci", "pybind11 fibonacci plugin");

    // generates binding code that exposes the compute_fibonacci() function to Python
    m.def("compute_fibonacci", &compute_fibonacci, "A function which computes the Nth Fibonacci number");

    // Notice how little code was needed to expose our function to Python: all details regarding the function’s
    // parameters and return value were automatically inferred using template metaprogramming


    return m.ptr();
}
