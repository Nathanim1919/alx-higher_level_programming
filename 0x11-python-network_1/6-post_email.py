#!/usr/bin/python3
"""
Module Name: 6-post_email.py
Description: a Python script that takes in a URL and an email address,
            `sends a POST request to the passed URL with the email as
            a parameter, and finally displays the body of the response.
"""


import sys
import requests


if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data)
    print(res.text)
