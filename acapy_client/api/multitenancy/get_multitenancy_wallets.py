from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.wallet_list import WalletList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    wallet_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/multitenancy/wallets".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["wallet_name"] = wallet_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[WalletList]:
    if response.status_code == 200:
        response_200 = WalletList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[WalletList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    wallet_name: Union[Unset, None, str] = UNSET,
) -> Response[WalletList]:
    """Query subwallets

    Args:
        wallet_name (Union[Unset, None, str]):

    Returns:
        Response[WalletList]
    """

    kwargs = _get_kwargs(
        client=client,
        wallet_name=wallet_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    wallet_name: Union[Unset, None, str] = UNSET,
) -> Optional[WalletList]:
    """Query subwallets

    Args:
        wallet_name (Union[Unset, None, str]):

    Returns:
        Response[WalletList]
    """

    return sync_detailed(
        client=client,
        wallet_name=wallet_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    wallet_name: Union[Unset, None, str] = UNSET,
) -> Response[WalletList]:
    """Query subwallets

    Args:
        wallet_name (Union[Unset, None, str]):

    Returns:
        Response[WalletList]
    """

    kwargs = _get_kwargs(
        client=client,
        wallet_name=wallet_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    wallet_name: Union[Unset, None, str] = UNSET,
) -> Optional[WalletList]:
    """Query subwallets

    Args:
        wallet_name (Union[Unset, None, str]):

    Returns:
        Response[WalletList]
    """

    return (
        await asyncio_detailed(
            client=client,
            wallet_name=wallet_name,
        )
    ).parsed
