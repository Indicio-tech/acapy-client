from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.create_wallet_token_request import CreateWalletTokenRequest
from ...models.create_wallet_token_response import CreateWalletTokenResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    wallet_id: str,
    json_body: CreateWalletTokenRequest,
) -> Dict[str, Any]:
    url = "{}/multitenancy/wallet/{wallet_id}/token".format(client.base_url, wallet_id=wallet_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CreateWalletTokenResponse]:
    if response.status_code == 200:
        response_200 = CreateWalletTokenResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CreateWalletTokenResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    wallet_id: str,
    json_body: CreateWalletTokenRequest,
) -> Response[CreateWalletTokenResponse]:
    kwargs = _get_kwargs(
        client=client,
        wallet_id=wallet_id,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    wallet_id: str,
    json_body: CreateWalletTokenRequest,
) -> Optional[CreateWalletTokenResponse]:
    """ """

    return sync_detailed(
        client=client,
        wallet_id=wallet_id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    wallet_id: str,
    json_body: CreateWalletTokenRequest,
) -> Response[CreateWalletTokenResponse]:
    kwargs = _get_kwargs(
        client=client,
        wallet_id=wallet_id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    wallet_id: str,
    json_body: CreateWalletTokenRequest,
) -> Optional[CreateWalletTokenResponse]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            wallet_id=wallet_id,
            json_body=json_body,
        )
    ).parsed
