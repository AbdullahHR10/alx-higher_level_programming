#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines a square by: (based on 1-square.py).

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

    @property
    def size(self):
        """Retrieves the value of size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #.
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
