#!/usr/bin/python3
"""
Module Name: 8-json_api.py
Description: Searches for a given letter with POST request to
             http://0.0.0.0:5000/search_user
"""
import sys
import requests

if __name__ == '__main__':
    payload = {}
    payload['q'] = "" if len(sys.argv) == 1 else sys.argv[1]

    res = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json_body = res.json()
    except Exception:
        print("Not a valid JSON")
    else:
        if len(json_body) != 0:
            print(f"[{json_body.get('id')}] {json_body.get('name')}")
        else:
            print("No result")
