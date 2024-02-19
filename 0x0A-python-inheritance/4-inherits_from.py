#!/usr/bin/python3
"""Module.
"""


def inherits_from(obj, a_class):
    """Function that:
    Returns True if the object is an instance of a class that inherited.
    Otherwise False.
    """
    if type(obj) == a_class:
        return False

    for base_class in obj.__class__.__bases__:
        if base_class == a_class:
            return True
            if inherits_from(base_class, a_class):
                return True

    return False
