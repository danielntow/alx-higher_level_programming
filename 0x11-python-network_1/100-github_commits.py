#!/usr/bin/python3
"""
GitHub API Script: List 10 most recent commits of a repository.
"""
import requests
from sys import argv

if __name__ == "__main__":
    # Extracting command line arguments
    repository_name = argv[1]
    owner_name = argv[2]

    # GitHub API endpoint for commits
    api_url = f"https://api.github.com/repos/{
        owner_name}/{repository_name}/commits"

    # Sending GET request to GitHub API
    response = requests.get(api_url)
    # Raise an exception for HTTP errors (4xx or 5xx)
    response.raise_for_status()

    # Extracting and printing the 10 most recent commits
    commits = response.json()[:10]
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
