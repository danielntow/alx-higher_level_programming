#!/usr/bin/python3
"""
Script documentation: Fetches the status from
https://alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request


def fetch_status(url):
    """
    Fetches the status from the specified URL using urllib.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the response.
    """
    with urllib.request.urlopen(url) as response:
        # Reading and decoding the body of the response
        content = response.read().decode('utf-8')
        return content


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    status_content = fetch_status(url)

    # Displaying the body of the response with tabulation
    print("- Body response:")
    print("\t- type: {}".format(type(status_content)))
    print("\t- content: {}".format(status_content))
    print('\t- utf8 content: {}'.format(status_content))
