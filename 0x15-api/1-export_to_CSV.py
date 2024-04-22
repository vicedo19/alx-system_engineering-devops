#!/usr/bin/python3
"""
Gather data from an API and export it to a CSV file
"""
import csv
from requests import get
from sys import argv


def fetch_and_export_tasks(user_id):
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    tasks = response.json()

    done_tasks = []
    for task in tasks:
        if task['completed']:
            done_tasks.append(task)

    with open({user_id}.csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        for task in done_tasks:
            writer.writerow([user_id, name, task['completed'], task['title']])


if __name__ == '__main__':
    user_id = argv[1]
    fetch_and_export_tasks(user_id)
