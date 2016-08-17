#!/bin/bash -ex

UPDATE_FILE=".new-revision-pushed"
IMAGE_NAME="${DOCKER_IMAGE_NAME:-product-details-json}"
docker build -t "$IMAGE_NAME" --pull .
docker run -v "$PWD/product-details:/app/product-details" "$IMAGE_NAME"

# UPDATE_FILE is an indicator we can use in Jenkins
# to run other jobs if there was, in fact, an update
rm -f "$UPDATE_FILE"

if [[ "$1" == "push" ]]; then
    git checkout master
    git add ./product-details/
    if git commit -m "Update product-details data"; then
        git push origin master
        git rev-parse HEAD > "$UPDATE_FILE"
    fi
fi
