#!/usr/bin/python3
"""
Module Name: 3-error_code.py
Description: a Python script that takes in a URL, sends a request to
            `the URL and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            body = response.read().decode('utf-8')
    except HTTPError as e:
        print('Error code: ', e.code)
    else:
        print(body)
