#!/usr/bin/env python
"""
This file illustrates the cross language polymorphism using SWIG directors.
"""
from colorama import Fore
import logging

import example


class PyLogger(example.Logger):

    def __init__(self):
        example.Logger.__init__(self)

        # Configure Python logging module root logger
        logging.basicConfig(format='%(asctime)s  %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.INFO)

    def log(self, level, message):
        if level == logging.ERROR:
            message = Fore.RED + message + Fore.RESET
        elif level == logging.WARNING:
            message = Fore.YELLOW + message + Fore.RESET
        logging.log(level, message)


if __name__ == '__main__':
    # Create an instance of the C++ Log class, which has a pointer to a C++ Logger class within it
    log = example.Log()

    # Add a simple C++ Logger (log owns the Logger, so we disown it first by clearing the .thisown flag).
    print("Adding and calling a normal C++ Logger")
    print("--------------------------------------")
    logger = example.Logger()
    logger.thisown = 0
    log.setLogger(logger)
    log.inf("Hello")
    log.war("World")
    log.log(5, "Yo")
    log.delLogger()

    # Add a Python Logger (log owns the logger, so we disown it first by calling __disown__).
    print()
    print("Adding and calling a Python Logger")
    print("----------------------------------")
    # TODO: Add a Python Logger (make sure to call .__disown__() on it
    # TODO: Set the Logger to this new Python Logger
    # TODO: Log a mix of ERROR, INFO, and WARNING messages
    # TODO: Don't forget to delete the logger to prevent a memory leak

    # All done.
    print()
    print("python exit")
