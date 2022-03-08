#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def gethib_creds():
    """"""
    from requests import get
    from requests.auth import HTTPBasicAuth
    from sys import argv
    requests = get('https://api.github.com/users/{}'.format(argv[1]),
                   auth=HTTPBasicAuth(argv[1], argv[2]))
    print(requests.json().get('id'))


if __name__ == "__main__":
    gethib_creds()
