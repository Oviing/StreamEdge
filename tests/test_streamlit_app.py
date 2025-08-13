import unittest
import sqlite3
import os
from ui.streamlit_app import get_table_names, get_table_data

class TestStreamlitApp(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test_data.db'
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY, value REAL)")
        cursor.execute("INSERT INTO test_table (value) VALUES (1.23)")
        conn.commit()
        conn.close()

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_get_table_names(self):
        conn = sqlite3.connect(self.db_path)
        tables = get_table_names(conn)
        self.assertIn('test_table', tables)
        conn.close()

    def test_get_table_data(self):
        conn = sqlite3.connect(self.db_path)
        columns, rows = get_table_data(conn, 'test_table')
        self.assertEqual(columns, ['id', 'value'])
        self.assertTrue(len(rows) > 0)
        conn.close()

if __name__ == "__main__":
    unittest.main()
