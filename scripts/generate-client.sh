#!/usr/bin/env bash
set -e

cd "$(dirname "$0")" || exit

CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-docker}

${CONTAINER_RUNTIME} build -t openapi-client-generator -f ../docker/Dockerfile.openapi-client-generator .

${CONTAINER_RUNTIME} run --rm \
    -v "$(realpath "$PWD/../"):/usr/src/app:z" \
    openapi-client-generator generate --path ./openapi.yml --config ./openapi-config.yml

for to_move in ../acapy-client/* ../acapy-client/.[!.]*; do
    filename="$(basename "${to_move}")"
    rm -rf --preserve-root "../$filename"
    mv "$to_move" ../
done
rmdir ../acapy-client
