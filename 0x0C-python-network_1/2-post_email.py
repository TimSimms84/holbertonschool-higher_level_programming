#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def hbtn_post():
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from sys import argv
    """gets status of hbtn intranet"""
    email = {'email': argv[2]}
    data = urlencode(email).encode("utf-8")
    request = Request(argv[1], data)
    with urlopen(request) as webpage:
        print(webpage.read().decode("utf-8"))


if __name__ == "__main__":
    hbtn_post()
