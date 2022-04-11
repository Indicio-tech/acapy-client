from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.action_menu_fetch_result import ActionMenuFetchResult
from ...types import Response


def _get_kwargs(
    conn_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/action-menu/{conn_id}/fetch".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionMenuFetchResult]:
    if response.status_code == 200:
        response_200 = ActionMenuFetchResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionMenuFetchResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    conn_id: str,
    *,
    client: Client,
) -> Response[ActionMenuFetchResult]:
    """Fetch the active menu

    Args:
        conn_id (str):

    Returns:
        Response[ActionMenuFetchResult]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    conn_id: str,
    *,
    client: Client,
) -> Optional[ActionMenuFetchResult]:
    """Fetch the active menu

    Args:
        conn_id (str):

    Returns:
        Response[ActionMenuFetchResult]
    """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    *,
    client: Client,
) -> Response[ActionMenuFetchResult]:
    """Fetch the active menu

    Args:
        conn_id (str):

    Returns:
        Response[ActionMenuFetchResult]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    *,
    client: Client,
) -> Optional[ActionMenuFetchResult]:
    """Fetch the active menu

    Args:
        conn_id (str):

    Returns:
        Response[ActionMenuFetchResult]
    """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
        )
    ).parsed
