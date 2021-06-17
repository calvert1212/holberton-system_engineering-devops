!/usr/bin/python3
"""This module saves employee task information to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
               .format(argv[1])
    user_dict = {}

    user = requests.get(user_url)
    todo = requests.get(todo_url)

    name = user.json().get('username')
    tasks = todo.json()

    user_dict[argv[1]] = []

    for task in tasks:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['username'] = name
        task_dict['completed'] = task.get('completed')
        user_dict[argv[1]].append(task_dict)

    filename = '{}.json'.format(argv[1])

    with open(filename, 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
