from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_records_present_proof_role_schema import GetRecordsPresentProofRoleSchema
from ...models.get_records_present_proof_state_schema import GetRecordsPresentProofStateSchema
from ...models.v20_pres_ex_record_list import V20PresExRecordList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetRecordsPresentProofRoleSchema] = UNSET,
    state: Union[Unset, None, GetRecordsPresentProofStateSchema] = UNSET,
    thread_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/present-proof-2.0/records".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["connection_id"] = connection_id

    json_role: Union[Unset, None, str] = UNSET
    if not isinstance(role, Unset):
        json_role = role.value if role else None

    params["role"] = json_role

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["thread_id"] = thread_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[V20PresExRecordList]:
    if response.status_code == 200:
        response_200 = V20PresExRecordList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V20PresExRecordList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetRecordsPresentProofRoleSchema] = UNSET,
    state: Union[Unset, None, GetRecordsPresentProofStateSchema] = UNSET,
    thread_id: Union[Unset, None, str] = UNSET,
) -> Response[V20PresExRecordList]:
    """Fetch all present-proof exchange records

    Args:
        connection_id (Union[Unset, None, str]):
        role (Union[Unset, None, GetRecordsPresentProofRoleSchema]):
        state (Union[Unset, None, GetRecordsPresentProofStateSchema]):
        thread_id (Union[Unset, None, str]):

    Returns:
        Response[V20PresExRecordList]
    """

    kwargs = _get_kwargs(
        client=client,
        connection_id=connection_id,
        role=role,
        state=state,
        thread_id=thread_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetRecordsPresentProofRoleSchema] = UNSET,
    state: Union[Unset, None, GetRecordsPresentProofStateSchema] = UNSET,
    thread_id: Union[Unset, None, str] = UNSET,
) -> Optional[V20PresExRecordList]:
    """Fetch all present-proof exchange records

    Args:
        connection_id (Union[Unset, None, str]):
        role (Union[Unset, None, GetRecordsPresentProofRoleSchema]):
        state (Union[Unset, None, GetRecordsPresentProofStateSchema]):
        thread_id (Union[Unset, None, str]):

    Returns:
        Response[V20PresExRecordList]
    """

    return sync_detailed(
        client=client,
        connection_id=connection_id,
        role=role,
        state=state,
        thread_id=thread_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetRecordsPresentProofRoleSchema] = UNSET,
    state: Union[Unset, None, GetRecordsPresentProofStateSchema] = UNSET,
    thread_id: Union[Unset, None, str] = UNSET,
) -> Response[V20PresExRecordList]:
    """Fetch all present-proof exchange records

    Args:
        connection_id (Union[Unset, None, str]):
        role (Union[Unset, None, GetRecordsPresentProofRoleSchema]):
        state (Union[Unset, None, GetRecordsPresentProofStateSchema]):
        thread_id (Union[Unset, None, str]):

    Returns:
        Response[V20PresExRecordList]
    """

    kwargs = _get_kwargs(
        client=client,
        connection_id=connection_id,
        role=role,
        state=state,
        thread_id=thread_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    connection_id: Union[Unset, None, str] = UNSET,
    role: Union[Unset, None, GetRecordsPresentProofRoleSchema] = UNSET,
    state: Union[Unset, None, GetRecordsPresentProofStateSchema] = UNSET,
    thread_id: Union[Unset, None, str] = UNSET,
) -> Optional[V20PresExRecordList]:
    """Fetch all present-proof exchange records

    Args:
        connection_id (Union[Unset, None, str]):
        role (Union[Unset, None, GetRecordsPresentProofRoleSchema]):
        state (Union[Unset, None, GetRecordsPresentProofStateSchema]):
        thread_id (Union[Unset, None, str]):

    Returns:
        Response[V20PresExRecordList]
    """

    return (
        await asyncio_detailed(
            client=client,
            connection_id=connection_id,
            role=role,
            state=state,
            thread_id=thread_id,
        )
    ).parsed
