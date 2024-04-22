#!/usr/bin/python3
"""Extend you Python script to csv format"""
import csv
from requests import get
from sys import argv


if __name__ == '__main__':
    USER_ID = argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    response = get(url)
    USERNAME = response.json().get('username')

    url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}/todos"
    response = get(url)
    tasks = response.json()

    with open(f"{USER_ID}.csv", 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(USER_ID, USERNAME, task['completed']),
                       task['title'])
