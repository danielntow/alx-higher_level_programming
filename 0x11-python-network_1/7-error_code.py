#!/usr/bin/python3
"""check the error code"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code is not requests.code.ok:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
