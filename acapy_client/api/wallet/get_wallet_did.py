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

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_key_type: Union[Unset, None, str] = UNSET
    if not isinstance(key_type, Unset):
        json_key_type = key_type.value if key_type else None

    json_method: Union[Unset, None, str] = UNSET
    if not isinstance(method, Unset):
        json_method = method.value if method else None

    json_posture: Union[Unset, None, str] = UNSET
    if not isinstance(posture, Unset):
        json_posture = posture.value if posture else None

    params: Dict[str, Any] = {
        "did": did,
        "key_type": json_key_type,
        "method": json_method,
        "posture": json_posture,
        "verkey": verkey,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
        "verify": client.verify_ssl,
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
    kwargs = _get_kwargs(
        client=client,
        did=did,
        key_type=key_type,
        method=method,
        posture=posture,
        verkey=verkey,
    )

    response = httpx.get(
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
    """ """

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
    kwargs = _get_kwargs(
        client=client,
        did=did,
        key_type=key_type,
        method=method,
        posture=posture,
        verkey=verkey,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

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
    """ """

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
