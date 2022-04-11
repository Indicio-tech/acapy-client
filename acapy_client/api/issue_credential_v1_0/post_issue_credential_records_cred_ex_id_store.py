from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v10_credential_exchange import V10CredentialExchange
from ...models.v10_credential_store_request import V10CredentialStoreRequest
from ...types import Response


def _get_kwargs(
    cred_ex_id: str,
    *,
    client: Client,
    json_body: V10CredentialStoreRequest,
) -> Dict[str, Any]:
    url = "{}/issue-credential/records/{cred_ex_id}/store".format(client.base_url, cred_ex_id=cred_ex_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[V10CredentialExchange]:
    if response.status_code == 200:
        response_200 = V10CredentialExchange.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V10CredentialExchange]:
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
    json_body: V10CredentialStoreRequest,
) -> Response[V10CredentialExchange]:
    """Store a received credential

    Args:
        cred_ex_id (str):
        json_body (V10CredentialStoreRequest):

    Returns:
        Response[V10CredentialExchange]
    """

    kwargs = _get_kwargs(
        cred_ex_id=cred_ex_id,
        client=client,
        json_body=json_body,
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
    json_body: V10CredentialStoreRequest,
) -> Optional[V10CredentialExchange]:
    """Store a received credential

    Args:
        cred_ex_id (str):
        json_body (V10CredentialStoreRequest):

    Returns:
        Response[V10CredentialExchange]
    """

    return sync_detailed(
        cred_ex_id=cred_ex_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cred_ex_id: str,
    *,
    client: Client,
    json_body: V10CredentialStoreRequest,
) -> Response[V10CredentialExchange]:
    """Store a received credential

    Args:
        cred_ex_id (str):
        json_body (V10CredentialStoreRequest):

    Returns:
        Response[V10CredentialExchange]
    """

    kwargs = _get_kwargs(
        cred_ex_id=cred_ex_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cred_ex_id: str,
    *,
    client: Client,
    json_body: V10CredentialStoreRequest,
) -> Optional[V10CredentialExchange]:
    """Store a received credential

    Args:
        cred_ex_id (str):
        json_body (V10CredentialStoreRequest):

    Returns:
        Response[V10CredentialExchange]
    """

    return (
        await asyncio_detailed(
            cred_ex_id=cred_ex_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
