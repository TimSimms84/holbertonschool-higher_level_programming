#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def hbtn_header():
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from urllib.error import HTTPError
    from sys import argv
    """gets status of hbtn intranet"""
    request = Request(argv[1])
    try:        
        with urlopen(request) as webpage:
            webpage = webpage.read()
            print(webpage.decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == "__main__":
    hbtn_header()
