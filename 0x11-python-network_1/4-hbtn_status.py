#!/usr/bin/python3
"""
Script documentation: Fetches the status from
https://alx-intranet.hbtn.io/status using the requests package.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Sending a GET request to the specified URL
    response = requests.get(url)
    # Raise an exception for HTTP errors (4xx or 5xx)
    response.raise_for_status()

    # Displaying the body of the response with tabulation
    print("- Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
