#!/usr/bin/env bash
set -e

cd "$(dirname "$0")" || exit

wget -i - < OPENAPI_URL -O ../openapi.yml
