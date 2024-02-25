#!/usr/bin/python3
"""Module of a Square class.
"""


class Square(Rectangle):
    """Square class.

    Attributes:
    size: size of square
    x: x
    y: y
    id: id of square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def width(self):
        return self.width
    def __str__(self):
        """Returns the string representation of the Square."""
