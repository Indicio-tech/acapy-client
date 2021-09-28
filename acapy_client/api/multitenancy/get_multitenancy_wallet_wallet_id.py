from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.wallet_record import WalletRecord
from ...types import Response


def _get_kwargs(
    wallet_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/multitenancy/wallet/{wallet_id}".format(client.base_url, wallet_id=wallet_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "verify": client.verify_ssl,
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
) -> Response[WalletRecord]:
    kwargs = _get_kwargs(
        wallet_id=wallet_id,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    wallet_id: str,
    *,
    client: Client,
) -> Optional[WalletRecord]:
    """ """

    return sync_detailed(
        wallet_id=wallet_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    wallet_id: str,
    *,
    client: Client,
) -> Response[WalletRecord]:
    kwargs = _get_kwargs(
        wallet_id=wallet_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    wallet_id: str,
    *,
    client: Client,
) -> Optional[WalletRecord]:
    """ """

    return (
        await asyncio_detailed(
            wallet_id=wallet_id,
            client=client,
        )
    ).parsed
