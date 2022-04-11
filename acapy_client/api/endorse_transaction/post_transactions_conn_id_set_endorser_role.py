from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.post_transactions_conn_id_set_endorser_role_transaction_my_job import (
    PostTransactionsConnIdSetEndorserRoleTransactionMyJob,
)
from ...models.transaction_jobs import TransactionJobs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conn_id: str,
    *,
    client: Client,
    transaction_my_job: Union[Unset, None, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Dict[str, Any]:
    url = "{}/transactions/{conn_id}/set-endorser-role".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_transaction_my_job: Union[Unset, None, str] = UNSET
    if not isinstance(transaction_my_job, Unset):
        json_transaction_my_job = transaction_my_job.value if transaction_my_job else None

    params["transaction_my_job"] = json_transaction_my_job

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[TransactionJobs]:
    if response.status_code == 200:
        response_200 = TransactionJobs.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TransactionJobs]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    conn_id: str,
    *,
    client: Client,
    transaction_my_job: Union[Unset, None, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Response[TransactionJobs]:
    """Set transaction jobs

    Args:
        conn_id (str):
        transaction_my_job (Union[Unset, None,
            PostTransactionsConnIdSetEndorserRoleTransactionMyJob]):

    Returns:
        Response[TransactionJobs]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        transaction_my_job=transaction_my_job,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    conn_id: str,
    *,
    client: Client,
    transaction_my_job: Union[Unset, None, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Optional[TransactionJobs]:
    """Set transaction jobs

    Args:
        conn_id (str):
        transaction_my_job (Union[Unset, None,
            PostTransactionsConnIdSetEndorserRoleTransactionMyJob]):

    Returns:
        Response[TransactionJobs]
    """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
        transaction_my_job=transaction_my_job,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    *,
    client: Client,
    transaction_my_job: Union[Unset, None, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Response[TransactionJobs]:
    """Set transaction jobs

    Args:
        conn_id (str):
        transaction_my_job (Union[Unset, None,
            PostTransactionsConnIdSetEndorserRoleTransactionMyJob]):

    Returns:
        Response[TransactionJobs]
    """

    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        transaction_my_job=transaction_my_job,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    *,
    client: Client,
    transaction_my_job: Union[Unset, None, PostTransactionsConnIdSetEndorserRoleTransactionMyJob] = UNSET,
) -> Optional[TransactionJobs]:
    """Set transaction jobs

    Args:
        conn_id (str):
        transaction_my_job (Union[Unset, None,
            PostTransactionsConnIdSetEndorserRoleTransactionMyJob]):

    Returns:
        Response[TransactionJobs]
    """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
            transaction_my_job=transaction_my_job,
        )
    ).parsed
