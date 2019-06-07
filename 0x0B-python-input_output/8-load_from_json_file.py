#!/usr/bin/python3
''' a function that creates an Object from a “JSON file”
'''


def load_from_json_file(filename):
    import json

    with open(filename, 'r') as file:
        return json.load(file)
