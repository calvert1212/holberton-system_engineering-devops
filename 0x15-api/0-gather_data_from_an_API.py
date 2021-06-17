#!/usr/bin/python3
"""using REST API"""
import requests
import sys
def get_employee_tasks(employeeId):
    """get employee data"""
    name = ''
    task_list = []
    c = 0
    user = "https://jsonplaceholder.typicode.com/users/"
    todo = "https://jsonplaceholder.typicode.com/users/"
    userRes = requests.get("{}{}".format(user, employeeId))
    todosRes = requests.get("{}{}/todos".format(todo, employeeId))
    name = userRes.json().get('name')
    todosJson = todosRes.json()
    for task in todosJson:
        if task.get('completed') is True:
            c += 1
            task_list.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, c, len(todosJson)))
    for title in task_list:
        print("\t {}".format(title))
    return 0
if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
