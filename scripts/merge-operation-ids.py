import deepmerge
import yaml


def merge_operation_ids(openapi: dict):
    with open("/app/operation-id-map.yml") as ops_file:
        ops = yaml.load(ops_file, Loader=yaml.FullLoader)

    return deepmerge.always_merger.merge(openapi, ops)


if __name__ == "__main__":
    with open("/app/openapi.yml") as openapi_file:
        openapi = yaml.load(openapi_file, Loader=yaml.FullLoader)

    result = merge_operation_ids(openapi)

    with open("/app/openapi.yml", "w") as openapi_file:
        yaml.dump(result, openapi_file, sort_keys=False)
