from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.v20_discovery_exchange_result import V20DiscoveryExchangeResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    query_goal_code: Union[Unset, None, str] = UNSET,
    query_protocol: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/discover-features-2.0/queries".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "connection_id": connection_id,
        "query_goal_code": query_goal_code,
        "query_protocol": query_protocol,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[V20DiscoveryExchangeResult]:
    if response.status_code == 200:
        response_200 = V20DiscoveryExchangeResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V20DiscoveryExchangeResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    query_goal_code: Union[Unset, None, str] = UNSET,
    query_protocol: Union[Unset, None, str] = UNSET,
) -> Response[V20DiscoveryExchangeResult]:
    kwargs = _get_kwargs(
        client=client,
        connection_id=connection_id,
        query_goal_code=query_goal_code,
        query_protocol=query_protocol,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    query_goal_code: Union[Unset, None, str] = UNSET,
    query_protocol: Union[Unset, None, str] = UNSET,
) -> Optional[V20DiscoveryExchangeResult]:
    """ """

    return sync_detailed(
        client=client,
        connection_id=connection_id,
        query_goal_code=query_goal_code,
        query_protocol=query_protocol,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    query_goal_code: Union[Unset, None, str] = UNSET,
    query_protocol: Union[Unset, None, str] = UNSET,
) -> Response[V20DiscoveryExchangeResult]:
    kwargs = _get_kwargs(
        client=client,
        connection_id=connection_id,
        query_goal_code=query_goal_code,
        query_protocol=query_protocol,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    query_goal_code: Union[Unset, None, str] = UNSET,
    query_protocol: Union[Unset, None, str] = UNSET,
) -> Optional[V20DiscoveryExchangeResult]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            connection_id=connection_id,
            query_goal_code=query_goal_code,
            query_protocol=query_protocol,
        )
    ).parsed
