#!/usr/bin/python3
"""return a header value"""
import requests
import sys
if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if 'X-Request-Id' in req.headers:
        print("{}".format(req.headers['X-Request-Id']))
