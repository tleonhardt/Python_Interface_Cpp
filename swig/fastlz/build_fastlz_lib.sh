# Compile fastlz.c with position-independent code
cc -std=c11 -c -Wall -Werror -g0 -O3 -fpic fastlz.c

# Create a shared library from an object file
cc -shared -o libfastlz.so fastlz.o
