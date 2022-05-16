#!/usr/bin/python3

"""
Gather data from an API
"""

from sys import argv
import requests
import json


API_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    userInfo = requests.get("{}/users/{}".format(API_URL, argv[1])).json()
    taskToDo = requests.get("{}/todos?userId={}".
                            format(API_URL, argv[1])).json()
    taskDone = 0
    completedTask = []
    for task in taskToDo:
        if task["completed"]:
            completedTask.append(task)

    print("Employee {} is done with tasks({}/{}):".
          format(userInfo['name'], len(completedTask), len(taskToDo)))

    for task in completedTask:
        print(f"\t{task['title']}")
