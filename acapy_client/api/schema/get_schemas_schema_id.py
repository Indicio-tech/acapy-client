from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.schema_get_result import SchemaGetResult
from ...types import Response


def _get_kwargs(
    schema_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/schemas/{schema_id}".format(client.base_url, schema_id=schema_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[SchemaGetResult]:
    if response.status_code == 200:
        response_200 = SchemaGetResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SchemaGetResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    schema_id: str,
    *,
    client: Client,
) -> Response[SchemaGetResult]:
    """Gets a schema from the ledger

    Args:
        schema_id (str):

    Returns:
        Response[SchemaGetResult]
    """

    kwargs = _get_kwargs(
        schema_id=schema_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    schema_id: str,
    *,
    client: Client,
) -> Optional[SchemaGetResult]:
    """Gets a schema from the ledger

    Args:
        schema_id (str):

    Returns:
        Response[SchemaGetResult]
    """

    return sync_detailed(
        schema_id=schema_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    schema_id: str,
    *,
    client: Client,
) -> Response[SchemaGetResult]:
    """Gets a schema from the ledger

    Args:
        schema_id (str):

    Returns:
        Response[SchemaGetResult]
    """

    kwargs = _get_kwargs(
        schema_id=schema_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    schema_id: str,
    *,
    client: Client,
) -> Optional[SchemaGetResult]:
    """Gets a schema from the ledger

    Args:
        schema_id (str):

    Returns:
        Response[SchemaGetResult]
    """

    return (
        await asyncio_detailed(
            schema_id=schema_id,
            client=client,
        )
    ).parsed
