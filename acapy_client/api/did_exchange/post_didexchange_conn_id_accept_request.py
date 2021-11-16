from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.conn_record import ConnRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conn_id: str,
    *,
    client: Client,
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/didexchange/{conn_id}/accept-request".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "mediation_id": mediation_id,
        "my_endpoint": my_endpoint,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
        "verify": client.verify_ssl,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ConnRecord]:
    if response.status_code == 200:
        response_200 = ConnRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ConnRecord]:
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
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
) -> Response[ConnRecord]:
    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        mediation_id=mediation_id,
        my_endpoint=my_endpoint,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    conn_id: str,
    *,
    client: Client,
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
) -> Optional[ConnRecord]:
    """ """

    return sync_detailed(
        conn_id=conn_id,
        client=client,
        mediation_id=mediation_id,
        my_endpoint=my_endpoint,
    ).parsed


async def asyncio_detailed(
    conn_id: str,
    *,
    client: Client,
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
) -> Response[ConnRecord]:
    kwargs = _get_kwargs(
        conn_id=conn_id,
        client=client,
        mediation_id=mediation_id,
        my_endpoint=my_endpoint,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    conn_id: str,
    *,
    client: Client,
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
) -> Optional[ConnRecord]:
    """ """

    return (
        await asyncio_detailed(
            conn_id=conn_id,
            client=client,
            mediation_id=mediation_id,
            my_endpoint=my_endpoint,
        )
    ).parsed
