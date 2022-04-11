from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.issue_credential_module_response import IssueCredentialModuleResponse
from ...types import Response


def _get_kwargs(
    cred_ex_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/issue-credential/records/{cred_ex_id}".format(client.base_url, cred_ex_id=cred_ex_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[IssueCredentialModuleResponse]:
    if response.status_code == 200:
        response_200 = IssueCredentialModuleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IssueCredentialModuleResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cred_ex_id: str,
    *,
    client: Client,
) -> Response[IssueCredentialModuleResponse]:
    """Remove an existing credential exchange record

    Args:
        cred_ex_id (str):

    Returns:
        Response[IssueCredentialModuleResponse]
    """

    kwargs = _get_kwargs(
        cred_ex_id=cred_ex_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cred_ex_id: str,
    *,
    client: Client,
) -> Optional[IssueCredentialModuleResponse]:
    """Remove an existing credential exchange record

    Args:
        cred_ex_id (str):

    Returns:
        Response[IssueCredentialModuleResponse]
    """

    return sync_detailed(
        cred_ex_id=cred_ex_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cred_ex_id: str,
    *,
    client: Client,
) -> Response[IssueCredentialModuleResponse]:
    """Remove an existing credential exchange record

    Args:
        cred_ex_id (str):

    Returns:
        Response[IssueCredentialModuleResponse]
    """

    kwargs = _get_kwargs(
        cred_ex_id=cred_ex_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cred_ex_id: str,
    *,
    client: Client,
) -> Optional[IssueCredentialModuleResponse]:
    """Remove an existing credential exchange record

    Args:
        cred_ex_id (str):

    Returns:
        Response[IssueCredentialModuleResponse]
    """

    return (
        await asyncio_detailed(
            cred_ex_id=cred_ex_id,
            client=client,
        )
    ).parsed
