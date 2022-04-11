from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.conn_record import ConnRecord
from ...types import Response


def _get_kwargs(
    conn_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/connections/{conn_id}".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ConnRecord]:
    if response.status_code == 200:
        response_200 = ConnRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ConnRecord]:
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
) -> Response[ConnRecord]:
    """Fetch a single connection record

    Args:
        conn_id (str):

    Returns:
        Response[ConnRecord]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
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
) -> Optional[ConnRecord]:
    """Fetch a single connection record

    Args:
        conn_id (str):

    Returns:
        Response[ConnRecord]
    """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    *,
    client: Client,
) -> Response[ConnRecord]:
    """Fetch a single connection record

    Args:
        conn_id (str):

    Returns:
        Response[ConnRecord]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    *,
    client: Client,
) -> Optional[ConnRecord]:
    """Fetch a single connection record

    Args:
        conn_id (str):

    Returns:
        Response[ConnRecord]
    """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
        )
    ).parsed
