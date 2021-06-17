#!/usr/bin/python3
""" Script to save employee task information to CSV"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    all_tasks = []
    """ Get user and task info """
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(argv[1]))
    """ Set variables """
    name = user.json().get('username')
    tasks = todo.json()
    """ Loop to create array of rows and append data """
    for task in tasks:
        task_row = []
        task_row.append(argv[1])
        task_row.append(name)
        task_row.append(task.get('completed'))
        task_row.append(task.get('title'))
        """ Appends row to the tasks list """
        all_tasks.append(task_row)

    f = '{}.csv'.format(argv[1])

    with open(f, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(all_tasks)
