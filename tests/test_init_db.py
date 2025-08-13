import unittest
import sqlite3
import os
from db.init_db import init_db, DB_NAME, TABLE_NAME

class TestInitDB(unittest.TestCase):
    def setUp(self):
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)
        init_db()

    def test_table_created(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';")
        self.assertIsNotNone(cursor.fetchone())
        conn.close()

if __name__ == "__main__":
    unittest.main()
