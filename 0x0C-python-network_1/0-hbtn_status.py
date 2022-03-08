#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def hbtn_status():
    request = Request("https://intranet.hbtn.io/status")
    with urlopen(request) as webpage:
        webpage = webpage.read()
        print("Body response:")
        print("\t- type: {}".format(type(webpage)))
        print("\t- content: {}".format(webpage))
        print("\t- utf8 content: {}".format(webpage.decode('utf8'))


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    hbtn_status()
