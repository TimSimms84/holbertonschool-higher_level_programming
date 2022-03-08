#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def hbtn_header2():
    """"""
    from requests import get
    from sys import argv
    request = get(argv[1])
    print(request.headers.get('X-Request-Id'))

if __name__ == "__main__":
    hbtn_header2()
