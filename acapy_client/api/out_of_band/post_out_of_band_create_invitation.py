from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.invitation_create_request import InvitationCreateRequest
from ...models.invitation_record import InvitationRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: InvitationCreateRequest,
    auto_accept: Union[Unset, None, bool] = UNSET,
    multi_use: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/out-of-band/create-invitation".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["auto_accept"] = auto_accept

    params["multi_use"] = multi_use

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[InvitationRecord]:
    if response.status_code == 200:
        response_200 = InvitationRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[InvitationRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: InvitationCreateRequest,
    auto_accept: Union[Unset, None, bool] = UNSET,
    multi_use: Union[Unset, None, bool] = UNSET,
) -> Response[InvitationRecord]:
    """Create a new connection invitation

    Args:
        auto_accept (Union[Unset, None, bool]):
        multi_use (Union[Unset, None, bool]):
        json_body (InvitationCreateRequest):

    Returns:
        Response[InvitationRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        auto_accept=auto_accept,
        multi_use=multi_use,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: InvitationCreateRequest,
    auto_accept: Union[Unset, None, bool] = UNSET,
    multi_use: Union[Unset, None, bool] = UNSET,
) -> Optional[InvitationRecord]:
    """Create a new connection invitation

    Args:
        auto_accept (Union[Unset, None, bool]):
        multi_use (Union[Unset, None, bool]):
        json_body (InvitationCreateRequest):

    Returns:
        Response[InvitationRecord]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        auto_accept=auto_accept,
        multi_use=multi_use,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: InvitationCreateRequest,
    auto_accept: Union[Unset, None, bool] = UNSET,
    multi_use: Union[Unset, None, bool] = UNSET,
) -> Response[InvitationRecord]:
    """Create a new connection invitation

    Args:
        auto_accept (Union[Unset, None, bool]):
        multi_use (Union[Unset, None, bool]):
        json_body (InvitationCreateRequest):

    Returns:
        Response[InvitationRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        auto_accept=auto_accept,
        multi_use=multi_use,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: InvitationCreateRequest,
    auto_accept: Union[Unset, None, bool] = UNSET,
    multi_use: Union[Unset, None, bool] = UNSET,
) -> Optional[InvitationRecord]:
    """Create a new connection invitation

    Args:
        auto_accept (Union[Unset, None, bool]):
        multi_use (Union[Unset, None, bool]):
        json_body (InvitationCreateRequest):

    Returns:
        Response[InvitationRecord]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            auto_accept=auto_accept,
            multi_use=multi_use,
        )
    ).parsed
