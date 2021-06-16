#!/usr/bin/python3
""" gathers data from API """

# Uses REST API for given employee ID,
# returns information about his/her TODO list progress.

import requests
import sys

def get_employee_tasks(employeeId):
    """ class for getting employee tasks """
    name = ''
    task_list = []
    completed_counter = 0

    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employeeId))

    """ Get JSON """
    name = userRes.json().get('name')
    todosJson = todosRes.json()

    for task in todosJson:
        if task.get('completed') is True:
            completed_counter += 1
            task_list.append(task.get('title'))

    """ Prints formatted string given JSON data """
    print("Employee {} is done with tasks ({}/{}):".format(name, completed_counter, len(todosJson)))
    for title in task_list:
        print("\t {}".format(title))

    return

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
