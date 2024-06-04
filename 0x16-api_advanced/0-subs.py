#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 125.0.6422.142"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 300:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
