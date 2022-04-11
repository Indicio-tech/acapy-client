from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.v10_discovery_exchange_result import V10DiscoveryExchangeResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    comment: Union[Unset, None, str] = UNSET,
    connection_id: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/discover-features/query".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["comment"] = comment

    params["connection_id"] = connection_id

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[V10DiscoveryExchangeResult]:
    if response.status_code == 200:
        response_200 = V10DiscoveryExchangeResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V10DiscoveryExchangeResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    comment: Union[Unset, None, str] = UNSET,
    connection_id: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Response[V10DiscoveryExchangeResult]:
    """Query supported features

    Args:
        comment (Union[Unset, None, str]):
        connection_id (Union[Unset, None, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[V10DiscoveryExchangeResult]
    """

    kwargs = _get_kwargs(
        client=client,
        comment=comment,
        connection_id=connection_id,
        query=query,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    comment: Union[Unset, None, str] = UNSET,
    connection_id: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[V10DiscoveryExchangeResult]:
    """Query supported features

    Args:
        comment (Union[Unset, None, str]):
        connection_id (Union[Unset, None, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[V10DiscoveryExchangeResult]
    """

    return sync_detailed(
        client=client,
        comment=comment,
        connection_id=connection_id,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    comment: Union[Unset, None, str] = UNSET,
    connection_id: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Response[V10DiscoveryExchangeResult]:
    """Query supported features

    Args:
        comment (Union[Unset, None, str]):
        connection_id (Union[Unset, None, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[V10DiscoveryExchangeResult]
    """

    kwargs = _get_kwargs(
        client=client,
        comment=comment,
        connection_id=connection_id,
        query=query,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    comment: Union[Unset, None, str] = UNSET,
    connection_id: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[V10DiscoveryExchangeResult]:
    """Query supported features

    Args:
        comment (Union[Unset, None, str]):
        connection_id (Union[Unset, None, str]):
        query (Union[Unset, None, str]):

    Returns:
        Response[V10DiscoveryExchangeResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            comment=comment,
            connection_id=connection_id,
            query=query,
        )
    ).parsed
