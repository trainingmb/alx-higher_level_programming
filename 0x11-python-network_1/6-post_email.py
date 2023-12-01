#!/usr/bin/python3
"""
Request Email
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    url = str(argv[1])
    response = requests.put(url, data={'email': argv[2]})
    print(response.text)
