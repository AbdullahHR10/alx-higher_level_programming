#!/usr/bin/python3
"""Module for printing names.
    Functions:

    say_my_name: Prints names.
    """


def say_my_name(first_name, last_name=""):
    """Function that prints names.
    first_name (str): first name.
    last_name (str): last name."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name and last_name:
        print("My name is {} {}".format(first_name, last_name))
    elif first_name:
        print("My name is {} ".format(first_name))
    elif last_name:
        print("My name is {}".format(last_name))
