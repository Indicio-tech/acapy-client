from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.cred_rev_record_details_result import CredRevRecordDetailsResult
from ...types import Response


def _get_kwargs(
    rev_reg_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/revocation/registry/{rev_reg_id}/issued/details".format(client.base_url, rev_reg_id=rev_reg_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[CredRevRecordDetailsResult]:
    if response.status_code == 200:
        response_200 = CredRevRecordDetailsResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CredRevRecordDetailsResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    rev_reg_id: str,
    *,
    client: Client,
) -> Response[CredRevRecordDetailsResult]:
    """Get details of credentials issued against revocation registry

    Args:
        rev_reg_id (str):

    Returns:
        Response[CredRevRecordDetailsResult]
    """

    kwargs = _get_kwargs(
        rev_reg_id=rev_reg_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    rev_reg_id: str,
    *,
    client: Client,
) -> Optional[CredRevRecordDetailsResult]:
    """Get details of credentials issued against revocation registry

    Args:
        rev_reg_id (str):

    Returns:
        Response[CredRevRecordDetailsResult]
    """

    return sync_detailed(
        rev_reg_id=rev_reg_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    rev_reg_id: str,
    *,
    client: Client,
) -> Response[CredRevRecordDetailsResult]:
    """Get details of credentials issued against revocation registry

    Args:
        rev_reg_id (str):

    Returns:
        Response[CredRevRecordDetailsResult]
    """

    kwargs = _get_kwargs(
        rev_reg_id=rev_reg_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    rev_reg_id: str,
    *,
    client: Client,
) -> Optional[CredRevRecordDetailsResult]:
    """Get details of credentials issued against revocation registry

    Args:
        rev_reg_id (str):

    Returns:
        Response[CredRevRecordDetailsResult]
    """

    return (
        await asyncio_detailed(
            rev_reg_id=rev_reg_id,
            client=client,
        )
    ).parsed
