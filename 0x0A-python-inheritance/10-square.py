#!/usr/bin/python3
"""Moudle of a Square that inherits from Rectangle (9-rectangle.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square.

    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size):
        """Initializes a Rectangle instance with the given width and height.

        Args:
            __size (int): size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
