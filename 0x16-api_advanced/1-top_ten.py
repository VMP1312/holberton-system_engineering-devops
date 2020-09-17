#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    if subreddit is None or type(subreddit) is not str:
        print(None)

    url = 'https://www.reddit.com/r/{}/hot.json'
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) \
         AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) \
              Chrome/27.0.1453 Safari/537.36"}

    req = requests.get(url.format(subreddit), headers=headers,
                       params={'limit': 10}, allow_redirects=False)

    if str(req) != '<Response [200]>':
        print(None)
    else:
        json_out = req.json()
        TenPosts = json_out.get('data', {}).get('children', None)
        for post in TenPosts:
            print(post.get('data', {}).get('title', None))
