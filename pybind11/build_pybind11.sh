# Path to pybind11 headers
#PYBIND11_INCLUDE=~/anaconda/include/python3.6m
PYBIND11_INCLUDE=~/anaconda/envs/py27/include/python2.7/

# On Linux and Mac OS, this example can be compiled using the following command (for Windows, use CMake)
c++ -O3 -shared -std=c++11 -Wall -Werror -I ${PYBIND11_INCLUDE} `python-config --cflags --ldflags` fibonacci.cpp -o fibonacci.so
