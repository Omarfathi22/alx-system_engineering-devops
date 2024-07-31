#!/usr/bin/python3
"""
This script uses the REST API to return information about an employee's TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the script received the correct number of arguments
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url).json()
    employee_name = user_response.get('name')

    # Fetch the TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url).json()

    total_tasks = len(todos_response)
    done_tasks = [task for task in todos_response if task.get('completed') is True]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

