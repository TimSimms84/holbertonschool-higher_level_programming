#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def hbtn_header():
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from sys import argv
    """gets status of hbtn intranet"""
    request = Request(argv[1], data)
    with urlopen(request) as webpage:
        print(webpage.read().decode("utf-8"))


if __name__ == "__main__":
    hbtn_header()
