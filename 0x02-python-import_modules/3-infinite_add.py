#!/usr/bin/python3
if __name__ == "__main__":
    import sys
args = sys.argv[1:]
num_args = len(sys.argv) - 1
if num_args > 0:
    result = 0
else:
    result = sum(map(int, args))
    print(result)
