#!/usr/bin/python3
"""A script that lists the 10 most recent commits of a given repository
by a given owner on GitHub.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
           sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
