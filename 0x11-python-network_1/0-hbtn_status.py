#!/usr/bin/python3

"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        content = response.read()

    print("Body response:")
    print("     - type:", type(content))
    print("     - content:", content)
    print("     - utf8 content:", content.decode('utf-8'))
