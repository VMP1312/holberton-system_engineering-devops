#!/usr/bin/python3
"""
Returns information using a REST API.
"""

import requests
from sys import argv
import csv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    users = requests.get('{}/users/{}'.format(url, user_id)).json()
    todos = requests.get('{}/users/{}/todos'.format(url, user_id)).json()
    name = users.get('username')

    with open('{}.csv'.format(user_id), 'w', newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for mv in todos:
            w.writerow([
                int(user_id),
                name,
                mv.get('completed'),
                mv.get('title')
            ])
