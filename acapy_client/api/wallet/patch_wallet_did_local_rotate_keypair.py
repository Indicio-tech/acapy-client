from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.wallet_module_response import WalletModuleResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    did: str,
) -> Dict[str, Any]:
    url = "{}/wallet/did/local/rotate-keypair".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["did"] = did

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[WalletModuleResponse]:
    if response.status_code == 200:
        response_200 = WalletModuleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[WalletModuleResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    did: str,
) -> Response[WalletModuleResponse]:
    """Rotate keypair for a DID not posted to the ledger

    Args:
        did (str):

    Returns:
        Response[WalletModuleResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    did: str,
) -> Optional[WalletModuleResponse]:
    """Rotate keypair for a DID not posted to the ledger

    Args:
        did (str):

    Returns:
        Response[WalletModuleResponse]
    """

    return sync_detailed(
        client=client,
        did=did,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    did: str,
) -> Response[WalletModuleResponse]:
    """Rotate keypair for a DID not posted to the ledger

    Args:
        did (str):

    Returns:
        Response[WalletModuleResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    did: str,
) -> Optional[WalletModuleResponse]:
    """Rotate keypair for a DID not posted to the ledger

    Args:
        did (str):

    Returns:
        Response[WalletModuleResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            did=did,
        )
    ).parsed
