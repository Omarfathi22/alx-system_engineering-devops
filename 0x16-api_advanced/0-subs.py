#!/usr/bin/python3
"""
0-subs - Queries the Reddit API to return the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {'User-Agent': u_agent}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return "OK" if res.status_code == 404 else 0

    data = res.json().get('data', {})
    return data.get('subscribers', 0)


