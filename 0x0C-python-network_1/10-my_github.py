#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def gethib_creds():
    """"""
    from requests import get
    from requests.auth import HTTPBasicAuth
    from sys import argv
    requests = get('https://api.github.com/user',
                   auth=HTTPBasicAuth(argv[1], argv[2])).json()
    print(requests.get('id'))


if __name__ == "__main__":
    gethib_creds()
