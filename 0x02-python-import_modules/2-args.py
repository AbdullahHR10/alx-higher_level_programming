#!/usr/bin/python3
import sys
args = sys.argv[1:]
for i, arg in enumerate(args, start=1):
    print("{}: {}".format(i, arg))
