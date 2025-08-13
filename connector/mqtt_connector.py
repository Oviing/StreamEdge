import yaml
import paho.mqtt.client as mqtt
import zmq
import sys
import time

# Load config
with open("mqtt_config.yaml", "r") as f:
    config = yaml.safe_load(f)["mqtt"]

broker = config["broker"]
port = config["port"]
topic = config["topic"]
username = config["username"]
password = config["password"]
ingest_agent_url = config["ingest_agent_url"]

import json
# Setup ZeroMQ client
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(ingest_agent_url)

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload}")
    try:
        payload_str = msg.payload.decode("utf-8")
        print(f"Decoded payload: {payload_str}")
        payload_json = json.loads(payload_str)  # Validate JSON
        print(f"Parsed JSON: {payload_json}")
        socket.send_string(payload_str)
        reply = socket.recv_string()
        print(f"Sent to ingest agent, reply: {reply}")
    except Exception as e:
        print(f"Failed to send payload to ingest agent: {e}")

client = mqtt.Client()
if username:
    client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("MQTT connector stopped.")
    sys.exit(0)
