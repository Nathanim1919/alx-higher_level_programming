#!/usr/bin/python3
"""
Module Name: 1-hbtn_header.py
Description: sends a request to the URL and displays the value of the
            `X-Request-Id variable found in the header of the response.
"""

from urllib.request import Request, urlopen
import sys

if __name__ == '__main__':
    req = Request(sys.argv[1])
    with urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
