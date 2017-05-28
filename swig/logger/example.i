/* File : example.i */
%module(directors="1") example
%{
#include "example.h"
%}

/* The std_string.i library provides typemaps for converting C++ std::string objects to and from Python strings */
%include "std_string.i"

/* turn on director wrapping Logger - directors enable cross-language polymorphism */
%feature("director") Logger;

%include "example.h"

