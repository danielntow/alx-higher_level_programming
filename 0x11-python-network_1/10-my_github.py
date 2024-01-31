#!/usr/bin/python3
"""
GitHub API Script: Display user id using Basic Authentication.
"""
import requests
from sys import argv

if __name__ == "__main__":
    # Extracting command line arguments
    username = argv[1]
    password = argv[2]

    # GitHub API endpoint for authenticated user
    api_url = "https://api.github.com/user"

    # Sending GET request to GitHub API with Basic Authentication
    response = requests.get(api_url, auth=(username, password))

    # Raise an exception for HTTP errors (4xx or 5xx)
    response.raise_for_status()

    # Extracting and printing the user id
    user_id = response.json().get('id')
    print(f"User ID: {user_id}")
