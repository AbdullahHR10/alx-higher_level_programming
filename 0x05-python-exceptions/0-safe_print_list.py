#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            print(i, end = "")
    except ValueError:
        print("Negative numbers are not allowed")
