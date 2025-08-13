import zmq
import yaml
import json

ZMQ_SERVER = "localhost"
ZMQ_PORT = 5555

# Load payload config
with open('payload_config.yaml', 'r') as f:
    payload_config = yaml.safe_load(f)

def build_payload():
    payload = {}
    for field in payload_config['fields']:
        value = input(f"Enter value for {field['name']} ({field['type']}): ")
        # Convert value to correct type
        if field['type'] == 'REAL':
            try:
                value = float(value)
            except ValueError:
                value = None
        elif field['type'] == 'INTEGER':
            try:
                value = int(value)
            except ValueError:
                value = None
        payload[field['name']] = value
    return payload

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{ZMQ_SERVER}:{ZMQ_PORT}")
    payload = build_payload()
    socket.send_string(json.dumps(payload))
    reply = socket.recv_string()
    print(f"Server reply: {reply}")
