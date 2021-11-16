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

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "verify": client.verify_ssl,
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
    kwargs = _get_kwargs(
        schema_id=schema_id,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    schema_id: str,
    *,
    client: Client,
) -> Optional[SchemaGetResult]:
    """ """

    return sync_detailed(
        schema_id=schema_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    schema_id: str,
    *,
    client: Client,
) -> Response[SchemaGetResult]:
    kwargs = _get_kwargs(
        schema_id=schema_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    schema_id: str,
    *,
    client: Client,
) -> Optional[SchemaGetResult]:
    """ """

    return (
        await asyncio_detailed(
            schema_id=schema_id,
            client=client,
        )
    ).parsed
