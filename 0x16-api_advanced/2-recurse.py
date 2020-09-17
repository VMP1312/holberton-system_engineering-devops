#!/usr/bin/python3
"""
Recursive function that queries the Reddit API.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    if after is None:
        return []

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    if after:
        url += '?after={}'.format(after)

    req = requests.get(url, headers=headers, allow_redirects=False)

    if str(req) != '<Response [200]>':
        return(None)
    Json_out = req.json()

    post = Json_out.get('data').get('children')

    for mv in post:
        hotlst.append(mv.get('data').get('title'))
    return hotlst + recurse(subreddit, [], Json_out.get('data').get('after'))
