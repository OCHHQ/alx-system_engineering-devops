#!/usr/bin/python3

"""
Python script that returns information using a REST API
"""

import requests
import sys


def fetch_employee_data(user_id):
    """
    Fetch employee data and TODO list from the API.

    :param user_id: ID of the employee
    :return: Tuple containing employee name, number of completed tasks,
             total tasks, and titles of completed tasks
    """
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_info = requests.get(f'{url}users/{user_id}')
    if user_info.status_code != 200:
        print("User ID not found.")
        sys.exit(1)

    user_info = user_info.json()
    employee_name = user_info.get('name')

    # Fetch todos data
    all_tasks = requests.get(f'{url}todos?userId={user_id}').json()

    # Get total number of tasks
    total_tasks = len(all_tasks)

    # Get completed tasks
    completed_tasks = [task for task in all_tasks if task.get('completed')]

    return (
        employee_name,
        len(completed_tasks),
        total_tasks,
        completed_tasks
    )


if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    # Check if the provided employee ID is an integer
    try:
        user_id = int(user_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Fetch employee data and TODO list progress
    (
        employee_name,
        done_tasks_count,
        total_tasks,
        done_tasks
    ) = fetch_employee_data(user_id)

    # Print employee's TODO list progress
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            done_tasks_count,
            total_tasks
        )
    )

    # Print titles of completed tasks
    for task in done_tasks:
        print("\t{}".format(task.get('title')))
