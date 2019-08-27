#!/usr/bin/python3
''' a Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8)
'''
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as request:
            print(request.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error Code: {}".format(error.code))
