from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.did_result import DIDResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    did: str,
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/wallet/did/public".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["did"] = did

    params["conn_id"] = conn_id

    params["create_transaction_for_endorser"] = create_transaction_for_endorser

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[DIDResult]:
    if response.status_code == 200:
        response_200 = DIDResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DIDResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    did: str,
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Response[DIDResult]:
    """Assign the current public DID

    Args:
        did (str):
        conn_id (Union[Unset, None, str]):
        create_transaction_for_endorser (Union[Unset, None, bool]):

    Returns:
        Response[DIDResult]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
        conn_id=conn_id,
        create_transaction_for_endorser=create_transaction_for_endorser,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    did: str,
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Optional[DIDResult]:
    """Assign the current public DID

    Args:
        did (str):
        conn_id (Union[Unset, None, str]):
        create_transaction_for_endorser (Union[Unset, None, bool]):

    Returns:
        Response[DIDResult]
    """

    return sync_detailed(
        client=client,
        did=did,
        conn_id=conn_id,
        create_transaction_for_endorser=create_transaction_for_endorser,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    did: str,
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Response[DIDResult]:
    """Assign the current public DID

    Args:
        did (str):
        conn_id (Union[Unset, None, str]):
        create_transaction_for_endorser (Union[Unset, None, bool]):

    Returns:
        Response[DIDResult]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
        conn_id=conn_id,
        create_transaction_for_endorser=create_transaction_for_endorser,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    did: str,
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Optional[DIDResult]:
    """Assign the current public DID

    Args:
        did (str):
        conn_id (Union[Unset, None, str]):
        create_transaction_for_endorser (Union[Unset, None, bool]):

    Returns:
        Response[DIDResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            did=did,
            conn_id=conn_id,
            create_transaction_for_endorser=create_transaction_for_endorser,
        )
    ).parsed
