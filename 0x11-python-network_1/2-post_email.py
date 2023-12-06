#!/usr/bin/python3
"""
Module Name: 2-post_email.py
Description: Sends a POST request to a given URL with email parameter and
             displays the body of the response (decoded in utf-8)
"""
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == '__main__':
    value = {}
    value['email'] = sys.argv[2]
    data = urlencode(value).encode('ascii')
    req = Request(sys.argv[1], data)
    with urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
