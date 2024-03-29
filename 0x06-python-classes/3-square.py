#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines a square by: (based on 2-square.py).

    Attributes:
        size: Size of a square.
        area: Area of a square.
    """

    def __init__(self, size=0):
        """Creates Instantiations.

        Args:
            size: Size of the square.
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square.
        """
        return self.__size ** 2
