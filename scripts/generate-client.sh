#!/usr/bin/env bash
set -e

cd "$(dirname "$0")" || exit

CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-docker}

${CONTAINER_RUNTIME} build -t openapi-client-generator - << DOCKERFILE
FROM python:3.7

WORKDIR /usr/src/app

RUN pip install openapi-python-client==0.11.1

ENTRYPOINT ["openapi-python-client"]
DOCKERFILE

${CONTAINER_RUNTIME} run --rm \
    -v "$(realpath "$PWD/../"):/usr/src/app:z" \
    openapi-client-generator generate --path ./openapi.yml --config /usr/src/app/openapi-config.yml

# Fix permissions so that the copy succeeds
sudo chown -R $(whoami). ../acapy-client || true # Don't error/exit here on failure

for to_move in ../acapy-client/* ../acapy-client/.[!.]*; do
    filename="$(basename "${to_move}")"
    rm -rf --preserve-root "../$filename"
    mv "$to_move" ../
done
rmdir ../acapy-client
