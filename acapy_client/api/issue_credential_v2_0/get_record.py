from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v20_cred_ex_record_detail import V20CredExRecordDetail
from ...types import Response


def _get_kwargs(
    cred_ex_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/issue-credential-2.0/records/{cred_ex_id}".format(client.base_url, cred_ex_id=cred_ex_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[V20CredExRecordDetail]:
    if response.status_code == 200:
        response_200 = V20CredExRecordDetail.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V20CredExRecordDetail]:
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
) -> Response[V20CredExRecordDetail]:
    """Fetch a single credential exchange record

    Args:
        cred_ex_id (str):

    Returns:
        Response[V20CredExRecordDetail]
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
) -> Optional[V20CredExRecordDetail]:
    """Fetch a single credential exchange record

    Args:
        cred_ex_id (str):

    Returns:
        Response[V20CredExRecordDetail]
    """

    return sync_detailed(
        cred_ex_id=cred_ex_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cred_ex_id: str,
    *,
    client: Client,
) -> Response[V20CredExRecordDetail]:
    """Fetch a single credential exchange record

    Args:
        cred_ex_id (str):

    Returns:
        Response[V20CredExRecordDetail]
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
) -> Optional[V20CredExRecordDetail]:
    """Fetch a single credential exchange record

    Args:
        cred_ex_id (str):

    Returns:
        Response[V20CredExRecordDetail]
    """

    return (
        await asyncio_detailed(
            cred_ex_id=cred_ex_id,
            client=client,
        )
    ).parsed
