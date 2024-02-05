#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            if i < 0:
                raise ValueError("Negative numbers are not allowed")
            print(i, end="")
    except ValueError as err:
        print(err)
