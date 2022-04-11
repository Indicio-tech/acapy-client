from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.get_mediation_requests_state import GetMediationRequestsState
from ...models.mediation_list import MediationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    conn_id: Union[Unset, None, str] = UNSET,
    mediator_terms: Union[Unset, None, List[str]] = UNSET,
    recipient_terms: Union[Unset, None, List[str]] = UNSET,
    state: Union[Unset, None, GetMediationRequestsState] = UNSET,
) -> Dict[str, Any]:
    url = "{}/mediation/requests".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["conn_id"] = conn_id

    json_mediator_terms: Union[Unset, None, List[str]] = UNSET
    if not isinstance(mediator_terms, Unset):
        if mediator_terms is None:
            json_mediator_terms = None
        else:
            json_mediator_terms = mediator_terms

    params["mediator_terms"] = json_mediator_terms

    json_recipient_terms: Union[Unset, None, List[str]] = UNSET
    if not isinstance(recipient_terms, Unset):
        if recipient_terms is None:
            json_recipient_terms = None
        else:
            json_recipient_terms = recipient_terms

    params["recipient_terms"] = json_recipient_terms

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[MediationList]:
    if response.status_code == 200:
        response_200 = MediationList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[MediationList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    conn_id: Union[Unset, None, str] = UNSET,
    mediator_terms: Union[Unset, None, List[str]] = UNSET,
    recipient_terms: Union[Unset, None, List[str]] = UNSET,
    state: Union[Unset, None, GetMediationRequestsState] = UNSET,
) -> Response[MediationList]:
    """Query mediation requests, returns list of all mediation records

    Args:
        conn_id (Union[Unset, None, str]):
        mediator_terms (Union[Unset, None, List[str]]):
        recipient_terms (Union[Unset, None, List[str]]):
        state (Union[Unset, None, GetMediationRequestsState]):

    Returns:
        Response[MediationList]
    """

    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        mediator_terms=mediator_terms,
        recipient_terms=recipient_terms,
        state=state,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    conn_id: Union[Unset, None, str] = UNSET,
    mediator_terms: Union[Unset, None, List[str]] = UNSET,
    recipient_terms: Union[Unset, None, List[str]] = UNSET,
    state: Union[Unset, None, GetMediationRequestsState] = UNSET,
) -> Optional[MediationList]:
    """Query mediation requests, returns list of all mediation records

    Args:
        conn_id (Union[Unset, None, str]):
        mediator_terms (Union[Unset, None, List[str]]):
        recipient_terms (Union[Unset, None, List[str]]):
        state (Union[Unset, None, GetMediationRequestsState]):

    Returns:
        Response[MediationList]
    """

    return sync_detailed(
        client=client,
        conn_id=conn_id,
        mediator_terms=mediator_terms,
        recipient_terms=recipient_terms,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    conn_id: Union[Unset, None, str] = UNSET,
    mediator_terms: Union[Unset, None, List[str]] = UNSET,
    recipient_terms: Union[Unset, None, List[str]] = UNSET,
    state: Union[Unset, None, GetMediationRequestsState] = UNSET,
) -> Response[MediationList]:
    """Query mediation requests, returns list of all mediation records

    Args:
        conn_id (Union[Unset, None, str]):
        mediator_terms (Union[Unset, None, List[str]]):
        recipient_terms (Union[Unset, None, List[str]]):
        state (Union[Unset, None, GetMediationRequestsState]):

    Returns:
        Response[MediationList]
    """

    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        mediator_terms=mediator_terms,
        recipient_terms=recipient_terms,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    conn_id: Union[Unset, None, str] = UNSET,
    mediator_terms: Union[Unset, None, List[str]] = UNSET,
    recipient_terms: Union[Unset, None, List[str]] = UNSET,
    state: Union[Unset, None, GetMediationRequestsState] = UNSET,
) -> Optional[MediationList]:
    """Query mediation requests, returns list of all mediation records

    Args:
        conn_id (Union[Unset, None, str]):
        mediator_terms (Union[Unset, None, List[str]]):
        recipient_terms (Union[Unset, None, List[str]]):
        state (Union[Unset, None, GetMediationRequestsState]):

    Returns:
        Response[MediationList]
    """

    return (
        await asyncio_detailed(
            client=client,
            conn_id=conn_id,
            mediator_terms=mediator_terms,
            recipient_terms=recipient_terms,
            state=state,
        )
    ).parsed
