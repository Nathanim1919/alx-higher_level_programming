#!/usr/bin/python3
"""
Module Name: 3-error_code.py
Description: Sends a request to a URL and displays the body of the response
             decoded in `utf-8`
"""
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

if __name__ == '__main__':
    req = Request(sys.argv[1])

    try:
        with urlopen(req) as response:
            body = response.read().decode('utf-8')
    except HTTPError as e:
        print('Error code:', e.code)
    else:
        print(body)
