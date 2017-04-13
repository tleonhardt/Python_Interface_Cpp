#!/usr/bin/env bash
# Path to pybind11 headers
ANACONDA=~/anaconda3
# PYBIND11_INCLUDE=${ANACONDA}/include/python3.6m
PYBIND11_INCLUDE=${ANACONDA}//envs/py27/include/python2.7/

# On Linux and Mac OS, this example can be compiled using the following command (for Windows, use CMake)
c++ -O3 -shared -std=c++11 -Wall -fPIC -I ${PYBIND11_INCLUDE} `python-config --cflags --ldflags` fibonacci.cpp -o fibonacci.so
