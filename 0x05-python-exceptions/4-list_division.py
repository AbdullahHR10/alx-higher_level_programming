#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                value_1 = my_list_1[i] if i < len(my_list_1) else 0
                value_2 = my_list_2[i] if i < len(my_list_2) else 0
                if isinstance(value_1, (int, float)) and \
                        isinstance(value_2, (int, float)):
                    if value_2 == 0:
                        raise ZeroDivisionError("division by 0")
                    result.append(value_1 / value_2)
                else:
                    raise TypeError("wrong type")
            except IndexError:
                print("out of range")
                result.append(0)
    except ZeroDivisionError as err:
        print(err)
        result.append(0)
    except TypeError as err:
        print(err)
        result.append(0)
    finally:
        return result
