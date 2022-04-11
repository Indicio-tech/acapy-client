from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.ping_request import PingRequest
from ...models.ping_request_response import PingRequestResponse
from ...types import Response


def _get_kwargs(
    conn_id: str,
    *,
    client: Client,
    json_body: PingRequest,
) -> Dict[str, Any]:
    url = "{}/connections/{conn_id}/send-ping".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PingRequestResponse]:
    if response.status_code == 200:
        response_200 = PingRequestResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PingRequestResponse]:
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
    json_body: PingRequest,
) -> Response[PingRequestResponse]:
    """Send a trust ping to a connection

    Args:
        conn_id (str):
        json_body (PingRequest):

    Returns:
        Response[PingRequestResponse]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        json_body=json_body,
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
    json_body: PingRequest,
) -> Optional[PingRequestResponse]:
    """Send a trust ping to a connection

    Args:
        conn_id (str):
        json_body (PingRequest):

    Returns:
        Response[PingRequestResponse]
    """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    *,
    client: Client,
    json_body: PingRequest,
) -> Response[PingRequestResponse]:
    """Send a trust ping to a connection

    Args:
        conn_id (str):
        json_body (PingRequest):

    Returns:
        Response[PingRequestResponse]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    *,
    client: Client,
    json_body: PingRequest,
) -> Optional[PingRequestResponse]:
    """Send a trust ping to a connection

    Args:
        conn_id (str):
        json_body (PingRequest):

    Returns:
        Response[PingRequestResponse]
    """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
