#!/usr/bin/python3
"""Moudle (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """An empty class.
    """
    def __init__(self):
        pass

    @property
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
