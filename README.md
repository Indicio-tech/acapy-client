# ACA-Py Client

This is a generated client for ACA-Py's RESTful Admin API.

# Generating the client

**Note:** We would like to automate this process eventually.

1. Download `swagger.json` from running instance of ACA-Py on the version you'd
   like your client to target.
2. Run `./scripts/convert-to-openapi3.sh`.
3. Run `./scripts/process-openapi.sh`.
4. Run `./scripts/generate-client.sh update` if you've already generated the
   client before or `./scripts/generate-client.sh generate` if you haven't.
