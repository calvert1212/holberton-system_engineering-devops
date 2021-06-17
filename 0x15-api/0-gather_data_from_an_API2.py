#!/usr/bin/python3
"""This module returns employee task information"""
import requests
from sys import argv


if __name__ == "__main__":

    count = 0
    task_list = []

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(argv[1]))

    name = user.json().get('name')
    tasks = todo.json()

    for task in tasks:
        if task.get('completed') is True:
            count += 1
            task_list.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name, count, len(tasks)))

    for task in task_list:
        print('\t {}'.format(task))
