#!/usr/bin/python3
"""
0-subs - Queries the Reddit API to return the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    headers = {'User-Agent': 'my-reddit-api'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        elif response.status_code == 302:  # Handle redirect
            return 0
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0

