#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Defines a rectangle by: based on 0-rectangle.py.

    Attributes:
        width: Width of a rectangle
        height: Height of a rectangle
    """

    def __init__(self, width=0, height=0):
        """Creates Instantiations.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
        """
        self.__width = width
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
    @property
    def width(self):
        """Returns the width of the rectangle.
        """
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the value of width.
        """
        if not isinstance(value, int):
             raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """Returns the height of the rectangle.
        """
        return self.__height
    @height.setter
    def height(self, value):
        """Sets the value of width.
        """
        if not isinstance(value, int):
             raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
