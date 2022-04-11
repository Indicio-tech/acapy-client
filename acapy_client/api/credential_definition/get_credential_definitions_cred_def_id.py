from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.credential_definition_get_result import CredentialDefinitionGetResult
from ...types import Response


def _get_kwargs(
    cred_def_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/credential-definitions/{cred_def_id}".format(client.base_url, cred_def_id=cred_def_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[CredentialDefinitionGetResult]:
    if response.status_code == 200:
        response_200 = CredentialDefinitionGetResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CredentialDefinitionGetResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cred_def_id: str,
    *,
    client: Client,
) -> Response[CredentialDefinitionGetResult]:
    """Gets a credential definition from the ledger

    Args:
        cred_def_id (str):

    Returns:
        Response[CredentialDefinitionGetResult]
    """

    kwargs = _get_kwargs(
        cred_def_id=cred_def_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cred_def_id: str,
    *,
    client: Client,
) -> Optional[CredentialDefinitionGetResult]:
    """Gets a credential definition from the ledger

    Args:
        cred_def_id (str):

    Returns:
        Response[CredentialDefinitionGetResult]
    """

    return sync_detailed(
        cred_def_id=cred_def_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cred_def_id: str,
    *,
    client: Client,
) -> Response[CredentialDefinitionGetResult]:
    """Gets a credential definition from the ledger

    Args:
        cred_def_id (str):

    Returns:
        Response[CredentialDefinitionGetResult]
    """

    kwargs = _get_kwargs(
        cred_def_id=cred_def_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cred_def_id: str,
    *,
    client: Client,
) -> Optional[CredentialDefinitionGetResult]:
    """Gets a credential definition from the ledger

    Args:
        cred_def_id (str):

    Returns:
        Response[CredentialDefinitionGetResult]
    """

    return (
        await asyncio_detailed(
            cred_def_id=cred_def_id,
            client=client,
        )
    ).parsed
