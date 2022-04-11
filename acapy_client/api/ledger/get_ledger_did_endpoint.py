from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_did_endpoint_response import GetDIDEndpointResponse
from ...models.get_ledger_did_endpoint_endpoint_type import GetLedgerDidEndpointEndpointType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    did: str,
    endpoint_type: Union[Unset, None, GetLedgerDidEndpointEndpointType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/ledger/did-endpoint".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["did"] = did

    json_endpoint_type: Union[Unset, None, str] = UNSET
    if not isinstance(endpoint_type, Unset):
        json_endpoint_type = endpoint_type.value if endpoint_type else None

    params["endpoint_type"] = json_endpoint_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetDIDEndpointResponse]:
    if response.status_code == 200:
        response_200 = GetDIDEndpointResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetDIDEndpointResponse]:
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
    endpoint_type: Union[Unset, None, GetLedgerDidEndpointEndpointType] = UNSET,
) -> Response[GetDIDEndpointResponse]:
    """Get the endpoint for a DID from the ledger.

    Args:
        did (str):
        endpoint_type (Union[Unset, None, GetLedgerDidEndpointEndpointType]):

    Returns:
        Response[GetDIDEndpointResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
        endpoint_type=endpoint_type,
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
    endpoint_type: Union[Unset, None, GetLedgerDidEndpointEndpointType] = UNSET,
) -> Optional[GetDIDEndpointResponse]:
    """Get the endpoint for a DID from the ledger.

    Args:
        did (str):
        endpoint_type (Union[Unset, None, GetLedgerDidEndpointEndpointType]):

    Returns:
        Response[GetDIDEndpointResponse]
    """

    return sync_detailed(
        client=client,
        did=did,
        endpoint_type=endpoint_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    did: str,
    endpoint_type: Union[Unset, None, GetLedgerDidEndpointEndpointType] = UNSET,
) -> Response[GetDIDEndpointResponse]:
    """Get the endpoint for a DID from the ledger.

    Args:
        did (str):
        endpoint_type (Union[Unset, None, GetLedgerDidEndpointEndpointType]):

    Returns:
        Response[GetDIDEndpointResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        did=did,
        endpoint_type=endpoint_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    did: str,
    endpoint_type: Union[Unset, None, GetLedgerDidEndpointEndpointType] = UNSET,
) -> Optional[GetDIDEndpointResponse]:
    """Get the endpoint for a DID from the ledger.

    Args:
        did (str):
        endpoint_type (Union[Unset, None, GetLedgerDidEndpointEndpointType]):

    Returns:
        Response[GetDIDEndpointResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            did=did,
            endpoint_type=endpoint_type,
        )
    ).parsed
