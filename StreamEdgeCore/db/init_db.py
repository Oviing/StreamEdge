import sqlite3
import yaml
import os

# Load DB setup config
config_path = os.path.join(os.path.dirname(__file__), '..', 'db_setup.yaml')
with open(config_path, 'r') as f:
    db_config = yaml.safe_load(f)

DB_NAME = db_config.get('DB_NAME', 'data.db')
TABLE_NAME = db_config.get('TABLE_NAME', 'ingested_data')
PRIMARY_KEY = db_config.get('PRIMARY_KEY', 'id')
PRIMARY_KEY_TYPE = db_config.get('PRIMARY_KEY_TYPE', 'INTEGER PRIMARY KEY AUTOINCREMENT')
EXTRA_FIELDS = db_config.get('EXTRA_FIELDS', [])

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    fields_def = f"{PRIMARY_KEY} {PRIMARY_KEY_TYPE}"
    for field in EXTRA_FIELDS:
        field_def = f"{field['name']} {field['type']}"
        if 'default' in field:
            field_def += f" DEFAULT {field['default']}"
        fields_def += f", {field_def}"
    c.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            {fields_def}
        )
    """)
    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' and table '{TABLE_NAME}' initialized with fields: {fields_def}")

if __name__ == "__main__":
    init_db()