# Faster code via static typing and Cython
Cython is a Python compiler. This means that it can compile normal Python code without changes (with a few 
obvious exceptions of some as-yet unsupported language features). However, for performance critical code, 
it is often helpful to add static type declarations, as they will allow Cython to step out of the dynamic 
nature of the Python code and generate simpler and faster C code - sometimes faster by orders of magnitude.

It must be noted, however, that type declarations can make the source code more verbose and thus less 
readable. It is therefore discouraged to use them without good reason, such as where benchmarks prove that 
they really make the code substantially faster in a performance critical section. Typically a few types in 
the right spots go a long way.

All C types are available for type declarations: integer and floating point types, complex numbers, structs, 
unions and pointer types. Cython can automatically and correctly convert between the types on assignment. 
This also includes Python’s arbitrary size integer types, where value overflows on conversion to a C type 
will raise a Python OverflowError at runtime. (It does not, however, check for overflow when doing 
arithmetic.) The generated C code will handle the platform dependent sizes of C types correctly and safely 
in this case.

Types are declared via the cdef keyword.

## Exercise

The file **integrate.py** contains pure Python code for numerically integrating a function.  The file 
**cyintegrate.pyx** contains an exact copy of the code in *integrate.py*.  The **build_cython.sh** script 
builds the Cython code present in **cyintegrate.pyx** using the configuration in **setup.py**.

The **cython_speedup.py** file is setup to import both the pure Python and the Cython version and to 
benchmark their performance using a common configuration.  

NOTE: You need to rebuild your Cython code anytime you make changes to **cyintegrate.pyx**


## Step 1 - see how things work to start with
Cython will give some performance benefit even when compiling Python code without any static type
declarations.

Build the Cython code:

```bash
python setup.py build_ext --inplace
```

Run **cython_speedup.py** to compare the two implementations at this point.

```bash
python cython_speedup.py
```

On my system, even though we have done **nothing** to change the pure Python code in any way, Cython
provides about a 60% speedup.


## Step 2 - look at the HTML annotation file
The **setup.py** file contains this code which tells Cython to create a *.html annotations file:

```python
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
```

This is equivalent to calling cythonize with the **-a** flag at the command line.

Open the **cyintegrate.html** file in the web browser of your choice.  Yellow lines show code which requires 
integration with the Python interpreter.  The darker the yellow, the more interactions with the Python
intepreter.  Any interactions with the Python intepreter slow Cython's generated C/C++ code down.  White lines
indicate no interaction with the Python intepreter (pure C code).

What you want to do is get rid of as much yellow as possible and end up with as much white as possible.  This
matters particularly inside loops.  The main way you get rid of these interactions with the Python interpreter
is to declare optional C static types, so Cython can use them to generate fast C code.


## Step 3 - Typing Variables
As we saw, simply compiling this code in Cython merely gives a 60% speedup. This is better than nothing, 
but adding some static types can make a much larger difference.

Types for function arguments can be added simply by prefacing the parameter name with a C type, such as:

```python
def f(double x):
    return cos(x)
```

Types for local variables can be added by declaring them wtih **cdef**:
```python
cdef int i
```

Try adding static types for all function arguments and all local variables.  I recommend using **double** for
floating point types since the Python **float** type corresponds to a C **double**.  Once you have done
this, recompile your Cython code and re-run **cython_speedup.py**.

This results in a 2.5 times speedup over the pure Python version.


## Step 4 - Typing Functions
Python function calls can be expensive – in Cython doubly so because one might need to convert to and from 
Python objects to do the call. In our example above, the argument is assumed to be a C double both inside 
f() and in the call to it, yet a Python float object must be constructed around the argument in order to 
pass it.

Therefore Cython provides a syntax for declaring a C-style function, the cdef keyword:
```python
cdef double f(double x) except? -2:
    return cos(x)
```

Some form of except-modifier should usually be added, otherwise Cython will not be able to propagate 
exceptions raised in the function (or a function it calls). The except? -2 means that an error will be 
checked for if -2 is returned (though the ? indicates that -2 may also be used as a valid return value). 
Alternatively, the slower except * is always safe. An except clause can be left out if the function returns 
a Python object or if it is guaranteed that an exception will not be raised within the function call.

A side-effect of cdef is that the function is no longer available from Python-space, as Python wouldn’t 
know how to call it. It is also no longer possible to change f() at runtime.

Using the cpdef keyword instead of cdef, a Python wrapper is also created, so that the function is 
available both from Cython (fast, passing typed values directly) and from Python (wrapping values in Python 
objects). In fact, cpdef does not just provide a Python wrapper, it also installs logic to allow the 
method to be overridden by python methods, even when called from within cython. This does add a tiny 
overhead compared to cdef methods.

Speedup: 5 times over pure Python.


## Step 5 - Replacing Python standard library calls with C library calls
The call to **cos(x)** still requires interaction with the Python interpreter.  The C standard library
also has a pure C implementation of the cosine function.  Wouldn't it be great if we could just call that
function instead?

Well, we can!  Cython supports this sort of syntax:

```python
from libc.math cimport cos
```

We can replace the "from math import cos" line with the above for further performance improvements.

Speedup: 28 times over pure Python.
