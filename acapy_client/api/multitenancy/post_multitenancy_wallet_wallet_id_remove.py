from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.multitenant_module_response import MultitenantModuleResponse
from ...models.remove_wallet_request import RemoveWalletRequest
from ...types import Response


def _get_kwargs(
    wallet_id: str,
    *,
    client: Client,
    json_body: RemoveWalletRequest,
) -> Dict[str, Any]:
    url = "{}/multitenancy/wallet/{wallet_id}/remove".format(client.base_url, wallet_id=wallet_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[MultitenantModuleResponse]:
    if response.status_code == 200:
        response_200 = MultitenantModuleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[MultitenantModuleResponse]:
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
    json_body: RemoveWalletRequest,
) -> Response[MultitenantModuleResponse]:
    kwargs = _get_kwargs(
        wallet_id=wallet_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    wallet_id: str,
    *,
    client: Client,
    json_body: RemoveWalletRequest,
) -> Optional[MultitenantModuleResponse]:
    """ """

    return sync_detailed(
        wallet_id=wallet_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    wallet_id: str,
    *,
    client: Client,
    json_body: RemoveWalletRequest,
) -> Response[MultitenantModuleResponse]:
    kwargs = _get_kwargs(
        wallet_id=wallet_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    wallet_id: str,
    *,
    client: Client,
    json_body: RemoveWalletRequest,
) -> Optional[MultitenantModuleResponse]:
    """ """

    return (
        await asyncio_detailed(
            wallet_id=wallet_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
