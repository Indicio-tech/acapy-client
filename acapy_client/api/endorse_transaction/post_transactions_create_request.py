from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.date import Date
from ...models.transaction_record import TransactionRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: Date,
    tran_id: str,
    endorser_write_txn: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/transactions/create-request".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["tran_id"] = tran_id

    params["endorser_write_txn"] = endorser_write_txn

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


def _parse_response(*, response: httpx.Response) -> Optional[TransactionRecord]:
    if response.status_code == 200:
        response_200 = TransactionRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TransactionRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Date,
    tran_id: str,
    endorser_write_txn: Union[Unset, None, bool] = UNSET,
) -> Response[TransactionRecord]:
    """For author to send a transaction request

    Args:
        tran_id (str):
        endorser_write_txn (Union[Unset, None, bool]):
        json_body (Date):

    Returns:
        Response[TransactionRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        tran_id=tran_id,
        endorser_write_txn=endorser_write_txn,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: Date,
    tran_id: str,
    endorser_write_txn: Union[Unset, None, bool] = UNSET,
) -> Optional[TransactionRecord]:
    """For author to send a transaction request

    Args:
        tran_id (str):
        endorser_write_txn (Union[Unset, None, bool]):
        json_body (Date):

    Returns:
        Response[TransactionRecord]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        tran_id=tran_id,
        endorser_write_txn=endorser_write_txn,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Date,
    tran_id: str,
    endorser_write_txn: Union[Unset, None, bool] = UNSET,
) -> Response[TransactionRecord]:
    """For author to send a transaction request

    Args:
        tran_id (str):
        endorser_write_txn (Union[Unset, None, bool]):
        json_body (Date):

    Returns:
        Response[TransactionRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        tran_id=tran_id,
        endorser_write_txn=endorser_write_txn,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Date,
    tran_id: str,
    endorser_write_txn: Union[Unset, None, bool] = UNSET,
) -> Optional[TransactionRecord]:
    """For author to send a transaction request

    Args:
        tran_id (str):
        endorser_write_txn (Union[Unset, None, bool]):
        json_body (Date):

    Returns:
        Response[TransactionRecord]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            tran_id=tran_id,
            endorser_write_txn=endorser_write_txn,
        )
    ).parsed
