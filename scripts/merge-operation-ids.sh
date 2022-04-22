#!/usr/bin/env bash

cd "$(dirname "$0")" || exit
CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-docker}

CONTAINER_NAME=merge-operation-ids
${CONTAINER_RUNTIME} build -t ${CONTAINER_NAME} - << DOCKERFILE
FROM python:3.8
RUN pip install pyyaml deepmerge
DOCKERFILE
${CONTAINER_RUNTIME} run --name ${CONTAINER_NAME} --rm -it \
    -v $(realpath $(pwd)/../openapi.yml):/app/openapi.yml:z \
    -v $(realpath $(pwd)/operation-id-map.yml):/app/operation-id-map.yml:z \
    -v $(realpath $(pwd)/merge-operation-ids.py):/app/merge-operation-ids.py:z \
    ${CONTAINER_NAME} python /app/merge-operation-ids.py
