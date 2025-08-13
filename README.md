# StreamEdge

Collect shopfloor data on the edge.

## Overview

StreamEdge is an edge computing solution designed to collect, process, and visualize shopfloor data in real-time. It supports integration with various industrial protocols and provides a modular architecture for data ingestion, storage, and visualization.

## Features

- Real-time data ingestion from shopfloor devices
- Modular connectors (e.g., MQTT)
- Local database storage
- Streamlit-based UI for data visualization
- Dockerized deployment for easy setup

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- pip

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/StreamEdge.git
   cd StreamEdge
   ```

2. Install dependencies:
   ```sh
   pip install -r StreamEdgeCore/requirements.txt
   ```

3. (Optional) Set up MQTT connector:
   ```sh
   pip install -r StreamEdgeCore/connector/requirements.txt
   ```

### Usage

- Start the ingest agent:
  ```sh
  python StreamEdgeCore/zmq_ingest_agent.py
  ```

- Start the Streamlit UI:
  ```sh
  streamlit run StreamEdgeCore/streamlit_app.py
  ```

- Use Docker Compose for full deployment:
  ```sh
  cd StreamEdgeCore
  docker-compose up
  ```

## Configuration

- Edit `StreamEdgeCore/config.yaml` for core settings.
- Edit `StreamEdgeCore/connector/mqtt_config.yaml` for MQTT connector settings.

## Folder Structure

- `StreamEdgeCore/`: Main application code and configuration
- `StreamEdgeCore/connector/`: MQTT connector and related files

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
