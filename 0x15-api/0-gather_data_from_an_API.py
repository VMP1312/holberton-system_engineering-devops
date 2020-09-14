#!/usr/bin/python3
"""
Returns information using a REST API.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    users = requests.get('{}/users/{}'.format(url, user_id)).json()
    todos = requests.get('{}/users/{}/todos'.format(url, user_id)).json()
    name = users.get('name')

    tasks_done = []
    for mv in todos:
        if mv.get('completed') is True:
            tasks_done.append(mv.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(tasks_done), len(todos)))

    for mv in tasks_done:
        print('\t {}'.format(mv))
