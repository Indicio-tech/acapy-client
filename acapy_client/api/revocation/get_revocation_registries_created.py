from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_revocation_registries_created_state import GetRevocationRegistriesCreatedState
from ...models.rev_regs_created import RevRegsCreated
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    cred_def_id: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetRevocationRegistriesCreatedState] = UNSET,
) -> Dict[str, Any]:
    url = "{}/revocation/registries/created".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cred_def_id"] = cred_def_id

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


def _parse_response(*, response: httpx.Response) -> Optional[RevRegsCreated]:
    if response.status_code == 200:
        response_200 = RevRegsCreated.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RevRegsCreated]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    cred_def_id: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetRevocationRegistriesCreatedState] = UNSET,
) -> Response[RevRegsCreated]:
    """Search for matching revocation registries that current agent created

    Args:
        cred_def_id (Union[Unset, None, str]):
        state (Union[Unset, None, GetRevocationRegistriesCreatedState]):

    Returns:
        Response[RevRegsCreated]
    """

    kwargs = _get_kwargs(
        client=client,
        cred_def_id=cred_def_id,
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
    cred_def_id: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetRevocationRegistriesCreatedState] = UNSET,
) -> Optional[RevRegsCreated]:
    """Search for matching revocation registries that current agent created

    Args:
        cred_def_id (Union[Unset, None, str]):
        state (Union[Unset, None, GetRevocationRegistriesCreatedState]):

    Returns:
        Response[RevRegsCreated]
    """

    return sync_detailed(
        client=client,
        cred_def_id=cred_def_id,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    cred_def_id: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetRevocationRegistriesCreatedState] = UNSET,
) -> Response[RevRegsCreated]:
    """Search for matching revocation registries that current agent created

    Args:
        cred_def_id (Union[Unset, None, str]):
        state (Union[Unset, None, GetRevocationRegistriesCreatedState]):

    Returns:
        Response[RevRegsCreated]
    """

    kwargs = _get_kwargs(
        client=client,
        cred_def_id=cred_def_id,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    cred_def_id: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, GetRevocationRegistriesCreatedState] = UNSET,
) -> Optional[RevRegsCreated]:
    """Search for matching revocation registries that current agent created

    Args:
        cred_def_id (Union[Unset, None, str]):
        state (Union[Unset, None, GetRevocationRegistriesCreatedState]):

    Returns:
        Response[RevRegsCreated]
    """

    return (
        await asyncio_detailed(
            client=client,
            cred_def_id=cred_def_id,
            state=state,
        )
    ).parsed
