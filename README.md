# Python_Interface_Cpp
Example code for interfacing with C and C++ from Python using Cython, SWIG, PyPy, CFFI, and pybind11:

* [Cython](http://cython.org)
* [SWIG](http://www.swig.org)
* [PyPy](https://pypy.org)
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
| pypy + CFFI        | 40      |
| Cython (optimized) | 27      |
| Cython (wrapper)   | 25      |
| SWIG               | 14      |
| pybind11           | 10      |
| pypy               |  8      |
| CFFI               |  6      |
| Python             |  1      |

NOTE: These numbers were originally measured on a 2013 15" Mac Book Pro using Python 3.6 via Anaconda distro
with the latest versions of all tools installed using the conda package manager.  I have more recently measured
using a Python 3.7 virtual environment via [Pipenv](https://github.com/pypa/pipenv) and confirmed that they
stayed approximately the same and relative rankings in terms of performance are identical.

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
lets you use optional C static types embedded in your Python code and automatically translate
that to C or C++ code and then automatically compile it.

But all of that happens pretty much behind the scenes, and you are left with code that looks
mostly like Python, but has the performance of C.

It has a bit of a learning curve, but it is amazing.  In particular it is awesome for
optimizing existing Python code.  But it is also good for providing really high performance
wrappers of existing C/C++ code with a clean Pythonic API.  It just requires you to manually
do the wrapping, so it involves significantly more work on your part to do so than using SWIG.

The [Cython documentation](http://docs.cython.org/en/latest/) is excellent and there is a great
[book](https://www.amazon.com/Cython-Programmers-Kurt-W-Smith/dp/1491901551) from OReilly and also some great
video presentations on [YouTube](https://www.youtube.com/watch?v=gMvkiQ-gOW8&t=14s) and on [Safari](http://shop.oreilly.com/product/0636920046813.do).

## SWIG
SWIG is the Simplified Wrapper and Interface Generator.  It is capable of wrapping C and C++
code/libraries in about 20 different target languages including Python, Java, C#, etc.

SWIG largely automates the process of wrapping existing C/C++ code so it is faster and easier
to use for that purpose than Cython.

The [SWIG documentation](http://www.swig.org/Doc3.0/index.html) can sometimes leave something to be desired, but it is an extremely powerful
tool which is an excellent choice in many situations.  A professor from the University of Oslo has
a decent [video tutorial](https://www.youtube.com/watch?v=J-iVTLp6M9I) with [example code](https://github.com/UiO-INF3331/code-snippets/tree/master/mixed/swig) on GitHub.

SWIG is the granddaddy of all of the tools here.  It has been around for a long time.  Given how
long it has been around and the wealth of target languages, it is probably the most widely used
of these tools.

## PyPy
PyPy is a fast, compliant alternative implementation of the Python language (2.7.13 and 3.5.3) in Python.
The normal implementation of Python is in C and is referred to as CPython.  PyPy uses a Just-in-Time (JIT)
compiler, so Python programs often run significantly faster on PyPy.  It also employs various memory
optimizations compared to CPython.

The major advantage of PyPy is that it can deliver some quick and easy wins.  You don't need to change
your existing Python code in any way!  You just install PyPy and run your Python program using **pypy**
instead of **python**.

The major disadvantage of PyPy is that not all 3rd-party Python libraries work with PyPy.  Detailed
information on which modules are compatible can be found [here](https://pypy.org/compat.html).

## CFFI
CFFI is the C Foreign Function Interface for Python.  It is basically an improved version of
Python's built-in ctypes.

It can call functions in a C dynamic library just by writing code inline in Python.  There
isn't any sort of need for an external wrapper.  Hence, it is the quickest and easiest
of these libraries to use to interface with existing C dynamic libraries.  However, the
performance is decidedly worse than the other options presented here unless it is used in combination
with PyPy, in which case the performance is truly excellent.

Its real strength lies in 100% compatibility with PyPy and lower overhead present when using CFFI
with PyPy's JIT.  So it is the go-to choice if you are
using the PyPy JIT.  That being said, I don't think I would recommend using it if you aren't using
PyPy because either Cython or SWIG tend to be a better fit for most applications when used with
the normal CPython implementation of Python.

CFFI has decent [documentation](https://cffi.readthedocs.io/en/latest/) and here is a [tutorial video](https://www.youtube.com/watch?v=ThDFmuXH15k).

## pybind11
pybind11 is essentially what arose from the ashes of Boost.Python.  It is the newest of the tools
presented here, but it is already better than
Boost.Python ever was.

It only works with bleeding-edge C++11 compilers.  My experience is that I couldn't get it to work on Mac OS X at all and I tried with both Python 3.6 and Python 2.7, both from Anaconda distro and using default LLVM compiler from Xcode on Mac OS X
10.12.4.  I also could not get it working on either Ubuntu 16.04 or 14.04 with either Python 2.7 or 3.6. I was able to get it working on Debian 9 with both Python 2.7 and 3.5 as installed from apt-get.  Given that experience I wouldn't even consider it remotely stable yet.

The performance is worse than either SWIG or Cython and the ease of use is not as easy to use as SWIG.
So does a niche exist for pybind11?  pybind11 does make it easy to embedded Python within a C++ project and it is well
supported on Windows.  Here is a [good video](https://channel9.msdn.com/Shows/Visual-Studio-Toolbox/Embedding-Python-in-a-C-Project) that demonstrates scripting a
C++ application with Python using pybind11 and Visual Studio 2017.

[pybind11 documentation](http://pybind11.readthedocs.io/en/stable/) is decent and here is a [conference video](https://www.youtube.com/watch?v=jQedHfF1Jfw).

pybind11 does appear to be under rapid development, so maybe it will get better in the future; but at this time I can
only recommend it for embedding Python within a C++ project (though it is probably worth noting that Cython is also
capable of doing that).

# Conclusion / Recommendations
Ok, here are some of my thoughts.  They are my opinions and are hence subjective in nature, though
they are grounded in my having actually evaluated these tools at length.

If what you care about most is performance, then Cython is the clear winner by a wide margin.  But on
the flip side, this tool has the largest learning curve, at least if you are looking at wrapping
existing C++ code.

If what you care about most is productivity, then SWIG is the clear winner if you want to wrap existing
C/C++ code and Cython is the clear winner if you want to optimize existing Python code.

If all of the 3rd-party Python libraries you are using are compatible with PyPy, then using PyPy can
provide a painless performance boost for free.  Given that there are no code changes required to use it,
it is very much worth trying it and seeing what sort of speedup you get.

CFFI is pretty lame unless you are using PyPy.  But it is super easy to use with near zero learning curve.
So if you just want to call a function or two from an existing C library, it may be your best bet.  On
the other hand, if all of the 3rd party libraries you are using work with PyPy and you only want to
interface with C code (not C++), then the combination of PyPy + CFFI can result in some truly impressive
performance improvements.

pybind11 struggles with easy cross-platform compatibility and its performance is worse than SWIG, but it is more of a
pain to use than SWIG.  So I'd recommend staying away from it for now unless you are looking to embed Python code within
a C++ project on Windows.

## Updates for 2019
Recent re-evaluation of all these options firmly confirms my original conclusions.  `Cython` and `SWIG` are both awesome 
with distinct tradeoffs.  The combination of `PyPy` + `CFFI` is attractive and shows a lot of potential.  While the 
cross-platform compatibility issues previously seen with `pybind11` appear to have been resolved, I still can't see a
use case for which it would be superior to one of the other options; but it has a ton of stars on GitHub so perhaps I 
am missing something?

# Running Example Code Yourself
For information on getting all of the necessary prerequisites installed, see
[Prerequisites for Running Example Code](https://github.com/tleonhardt/Python_Interface_Cpp/blob/master/Prerequisites.md).

For info on how to build and run each particular example, see the **Readme.md** in the example directory.


# Excercises
There are a few examples here which are intended as guided exercises to help build your knowledge of how
to use Cython and SWIG.

The exercises exist on the **master** branch, while the solutions exist on the **solutions** branch.

Most exercises have **TODO:** comments in the locations where they want you to write some code and have
instructions in the Readme.md for that exercise.

## Cython Exercises

### Intro to Cython Exercise
The [integrate](https://github.com/tleonhardt/Python_Interface_Cpp/tree/master/cython/integrate) Cython
example serves as a good basic introduction to using Cython to optimize existing Python code.  It
details a relatively typical series of steps which are followed in using Cython for process of
progressively optimizing existing Python code.

### Cython for Wrapping
The [wrap_arrays](https://github.com/tleonhardt/Python_Interface_Cpp/tree/master/cython/wrap_arrays)
Cython example serves as an introduction to using Cython to wrap existing C code.  It purposely uses
an example where the C functions take pointers to arrays, so it can help you learn how to generate
wrapper code for this common type of scenario.

There are better (more optimal) ways of doing this than presented in the solution.  The solution tries
to keep it simple.

## SWIG Exercises

### Cross-language Polymorphism in SWIG
The [logger](https://github.com/tleonhardt/Python_Interface_Cpp/tree/master/swig/logger) SWIG example
serves as an introduction to how to achieve true cross-language polymorphism in SWIG by using directors.
This allows you to have a base class defined in C++, inherit from this class in Python, and then
instantiate a C++ class which takes a pointer to the base class and you pass it a pointer to an instance
of the derived class and your C++ class will end up calling virtual methods defined in Python.

While this sounds complicated and abstract, it is actually pretty simple to make use of it and is of
great practical utility.

As a side benefit, this example also covers how to wrap STL std::string strings and effectively auto-cast
them to Python str objects.

### Using STL Containers in SWIG
The [fastlz](https://github.com/tleonhardt/Python_Interface_Cpp/tree/master/swig/fastlz) SWIG example
serves as an introduction to how to use STL containers such as vectors in your SWIG Python wrappers.  Also
serves as an example of how to get your SWIG wrappers to link to dynamic libraries.

## Solutions
Solutions to all exercises are in the same location as the exercise, but on the **solutions** branch.


# Presentation
The repository also has an overview [presentation](https://github.com/tleonhardt/Python_Interface_Cpp/tree/master/Interfacing_C_C++_with_Python.pdf) covering the basics of Cython, SWIG, and CFFI as well
as when you might want to use each one.

To accompany this presentation, there is a [lab guide](https://github.com/tleonhardt/Python_Interface_Cpp/tree/master/Interfacing_C_C++_with_Python-Exercises.pdf) 
which provides an overview of the Cython and SWIG hand-on exercises in this repository.
