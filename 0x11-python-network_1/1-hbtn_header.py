#!/usr/bin/python3
"""
Response header value #0
"""


if __name__ == "__main__":
    from sys import argv, exit
    if len(argv) < 2:
        exit()
    url = str(argv[1])
    from urllib.request import urlopen
    with urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
