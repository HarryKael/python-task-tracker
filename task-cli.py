#! /usr/local/bin/python3
import sys
from datetime import datetime
from src.json_utilities import JsonUtilitiesRead, JsonUtilitiesWrite

def show_task(data):
    print(f'{data[1]['id']} | {data[1]['description']} | {data[1]['status']} | {data[1]['created_at']} | {data[1]['updated_at']}')

def functionality(method:str, id:int = None, value:str = None):
    read = JsonUtilitiesRead()
    write = JsonUtilitiesWrite()
    if id:
        match(method.lower()):
            case 'delete':
                if read.delete_one(id):
                    # ! Save the data
                    write.save_data(read.data)
            case 'mark-in-progress':
                if read.change_status(id, 'In Progress'):
                    # ! Save the data
                    write.save_data(read.data)
            case 'mark-done':
                if read.change_status(id, 'Done'):
                    # ! Save the data
                    write.save_data(read.data)
            case 'update':
                if value:
                    if read.update_one(id, value):
                        # ! Save the data
                        write.save_data(read.data)
    elif value:
        match(method.lower()):
            case 'add':
                data:dict = {
                    'id': None,
                    'description': value,
                    'status': 'ToDo',
                    'created_at': str(datetime.now()),
                    'updated_at': None,
                }
                if read.add_one(data):
                    # ! Save the data
                    write.save_data(read.data)
            case 'list':
                print(f'ID | Description | Status | CreatedAt | UpdateAt')
                for d in read.items:
                    if d[1]['status'].lower() == value.replace('-', ' ').lower():
                        show_task(d)
            case 'path_file':
                try:
                    with open(value, 'x') as f:
                        f.close()
                    print('The file has been created')
                except Exception as e:
                    print(f'There has been an error creating the file\nError: {e}')
    else:
        if method.lower() == 'list':
            print(f'ID | Description | Status | CreatedAt | UpdateAt')
            for d in read.items:
                show_task(d)

    # ! Close file
    if write.f:
        write.close_file()

def main():
    arguments = sys.argv
    id = None
    method = None
    value = None
    if len(arguments) >= 4:
        method = arguments[1]
        id = arguments[2]
        value = arguments[3]
    elif len(arguments) <= 3:
        method = arguments[1]
        try:
            if arguments[2]:
                try:
                    int(arguments[2])
                    id = arguments[2]
                except:
                    value = arguments[2]
        except IndexError:pass
    functionality(method, id, value)

main()