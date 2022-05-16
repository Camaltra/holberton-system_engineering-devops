#!/usr/bin/python3

"""
Gather data from an API
"""

import requests
from sys import argv


API_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    userInfo = requests.get("{}/users/{}".format(API_URL, argv[1])).json()
    taskToDo = requests.get("{}/todos?userId={}".
                            format(API_URL, argv[1])).json()
    completedTask = []
    for task in taskToDo:
        if task["completed"]:
            completedTask.append(task['title'])

    print("Employee {} is done with tasks({}/{}):".
          format(userInfo['name'], len(completedTask), len(taskToDo)))

    print("\n".join("\t {}".format(task) for task in completedTask))
