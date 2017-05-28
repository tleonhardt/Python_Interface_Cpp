#!/usr/bin/env python
"""
This file illustrates the cross language polymorphism using directors.
"""
import example


class PyLogger(example.Logger):

    def __init__(self):
        example.Logger.__init__(self)

    def log(self):
        print("PyLogger.log()")

# Create an instance of the C++ Log class, which has a pointer to a C++ Logger class within it
log = example.Log()

# Add a simple C++ Logger (log owns the Logger, so we disown it first by clearing the .thisown flag).
print("Adding and calling a normal C++ Logger")
print("--------------------------------------")
logger = example.Logger()
logger.thisown = 0
log.setLogger(logger)
log.log()
log.delLogger()

# Add a Python Logger (log owns the logger, so we disown it first by calling __disown__).
print()
print("Adding and calling a Python Logger")
print("----------------------------------")
log.setLogger(PyLogger().__disown__())
log.log()
log.delLogger()

# Let's do the same but use the weak reference this time.
print()
print("Adding and calling another Python logger")
print("------------------------------------------")
logger = PyLogger().__disown__()
log.setLogger(logger)
log.log()
log.delLogger()

# All done.
print()
print("python exit")
