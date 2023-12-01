#!/usr/bin/python3
"""
Interview Question Github API
"""


def printCommits(ujsn, limit=10):
    """
    Print <limit> commit message sha and commiter
    name
    """
    jsn = sorted(ujsn,
                 key=lambda name: name.get('commit').get('author').get('date'),
                 reverse=True)
    i = 0
    if len(jsn) < limit:
        limit = len(jsn)
    while i < limit:
        sha = jsn[i].get('sha')
        date = jsn[i].get('commit').get('author').get('date')
        name = jsn[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
        i += 1


if __name__ == "__main__":
    from sys import argv, exit
    import requests
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2])
    header = {'Accept': 'application/vnd.github+json',
              'X-GitHub-Api-Version': '2022-11-28'}
    data = {'per_page': 10}
    response = requests.get(url, headers=header, data=data)
    if response.status_code == 200 and \
       'application/json' in response.headers.get('Content-Type'):
        jsn = response.json()
        printCommits(jsn)
