# Kafka-class-demo

## Overview
You can find a demonstration of the files [here](https://screenapp.io/app/#/shared/2151e0ac-a4a2-4c9e-ad32-b36cc57074ca).


This project showcases various features of Apache Kafka using a set of Python scripts. Each set of script demonstrates a specific Kafka capability, including basic message publishing and consumption, keyed messages, managing multiple topics, and offset commit functionality.

## Requirements

Before running the scripts, ensure the following:

- If you are on a Windows/Mac, make sure Docker Desktop is running
- Install a Python client for Apache Kafka using pip: `pip install kafka-python`. Recommended to do it in a virtual environment
- Make the shell files executable by running the command: `chmod +x [name of file]`. Eg., `chmod +x reset_kafka.sh`

## Docker-Compose File Overview

The `docker-compose.yml` file is used to set up and run Apache Kafka and Zookeeper services in Docker containers. This approach simplifies the deployment and management of Kafka and Zookeeper, making it easier to demonstrate Kafka features without the need for complex installation and configuration processes. Otherwise, we'd need to install Java and Kafka separately in order to make this work.

### Key Components:

- **Zookeeper**: This service is essential for Kafka's operation. Zookeeper acts as a centralized service for maintaining configuration information, naming, and providing distributed synchronization.
- **Kafka**: The main Kafka broker service, responsible for message storage and processing.

## Script Descriptions

### Basic Producer and Consumer
- `producer.py`: Sends messages to a Kafka topic.
- `consumer.py`: Consumes messages from a Kafka topic.

### Keyed Messages
- `producer_km.py`: Produces keyed messages, demonstrating how Kafka distributes messages with the same key to the same partition.
- `consumer_km.py`: Consumes keyed messages and displays their partition assignment.

### Multiple Topics
- `producer_mt.py`: Sends messages to several topics, showcasing how Kafka handles multiple topics.
- `consumer_mt.py`: Consumes messages from multiple topics, illustrating Kafka's topic-based message organization.

### Offset Commits
- `producer_oc.py`: Produces messages for demonstrating Kafka's offset commit feature.
- `consumer_oc.py`: Consumes messages and manually commits offsets, showcasing how Kafka prevents re-consumption of processed messages.

### Shell files
- `reset_kafka.sh`: Resets the Kafka environment, clearing all data and restarting Kafka and Zookeeper services. This script ensures a clean state for each demonstration.
- `setup_multiple_partitions`: Sets up a topic with multiple partitions and used when showcasing the keyed messages and multiple topics features. We need to run this script before running the scripts for those two features.
- `reset_environment`: Stops and removes all docker containers and volumes. Only use this after finishing everything.