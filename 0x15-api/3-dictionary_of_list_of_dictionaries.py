#!/usr/bin/python3
import json
import requests

def fetch_data(url):
    """Fetch data from a given URL."""
    response = requests.get(url)
    return response.json()

def main():
    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch all users
    users = fetch_data(f'{base_url}/users')

    # Dictionary to store all tasks of all employees
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetch all tasks for the current user
        todos = fetch_data(f'{base_url}/todos?userId={user_id}')

        # List to store the tasks in the required format
        user_tasks = []

        for todo in todos:
            task_info = {
                'username': username,
                'task': todo['title'],
                'completed': todo['completed']
            }
            user_tasks.append(task_info)

        # Add the user's tasks to the dictionary
        all_tasks[user_id] = user_tasks

    # Write the dictionary to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

if __name__ == '__main__':
    main()

