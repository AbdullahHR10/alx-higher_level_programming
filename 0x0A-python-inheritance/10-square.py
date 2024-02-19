#!/usr/bin/python3
"""Moudle of a Square that inherits from Rectangle (9-rectangle.py).
"""


class Square(Rectangle):
    """Class Square.

    Attributes:
    __size (int): size of the square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
