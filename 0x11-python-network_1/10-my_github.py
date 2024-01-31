#!/usr/bin/python3
"""
GitHub API Script: Display GitHub user id using Basic Authentication.
"""
import requests
from sys import argv

if __name__ == "__main__":
    # Extracting command line arguments
    username = argv[1]
    password = argv[2]

    # GitHub API endpoint for user information
    api_url = "https://api.github.com/user"

    # Creating a session with Basic Authentication
    session = requests.Session()
    session.auth = (username, password)

    try:
        # Sending GET request to GitHub API for user information
        response = session.get(api_url)
        # Raise an exception for HTTP errors (4xx or 5xx)
        response.raise_for_status()

        # Extracting and printing the user id
        user_id = response.json().get('id')
        print(f"{user_id}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
