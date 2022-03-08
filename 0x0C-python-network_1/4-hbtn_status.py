#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def hbtn_status():
    """"""
    from requests import get
    request = get("https://intranet.hbtn.io/status")
    text = request.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))


if __name__ == "__main__":
    hbtn_status()
