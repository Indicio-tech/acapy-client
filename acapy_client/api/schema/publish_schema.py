from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.schema_send_request import SchemaSendRequest
from ...models.schema_send_result import SchemaSendResult
from ...models.txn_or_schema_send_result import TxnOrSchemaSendResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: SchemaSendRequest,
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/schemas".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["conn_id"] = conn_id

    params["create_transaction_for_endorser"] = create_transaction_for_endorser

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[SchemaSendResult, TxnOrSchemaSendResult]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union[SchemaSendResult, TxnOrSchemaSendResult]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = SchemaSendResult.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = TxnOrSchemaSendResult.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[SchemaSendResult, TxnOrSchemaSendResult]]:
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
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Response[Union[SchemaSendResult, TxnOrSchemaSendResult]]:
    """Sends a schema to the ledger

    Args:
        conn_id (Union[Unset, None, str]):
        create_transaction_for_endorser (Union[Unset, None, bool]):
        json_body (SchemaSendRequest):

    Returns:
        Response[Union[SchemaSendResult, TxnOrSchemaSendResult]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: SchemaSendRequest,
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[SchemaSendResult, TxnOrSchemaSendResult]]:
    """Sends a schema to the ledger

    Args:
        conn_id (Union[Unset, None, str]):
        create_transaction_for_endorser (Union[Unset, None, bool]):
        json_body (SchemaSendRequest):

    Returns:
        Response[Union[SchemaSendResult, TxnOrSchemaSendResult]]
    """

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
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Response[Union[SchemaSendResult, TxnOrSchemaSendResult]]:
    """Sends a schema to the ledger

    Args:
        conn_id (Union[Unset, None, str]):
        create_transaction_for_endorser (Union[Unset, None, bool]):
        json_body (SchemaSendRequest):

    Returns:
        Response[Union[SchemaSendResult, TxnOrSchemaSendResult]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        conn_id=conn_id,
        create_transaction_for_endorser=create_transaction_for_endorser,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SchemaSendRequest,
    conn_id: Union[Unset, None, str] = UNSET,
    create_transaction_for_endorser: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[SchemaSendResult, TxnOrSchemaSendResult]]:
    """Sends a schema to the ledger

    Args:
        conn_id (Union[Unset, None, str]):
        create_transaction_for_endorser (Union[Unset, None, bool]):
        json_body (SchemaSendRequest):

    Returns:
        Response[Union[SchemaSendResult, TxnOrSchemaSendResult]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            conn_id=conn_id,
            create_transaction_for_endorser=create_transaction_for_endorser,
        )
    ).parsed
