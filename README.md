# ACA-Py Client

A client library for accessing Aries Cloud Agent

## Note
This client is automatically generated from an openapi definition
derived from ACA-Py's `swagger.json`. As such, there may be errors caused by the
conversion process or even just inherent in the route definitions in ACA-Py.

This client has been tuned for our use and may not be suitable for all use
cases.

Support for specific versions of ACA-Py is performed on a best effort basis.

## Usage
First, create a client:

```python
from acapy_client import Client

client = Client(base_url="https://api.example.com")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from acapy_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from acapy_client.models import MyDataModel
from acapy_client.api.my_tag import get_my_data_model
from acapy_client.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from acapy_client.models import MyDataModel
from acapy_client.api.my_tag import get_my_data_model
from acapy_client.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but the async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` by async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `acapy_client.api.default`
