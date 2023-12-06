#!/usr/bin/python3
"""
Module Name: 4-hbtn_status.py
Description: Write a Python script that fetches
            `https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(res.text))
    print("\t- content:", res.text)
