#!/usr/bin/python3
"""
Returns information using a REST API.
"""

import requests
from sys import argv
import json

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    users = requests.get('{}/users/{}'.format(url, user_id)).json()
    todos = requests.get('{}/users/{}/todos'.format(url, user_id)).json()
    name = users.get('username')

    task_list = []
    for mv in todos:
        task_dic = {}
        task_dic['task'] = mv.get('title')
        task_dic['completed'] = mv.get('completed')
        task_dic['username'] = name
        task_list.append(task_dic)

    full_json = {}
    full_json[user_id] = task_list
    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump(full_json, jsonfile)
