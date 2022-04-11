from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.did_list import DIDList
from ...models.get_wallet_did_key_type import GetWalletDidKeyType
from ...models.get_wallet_did_method import GetWalletDidMethod
from ...models.get_wallet_did_posture import GetWalletDidPosture
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    did: Union[Unset, None, str] = UNSET,
    key_type: Union[Unset, None, GetWalletDidKeyType] = UNSET,
    method: Union[Unset, None, GetWalletDidMethod] = UNSET,
    posture: Union[Unset, None, GetWalletDidPosture] = UNSET,
    verkey: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/wallet/did".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["did"] = did

    json_key_type: Union[Unset, None, str] = UNSET
    if not isinstance(key_type, Unset):
        json_key_type = key_type.value if key_type else None

    params["key_type"] = json_key_type

    json_method: Union[Unset, None, str] = UNSET
    if not isinstance(method, Unset):
        json_method = method.value if method else None

    params["method"] = json_method

    json_posture: Union[Unset, None, str] = UNSET
    if not isinstance(posture, Unset):
        json_posture = posture.value if posture else None

    params["posture"] = json_posture

    params["verkey"] = verkey

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[DIDList]:
    if response.status_code == 200:
        response_200 = DIDList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DIDList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    did: Union[Unset, None, str] = UNSET,
    key_type: Union[Unset, None, GetWalletDidKeyType] = UNSET,
    method: Union[Unset, None, GetWalletDidMethod] = UNSET,
    posture: Union[Unset, None, GetWalletDidPosture] = UNSET,
    verkey: Union[Unset, None, str] = UNSET,
) -> Response[DIDList]:
    """List wallet DIDs

    Args:
        did (Union[Unset, None, str]):
        key_type (Union[Unset, None, GetWalletDidKeyType]):
        method (Union[Unset, None, GetWalletDidMethod]):
        posture (Union[Unset, None, GetWalletDidPosture]):
        verkey (Union[Unset, None, str]):

    Returns:
        Response[DIDList]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
        key_type=key_type,
        method=method,
        posture=posture,
        verkey=verkey,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    did: Union[Unset, None, str] = UNSET,
    key_type: Union[Unset, None, GetWalletDidKeyType] = UNSET,
    method: Union[Unset, None, GetWalletDidMethod] = UNSET,
    posture: Union[Unset, None, GetWalletDidPosture] = UNSET,
    verkey: Union[Unset, None, str] = UNSET,
) -> Optional[DIDList]:
    """List wallet DIDs

    Args:
        did (Union[Unset, None, str]):
        key_type (Union[Unset, None, GetWalletDidKeyType]):
        method (Union[Unset, None, GetWalletDidMethod]):
        posture (Union[Unset, None, GetWalletDidPosture]):
        verkey (Union[Unset, None, str]):

    Returns:
        Response[DIDList]
    """

    return sync_detailed(
        client=client,
        did=did,
        key_type=key_type,
        method=method,
        posture=posture,
        verkey=verkey,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    did: Union[Unset, None, str] = UNSET,
    key_type: Union[Unset, None, GetWalletDidKeyType] = UNSET,
    method: Union[Unset, None, GetWalletDidMethod] = UNSET,
    posture: Union[Unset, None, GetWalletDidPosture] = UNSET,
    verkey: Union[Unset, None, str] = UNSET,
) -> Response[DIDList]:
    """List wallet DIDs

    Args:
        did (Union[Unset, None, str]):
        key_type (Union[Unset, None, GetWalletDidKeyType]):
        method (Union[Unset, None, GetWalletDidMethod]):
        posture (Union[Unset, None, GetWalletDidPosture]):
        verkey (Union[Unset, None, str]):

    Returns:
        Response[DIDList]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
        key_type=key_type,
        method=method,
        posture=posture,
        verkey=verkey,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    did: Union[Unset, None, str] = UNSET,
    key_type: Union[Unset, None, GetWalletDidKeyType] = UNSET,
    method: Union[Unset, None, GetWalletDidMethod] = UNSET,
    posture: Union[Unset, None, GetWalletDidPosture] = UNSET,
    verkey: Union[Unset, None, str] = UNSET,
) -> Optional[DIDList]:
    """List wallet DIDs

    Args:
        did (Union[Unset, None, str]):
        key_type (Union[Unset, None, GetWalletDidKeyType]):
        method (Union[Unset, None, GetWalletDidMethod]):
        posture (Union[Unset, None, GetWalletDidPosture]):
        verkey (Union[Unset, None, str]):

    Returns:
        Response[DIDList]
    """

    return (
        await asyncio_detailed(
            client=client,
            did=did,
            key_type=key_type,
            method=method,
            posture=posture,
            verkey=verkey,
        )
    ).parsed
