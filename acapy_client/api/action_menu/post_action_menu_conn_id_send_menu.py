from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.action_menu_modules_result import ActionMenuModulesResult
from ...models.send_menu import SendMenu
from ...types import Response


def _get_kwargs(
    conn_id: str,
    *,
    client: Client,
    json_body: SendMenu,
) -> Dict[str, Any]:
    url = "{}/action-menu/{conn_id}/send-menu".format(client.base_url, conn_id=conn_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[ActionMenuModulesResult]:
    if response.status_code == 200:
        response_200 = ActionMenuModulesResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionMenuModulesResult]:
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
    json_body: SendMenu,
) -> Response[ActionMenuModulesResult]:
    """Send an action menu to a connection

    Args:
        conn_id (str):
        json_body (SendMenu):

    Returns:
        Response[ActionMenuModulesResult]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        json_body=json_body,
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
    json_body: SendMenu,
) -> Optional[ActionMenuModulesResult]:
    """Send an action menu to a connection

    Args:
        conn_id (str):
        json_body (SendMenu):

    Returns:
        Response[ActionMenuModulesResult]
    """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    *,
    client: Client,
    json_body: SendMenu,
) -> Response[ActionMenuModulesResult]:
    """Send an action menu to a connection

    Args:
        conn_id (str):
        json_body (SendMenu):

    Returns:
        Response[ActionMenuModulesResult]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    *,
    client: Client,
    json_body: SendMenu,
) -> Optional[ActionMenuModulesResult]:
    """Send an action menu to a connection

    Args:
        conn_id (str):
        json_body (SendMenu):

    Returns:
        Response[ActionMenuModulesResult]
    """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
