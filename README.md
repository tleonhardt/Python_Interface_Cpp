# Python_Interface_Cpp
Example code for interfacing with C and C++ from Python using Cython, SWIG, CFFI, and pybind11:

* [Cython](http://cython.org)
* [SWIG](http://www.swig.org)
* [CFFI](http://cffi.readthedocs.io)
* [pybind11](https://github.com/pybind/pybind11)

## Fibonacci Example
This repository has example code for interfacing with some C code for calculating the Nth
fibonacci number from Python using the four different tools.

This is the one universal example present for all tools and is thus intended to provide
an apples-to-apples comparison both in terms of API/usage and performance.

### Fibonacci Performance Benchmarks
One metric for evaluating these tools is performance.  Here is a table which shows speedup
factor relative to the pure Python implementation of the Fibonacci code.  So a speedup of **2**
means that code ran twice as fast as the pure Python version.

| Tool               | Speedup |
| ------------------ | -------:|
| Cython (optimized) | 30      |
| C                  | 28      |
| Cython (wrapper)   | 27      |
| SWIG               | 15      |
| CFFI               |  6      |
| Python             |  1      |

NOTE: These numbers were measured on a 2013 15" Mac Book Pro using Python 3.6 via Anaconda distro
with the latest versions of all tools installed using the conda package manager.

And yes, the Cython version actually runs faster than my hand-coded (in the obvious way) pure C
implementation.

The Fibonacci example presented here is pretty trivial.  Your mileage may vary depending on your
application.  But overall these performance measurements are fairly representative of what you
may typically expect from each of these tools.  

In general whenever you see nested loops in your Python code, that is where you should expect the
most speedup can be gained by optimizing with C/C++.  Speedups on the order of 1000 are not
uncommon if you are dealing with triply-nested loops for things like image processing code.

## Other Examples
Some of the tools have other examples provided as well, typically for more advanced features.
But no attempt is made to provide an apples-to-apples cross-tool comparison for these other
examples.

# Meet the tools

## Cython
Cython is the C-Extensions for Python module and it is an optimising static transpiler which
lets you use optional C static types embedded in your Python code and automatically tranlate
that to C or C++ code and then automatically compile it.

But all of that happens pretty much behind the scenes, and you are left with code that looks
mostly like Python, but has the performance of C.

It has a bit of a learning curve, but it is amazing.  In particular it is awesome for
optimizing existing Python code.  But it is also good for providing really high performance
wrappers of existing C/C++ code with a clean Pythonic API.  It just requires you to manually
do the wrapping, so it involves significantly more work on your part to do so than using SWIG.

The Cython documentation is excellent and there is a great book from OReilly and also some great
video presentations on YouTube and on Safari.

## SWIG
SWIG is the Simplified Wrapper and Interface Generator.  It is capable of wrapping C and C++
code/libraries in about 20 different target languages including Python, Java, C#, etc.  

SWIG largely automates the process of wrapping existing C/C++ code so it is faster and easier
to use for that purpose than Cython.

The SWIG documentation can sometimes leave something to be desired, but it is an extremely powerful
tool which is an excellent choice in many situaitons.

SWIG is the granddaddy of all of the tools here.  It has been around for a long time.  Given how
long it has been around and the wealth of target languages, it is probably the most widely used
of these tools.

## CFFI
CFFI is the C Foreign Function Interface for Python.  It is basically an improved version of
Python's built-in ctypes.  

It can call functions in a C dynamic library just by writing code inline in Python.  There
isn't any sort of need for an external wrapper.  Hence, it is the quickest and easiest
of these libraries to use to interface with existing C dynamic libraries.  However, the
performance is decidedly worse than the other options presented here.

Its real strength lies in 100% compatibility with PyPy.  So it is the go-to choice if you are
using the PyPy JIT.  That being said, I don't think I would recommend using it if you aren't using
PyPy because either Cython or SWIG tend to be a better fit for most applications.

## pybind11
pybind11 is essentially what arose from the ashes of Boost.Python.  It is the newest of the tools
presented here, but it is already dramatically better, more stable, and easier to use than
Boost.Python ever was.

It only works with modern C++11 compilers.

My experience is limited with this tool so far, but it appears to be under rapid development
and is definitely a tool to watch.

# Conclusion / Recommendations
Ok, here are some of my thoughts.  They are my opinions and are hence subjective in nature, though
they are grounded in my having actually evaluated these tools at length.  

If what you care about most is performance, then Cython is the clear winner by a wide margin.  But on the
flip side, this tool has the largest learning curve, at least if you are looking at wrapping existing
C++ code.

If what you care about most is productivity, then SWIG is the clear winner if you want to wrap existing
C/C++ code and Cython is the clear winner if you want to optimize existing Python code.

CFFI is pretty lame unless you are using PyPy.  But it is super easy to use with near zero learning curve.
So if you just want to call a function or two from an existing C library, it may be your best bet.

pybind11 ... I'll update this once I have more experience under my belt using it.
