#!/usr/bin/env bash

cd "$(dirname "$0")" || exit
CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-docker}

CONTAINER_NAME=insert-operation-ids
${CONTAINER_RUNTIME} build -t ${CONTAINER_NAME} -f ../docker/Dockerfile.insert-operation-ids .
${CONTAINER_RUNTIME} run --name ${CONTAINER_NAME} --rm -it \
    -v ../openapi.yml:/app/openapi.yml:z \
    -v ./operation-id-map.yml:/app/operation-id-map.yml:z \
    -v ./insert-operation-ids.py:/app/insert-operation-ids.py:z \
    ${CONTAINER_NAME} python /app/insert-operation-ids.py
