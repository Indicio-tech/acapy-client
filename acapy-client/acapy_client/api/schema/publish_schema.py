from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.schema_send_request import SchemaSendRequest
from ...models.txn_or_schema_send_result import TxnOrSchemaSendResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: SchemaSendRequest,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/schemas".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "conn_id": conn_id,
        "create_transaction_for_endorser": create_transaction_for_endorser,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[TxnOrSchemaSendResult]:
    if response.status_code == 200:
        response_200 = TxnOrSchemaSendResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TxnOrSchemaSendResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SchemaSendRequest,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Response[TxnOrSchemaSendResult]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: SchemaSendRequest,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Optional[TxnOrSchemaSendResult]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        conn_id=conn_id,
        create_transaction_for_endorser=create_transaction_for_endorser,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SchemaSendRequest,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Response[TxnOrSchemaSendResult]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        conn_id=conn_id,
        create_transaction_for_endorser=create_transaction_for_endorser,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SchemaSendRequest,
    conn_id: Union[Unset, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, bool] = UNSET,
) -> Optional[TxnOrSchemaSendResult]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            conn_id=conn_id,
            create_transaction_for_endorser=create_transaction_for_endorser,
        )
    ).parsed
