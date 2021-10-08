from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.transaction_record import TransactionRecord
from ...types import Response


def _get_kwargs(
    tran_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/transactions/{tran_id}/refuse".format(client.base_url, tran_id=tran_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
) -> Response[TransactionRecord]:
    kwargs = _get_kwargs(
        tran_id=tran_id,
        client=client,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    tran_id: str,
    *,
    client: Client,
) -> Optional[TransactionRecord]:
    """ """

    return sync_detailed(
        tran_id=tran_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tran_id: str,
    *,
    client: Client,
) -> Response[TransactionRecord]:
    kwargs = _get_kwargs(
        tran_id=tran_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    tran_id: str,
    *,
    client: Client,
) -> Optional[TransactionRecord]:
    """ """

    return (
        await asyncio_detailed(
            tran_id=tran_id,
            client=client,
        )
    ).parsed
