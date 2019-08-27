#!/usr/bin/python3
''' a Python script that takes in a string and sends a search request to the
    Star Wars API
'''
import requests
import sys


if __name__ == '__main__':

    response = requests.get(
            'https://swapi.co/api/people/?search=' + sys.argv[1])
    swapi_json = response.json()
    num_result = swapi_json.get('count')
    results = swapi_json.get('results')

    print("Number of results: {}".format(num_result))

    for name in results:
        print("{}".format(name.get('name')))
    
