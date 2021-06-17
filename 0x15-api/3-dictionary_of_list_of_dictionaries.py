#!/usr/bin/python3
"""This module saves all employees task information to JSON"""


if __name__ == "__main__":
    import json
    import requests

    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    user_info = {}
    users_and_tasks = {}

    for user in users:
        user_info[user['id']] = user['username']

    for task in todos:
        if users_and_tasks.get(task['userId'], False) is False:
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['task'] = task['title']
        task_dict['username'] = user_info[task['userId']]
        task_dict['completed'] = task['completed']

        users_and_tasks[task['userId']].append(task_dict)

    filename = 'todo_all_employees.json'

    with open(filename, 'w') as jsonfile:
        json.dump(users_and_tasks, jsonfile)
