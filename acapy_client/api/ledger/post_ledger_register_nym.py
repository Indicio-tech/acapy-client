from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.post_ledger_register_nym_role import PostLedgerRegisterNymRole
from ...models.register_ledger_nym_response import RegisterLedgerNymResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    did: str,
    verkey: str,
    alias: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, PostLedgerRegisterNymRole] = UNSET,
) -> Dict[str, Any]:
    url = "{}/ledger/register-nym".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["did"] = did

    params["verkey"] = verkey

    params["alias"] = alias

    json_role: Union[Unset, None, str] = UNSET
    if not isinstance(role, Unset):
        json_role = role.value if role else None

    params["role"] = json_role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[RegisterLedgerNymResponse]:
    if response.status_code == 200:
        response_200 = RegisterLedgerNymResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RegisterLedgerNymResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    did: str,
    verkey: str,
    alias: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, PostLedgerRegisterNymRole] = UNSET,
) -> Response[RegisterLedgerNymResponse]:
    """Send a NYM registration to the ledger.

    Args:
        did (str):
        verkey (str):
        alias (Union[Unset, None, str]):
        role (Union[Unset, None, PostLedgerRegisterNymRole]):

    Returns:
        Response[RegisterLedgerNymResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
        verkey=verkey,
        alias=alias,
        role=role,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    did: str,
    verkey: str,
    alias: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, PostLedgerRegisterNymRole] = UNSET,
) -> Optional[RegisterLedgerNymResponse]:
    """Send a NYM registration to the ledger.

    Args:
        did (str):
        verkey (str):
        alias (Union[Unset, None, str]):
        role (Union[Unset, None, PostLedgerRegisterNymRole]):

    Returns:
        Response[RegisterLedgerNymResponse]
    """

    return sync_detailed(
        client=client,
        did=did,
        verkey=verkey,
        alias=alias,
        role=role,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    did: str,
    verkey: str,
    alias: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, PostLedgerRegisterNymRole] = UNSET,
) -> Response[RegisterLedgerNymResponse]:
    """Send a NYM registration to the ledger.

    Args:
        did (str):
        verkey (str):
        alias (Union[Unset, None, str]):
        role (Union[Unset, None, PostLedgerRegisterNymRole]):

    Returns:
        Response[RegisterLedgerNymResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
        verkey=verkey,
        alias=alias,
        role=role,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    did: str,
    verkey: str,
    alias: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, PostLedgerRegisterNymRole] = UNSET,
) -> Optional[RegisterLedgerNymResponse]:
    """Send a NYM registration to the ledger.

    Args:
        did (str):
        verkey (str):
        alias (Union[Unset, None, str]):
        role (Union[Unset, None, PostLedgerRegisterNymRole]):

    Returns:
        Response[RegisterLedgerNymResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            did=did,
            verkey=verkey,
            alias=alias,
            role=role,
        )
    ).parsed
