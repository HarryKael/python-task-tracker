#! /usr/local/bin/python3
import sys
from datetime import datetime
from src.json_utilities import JsonUtilitiesRead, JsonUtilitiesWrite

def functionality(method:str, id:int = None, value:str = None):
    read = JsonUtilitiesRead()
    write = JsonUtilitiesWrite()
    if id:
        match(method.lower()):
            case 'delete':
                pass
            case 'mark-in-progress':
                pass
            case 'mark-done':
                pass
            case 'update':
                if value:
                    pass
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
                for d in read.items:
                    print(d)
    else:
        if method.lower() == 'list':
            for d in read.items:
                print(d)

    # ! Close file
    write.close_file()



def main():
    arguments = sys.argv
    id = None
    method = None
    value = None
    if len(arguments) >= 4:
        method = arguments[1]
        id = int(arguments[2])
        value = arguments[3]
    elif len(arguments) <= 3:
        method = arguments[1]
        try:
            value = arguments[2]
        except:pass
    functionality(method, id, value)

main()