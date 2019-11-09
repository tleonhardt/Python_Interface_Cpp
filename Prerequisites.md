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
There are a number of options for Windows, but by far the simplest is to use the same compiler which
Python itself was compiled with.  For recent versions of Python released within the past couple years, 
this is the Visual C++ compiler which comes with Visual Studio 2017.

It is relatively easy to use both SWIG and Cython on Windows because all C/C++ compilation can 
coordinated within the setup.py file and handled either by the setuptools or distutils Python module.
In this case, Python will automatically know where all of the correct libraries to link against are.

Using CFFI can be a little bit more finicky since it is directly calls into pre-compiled dynamic
libraries and makes some assumptions regarding the C ABI.  So you really need to make sure you are 
using the exact compiler that Python itself was compiled with.

See the [WindowsCompliers](https://wiki.python.org/moin/WindowsCompilers) section of the Python Wiki for more 
information.

**If you try to use the examples on Windows and run into difficulties, you may wish to setup a Linux
virtual machine (VM) for evaluation purposes since C/C++ compilers are a lot easier to setup on Linux.
We recommend using 
[VMware Player](http://www.vmware.com/products/player/playerpro-evaluation.html) or 
[Virtualbox](https://www.virtualbox.org) to install a Linux Virtual Machine (VM).**  


## Python and Other Tools

### Pipenv
[Pipenv](https://github.com/pypa/pipenv) is an easy way to install compatible versions of `cffi`, `cython`, and 
`pybind11`.  Once `pipenv` in installed, these other packages can be installed in a virtual environment using:
```shell script
pipenv install
```  

Then this Python virtual environment can be entered using:
```shell script
pipenv shell
```

### Anaconda Python
Another easy way to get all of the tools installed and setup is by using the Anaconda Python
distribution.  This is a free distribution of Python available for Windows, Mac OS X, and Linux which
comes with a couple hundred of the most common and useful Python modules pre-installed including Cython
and CFFI.  It also comes with the ``conda`` package manager which can be used to install additional
tools such as SWIG.

Download the latest version of [Anaconda](https://www.continuum.io/downloads).  We recommend Python 3.6 or newer.

Install Anaconda per the instructions and let it modify your .bashrc, .bash_profile, or path accordingly.
NOTE: Do not use ``sudo`` to install Anaconda, just install it as a normal user.

This also installs Cython and CFFI.

## SWIG
If Anaconda is installed, you can use the included **conda** package manager to install SWIG.  Do
the following in a command-line terminal:

```bash
conda install swig
```

Alternatively, on macOS you can use the Homebrew package manager to install SWIG:

```shell script
brew install swig
```

## PyPy
PyPy is best installed with a package manager such as *brew* on Mac OS X or *apt-get** on many Linux distros.

### PyPy on Mac
Use the Homebrew package manager to install

```bash
brew install pypy
```

### PyPy on Linux
Use your the package manager which comes your distro to install pypy.  For example, on Debian, Ubuntu, or Mint
distros:

```bash
sudo apt-get install pypy
```

### PyPy on Windows
Download a Windows binary from the PyPy website:  http://pypy.org/download.html
