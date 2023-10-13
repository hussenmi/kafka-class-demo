#!/bin/bash

# Reset Kafka Environment Script

# Step 1: Stop Kafka and Zookeeper services with multiple partitions
echo "Stopping Kafka and Zookeeper..."
docker-compose -f docker-compose.yml down

# Step 2: Remove all Docker volumes to clear all data
echo "Removing all Docker volumes..."
docker volume prune -f

# Step 3: Start Kafka and Zookeeper services fresh
echo "Starting Kafka and Zookeeper..."
docker-compose -f docker-compose.yml up -d

echo "Reset complete. Kafka is ready for a fresh start."
