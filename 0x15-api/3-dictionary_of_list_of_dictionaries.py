#!/usr/bin/python3
"""
Returns information using a REST API.
"""

import requests
from sys import argv
import json

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user_dic = {}
    username_dic = {}

    for usermv in users:
        user_id = usermv.get('id')
        user_dic[user_id] = []
        username_dic[user_id] = usermv.get('username')

    for mv in todos:
        task_dic = {}
        user_id = mv.get('userId')
        task_dic['task'] = mv.get('title')
        task_dic['completed'] = mv.get('completed')
        task_dic['username'] = username_dic.get(user_id)
        user_dic.get(user_id).append(task_dic)

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_dic, jsonfile)
