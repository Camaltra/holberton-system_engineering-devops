#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Get the numbers of followers from a given subreddit
    """
    if subreddit is None:
        return 0
    URL = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'Holberton User Agent 1.0',
        'From': 'mickael.boillaud@gmail.com'
    }
    data = requests.get(URL, headers=headers).json()
    return data.get("data", {}).get("subscribers", 0)
