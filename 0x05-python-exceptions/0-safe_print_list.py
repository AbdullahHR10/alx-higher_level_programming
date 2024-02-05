#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        element_count = 0
        if x < 0:
            raise ValueError("Negative numbers are not allowed")
        for i in range(x):
            if element_count >= x:
                break
            print(my_list[i], end="")
            element_count += 1
    except IndexError:
        pass
    except ValueError as err:
        print(err)
    print()
    return element_count
