#!/usr/bin/python3
"""Module that appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """Function that takes a string as a parameter and appends it at the end
    of a text file.
    Returns: the number of chars added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        count = 0
        for chars in text:
            count += 1
        return count
