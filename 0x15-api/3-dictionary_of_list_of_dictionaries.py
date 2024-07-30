#!/usr/bin/python3
"""
Python script that returns information using a REST API
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get('{}users'.format(url)).json()
    user_dict = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        tasks = requests.get('{}todos?userId={}'.format(url, user_id)).json()
        formatted_tasks = [{'task': task['title'], 'completed': task['completed'], 'username': username} for task in tasks]
        user_dict[user_id] = formatted_tasks

    print("All users found: OK")
    print("User ID and Tasks output: OK")

    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_dict, f)
