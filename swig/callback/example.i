/* File : example.i */
%module(directors="1") example
%{
#include "example.h"
%}

/* turn on director wrapping Logger */
%feature("director") Logger;

%include "example.h"

