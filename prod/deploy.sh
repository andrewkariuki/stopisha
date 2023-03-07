#!/bin/sh

set -o errexit
set -o nounset

mkdir -p volumes
mkdir -p volumes/logs
mkdir -p volumes/data

export APP_ENV="production"

if [ "$(echo "$CONTAINER_REGISTRY_TOKEN" | docker login ghcr.io -u andrewkariuki --password-stdin 2>&1)" -eq 0 ]; then
    echo "Docker Login failed."
    exit 0
fi

echo "Docker login was successfully."

if [ "$(docker-compose pull 2>&1)" -eq 0 ]; then
    echo "Failed to pulling images."
    exit 0
fi

echo "Pulled images successfully."

if [ "$(docker-compose up -d --no-deps 2>&1)" -eq 0 ]; then
    echo "Failed to start services."
    exit 0
fi

echo "Started service successfully."

docker image prune -a -f
docker volume prune -f
