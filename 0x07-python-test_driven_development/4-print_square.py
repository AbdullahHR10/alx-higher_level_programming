#!/usr/bin/python3
"""Module square with the character #.
"""


def print_square(size):
    """Function that prints a square.
    size (int): Size of the square."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
