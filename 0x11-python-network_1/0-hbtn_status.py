#!/usr/bin/python3
"""
Uses the urllib module to fetch a webpage.
"""

import urllib.request as req

url_to_fetch = 'https://alx-intranet.hbtn.io/status'

with req.urlopen(url_to_fetch) as response:
    # Reading and decoding the body of the response
    content = response.read()

    # Displaying the body of the response with tabulation
    print("- Body response:")
    print("\t- Type: {}".format(type(content)))
    print("\t- Content: {}".format(content))
    print("\t- UTF-8 Content: {}".format(content.decode('utf-8')))
