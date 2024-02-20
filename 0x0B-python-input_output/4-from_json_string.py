#!/usr/bin/python3
"""Module that returns an object represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """Function that returns an object (Python data structure)
    represented by a JSON string.
    """
    json.loads(my_str)
