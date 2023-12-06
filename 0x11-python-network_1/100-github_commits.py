#!/usr/bin/python3
"""
Module Name: 100-github_commits.py
Description: Lists 10 most recent GitHub commits of the repository "rails"
"""
import sys
import requests


if __name__ == '__main__':
    repo, owner = sys.argv[1:]
    res = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
    json_data = res.json()[:10]
    for commit in json_data:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
