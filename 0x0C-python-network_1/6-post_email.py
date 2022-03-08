#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def hbtn_post2():
    """"""
    from requests import post
    from sys import argv
    email = {"email": argv[2]}
    request = post(argv[1], email)
    print(request.text)

if __name__ == "__main__":
    hbtn_post2()
