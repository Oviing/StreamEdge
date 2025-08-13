import unittest
import sqlite3
import os
from ingest.zmq_ingest_agent import init_db, insert_data, DB_NAME, TABLE_NAME

class TestZMQIngestAgent(unittest.TestCase):
    def setUp(self):
        # Remove test DB if exists
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)
        init_db()

    def test_table_created(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';")
        self.assertIsNotNone(cursor.fetchone())
        conn.close()

    def test_insert_data(self):
        payload = {"field1": 123, "field2": 45.6}  # Adjust fields to match your payload_config.yaml
        insert_data(payload)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        rows = cursor.fetchall()
        self.assertTrue(len(rows) > 0)
        conn.close()

if __name__ == "__main__":
    unittest.main()
