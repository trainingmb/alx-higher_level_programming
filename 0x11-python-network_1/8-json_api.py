#!/usr/bin/python3
"""
Search API
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    value = ""
    if len(argv) > 1:
        value = str(argv[1])
    response = requests.post(url, data={'q': value})
    if response.headers.get('content-type') == 'application/json':
        jsn = response.json()
        if jsn.get('id') is None:
            print("No result")
        else:
            print("[{}] {}".format(jsn.get('id'),
                                   jsn.get('name')))
    else:
        print("Not a valid Json")
