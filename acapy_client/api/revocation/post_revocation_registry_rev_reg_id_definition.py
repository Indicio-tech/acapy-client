from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.txn_or_rev_reg_result import TxnOrRevRegResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    rev_reg_id: str,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/revocation/registry/{rev_reg_id}/definition".format(client.base_url, rev_reg_id=rev_reg_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "conn_id": conn_id,
        "create_transaction_for_endorser": create_transaction_for_endorser,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[TxnOrRevRegResult]:
    if response.status_code == 200:
        response_200 = TxnOrRevRegResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TxnOrRevRegResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    rev_reg_id: str,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Response[TxnOrRevRegResult]:
    kwargs = _get_kwargs(
        client=client,
        rev_reg_id=rev_reg_id,
        conn_id=conn_id,
        create_transaction_for_endorser=create_transaction_for_endorser,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    rev_reg_id: str,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Optional[TxnOrRevRegResult]:
    """ """

    return sync_detailed(
        client=client,
        rev_reg_id=rev_reg_id,
        conn_id=conn_id,
        create_transaction_for_endorser=create_transaction_for_endorser,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    rev_reg_id: str,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Response[TxnOrRevRegResult]:
    kwargs = _get_kwargs(
        client=client,
        rev_reg_id=rev_reg_id,
        conn_id=conn_id,
        create_transaction_for_endorser=create_transaction_for_endorser,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    rev_reg_id: str,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Optional[TxnOrRevRegResult]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            rev_reg_id=rev_reg_id,
            conn_id=conn_id,
            create_transaction_for_endorser=create_transaction_for_endorser,
        )
    ).parsed
