#!/usr/bin/python3
"""
Python script to export employee TODO list data to JSON format
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user_info = requests.get(f'{url}users/{user_id}').json()
    username = user_info['username']
    tasks = requests.get(f'{url}todos?userId={user_id}').json()

    task_list = [
        {
            'task': task['title'],
            'completed': task['completed'],
            'username': username
        }
        for task in tasks
    ]

    with open(f'{user_id}.json', 'w') as f:
        json.dump({user_id: task_list}, f)
