#!/usr/bin/python3
"""Module for adding integers.
    Functions:

    add_integer: Calculates the sum of two numbers.
    """


def add_integer(a, b=98):
    """Function that calculates the sum of two numbers.
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return int(a + b)
