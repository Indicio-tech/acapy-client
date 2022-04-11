from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.cred_info_list import CredInfoList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/credentials".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["count"] = count

    params["start"] = start

    params["wql"] = wql

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CredInfoList]:
    if response.status_code == 200:
        response_200 = CredInfoList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CredInfoList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Response[CredInfoList]:
    """Fetch credentials from wallet

    Args:
        count (Union[Unset, None, str]):
        start (Union[Unset, None, str]):
        wql (Union[Unset, None, str]):

    Returns:
        Response[CredInfoList]
    """

    kwargs = _get_kwargs(
        client=client,
        count=count,
        start=start,
        wql=wql,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Optional[CredInfoList]:
    """Fetch credentials from wallet

    Args:
        count (Union[Unset, None, str]):
        start (Union[Unset, None, str]):
        wql (Union[Unset, None, str]):

    Returns:
        Response[CredInfoList]
    """

    return sync_detailed(
        client=client,
        count=count,
        start=start,
        wql=wql,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Response[CredInfoList]:
    """Fetch credentials from wallet

    Args:
        count (Union[Unset, None, str]):
        start (Union[Unset, None, str]):
        wql (Union[Unset, None, str]):

    Returns:
        Response[CredInfoList]
    """

    kwargs = _get_kwargs(
        client=client,
        count=count,
        start=start,
        wql=wql,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Optional[CredInfoList]:
    """Fetch credentials from wallet

    Args:
        count (Union[Unset, None, str]):
        start (Union[Unset, None, str]):
        wql (Union[Unset, None, str]):

    Returns:
        Response[CredInfoList]
    """

    return (
        await asyncio_detailed(
            client=client,
            count=count,
            start=start,
            wql=wql,
        )
    ).parsed
