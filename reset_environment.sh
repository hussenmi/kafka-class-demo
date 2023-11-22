#!/bin/bash

# Stop and Remove All Docker Containers
echo "Stopping all Docker containers..."
docker stop $(docker ps -aq)

echo "Removing all Docker containers..."
docker rm $(docker ps -aq)

# Remove All Docker Volumes
echo "Removing all Docker volumes..."
docker volume prune -f

echo "Environment reset complete."
