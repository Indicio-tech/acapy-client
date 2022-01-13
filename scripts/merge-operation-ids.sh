#!/usr/bin/env bash

cd "$(dirname "$0")" || exit
CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-docker}

CONTAINER_NAME=merge-operation-ids
${CONTAINER_RUNTIME} build -t ${CONTAINER_NAME} - << DOCKERFILE
FROM python:3.8
RUN pip install pyyaml deepmerge
DOCKERFILE
${CONTAINER_RUNTIME} run --name ${CONTAINER_NAME} --rm -it \
    -v ../openapi.yml:/app/openapi.yml:z \
    -v ./operation-id-map.yml:/app/operation-id-map.yml:z \
    -v ./merge-operation-ids.py:/app/merge-operation-ids.py:z \
    ${CONTAINER_NAME} python /app/merge-operation-ids.py
