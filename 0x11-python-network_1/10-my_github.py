#!/usr/bin/python3
"""
Module Name:  a Python script that takes your GitHub credentials
            `(username and password) and uses the GitHub API to
            `display your id
"""


import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    auth = HTTPBasicAuth(username, passwd)
    res = requests.get('https://api.github.com/user', auth=auth)

    print(res.json().get('id'))
