import zmq
import sqlite3
import logging
import yaml
import json



# Load main config from YAML file using absolute path
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(BASE_DIR, 'config.yaml')
payload_config_path = os.path.join(BASE_DIR, 'payload_config.yaml')

with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

with open(payload_config_path, 'r') as f:
    payload_config = yaml.safe_load(f)

DB_NAME = config.get('DB_NAME', 'data.db')
TABLE_NAME = config.get('TABLE_NAME', 'ingested_data')
ZMQ_PORT = config.get('ZMQ_PORT', 5555)
LOG_LEVEL = getattr(logging, config.get('LOG_LEVEL', 'INFO').upper(), logging.INFO)

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.StreamHandler()]
)

# Dynamically create table if not exists
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    fields_def = ', '.join([f"{field['name']} {field['type']}" for field in payload_config['fields']])
    c.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {fields_def}
        )
    """)
    conn.commit()
    conn.close()
    logging.info(f"Database '{DB_NAME}' and table '{TABLE_NAME}' initialized with fields: {fields_def}")

# Insert data according to payload config
def insert_data(payload):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        field_names = [field['name'] for field in payload_config['fields']]
        placeholders = ', '.join(['?' for _ in field_names])
        values = [payload.get(name) for name in field_names]
        logging.debug(f"Insert values: {values} for fields: {field_names}")
        c.execute(
            f"INSERT INTO {TABLE_NAME} ({', '.join(field_names)}) VALUES ({placeholders})",
            values
        )
        conn.commit()
        conn.close()
        logging.info(f"Inserted payload: {payload}")
    except Exception as e:
        logging.error(f"Failed to insert payload: {payload}. Error: {e}")

if __name__ == "__main__":
    init_db()
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:{ZMQ_PORT}")
    logging.info(f"ZeroMQ agent listening on port {ZMQ_PORT}")
    while True:
        message = socket.recv_string()
        logging.info(f"Received message: {message}")
        try:
            payload = json.loads(message)
            logging.debug(f"Parsed payload: {payload}")
            insert_data(payload)
            socket.send_string("OK")
        except Exception as e:
            logging.error(f"Invalid payload: {message}. Error: {e}")
            socket.send_string("ERROR")