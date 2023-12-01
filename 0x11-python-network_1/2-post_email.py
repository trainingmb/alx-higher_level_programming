#!/usr/bin/python3
"""
POST an email #0
"""


if __name__ == "__main__":
    from sys import argv, exit
    if len(argv) < 3:
        exit()
    url = str(argv[1])
    values = {'email': str(argv[2])}
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    data = urlencode(values).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
