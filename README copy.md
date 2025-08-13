# StreamEdge Project

## Overview
This project consists of three main components, each running in its own Docker container:
- **Ingest Agent**: Receives data via ZeroMQ and stores it in a SQLite database.
- **Connectors**: Forward data from external sources (e.g., MQTT) to the ingest agent.
- **Streamlit UI**: Visualizes the database and allows charting.

## Prerequisites
- Docker and Docker Compose installed
- Docker Hub account (for pushing images)

## Setup & Usage

### 1. Build All Containers
Run the following command in the project root:
```sh
docker-compose build
```

### 2. Start All Services
```sh
docker-compose up
```
This will start the ingest agent, MQTT connector, and UI. The UI will be available at [http://localhost:8501](http://localhost:8501).

### 3. Tag Images for Docker Hub
Replace `<your-username>` with your Docker Hub username:
```sh
docker tag streamedge_ingest_agent <your-username>/streamedge_ingest_agent:latest
docker tag streamedge_mqtt_connector <your-username>/streamedge_mqtt_connector:latest
docker tag streamedge_ui <your-username>/streamedge_ui:latest
```

### 4. Push Images to Docker Hub
```sh
docker login
# Then push each image:
docker push <your-username>/streamedge_ingest_agent:latest
docker push <your-username>/streamedge_mqtt_connector:latest
docker push <your-username>/streamedge_ui:latest
```

## Configuration
- **Ingest Agent**: Configure via `config.yaml` and `payload_config.yaml`.
- **Connectors**: Each connector has its own config file (e.g., `connector/mqtt_config.yaml`).
- **UI**: No special config required, but uses `data.db` for visualization.

## Adding More Connectors
- Place new connector scripts and their config files in the `connector` folder.
- Create a Dockerfile for each new connector.
- Update `docker-compose.yml` to add the new service.

## Troubleshooting
- Check logs in each container for errors.
- Ensure ports are not blocked by firewalls.
- Make sure config files are correctly mounted and formatted.

---
For questions or issues, contact the project maintainer.
