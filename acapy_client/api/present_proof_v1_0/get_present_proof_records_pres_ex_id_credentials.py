from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.indy_cred_precis import IndyCredPrecis
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pres_ex_id: str,
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    extra_query: Union[Unset, None, str] = UNSET,
    referent: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/present-proof/records/{pres_ex_id}/credentials".format(client.base_url, pres_ex_id=pres_ex_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["count"] = count

    params["extra_query"] = extra_query

    params["referent"] = referent

    params["start"] = start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[IndyCredPrecis]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IndyCredPrecis.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[IndyCredPrecis]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    pres_ex_id: str,
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    extra_query: Union[Unset, None, str] = UNSET,
    referent: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
) -> Response[List[IndyCredPrecis]]:
    """Fetch credentials for a presentation request from wallet

    Args:
        pres_ex_id (str):
        count (Union[Unset, None, str]):
        extra_query (Union[Unset, None, str]):
        referent (Union[Unset, None, str]):
        start (Union[Unset, None, str]):

    Returns:
        Response[List[IndyCredPrecis]]
    """

    kwargs = _get_kwargs(
        pres_ex_id=pres_ex_id,
        client=client,
        count=count,
        extra_query=extra_query,
        referent=referent,
        start=start,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    pres_ex_id: str,
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    extra_query: Union[Unset, None, str] = UNSET,
    referent: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
) -> Optional[List[IndyCredPrecis]]:
    """Fetch credentials for a presentation request from wallet

    Args:
        pres_ex_id (str):
        count (Union[Unset, None, str]):
        extra_query (Union[Unset, None, str]):
        referent (Union[Unset, None, str]):
        start (Union[Unset, None, str]):

    Returns:
        Response[List[IndyCredPrecis]]
    """

    return sync_detailed(
        pres_ex_id=pres_ex_id,
        client=client,
        count=count,
        extra_query=extra_query,
        referent=referent,
        start=start,
    ).parsed


async def asyncio_detailed(
    pres_ex_id: str,
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    extra_query: Union[Unset, None, str] = UNSET,
    referent: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
) -> Response[List[IndyCredPrecis]]:
    """Fetch credentials for a presentation request from wallet

    Args:
        pres_ex_id (str):
        count (Union[Unset, None, str]):
        extra_query (Union[Unset, None, str]):
        referent (Union[Unset, None, str]):
        start (Union[Unset, None, str]):

    Returns:
        Response[List[IndyCredPrecis]]
    """

    kwargs = _get_kwargs(
        pres_ex_id=pres_ex_id,
        client=client,
        count=count,
        extra_query=extra_query,
        referent=referent,
        start=start,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    pres_ex_id: str,
    *,
    client: Client,
    count: Union[Unset, None, str] = UNSET,
    extra_query: Union[Unset, None, str] = UNSET,
    referent: Union[Unset, None, str] = UNSET,
    start: Union[Unset, None, str] = UNSET,
) -> Optional[List[IndyCredPrecis]]:
    """Fetch credentials for a presentation request from wallet

    Args:
        pres_ex_id (str):
        count (Union[Unset, None, str]):
        extra_query (Union[Unset, None, str]):
        referent (Union[Unset, None, str]):
        start (Union[Unset, None, str]):

    Returns:
        Response[List[IndyCredPrecis]]
    """

    return (
        await asyncio_detailed(
            pres_ex_id=pres_ex_id,
            client=client,
            count=count,
            extra_query=extra_query,
            referent=referent,
            start=start,
        )
    ).parsed
