#!/usr/bin/python3
"""
This script uses a REST API to return information about an employee's TODO list progress
and export the data in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    
    # Fetch employee's tasks
    tasks_url = f"{base_url}/todos?userId={employee_id}"
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()
    
    employee_username = employee_data.get('username')
    
    # Create JSON data structure
    tasks_list = []
    for task in tasks_data:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_username
        }
        tasks_list.append(task_dict)
    
    json_data = {str(employee_id): tasks_list}
    
    # Create JSON filename
    filename = f"{employee_id}.json"
    
    # Write data to JSON file
    with open(filename, mode='w') as file:
        json.dump(json_data, file)
    
    print(f"Data exported to {filename}")

