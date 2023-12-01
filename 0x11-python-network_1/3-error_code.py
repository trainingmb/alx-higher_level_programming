#!/usr/bin/python3
"""
Error code #0
"""


if __name__ == "__main__":
    from sys import argv, exit
    if len(argv) < 2:
        exit()
    url = str(argv[1])
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from urllib.error import HTTPError
    try:
        with urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print('Error code:', e.code)
