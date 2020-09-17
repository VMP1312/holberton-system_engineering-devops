#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko; Google Web Preview) \
            Chrome/27.0.1453 Safari/537.36"
    headers = {"User-Agent": agent}
    req = requests.get(url, allow_redirects=False,
                       headers=headers)

    if str(req) == "<Response [200]>":
        data_json = req.json()
        return data_json.get("data").get("subscribers")
    return 0
