#!/usr/bin/python3
"""
Fetch Alx page
"""

import urllib.request as r

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    the_page = ""
    with r.urlopen(url) as response:
        the_page = response.read()
        print("Body Response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        if 'utf-8' in response.info().get_charsets():
            print("\t- utf8 content: OK")
