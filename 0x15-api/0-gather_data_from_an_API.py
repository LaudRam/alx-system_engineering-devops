#!/usr/bin/python3
'''Returns info about employee todo list progress'''
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    my_user_url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    todo = 'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id
    employee_response = requests.get(my_user_url)
    employee_data = employee_response.json()
    name = employee_data.get('name')
    todo_response = requests.get(todo)
    todo_data = todo_response.json()
    final_count = 0
    count = 0
    my_text = []
    for item in todo_data:
        if item.get('completed') is True:
            my_text.append(item.get('title'))
            count += 1
        final_count += 1
    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          count,
                                                          final_count))
    for i in my_text:
        print('\t {}'.format(i))
