#!/usr/bin/python3
''' a Python script that fetches https://intranet.hbtn.io/status
'''
import requests


response = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
