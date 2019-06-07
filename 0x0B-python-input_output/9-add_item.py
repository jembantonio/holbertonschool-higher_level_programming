#!/usr/bin/python3
''' a script that adds all arguments to a Python list
and then save them to a file
'''


import sys
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

items = []

try:
    items = load_from_json_file("add_item.json")

except FileNotFoundError:
    pass

finally:
    for args in sys.argv[1:]:
        items.append(args)
    save_to_json_file(items, "add_item.json")
