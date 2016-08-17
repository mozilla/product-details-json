#!/bin/bash -ex

IMAGE_NAME="${DOCKER_IMAGE_NAME:-product-details-json}"
docker build -t "$IMAGE_NAME" --pull .
docker run -v "$PWD/product-details:/app/product-details" "$IMAGE_NAME"

if [[ "$1" == "push" ]]; then
    git add ./product-details/
    if git commit -m "Update product-details data"; then
        git push origin master
    fi
fi
