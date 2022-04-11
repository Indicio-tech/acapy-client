from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.vc_record_list import VCRecordList
from ...models.w3c_credentials_list_request import W3CCredentialsListRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/credentials/w3c".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["count"] = count

    params["start"] = start

    params["wql"] = wql

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[VCRecordList]:
    if response.status_code == 200:
        response_200 = VCRecordList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[VCRecordList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Response[VCRecordList]:
    """Fetch W3C credentials from wallet

    Args:
        count (Union[Unset, None, str]):
        start (Union[Unset, None, str]):
        wql (Union[Unset, None, str]):
        json_body (W3CCredentialsListRequest):

    Returns:
        Response[VCRecordList]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Optional[VCRecordList]:
    """Fetch W3C credentials from wallet

    Args:
        count (Union[Unset, None, str]):
        start (Union[Unset, None, str]):
        wql (Union[Unset, None, str]):
        json_body (W3CCredentialsListRequest):

    Returns:
        Response[VCRecordList]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        count=count,
        start=start,
        wql=wql,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Response[VCRecordList]:
    """Fetch W3C credentials from wallet

    Args:
        count (Union[Unset, None, str]):
        start (Union[Unset, None, str]):
        wql (Union[Unset, None, str]):
        json_body (W3CCredentialsListRequest):

    Returns:
        Response[VCRecordList]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: W3CCredentialsListRequest,
    count: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    wql: Union[Unset, None, str] = UNSET,
) -> Optional[VCRecordList]:
    """Fetch W3C credentials from wallet

    Args:
        count (Union[Unset, None, str]):
        start (Union[Unset, None, str]):
        wql (Union[Unset, None, str]):
        json_body (W3CCredentialsListRequest):

    Returns:
        Response[VCRecordList]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            count=count,
            start=start,
            wql=wql,
        )
    ).parsed
