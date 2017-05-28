# coding=utf-8
"""
Pure Python code for numerically integrating a function.
"""
from math import cos


def f(x):
    """Example function in one variable.

    :param x: float - point we wish to evaluate the function at
    :return: float - function value at point x
    """
    return cos(x)


def integrate_f(a, b, N):
    """Numerically integrate function f starting at point a and going to point b, using N rectangles.

    :param a: float - starting point
    :param b: float - ending point
    :param N: int - number of points to use in the rectangluar approximation to the integral
    :return: float - approximation to the true integral, which improves as N increases
    """
    s = 0.0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
