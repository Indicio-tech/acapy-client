from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.ledger_config_list import LedgerConfigList
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ledger/multiple/config".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[LedgerConfigList]:
    if response.status_code == 200:
        response_200 = LedgerConfigList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[LedgerConfigList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[LedgerConfigList]:
    """Fetch the multiple ledger configuration currently in use

    Returns:
        Response[LedgerConfigList]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[LedgerConfigList]:
    """Fetch the multiple ledger configuration currently in use

    Returns:
        Response[LedgerConfigList]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[LedgerConfigList]:
    """Fetch the multiple ledger configuration currently in use

    Returns:
        Response[LedgerConfigList]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[LedgerConfigList]:
    """Fetch the multiple ledger configuration currently in use

    Returns:
        Response[LedgerConfigList]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
