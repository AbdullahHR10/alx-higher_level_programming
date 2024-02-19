#!/usr/bin/python3
"""Module of Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class.

    Attributes:
    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
