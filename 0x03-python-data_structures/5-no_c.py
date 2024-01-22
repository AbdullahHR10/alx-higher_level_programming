#!/usr/bin/env python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            continue
        return my_string
