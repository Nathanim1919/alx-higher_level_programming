#!/usr/bin/python3

"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()

    print("Body response:")
    print("     - type:", type(content))
    print("     - content:", content)
    print("     - utf8 content:", content.decode('utf-8'))
