from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.transaction_record import TransactionRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tran_id: str,
    *,
    client: Client,
    endorser_did: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/transactions/{tran_id}/endorse".format(client.base_url, tran_id=tran_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["endorser_did"] = endorser_did

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    tran_id: str,
    *,
    client: Client,
    endorser_did: Union[Unset, None, str] = UNSET,
) -> Response[TransactionRecord]:
    """For Endorser to endorse a particular transaction record

    Args:
        tran_id (str):
        endorser_did (Union[Unset, None, str]):

    Returns:
        Response[TransactionRecord]
    """

    kwargs = _get_kwargs(
        tran_id=tran_id,
        client=client,
        endorser_did=endorser_did,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    tran_id: str,
    *,
    client: Client,
    endorser_did: Union[Unset, None, str] = UNSET,
) -> Optional[TransactionRecord]:
    """For Endorser to endorse a particular transaction record

    Args:
        tran_id (str):
        endorser_did (Union[Unset, None, str]):

    Returns:
        Response[TransactionRecord]
    """

    return sync_detailed(
        tran_id=tran_id,
        client=client,
        endorser_did=endorser_did,
    ).parsed


async def asyncio_detailed(
    tran_id: str,
    *,
    client: Client,
    endorser_did: Union[Unset, None, str] = UNSET,
) -> Response[TransactionRecord]:
    """For Endorser to endorse a particular transaction record

    Args:
        tran_id (str):
        endorser_did (Union[Unset, None, str]):

    Returns:
        Response[TransactionRecord]
    """

    kwargs = _get_kwargs(
        tran_id=tran_id,
        client=client,
        endorser_did=endorser_did,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    tran_id: str,
    *,
    client: Client,
    endorser_did: Union[Unset, None, str] = UNSET,
) -> Optional[TransactionRecord]:
    """For Endorser to endorse a particular transaction record

    Args:
        tran_id (str):
        endorser_did (Union[Unset, None, str]):

    Returns:
        Response[TransactionRecord]
    """

    return (
        await asyncio_detailed(
            tran_id=tran_id,
            client=client,
            endorser_did=endorser_did,
        )
    ).parsed
