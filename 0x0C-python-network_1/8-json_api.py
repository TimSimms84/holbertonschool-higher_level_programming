#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


from distutils.log import error
from logging import exception


def json_api():
    """"""
    from requests import get, post
    from sys import argv
    if len(argv) <= 1:
        q = ""
    elif len(argv) == 2:
        q = argv[1]
    request = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = request.json()
        id = dic.get('id')
        name = dic.get('name')
        if len(dic) == 0 or not id or not name:
            print("No Results")
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))

    except:
        print("Not a valid JSON")

if __name__ == "__main__":
    json_api()
