#!/bin/bash -ex

UPDATE_FILE=".new-revision-pushed"
IMAGE_NAME="${DOCKER_IMAGE_NAME:-product-details-json}"

docker build -f Dockerfile-update -t "$IMAGE_NAME" --pull .
docker run -v "$PWD/product-details:/app/product-details" "$IMAGE_NAME"

# UPDATE_FILE is an indicator we can use in Jenkins
# to run other jobs if there was, in fact, an update
rm -f "$UPDATE_FILE"

if [[ "$1" == "commit" ]]; then
    if git status --porcelain | grep -E "\.json$"; then
        git add ./product-details/
        git commit -m "Update product-details data"
        git rev-parse HEAD > "$UPDATE_FILE"
        echo "Product-details update committed"
    else
        echo "No new product-details"
    fi
fi
