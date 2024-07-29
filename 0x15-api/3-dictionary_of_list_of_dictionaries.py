#!/usr/bin/python3
"""
This script fetches data from a REST API and saves it to a JSON file.
It exports all employees' tasks in a JSON format.
"""
import json
import requests


def fetch_data():
    """Fetches user and task data from the REST API"""
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    return users, todos


def format_data(users, todos):
    """Formats data into a dictionary of lists of dictionaries"""
    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [task for task in todos if task['userId'] == user_id]
        tasks_list = [{
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        } for task in user_tasks]
        data[user_id] = tasks_list

    return data


def save_to_json(data, filename='todo_all_employees.json'):
    """Saves the data to a JSON file"""
    with open(filename, 'w') as file:
        json.dump(data, file)


def main():
    """Main function"""
    users, todos = fetch_data()
    data = format_data(users, todos)
    save_to_json(data)


if __name__ == "__main__":
    main()
