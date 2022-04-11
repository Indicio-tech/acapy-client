from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.cred_revoked_result import CredRevokedResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    credential_id: str,
    *,
    client: Client,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/credential/revoked/{credential_id}".format(client.base_url, credential_id=credential_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CredRevokedResult]:
    if response.status_code == 200:
        response_200 = CredRevokedResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CredRevokedResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    credential_id: str,
    *,
    client: Client,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Response[CredRevokedResult]:
    """Query credential revocation status by id

    Args:
        credential_id (str):
        from_ (Union[Unset, None, str]):
        to (Union[Unset, None, str]):

    Returns:
        Response[CredRevokedResult]
    """

    kwargs = _get_kwargs(
        credential_id=credential_id,
        client=client,
        from_=from_,
        to=to,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    credential_id: str,
    *,
    client: Client,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Optional[CredRevokedResult]:
    """Query credential revocation status by id

    Args:
        credential_id (str):
        from_ (Union[Unset, None, str]):
        to (Union[Unset, None, str]):

    Returns:
        Response[CredRevokedResult]
    """

    return sync_detailed(
        credential_id=credential_id,
        client=client,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    credential_id: str,
    *,
    client: Client,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Response[CredRevokedResult]:
    """Query credential revocation status by id

    Args:
        credential_id (str):
        from_ (Union[Unset, None, str]):
        to (Union[Unset, None, str]):

    Returns:
        Response[CredRevokedResult]
    """

    kwargs = _get_kwargs(
        credential_id=credential_id,
        client=client,
        from_=from_,
        to=to,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    credential_id: str,
    *,
    client: Client,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Optional[CredRevokedResult]:
    """Query credential revocation status by id

    Args:
        credential_id (str):
        from_ (Union[Unset, None, str]):
        to (Union[Unset, None, str]):

    Returns:
        Response[CredRevokedResult]
    """

    return (
        await asyncio_detailed(
            credential_id=credential_id,
            client=client,
            from_=from_,
            to=to,
        )
    ).parsed
