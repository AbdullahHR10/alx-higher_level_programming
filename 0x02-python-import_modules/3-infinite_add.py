#!/usr/bin/python3
import sys


result = 0
if __name__ == "__main__":
    for i in sys.argv[1:]:
        result += int(i)
    print(result)
