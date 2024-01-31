#!/usr/bin/python3
"""
Script documentation: Fetches the status from
https://alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        # Reading and decoding the body of the response
        content = response.read().decode('utf-8')

        # Displaying the body of the response with tabulation
        print("- Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print('\t- utf8 content: {}'.format(content))
