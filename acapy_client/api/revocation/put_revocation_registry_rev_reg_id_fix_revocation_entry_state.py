from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.rev_reg_wallet_updated_result import RevRegWalletUpdatedResult
from ...types import UNSET, Response


def _get_kwargs(
    rev_reg_id: str,
    *,
    client: Client,
    apply_ledger_update: bool,
) -> Dict[str, Any]:
    url = "{}/revocation/registry/{rev_reg_id}/fix-revocation-entry-state".format(
        client.base_url, rev_reg_id=rev_reg_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["apply_ledger_update"] = apply_ledger_update

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[RevRegWalletUpdatedResult]:
    if response.status_code == 200:
        response_200 = RevRegWalletUpdatedResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RevRegWalletUpdatedResult]:
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
    apply_ledger_update: bool,
) -> Response[RevRegWalletUpdatedResult]:
    """Fix revocation state in wallet and return number of updated entries

    Args:
        rev_reg_id (str):
        apply_ledger_update (bool):

    Returns:
        Response[RevRegWalletUpdatedResult]
    """

    kwargs = _get_kwargs(
        rev_reg_id=rev_reg_id,
        client=client,
        apply_ledger_update=apply_ledger_update,
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
    apply_ledger_update: bool,
) -> Optional[RevRegWalletUpdatedResult]:
    """Fix revocation state in wallet and return number of updated entries

    Args:
        rev_reg_id (str):
        apply_ledger_update (bool):

    Returns:
        Response[RevRegWalletUpdatedResult]
    """

    return sync_detailed(
        rev_reg_id=rev_reg_id,
        client=client,
        apply_ledger_update=apply_ledger_update,
    ).parsed


async def asyncio_detailed(
    rev_reg_id: str,
    *,
    client: Client,
    apply_ledger_update: bool,
) -> Response[RevRegWalletUpdatedResult]:
    """Fix revocation state in wallet and return number of updated entries

    Args:
        rev_reg_id (str):
        apply_ledger_update (bool):

    Returns:
        Response[RevRegWalletUpdatedResult]
    """

    kwargs = _get_kwargs(
        rev_reg_id=rev_reg_id,
        client=client,
        apply_ledger_update=apply_ledger_update,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    rev_reg_id: str,
    *,
    client: Client,
    apply_ledger_update: bool,
) -> Optional[RevRegWalletUpdatedResult]:
    """Fix revocation state in wallet and return number of updated entries

    Args:
        rev_reg_id (str):
        apply_ledger_update (bool):

    Returns:
        Response[RevRegWalletUpdatedResult]
    """

    return (
        await asyncio_detailed(
            rev_reg_id=rev_reg_id,
            client=client,
            apply_ledger_update=apply_ledger_update,
        )
    ).parsed
