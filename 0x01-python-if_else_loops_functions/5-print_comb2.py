#!/usr/bin/python3
for i in range(1, 100):
    if i == 99:
        print("{}".format(i))
        break
    else:
        print("{} ,".format(i), end="")
