#!/usr/bin/python3
"""Module of Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


class Rectangle(BaseGeometry):
    """Rectangle class.
    width: Width of the rectangle.
    height: height of the rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
