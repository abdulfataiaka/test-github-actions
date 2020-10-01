from src.db import DB
from unittest import TestCase

class TestDB(TestCase):
    def test_connect(self):
        conn = DB.connect()
        self.assertIsNotNone(conn)
    
    def test_create(self):
        DB.create()
