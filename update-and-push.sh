#!/bin/bash -ex

IMAGE_NAME="${DOCKER_IMAGE_NAME:-product-details-json}"
docker build -t "$IMAGE_NAME" --pull .
docker run -v "$PWD/product-details:/app/product-details" "$IMAGE_NAME"

