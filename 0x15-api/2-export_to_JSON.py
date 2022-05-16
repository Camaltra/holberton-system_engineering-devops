#!/usr/bin/python3

"""
Gather data from an API and save it to csv file
"""

import csv
import json
import requests
from sys import argv


API_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    userInfo = requests.get("{}/users/{}".format(API_URL, argv[1])).json()
    taskToDo = requests.get("{}/todos?userId={}".
                            format(API_URL, argv[1])).json()
    taskList = []
    for task in taskToDo:
        dictTask = {}
        dictTask["task"] = task["title"]
        dictTask["completed"] = task["completed"]
        dictTask["username"] = userInfo["username"]
        taskList.append(dictTask)
    objJson = {}
    objJson[str(argv[1])] = taskList
    with open("{}.json".format(argv[1]), 'w') as jsonfile:
        json.dump(objJson, jsonfile)
