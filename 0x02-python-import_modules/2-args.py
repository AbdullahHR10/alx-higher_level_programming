#!/usr/bin/python3
if __name__ == "__main__":
    import sys
num_arg = len(sys.argv) - 1
if num_arg == 0:
    print("0 arguments.")
elif num_arg == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_arg))
args = sys.argv[1:]
for i, arg in enumerate(args, start=1):
    print("{}: {}".format(i, arg))
