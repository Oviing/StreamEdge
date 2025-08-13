# StreamEdge Wiki

Welcome to the StreamEdge Wiki! This documentation provides detailed information about the architecture, setup, usage, and extension of StreamEdge for collecting shopfloor data on the edge.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Setup & Installation](#setup--installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Connectors](#connectors)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

StreamEdge is an edge computing platform designed to collect, process, and visualize shopfloor data in real-time. It supports modular connectors, local storage, and a user-friendly UI.

## Architecture

- **Ingest Agent:** Collects data from shopfloor devices using ZeroMQ.
- **Connectors:** Modular components (e.g., MQTT) for protocol integration.
- **Database:** Local SQLite database for persistent storage.
- **UI:** Streamlit-based dashboard for visualization and monitoring.
- **Docker Support:** Containerized deployment for easy setup.

## Setup & Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/StreamEdge.git
   cd StreamEdge
   ```

2. **Install dependencies:**
   ```sh
   pip install -r StreamEdgeCore/requirements.txt
   ```

3. **(Optional) Install connector dependencies:**
   ```sh
   pip install -r StreamEdgeCore/connector/requirements.txt
   ```

4. **Run with Docker Compose:**
   ```sh
   cd StreamEdgeCore
   docker-compose up
   ```

## Configuration

- Main settings: `StreamEdgeCore/config.yaml`
- Connector settings: `StreamEdgeCore/connector/mqtt_config.yaml`
- Database setup: `StreamEdgeCore/db_setup.yaml`

## Usage

- Start ingest agent: `python StreamEdgeCore/zmq_ingest_agent.py`
- Launch UI: `streamlit run StreamEdgeCore/streamlit_app.py`
- Use Docker Compose for full deployment.

## Connectors

- **MQTT Connector:** Located in `StreamEdgeCore/connector/`
  - Configuration: `mqtt_config.yaml`
  - Example payload: `example_payload.json`

## Troubleshooting

- Check logs for errors in the UI and ingest agent.
- Ensure all dependencies are installed.
- Verify configuration files for correct settings.

## Contributing

We welcome contributions! Please open issues for bugs or feature requests, and submit pull requests for improvements.

## License

StreamEdge is licensed under the MIT License.
