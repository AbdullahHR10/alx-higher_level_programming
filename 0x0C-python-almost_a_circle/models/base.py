#!/usr/bin/python3
"""module of a base class.
"""


import json


class Base:
    """Base class of all other classes in this project.

    Attributes:
        __nb_objects (int): Objects of base.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base object.

        Args:
            id (int, optional): ID of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
