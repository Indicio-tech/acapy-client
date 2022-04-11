from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_mediation_keylists_role import GetMediationKeylistsRole
from ...models.keylist import Keylist
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    conn_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetMediationKeylistsRole] = GetMediationKeylistsRole.SERVER,
) -> Dict[str, Any]:
    url = "{}/mediation/keylists".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["conn_id"] = conn_id

    json_role: Union[Unset, None, str] = UNSET
    if not isinstance(role, Unset):
        json_role = role.value if role else None

    params["role"] = json_role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Keylist]:
    if response.status_code == 200:
        response_200 = Keylist.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Keylist]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    conn_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetMediationKeylistsRole] = GetMediationKeylistsRole.SERVER,
) -> Response[Keylist]:
    """Retrieve keylists by connection or role

    Args:
        conn_id (Union[Unset, None, str]):
        role (Union[Unset, None, GetMediationKeylistsRole]):  Default:
            GetMediationKeylistsRole.SERVER.

    Returns:
        Response[Keylist]
    """

    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
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
    conn_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetMediationKeylistsRole] = GetMediationKeylistsRole.SERVER,
) -> Optional[Keylist]:
    """Retrieve keylists by connection or role

    Args:
        conn_id (Union[Unset, None, str]):
        role (Union[Unset, None, GetMediationKeylistsRole]):  Default:
            GetMediationKeylistsRole.SERVER.

    Returns:
        Response[Keylist]
    """

    return sync_detailed(
        client=client,
        conn_id=conn_id,
        role=role,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    conn_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetMediationKeylistsRole] = GetMediationKeylistsRole.SERVER,
) -> Response[Keylist]:
    """Retrieve keylists by connection or role

    Args:
        conn_id (Union[Unset, None, str]):
        role (Union[Unset, None, GetMediationKeylistsRole]):  Default:
            GetMediationKeylistsRole.SERVER.

    Returns:
        Response[Keylist]
    """

    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        role=role,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    conn_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetMediationKeylistsRole] = GetMediationKeylistsRole.SERVER,
) -> Optional[Keylist]:
    """Retrieve keylists by connection or role

    Args:
        conn_id (Union[Unset, None, str]):
        role (Union[Unset, None, GetMediationKeylistsRole]):  Default:
            GetMediationKeylistsRole.SERVER.

    Returns:
        Response[Keylist]
    """

    return (
        await asyncio_detailed(
            client=client,
            conn_id=conn_id,
            role=role,
        )
    ).parsed
