import json
import requests

def fetch_data():
    # Fetch users
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    # Fetch todos
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos_response.json()

    return users, todos

def create_data_structure(users, todos):
    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = []

        for todo in todos:
            if todo['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks.append(task_info)

        data[user_id] = user_tasks

    return data

def export_to_json(data):
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)

def main():
    users, todos = fetch_data()
    data = create_data_structure(users, todos)
    export_to_json(data)

if __name__ == '__main__':
    main()

