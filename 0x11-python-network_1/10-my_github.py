#!/usr/bin/python3
"""
Github API
"""


if __name__ == "__main__":
    from sys import argv, exit
    import requests
    url = "https://api.github.com/users/{}".format(argv[1])
    header = {'Accept': 'application/vnd.github+json',
              'X-GitHub-Api-Version': '2022-11-28',
              'Authorization': 'Bearer {}'.format(str(argv[2]))}
    response = requests.get(url, headers=header)
    if response.status_code == 200 and \
       'application/json' in response.headers.get('Content-Type'):
        jsn = response.json()
        if jsn.get('id') is not None:
            print(jsn.get('id'))
            exit()
    print("None")
