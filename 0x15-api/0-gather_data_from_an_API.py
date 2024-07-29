#!/usr/bin/python3
"""
This script uses a REST API to return
information about an employee's TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
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
    
    employee_name = employee_data.get('name')
    total_tasks = len(tasks_data)
    done_tasks = [task for task in tasks_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)
    
    # Print employee TODO list progress
    print(f"Employee {employee_name} is 
            done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

