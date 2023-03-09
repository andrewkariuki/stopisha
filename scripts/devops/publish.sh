#!/bin/sh

set -o errexit
set -o nounset

if [ "$(echo "$CONTAINER_REGISTRY_TOKEN" | docker login ghcr.io -u andrewkariuki --password-stdin 2>&1)" -eq 0 ]; then
    exit 0
fi

for VERSION in "$(date "+%Y.%-m.%-d")" "$GIT_TAGGED" "latest"; do
    docker build -t ghcr.io/andrewkariuki/stopisha:"$VERSION" .
done

docker push ghcr.io/andrewkariuki/stopisha --all-tags
