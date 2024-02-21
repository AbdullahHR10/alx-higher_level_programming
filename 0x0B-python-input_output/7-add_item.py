#!/usr/bin/python3
"""Module that adds all arguments to a Python list,
and then saves them into a file.
"""


import json
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"


my_list = load_from_json_file(filename) if args else []
my_list.extend(args)
save_to_json_file(my_list, filename)
print(load_from_json_file(filename))

