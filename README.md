# Kafka Compose - I spent hours on this, so you don't have to.

Minimal start for Kafka Broker development without Zookeeper 

**I lost a whole day trying to start dev with Kafka just because I couldn't figure out how to configure the environment :sob:**

## Overview

This project provides:
- Apache Kafka broker with Kraft running in Docker
- Kafka UI for visual management and monitoring
- Python test scripts to verify producer/consumer functionality

## Prerequisites

- Docker and Docker Compose
- Python 3.7+ (for testing)

## Quick Start

### 1. Start Kafka Services

```bash
docker-compose up -d
```

This will start:
- **Kafka broker** on `localhost:9092`
- **Kafka UI** on `http://localhost:8080`

### 2. Verify Services

Check that containers are running:
```bash
docker-compose ps
```

Access Kafka UI in your browser at `http://localhost:8080` to see the cluster status.

### 3. Test Connection with Python

Install Python dependencies:
```bash
cd test
pip install -r requirements.txt
```

Run the test script:
```bash
python main.py
```

The script will:
- Send a test message to the `test_topic`
- Consume and display the message
- Show success/error status

## Project Structure

```
.
├── docker-compose.yml      # Kafka and Kafka UI services
├── test/
│   ├── main.py            # Python producer/consumer test
│   └── requirements.txt   # Python dependencies
└── README.md              # This file
```

## Configuration Details

### Kafka Broker
- **Port**: 9092 (external), 29092 (internal Docker network)
- **Mode**: Combined broker and controller (KRaft mode)
- **Auto-create topics**: Enabled

### Kafka UI
- **Port**: 8080
- **Cluster name**: local
- **Features**: Topic management, message browsing, consumer groups

## Stopping Services

```bash
docker-compose down
```

To remove volumes and clean up completely:
```bash
docker-compose down -v
```