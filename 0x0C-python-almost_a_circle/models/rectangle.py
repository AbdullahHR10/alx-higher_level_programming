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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the value of x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the value of y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        for i in range(self.__height):
            print("#" * self.__width)
