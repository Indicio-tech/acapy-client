from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.get_nym_role_response import GetNymRoleResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    did: str,
) -> Dict[str, Any]:
    url = "{}/ledger/get-nym-role".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["did"] = did

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetNymRoleResponse]:
    if response.status_code == 200:
        response_200 = GetNymRoleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetNymRoleResponse]:
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
) -> Response[GetNymRoleResponse]:
    """Get the role from the NYM registration of a public DID.

    Args:
        did (str):

    Returns:
        Response[GetNymRoleResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
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
) -> Optional[GetNymRoleResponse]:
    """Get the role from the NYM registration of a public DID.

    Args:
        did (str):

    Returns:
        Response[GetNymRoleResponse]
    """

    return sync_detailed(
        client=client,
        did=did,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    did: str,
) -> Response[GetNymRoleResponse]:
    """Get the role from the NYM registration of a public DID.

    Args:
        did (str):

    Returns:
        Response[GetNymRoleResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    did: str,
) -> Optional[GetNymRoleResponse]:
    """Get the role from the NYM registration of a public DID.

    Args:
        did (str):

    Returns:
        Response[GetNymRoleResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            did=did,
        )
    ).parsed
