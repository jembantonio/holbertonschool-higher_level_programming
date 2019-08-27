#!/usr/bin/python3
''' a Python script that takes your Github credentials (username and password)
    and uses the Github API to display your id
'''
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=HTTPBasicAuth(usr, pwd))

    results = response.json()
    print(results.get('id'))
