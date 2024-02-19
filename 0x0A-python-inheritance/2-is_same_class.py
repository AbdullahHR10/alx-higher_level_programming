#!/usr/bin/python3
"""Moudle checks if the object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """Function checks if an object is exactly an instance of a class.
    Returns: True if the object is exactly an instance of the specified class.
    False otherwise.
    """
    if isintance(obj, a_class):
        return True
    else:
        return False
