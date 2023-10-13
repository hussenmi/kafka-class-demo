#!/bin/bash

# Step 1: Stop and remove all running containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Step 2: Remove all Docker volumes
docker volume prune -f

# Step 3: Start up Kafka and Zookeeper using docker-compose
docker-compose -f docker-compose.yml up -d

# Step 4: Wait for Kafka to start up. You might need to adjust the sleep time.
sleep 30

# Step 5: Create a topic with multiple partitions using Kafka's command-line tool inside the Docker container
docker exec -it kafka-class-demo-kafka-1 /opt/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic keyed_topic

echo "Setup complete. You can now have access to multiple partitions."
