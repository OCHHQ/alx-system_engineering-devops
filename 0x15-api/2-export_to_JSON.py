#!/usr/bin/python3

"""
Python script to export employee TODO list data to JSON format
"""

import json
import requests
import sys


def fetch_data(user_id):
    """Fetch user and tasks data from API"""
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f'{url}users/{user_id}').json()
    tasks = requests.get(f'{url}todos?userId={user_id}').json()
    return user['username'], [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        }
        for task in tasks
    ]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = sys.argv[1]
    username, tasks = fetch_data(user_id)

with open(f'{user_id}.json', 'w', encoding='utf-8') as file:
    json.dump({user_id: tasks}, file, indent=4)
