from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.connection_module_response import ConnectionModuleResponse
from ...types import Response


def _get_kwargs(
    conn_id: str,
    ref_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/connections/{conn_id}/establish-inbound/{ref_id}".format(client.base_url, conn_id=conn_id, ref_id=ref_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ConnectionModuleResponse]:
    if response.status_code == 200:
        response_200 = ConnectionModuleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ConnectionModuleResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    conn_id: str,
    ref_id: str,
    *,
    client: Client,
) -> Response[ConnectionModuleResponse]:
    """Assign another connection as the inbound connection

    Args:
        conn_id (str):
        ref_id (str):

    Returns:
        Response[ConnectionModuleResponse]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        ref_id=ref_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    conn_id: str,
    ref_id: str,
    *,
    client: Client,
) -> Optional[ConnectionModuleResponse]:
    """Assign another connection as the inbound connection

    Args:
        conn_id (str):
        ref_id (str):

    Returns:
        Response[ConnectionModuleResponse]
    """

    return sync_detailed(
        conn_id=conn_id,
        ref_id=ref_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    ref_id: str,
    *,
    client: Client,
) -> Response[ConnectionModuleResponse]:
    """Assign another connection as the inbound connection

    Args:
        conn_id (str):
        ref_id (str):

    Returns:
        Response[ConnectionModuleResponse]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        ref_id=ref_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    ref_id: str,
    *,
    client: Client,
) -> Optional[ConnectionModuleResponse]:
    """Assign another connection as the inbound connection

    Args:
        conn_id (str):
        ref_id (str):

    Returns:
        Response[ConnectionModuleResponse]
    """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            ref_id=ref_id,
            client=client,
        )
    ).parsed
