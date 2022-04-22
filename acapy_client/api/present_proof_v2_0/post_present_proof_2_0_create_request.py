from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v20_pres_create_request_request import V20PresCreateRequestRequest
from ...models.v20_pres_ex_record import V20PresExRecord
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: V20PresCreateRequestRequest,
) -> Dict[str, Any]:
    url = "{}/present-proof-2.0/create-request".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[V20PresExRecord]:
    if response.status_code == 200:
        response_200 = V20PresExRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V20PresExRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: V20PresCreateRequestRequest,
) -> Response[V20PresExRecord]:
    """Creates a presentation request not bound to any proposal or connection

    Args:
        json_body (V20PresCreateRequestRequest):

    Returns:
        Response[V20PresExRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: V20PresCreateRequestRequest,
) -> Optional[V20PresExRecord]:
    """Creates a presentation request not bound to any proposal or connection

    Args:
        json_body (V20PresCreateRequestRequest):

    Returns:
        Response[V20PresExRecord]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: V20PresCreateRequestRequest,
) -> Response[V20PresExRecord]:
    """Creates a presentation request not bound to any proposal or connection

    Args:
        json_body (V20PresCreateRequestRequest):

    Returns:
        Response[V20PresExRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: V20PresCreateRequestRequest,
) -> Optional[V20PresExRecord]:
    """Creates a presentation request not bound to any proposal or connection

    Args:
        json_body (V20PresCreateRequestRequest):

    Returns:
        Response[V20PresExRecord]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
