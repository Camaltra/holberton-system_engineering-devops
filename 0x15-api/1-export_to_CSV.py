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
    userInfo = requests.get("{}/users/{}".format(API_URL, argv[1])).json()
    taskToDo = requests.get("{}/todos?userId={}".
                            format(API_URL, argv[1])).json()
    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in taskToDo:
            writer.writerow(['{}'.format(int(argv[1])),
                             userInfo['username'],
                             task['completed'],
                             task['title']])
