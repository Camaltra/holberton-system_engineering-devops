#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, dictWord={}, after=None):
    """
    Recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit,
    the function should return None
    """
    if subreddit is None:
        print(None)
    URL = f'http://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'Holberton User Agent 1.0',
        'From': 'mickael.boillaud@gmail.com',
    }
    response = requests.get(
        URL,
        headers=headers,
        params={'after': after, 'limit': 100}
    )
    if response.status_code == 404:
        print("")
        return
    data = response.json()
    allHot = data.get("data", {}).get("children", None)
    after = data.get("data", {}).get("after", None)
    for hotPost in allHot:
        title = hotPost.get("data", {}).get("title", "").lower().split()
        for word in word_list.lower().split():
            if word in title:
                if word not in dictWord.keys():
                    dictWord[word] = 1
                else:
                    dictWord[word] += 1
    if after is None:
        if len(dictWord) == 0:
            print("")
        else:
            dictWord = sorted(dictWord.items(), key=lambda kv: (-kv[1], kv[0]))
            for key, value in dictWord:
                print(f'{key}: {value}')
        return
    return count_words(subreddit, word_list, dictWord, after)
