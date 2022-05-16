#!/usr/bin/python3

"""
Gather data from an API and save it to csv file
"""

from sys import argv
import requests
import json
import csv


API_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    objJson = {}
    for i in range(1, 11):
        userInfo = requests.get("{}/users/{}".format(API_URL, i)).json()
        taskToDo = requests.get("{}/todos?userId={}".format(API_URL, i)).json()
        taskList = []
        for task in taskToDo:
            dictTask = {}
            dictTask["task"] = task["title"]
            dictTask["completed"] = task["completed"]
            dictTask["username"] = userInfo["name"]
            taskList.append(dictTask)
        objJson[str(i)] = taskList
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(objJson, jsonfile)
