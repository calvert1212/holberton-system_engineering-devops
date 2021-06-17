#!/usr/bin/python3
""" Returns employee progress as formatted string """

import requests
import sys


if __name__ == "__main__":

    c = 0
    task_list = []
    """ Gets the user and task data """
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(argv[1]))

    name = user.json().get('name')
    tasks = todo.json()
    """ Checks if the tasks are completed """
    for task in tasks:
        if task.get('completed') is True:
            c += 1
            task_list.append(task.get('title'))
    """ Prints formated string """
    print('Employee {} is done with tasks({}/{}):'
          .format(name, c, len(tasks)))

    for task in task_list:
        print('\t {}'.format(task))
