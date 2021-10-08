from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.basic_message_module_response import BasicMessageModuleResponse
from ...models.send_message import SendMessage
from ...types import Response


def _get_kwargs(
    conn_id: str,
    *,
    client: Client,
    json_body: SendMessage,
) -> Dict[str, Any]:
    url = "{}/connections/{conn_id}/send-message".format(client.base_url, conn_id=conn_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[BasicMessageModuleResponse]:
    if response.status_code == 200:
        response_200 = BasicMessageModuleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[BasicMessageModuleResponse]:
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
    json_body: SendMessage,
) -> Response[BasicMessageModuleResponse]:
    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    conn_id: str,
    *,
    client: Client,
    json_body: SendMessage,
) -> Optional[BasicMessageModuleResponse]:
    """ """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    *,
    client: Client,
    json_body: SendMessage,
) -> Response[BasicMessageModuleResponse]:
    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    *,
    client: Client,
    json_body: SendMessage,
) -> Optional[BasicMessageModuleResponse]:
    """ """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
