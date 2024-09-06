import json
from datetime import datetime
import os

def get_current_dir() -> str:
    return os.path.dirname(os.path.realpath(__file__))

class JsonUtilitiesRead():
    file_path = ''
    current_dir = get_current_dir()
    f = None
    data:dict = {}
    items = None
    next_id:int = 1

    def add_one(self, data) -> bool:
        """Add one task to the list"""
        try:
            data['id'] = self.next_id
            self.data[self.next_id] = data
            print(f'Task added successfully (ID: {self.next_id})')
            return True
        except Exception as e:
            print(f'------- Error: {e}')
            return False
    
    def update_one(self, id, value) -> bool:
        """Update one task to the list"""
        try:
            self.data[id]['description'] = value
            self.data[id]['updated_at'] = str(datetime.now())
            return True
        except Exception as e:
            print(f'------- Error: {e}')
            return False
    
    def change_status(self, id, status) -> bool:
        """Update one task to the list"""
        try:
            self.data[id]['status'] = status
            self.data[id]['updated_at'] = str(datetime.now())
            return True
        except Exception as e:
            print(f'------- Error: {e}')
            return False
    
    def delete_one(self, id) -> bool:
        """Add one task to the list"""
        try:
            self.data.pop(id)
            return True
        except Exception as e:
            print(f'------- Error: {e}')
            return False

    def get_next_id(self) -> int:
        """Method for getting the next id for the tasks"""
        self.items = list(self.data.items())
        if len(self.items):
            self.next_id = int(self.items[-1][0]) + 1

    def get_file_path(self) -> str | None:
        with open(f'{self.current_dir}/file_path.txt', 'r') as f:
            self.file_path = f.read().strip()
            f.close()
        if not len(self.file_path) > 0:
            raise Exception('You haven\'t setted the file path for the tasks')

    def __init__(self, path:str = None) -> None:
        # ? If I introduce the path of the file I want to use.
        if not path:
            self.get_file_path()
        else:
            self.file_path = path
        # ! Inicialization
        try:
            with open(self.file_path, 'r') as f:
                data = f.read()
                if data:
                    self.data = json.loads(data)
                f.close()
        except Exception as e:
            print(f'------- Error:  {e}')
            with open(self.file_path, 'x') as f:
                f.close()
        self.get_next_id()

class JsonUtilitiesWrite():
    file_path = ''
    current_dir = get_current_dir()
    f = None

    def before_writing(self):
        self.f = open(self.file_path, 'w')

    def save_data(self, data):
        self.before_writing()
        self.f.write(json.dumps(data))

    def close_file(self) -> None:
        if self.f:
            self.f.close()

    def get_file_path(self) -> str | None:
        with open(f'{self.current_dir}/file_path.txt', 'r') as f:
            self.file_path = f.read()
            f.close()
        if not len(self.file_path) > 0:
            raise Exception('You haven\'t setted the file path for the tasks')
    
    def __init__(self, path:str = None) -> None:
        if not path:
            self.get_file_path()
        else:
            self.file_path = path