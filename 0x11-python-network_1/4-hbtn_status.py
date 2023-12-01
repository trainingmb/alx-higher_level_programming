#!/usr/bin/python3
"""
Request only please
"""


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    import requests
    response = requests.get(url)
    print("Body Response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
