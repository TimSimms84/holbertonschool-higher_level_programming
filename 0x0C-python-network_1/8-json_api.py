#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


def json_api():
    """"""
    from requests import get, post
    from sys import argv
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    site = 'http://0.0.0.0:5000/search_user'
    request = post(site, data={'q': q})
    try:
        dic = request.json()
        id = dic.get('id')
        name = dic.get('name')
        if len(dic) == 0 or not id or not name:
            print("No Results")
        else:
            print("[{}] {}".format(name, id))

    except:
        print("Not a valid JSON")

if __name__ == "__main__":
    json_api()
