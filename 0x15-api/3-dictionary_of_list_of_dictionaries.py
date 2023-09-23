#!/usr/bin/python3
'''
    Extends Python script from "0-gather_data_from_an_API.py"
    to export all employee data in JSON format
'''
import json
import requests


if __name__ == "__main__":
    my_user_url = 'https://jsonplaceholder.typicode.com/users'
    employee_response = requests.get(my_user_url)
    employee_data = employee_response.json()
    final_dict = {}
    my_dict = {}
    for g in employee_data:
        todo = 'https://jsonplaceholder.typicode.com/todos?userId='
        todo = todo + str(g.get('id'))
        todo_response = requests.get(todo)
        todo_data = todo_response.json()
        the_list = []
        for i in todo_data:
            my_dict = {}
            if i['userId'] == g.get('id'):
                my_dict['task'] = i.get('title')
                my_dict['completed'] = i.get('completed')
                my_dict['username'] = g.get('username')
                the_list.append(my_dict)
                final_dict[g.get('id')] = the_list
    my_file = 'todo_all_employees.json'
    with open(my_file, 'w') as f:
        json_obj = json.dumps(final_dict)
        f.write(json_obj)
