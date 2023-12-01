#!/usr/bin/python3
"""
Request Reposnse header
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    url = str(argv[1])
    response = requests.get(url)
    print(response.headers.get("X-Request-id"))
