#!/usr/bin/python3
"""
Gather data from an API
"""

from requests import get
import sys


def fetch_todo_list_progress(employee_id):
    url = get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    res = url.json()
    name = res['name']

    url = (f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    task_res = get(url)
    tasks = task_res.json()

    total_tasks = len(tasks)
    done_tasks = []
    done = 0
    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print(f"Employee {name} is done with tasks ({done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
