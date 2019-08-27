#!/usr/bin/python3
''' a Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter
'''
import requests
import sys


if __name__ == '__main__':

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    response = requests.post(
            'http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        instance = response.json()
        if len(instance) == 0:
            print("No result")
        else:
            print("[{}] {}".format(instance.get('id'), instance.get('name')))
    except Exception:
        print("Not a valid JSON")

