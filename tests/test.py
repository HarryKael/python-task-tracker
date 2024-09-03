from ..src.json_utilities import JsonUtilitiesRead
from datetime import datetime
from unittest import TestCase

class TestJsonUtilitiesReadModel(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.read = JsonUtilitiesRead()
        super().__init__(methodName)
        
    def test_add_data():
        pass