#!/usr/bin/python3
"""
This script uses a REST API to return information
about an employee's TODO list progress and
exports the data in CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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

    employee_name = employee_data.get('username')

    # Create CSV filename
    filename = f"{employee_id}.csv"

    # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks_data:
            writer.writerow([
                employee_id,
                employee_name,
                task.get('completed'),
                task.get('title')
            ])

    print(f"Data exported to {filename}")
