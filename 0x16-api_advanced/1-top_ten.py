#!/usr/bin/python3

"""
Python file 0x16 - API Advenced
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    if subreddit is None:
        print(None)
    URL = f'http://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'Holberton User Agent 1.0',
        'From': 'mickael.boillaud@gmail.com',
    }
    response = requests.get(URL, headers=headers, params={'limit': 10})
    if response.status_code == 404:
        print(None)
        return
    data = response.json()
    allHot = data.get("data", {}).get("children", None)
    if allHot is None or len(allHot) <= 0 or allHot[0].get('kind') != 't3':
        print(None)
    for title in allHot:
        print(title.get("data", {}).get("title", ""))
