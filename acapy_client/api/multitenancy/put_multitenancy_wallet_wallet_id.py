from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.update_wallet_request import UpdateWalletRequest
from ...models.wallet_record import WalletRecord
from ...types import Response


def _get_kwargs(
    wallet_id: str,
    *,
    client: Client,
    json_body: UpdateWalletRequest,
) -> Dict[str, Any]:
    url = "{}/multitenancy/wallet/{wallet_id}".format(client.base_url, wallet_id=wallet_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[WalletRecord]:
    if response.status_code == 200:
        response_200 = WalletRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[WalletRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    wallet_id: str,
    *,
    client: Client,
    json_body: UpdateWalletRequest,
) -> Response[WalletRecord]:
    """Update a subwallet

    Args:
        wallet_id (str):
        json_body (UpdateWalletRequest):

    Returns:
        Response[WalletRecord]
    """

    kwargs = _get_kwargs(
        wallet_id=wallet_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    wallet_id: str,
    *,
    client: Client,
    json_body: UpdateWalletRequest,
) -> Optional[WalletRecord]:
    """Update a subwallet

    Args:
        wallet_id (str):
        json_body (UpdateWalletRequest):

    Returns:
        Response[WalletRecord]
    """

    return sync_detailed(
        wallet_id=wallet_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    wallet_id: str,
    *,
    client: Client,
    json_body: UpdateWalletRequest,
) -> Response[WalletRecord]:
    """Update a subwallet

    Args:
        wallet_id (str):
        json_body (UpdateWalletRequest):

    Returns:
        Response[WalletRecord]
    """

    kwargs = _get_kwargs(
        wallet_id=wallet_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    wallet_id: str,
    *,
    client: Client,
    json_body: UpdateWalletRequest,
) -> Optional[WalletRecord]:
    """Update a subwallet

    Args:
        wallet_id (str):
        json_body (UpdateWalletRequest):

    Returns:
        Response[WalletRecord]
    """

    return (
        await asyncio_detailed(
            wallet_id=wallet_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
