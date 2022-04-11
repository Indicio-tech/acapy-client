from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.connection_metadata import ConnectionMetadata
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conn_id: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/connections/{conn_id}/metadata".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ConnectionMetadata]:
    if response.status_code == 200:
        response_200 = ConnectionMetadata.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ConnectionMetadata]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    conn_id: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = UNSET,
) -> Response[ConnectionMetadata]:
    """Fetch connection metadata

    Args:
        conn_id (str):
        key (Union[Unset, None, str]):

    Returns:
        Response[ConnectionMetadata]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        key=key,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    conn_id: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[ConnectionMetadata]:
    """Fetch connection metadata

    Args:
        conn_id (str):
        key (Union[Unset, None, str]):

    Returns:
        Response[ConnectionMetadata]
    """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
        key=key,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = UNSET,
) -> Response[ConnectionMetadata]:
    """Fetch connection metadata

    Args:
        conn_id (str):
        key (Union[Unset, None, str]):

    Returns:
        Response[ConnectionMetadata]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        key=key,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[ConnectionMetadata]:
    """Fetch connection metadata

    Args:
        conn_id (str):
        key (Union[Unset, None, str]):

    Returns:
        Response[ConnectionMetadata]
    """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
            key=key,
        )
    ).parsed
