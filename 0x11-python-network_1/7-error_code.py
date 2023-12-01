#!/usr/bin/python3
"""
Request Error Eroor
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    url = str(argv[1])
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
