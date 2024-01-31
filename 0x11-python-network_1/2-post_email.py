#!/usr/bin/python3
"""return the value of a specific header"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    res = urllib.request.Request(url, data)
    with urllib.request.urlopen(res) as response:
        print(response.read().decode('utf-8'))
