#!/usr/bin/python3
"""Moudle checks if the object is an instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """Function that checks if the object is an instance of.
    or if the object is an instance of a class that inherited from.
    Returns: True if conditions are met.
    Otherwise False.
    """
    return isinstance(obj, a_class)
