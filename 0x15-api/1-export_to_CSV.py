#!/usr/bin/python3
'''
    Extends Python script from "0-gather_data_from_an_API.py"
    to export data in csv format
'''
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    my_user_url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    todo = 'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id
    employee_response = requests.get(my_user_url)
    employee_data = employee_response.json()
    employee_data = dict(employee_data)
    name = employee_data.get('username')
    todo_response = requests.get(todo)
    todo_data = todo_response.json()
    my_dict = {}
    count = 0
    for item in todo_data:
        my_dict[count] = item
        count += 1
    my_file = employee_id + '.csv'
    big_list = []
    for key, val in my_dict.items():
        my_list = []
        result = val.get('completed')
        my_list.append(employee_id)
        my_list.append(name)
        my_list.append(result)
        my_list.append(val.get('title'))
        big_list.append(my_list)
    with open(my_file, 'w', newline="\n") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(big_list)
