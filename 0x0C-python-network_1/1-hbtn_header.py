#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def hbtn_header():
    from urllib.request import Request, urlopen
    from sys import argv
    """gets status of hbtn intranet"""
    request = Request("https://intranet.hbtn.io/status")
    with urlopen(request) as webpage:
        header = webpage.info()
        print(header['X-Request-Id'])


if __name__ == "__main__":
    hbtn_header()
