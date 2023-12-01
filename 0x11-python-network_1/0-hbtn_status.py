#!/usr/bin/python3
"""
Fetch Alx page
"""


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    the_page = ""
    from urllib.request import urlopen
    with urlopen(url) as response:
        the_page = response.read()
        print("Body Response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode('utf8')))
