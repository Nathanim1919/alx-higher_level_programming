#!/usr/bin/python3
"""
Module Name: 8-json_api.py
Description: a Python script that takes in a letter
            `and sends a POST request to http://0.0.0.0:5000/search_user
            `with the letter as a parameter.
"""

import requests
import sys


if _name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': sys.argv[1])
    if (!sys.argv[1]):
        data.q = ""

    res = requests.post(url, data)
    try:
        json_body = res.json()
    except Exception:
        print("Not a valid JSON")
    else:
        if len(json_body) != 0:
            print(f"[{json_body.get('id')}] {json_body.get('name')}")
        else:
            print("No results")
