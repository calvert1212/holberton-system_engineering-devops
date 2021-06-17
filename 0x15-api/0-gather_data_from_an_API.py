#!/usr/bin/python3
""" Returns info about given employee for TODO list"""


if __name__ == "__main__":

    import requests
    import sys
    user = 'https://jsonplaceholder.typicode.com/users/'
    todo = 'https://jsonplaceholder.typicode.com/todos/'
    """ Get data """
    if len(argv) > 1:
        todo_dict = requests.get(todo, params={"userId": argv[1]}).json()
        user_dict = requests.get(user, params={"id": argv[1]}).json()
        EMPLOYEE_NAME = user_dict[0].get("name")
    TOTAL_NUMBER_OF_TASKS = len(todo_dict)
    NUMBER_OF_DONE_TASKS = 0
    """ Count done tasks """
    for dic in todo_dict:
        if dic["completed"] is True:
            NUMBER_OF_DONE_TASKS += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for dic in todo_dict:
        if dic["completed"] is True:
            print("\t {}".format(dic["title"]))
