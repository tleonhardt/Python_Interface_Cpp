# Prerequisites for Running Example Code
The examples on this site are compatible with Mac OS X, Linux, and Windows.  To run these examples
you will need various C/C++ and Python software installed.  The instructions here cover the 
prerequisites necessary to run the Cython, SWIG, and CFFI examples.  


## C and C++ compiler toolchains
To run most of the examples you need a C compiler toolchain and for some of them you also need
a C++ compiler toolchain.  How to get this installed depends on which operating system (OS) you
 are running.
 
### Linux
If you are using any of Linux OSes which use **apt** for a package manager (Debian, Ubuntu, or Mint),
then you can do the following to get all of the C and C++ tools you need:

```bash
sudo apt-get install build-essential
```

For other Linux package managers, the fundamental tools you want to install are ``gcc`` and ``g++``.

### Mac OS X
Install the free **XCode** developer tools from the App Store.  Make sure you run it at least once and 
say "yes" if it asks you if you want to install the command-line tools.

### Windows
**At this time, the build scripts in this repository are all setup to work on Mac OS X or Linux.  So if you 
are using Windows, we recommend using 
[VMware Player](http://www.vmware.com/products/player/playerpro-evaluation.html) or 
[Virtualbox](https://www.virtualbox.org) to install a Linux Virtual Machine (VM).**  
*We will consider converting to a CMake-based build system in the near future which would enable 
consistent compilation across OSes.*

There are a number of options for Windows, but by far the simplest is to use the same compiler which
Python itself was compiled with.  For recent versions of Python released within the past couple years, 
this is Visual C++ 2015, which comes with Visual Studio 2015.  However, Visual Studio 2017 is now out
and newer versions of Python will likely be compiled with that.  Unfortunately, to download Visual 
Studio 2015 at this point requires an MSDN subscription.


## Python and Other Tools
By far the easiest way to get all of the tools installed and setup is by using the Anaconda Python
distribution.  This is a free distribution of Python available for Windows, Mac OS X, and Linux which
comes with a couple hundred of the most common and useful Python modules pre-installed including Cython
and CFFI.  It also comes with the ``conda`` package manager which can be used to install additional
tools such as SWIG.

## Anaconda Python
Download the latest version of [Anaconda](https://www.continuum.io/downloads).  Either the Python 3.6 or
Python 2.7 version should be fine, but we recommend the Python 3.6 version.

Install Anaconda per the instructions and let it modify your .bashrc, .bash_profile, or path accordingly.
NOTE: Do not use ``sudo`` to install Anaconda, just install it as a normal user.

This also installs Cython and CFFI.

## SWIG
Now that Anaconda is installed, you can use the included **conda** package manager to install SWIG.  Do
the following in a command-line terminal:

```bash
conda install swig
```
