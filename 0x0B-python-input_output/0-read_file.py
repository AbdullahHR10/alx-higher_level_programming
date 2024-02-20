#!/usr/bin/python3
"""Module to read a file.
"""


def read_file(filename=""):
    """Function that takes a filename as a parameter and reads it.
    then prints it to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
