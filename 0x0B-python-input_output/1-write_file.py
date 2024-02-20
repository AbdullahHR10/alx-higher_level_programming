#!/usr/bin/python3
"""Moudle that writes a string to a file.
"""


def write_file(filename="", text=""):
    """Function that takes a string as a parameter and writes it.
    to a text file that is also taken as a parameter.
    Returns: number of chars written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        count = 0
        for chars in text:
            count +=1
        return count
