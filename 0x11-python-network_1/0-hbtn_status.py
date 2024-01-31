#!/usr/bin/python3
"""
Script documentation: Fetches the status from
https://alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request


def fetch_status(url):
    with urllib.request.urlopen(url) as response:
        # Reading and decoding the body of the response
        content = response.read().decode('utf-8')

        # Displaying the body of the response with tabulation
        print("- Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))


if __name__ == "__main__":
    # URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # Calling the function to fetch and display the status
    fetch_status(url)
