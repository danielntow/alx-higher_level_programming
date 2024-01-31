#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}

    response = requests.post(url, values)

    try:
        if (len(response.json()) > 0):
            print('[{}] {}'.format(response.json()
                  ['id'], response.json()['name']))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
