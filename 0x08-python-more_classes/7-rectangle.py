#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Defines a rectangle by: based on 4-rectangle.py.

    Attributes:
        width: Width of a rectangle
        height: Height of a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creates Instantiations.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
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

    def area(self):
        """Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rectangle_str = ""
        if self.__width <= 0 or self.__height <= 0:
            return ""
        for i in range(self.__height - 1):
            rectangle_str += Rectangle.print_symbol * self.__width + "\n"
        rectangle_str += Rectangle.print_symbol * self.__width
        return rectangle_str

    def __repr__(self):
        return f"Rectangle({self.__width},{self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
