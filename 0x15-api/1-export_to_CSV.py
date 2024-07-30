#!/usr/bin/python3

"""
Python script to export employee TODO list data to CSV format
"""
import csv
import requests
import sys


def fetch_data(user_id):
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f'{url}users/{user_id}').json()
    tasks = requests.get(f'{url}todos?userId={user_id}').json()
    return user['username'], [
        (user_id, user['username'], task['completed'], task['title'])
        for task in tasks
    ]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = sys.argv[1]
    username, tasks = fetch_data(user_id)

    with open(f'{user_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks)
