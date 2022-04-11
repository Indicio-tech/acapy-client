from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.conn_record import ConnRecord
from ...models.receive_invitation_request import ReceiveInvitationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: ReceiveInvitationRequest,
    alias: Union[Unset, None, str] = UNSET,
    auto_accept: Union[Unset, None, bool] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/connections/receive-invitation".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["alias"] = alias

    params["auto_accept"] = auto_accept

    params["mediation_id"] = mediation_id

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


def _parse_response(*, response: httpx.Response) -> Optional[ConnRecord]:
    if response.status_code == 200:
        response_200 = ConnRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ConnRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ReceiveInvitationRequest,
    alias: Union[Unset, None, str] = UNSET,
    auto_accept: Union[Unset, None, bool] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
) -> Response[ConnRecord]:
    """Receive a new connection invitation

    Args:
        alias (Union[Unset, None, str]):
        auto_accept (Union[Unset, None, bool]):
        mediation_id (Union[Unset, None, str]):
        json_body (ReceiveInvitationRequest):

    Returns:
        Response[ConnRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        alias=alias,
        auto_accept=auto_accept,
        mediation_id=mediation_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: ReceiveInvitationRequest,
    alias: Union[Unset, None, str] = UNSET,
    auto_accept: Union[Unset, None, bool] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
) -> Optional[ConnRecord]:
    """Receive a new connection invitation

    Args:
        alias (Union[Unset, None, str]):
        auto_accept (Union[Unset, None, bool]):
        mediation_id (Union[Unset, None, str]):
        json_body (ReceiveInvitationRequest):

    Returns:
        Response[ConnRecord]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        alias=alias,
        auto_accept=auto_accept,
        mediation_id=mediation_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ReceiveInvitationRequest,
    alias: Union[Unset, None, str] = UNSET,
    auto_accept: Union[Unset, None, bool] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
) -> Response[ConnRecord]:
    """Receive a new connection invitation

    Args:
        alias (Union[Unset, None, str]):
        auto_accept (Union[Unset, None, bool]):
        mediation_id (Union[Unset, None, str]):
        json_body (ReceiveInvitationRequest):

    Returns:
        Response[ConnRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        alias=alias,
        auto_accept=auto_accept,
        mediation_id=mediation_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: ReceiveInvitationRequest,
    alias: Union[Unset, None, str] = UNSET,
    auto_accept: Union[Unset, None, bool] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
) -> Optional[ConnRecord]:
    """Receive a new connection invitation

    Args:
        alias (Union[Unset, None, str]):
        auto_accept (Union[Unset, None, bool]):
        mediation_id (Union[Unset, None, str]):
        json_body (ReceiveInvitationRequest):

    Returns:
        Response[ConnRecord]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            alias=alias,
            auto_accept=auto_accept,
            mediation_id=mediation_id,
        )
    ).parsed
