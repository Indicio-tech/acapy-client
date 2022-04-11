from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.patch_revocation_registry_rev_reg_id_set_state_state import PatchRevocationRegistryRevRegIdSetStateState
from ...models.rev_reg_result import RevRegResult
from ...types import UNSET, Response


def _get_kwargs(
    rev_reg_id: str,
    *,
    client: Client,
    state: PatchRevocationRegistryRevRegIdSetStateState,
) -> Dict[str, Any]:
    url = "{}/revocation/registry/{rev_reg_id}/set-state".format(client.base_url, rev_reg_id=rev_reg_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_state = state.value

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[RevRegResult]:
    if response.status_code == 200:
        response_200 = RevRegResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RevRegResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    rev_reg_id: str,
    *,
    client: Client,
    state: PatchRevocationRegistryRevRegIdSetStateState,
) -> Response[RevRegResult]:
    """Set revocation registry state manually

    Args:
        rev_reg_id (str):
        state (PatchRevocationRegistryRevRegIdSetStateState):

    Returns:
        Response[RevRegResult]
    """

    kwargs = _get_kwargs(
        rev_reg_id=rev_reg_id,
        client=client,
        state=state,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    rev_reg_id: str,
    *,
    client: Client,
    state: PatchRevocationRegistryRevRegIdSetStateState,
) -> Optional[RevRegResult]:
    """Set revocation registry state manually

    Args:
        rev_reg_id (str):
        state (PatchRevocationRegistryRevRegIdSetStateState):

    Returns:
        Response[RevRegResult]
    """

    return sync_detailed(
        rev_reg_id=rev_reg_id,
        client=client,
        state=state,
    ).parsed


async def asyncio_detailed(
    rev_reg_id: str,
    *,
    client: Client,
    state: PatchRevocationRegistryRevRegIdSetStateState,
) -> Response[RevRegResult]:
    """Set revocation registry state manually

    Args:
        rev_reg_id (str):
        state (PatchRevocationRegistryRevRegIdSetStateState):

    Returns:
        Response[RevRegResult]
    """

    kwargs = _get_kwargs(
        rev_reg_id=rev_reg_id,
        client=client,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    rev_reg_id: str,
    *,
    client: Client,
    state: PatchRevocationRegistryRevRegIdSetStateState,
) -> Optional[RevRegResult]:
    """Set revocation registry state manually

    Args:
        rev_reg_id (str):
        state (PatchRevocationRegistryRevRegIdSetStateState):

    Returns:
        Response[RevRegResult]
    """

    return (
        await asyncio_detailed(
            rev_reg_id=rev_reg_id,
            client=client,
            state=state,
        )
    ).parsed
