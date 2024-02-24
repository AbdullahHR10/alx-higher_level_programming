#!/usr/bin/python3
"""Module of a Rectangle class.
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class.

    Attributes:
    __width: width of the rectangle.
    __height: height of the rectangle.
    __x: x.
    __y: y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__Y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """Gets the value of x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x."""
        self.__x = value

    @property
    def y(self):
        """Gets the value of y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y."""
        self.__y = value
