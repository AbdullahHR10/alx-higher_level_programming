#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines a square by: (based on 1-square.py).

    Attributes:
        size: Size of a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Creates Instantiations.

        Args:
            size: Size of the square.
            position: Position of the square.
        """

        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        """Returns the value of position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of position.
        """
        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with the character #.
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
