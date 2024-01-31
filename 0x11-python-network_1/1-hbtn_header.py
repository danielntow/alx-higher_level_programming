#!/usr/bin/python3
"""
Uses the urllib and sys modules to send a request to a URL and display the X-Request-Id value.
"""

import urllib.request as req
import sys

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url_to_fetch = sys.argv[1]

    try:
        # Sending a request to the specified URL
        with req.urlopen(url_to_fetch) as response:
            # Checking if the 'X-Request-Id' header is present
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(x_request_id)
            else:
                print("X-Request-Id not found in the response headers.")
    except Exception as e:
        print("Error:", e)
