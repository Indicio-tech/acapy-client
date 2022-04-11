from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.endorser_info import EndorserInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conn_id: str,
    *,
    client: Client,
    endorser_did: str,
    endorser_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/transactions/{conn_id}/set-endorser-info".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["endorser_did"] = endorser_did

    params["endorser_name"] = endorser_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[EndorserInfo]:
    if response.status_code == 200:
        response_200 = EndorserInfo.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[EndorserInfo]:
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
    endorser_did: str,
    endorser_name: Union[Unset, None, str] = UNSET,
) -> Response[EndorserInfo]:
    """Set Endorser Info

    Args:
        conn_id (str):
        endorser_did (str):
        endorser_name (Union[Unset, None, str]):

    Returns:
        Response[EndorserInfo]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        endorser_did=endorser_did,
        endorser_name=endorser_name,
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
    endorser_did: str,
    endorser_name: Union[Unset, None, str] = UNSET,
) -> Optional[EndorserInfo]:
    """Set Endorser Info

    Args:
        conn_id (str):
        endorser_did (str):
        endorser_name (Union[Unset, None, str]):

    Returns:
        Response[EndorserInfo]
    """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
        endorser_did=endorser_did,
        endorser_name=endorser_name,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    *,
    client: Client,
    endorser_did: str,
    endorser_name: Union[Unset, None, str] = UNSET,
) -> Response[EndorserInfo]:
    """Set Endorser Info

    Args:
        conn_id (str):
        endorser_did (str):
        endorser_name (Union[Unset, None, str]):

    Returns:
        Response[EndorserInfo]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        endorser_did=endorser_did,
        endorser_name=endorser_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    *,
    client: Client,
    endorser_did: str,
    endorser_name: Union[Unset, None, str] = UNSET,
) -> Optional[EndorserInfo]:
    """Set Endorser Info

    Args:
        conn_id (str):
        endorser_did (str):
        endorser_name (Union[Unset, None, str]):

    Returns:
        Response[EndorserInfo]
    """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
            endorser_did=endorser_did,
            endorser_name=endorser_name,
        )
    ).parsed
