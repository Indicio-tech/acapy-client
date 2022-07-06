from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.connection_list import ConnectionList
from ...models.get_connections_connection_protocol import GetConnectionsConnectionProtocol
from ...models.get_connections_state import GetConnectionsState
from ...models.get_connections_their_role import GetConnectionsTheirRole
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    alias: Union[Unset, None, str] = UNSET,
    connection_protocol: Union[Unset, None, GetConnectionsConnectionProtocol] = UNSET,
    invitation_key: Union[Unset, None, str] = UNSET,
    invitation_msg_id: Union[Unset, None, str] = UNSET,
    my_did: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetConnectionsState] = UNSET,
    their_did: Union[Unset, None, str] = UNSET,
    their_public_did: Union[Unset, None, str] = UNSET,
    their_role: Union[Unset, None, GetConnectionsTheirRole] = UNSET,
) -> Dict[str, Any]:
    url = "{}/connections".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["alias"] = alias

    json_connection_protocol: Union[Unset, None, str] = UNSET
    if not isinstance(connection_protocol, Unset):
        json_connection_protocol = connection_protocol.value if connection_protocol else None

    params["connection_protocol"] = json_connection_protocol

    params["invitation_key"] = invitation_key

    params["invitation_msg_id"] = invitation_msg_id

    params["my_did"] = my_did

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["their_did"] = their_did

    params["their_public_did"] = their_public_did

    json_their_role: Union[Unset, None, str] = UNSET
    if not isinstance(their_role, Unset):
        json_their_role = their_role.value if their_role else None

    params["their_role"] = json_their_role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ConnectionList]:
    if response.status_code == 200:
        response_200 = ConnectionList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ConnectionList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    alias: Union[Unset, None, str] = UNSET,
    connection_protocol: Union[Unset, None, GetConnectionsConnectionProtocol] = UNSET,
    invitation_key: Union[Unset, None, str] = UNSET,
    invitation_msg_id: Union[Unset, None, str] = UNSET,
    my_did: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetConnectionsState] = UNSET,
    their_did: Union[Unset, None, str] = UNSET,
    their_public_did: Union[Unset, None, str] = UNSET,
    their_role: Union[Unset, None, GetConnectionsTheirRole] = UNSET,
) -> Response[ConnectionList]:
    """Query agent-to-agent connections

    Args:
        alias (Union[Unset, None, str]):
        connection_protocol (Union[Unset, None, GetConnectionsConnectionProtocol]):
        invitation_key (Union[Unset, None, str]):
        invitation_msg_id (Union[Unset, None, str]):
        my_did (Union[Unset, None, str]):
        state (Union[Unset, None, GetConnectionsState]):
        their_did (Union[Unset, None, str]):
        their_public_did (Union[Unset, None, str]):
        their_role (Union[Unset, None, GetConnectionsTheirRole]):

    Returns:
        Response[ConnectionList]
    """

    kwargs = _get_kwargs(
        client=client,
        alias=alias,
        connection_protocol=connection_protocol,
        invitation_key=invitation_key,
        invitation_msg_id=invitation_msg_id,
        my_did=my_did,
        state=state,
        their_did=their_did,
        their_public_did=their_public_did,
        their_role=their_role,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    alias: Union[Unset, None, str] = UNSET,
    connection_protocol: Union[Unset, None, GetConnectionsConnectionProtocol] = UNSET,
    invitation_key: Union[Unset, None, str] = UNSET,
    invitation_msg_id: Union[Unset, None, str] = UNSET,
    my_did: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetConnectionsState] = UNSET,
    their_did: Union[Unset, None, str] = UNSET,
    their_public_did: Union[Unset, None, str] = UNSET,
    their_role: Union[Unset, None, GetConnectionsTheirRole] = UNSET,
) -> Optional[ConnectionList]:
    """Query agent-to-agent connections

    Args:
        alias (Union[Unset, None, str]):
        connection_protocol (Union[Unset, None, GetConnectionsConnectionProtocol]):
        invitation_key (Union[Unset, None, str]):
        invitation_msg_id (Union[Unset, None, str]):
        my_did (Union[Unset, None, str]):
        state (Union[Unset, None, GetConnectionsState]):
        their_did (Union[Unset, None, str]):
        their_public_did (Union[Unset, None, str]):
        their_role (Union[Unset, None, GetConnectionsTheirRole]):

    Returns:
        Response[ConnectionList]
    """

    return sync_detailed(
        client=client,
        alias=alias,
        connection_protocol=connection_protocol,
        invitation_key=invitation_key,
        invitation_msg_id=invitation_msg_id,
        my_did=my_did,
        state=state,
        their_did=their_did,
        their_public_did=their_public_did,
        their_role=their_role,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    alias: Union[Unset, None, str] = UNSET,
    connection_protocol: Union[Unset, None, GetConnectionsConnectionProtocol] = UNSET,
    invitation_key: Union[Unset, None, str] = UNSET,
    invitation_msg_id: Union[Unset, None, str] = UNSET,
    my_did: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetConnectionsState] = UNSET,
    their_did: Union[Unset, None, str] = UNSET,
    their_public_did: Union[Unset, None, str] = UNSET,
    their_role: Union[Unset, None, GetConnectionsTheirRole] = UNSET,
) -> Response[ConnectionList]:
    """Query agent-to-agent connections

    Args:
        alias (Union[Unset, None, str]):
        connection_protocol (Union[Unset, None, GetConnectionsConnectionProtocol]):
        invitation_key (Union[Unset, None, str]):
        invitation_msg_id (Union[Unset, None, str]):
        my_did (Union[Unset, None, str]):
        state (Union[Unset, None, GetConnectionsState]):
        their_did (Union[Unset, None, str]):
        their_public_did (Union[Unset, None, str]):
        their_role (Union[Unset, None, GetConnectionsTheirRole]):

    Returns:
        Response[ConnectionList]
    """

    kwargs = _get_kwargs(
        client=client,
        alias=alias,
        connection_protocol=connection_protocol,
        invitation_key=invitation_key,
        invitation_msg_id=invitation_msg_id,
        my_did=my_did,
        state=state,
        their_did=their_did,
        their_public_did=their_public_did,
        their_role=their_role,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    alias: Union[Unset, None, str] = UNSET,
    connection_protocol: Union[Unset, None, GetConnectionsConnectionProtocol] = UNSET,
    invitation_key: Union[Unset, None, str] = UNSET,
    invitation_msg_id: Union[Unset, None, str] = UNSET,
    my_did: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetConnectionsState] = UNSET,
    their_did: Union[Unset, None, str] = UNSET,
    their_public_did: Union[Unset, None, str] = UNSET,
    their_role: Union[Unset, None, GetConnectionsTheirRole] = UNSET,
) -> Optional[ConnectionList]:
    """Query agent-to-agent connections

    Args:
        alias (Union[Unset, None, str]):
        connection_protocol (Union[Unset, None, GetConnectionsConnectionProtocol]):
        invitation_key (Union[Unset, None, str]):
        invitation_msg_id (Union[Unset, None, str]):
        my_did (Union[Unset, None, str]):
        state (Union[Unset, None, GetConnectionsState]):
        their_did (Union[Unset, None, str]):
        their_public_did (Union[Unset, None, str]):
        their_role (Union[Unset, None, GetConnectionsTheirRole]):

    Returns:
        Response[ConnectionList]
    """

    return (
        await asyncio_detailed(
            client=client,
            alias=alias,
            connection_protocol=connection_protocol,
            invitation_key=invitation_key,
            invitation_msg_id=invitation_msg_id,
            my_did=my_did,
            state=state,
            their_did=their_did,
            their_public_did=their_public_did,
            their_role=their_role,
        )
    ).parsed
