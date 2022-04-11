from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.conn_record import ConnRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    their_public_did: str,
    alias: Union[Unset, None, str] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
    my_label: Union[Unset, None, str] = UNSET,
    use_public_did: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/didexchange/create-request".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["their_public_did"] = their_public_did

    params["alias"] = alias

    params["mediation_id"] = mediation_id

    params["my_endpoint"] = my_endpoint

    params["my_label"] = my_label

    params["use_public_did"] = use_public_did

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    *,
    client: Client,
    their_public_did: str,
    alias: Union[Unset, None, str] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
    my_label: Union[Unset, None, str] = UNSET,
    use_public_did: Union[Unset, None, bool] = UNSET,
) -> Response[ConnRecord]:
    """Create and send a request against public DID's implicit invitation

    Args:
        their_public_did (str):
        alias (Union[Unset, None, str]):
        mediation_id (Union[Unset, None, str]):
        my_endpoint (Union[Unset, None, str]):
        my_label (Union[Unset, None, str]):
        use_public_did (Union[Unset, None, bool]):

    Returns:
        Response[ConnRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        their_public_did=their_public_did,
        alias=alias,
        mediation_id=mediation_id,
        my_endpoint=my_endpoint,
        my_label=my_label,
        use_public_did=use_public_did,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    their_public_did: str,
    alias: Union[Unset, None, str] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
    my_label: Union[Unset, None, str] = UNSET,
    use_public_did: Union[Unset, None, bool] = UNSET,
) -> Optional[ConnRecord]:
    """Create and send a request against public DID's implicit invitation

    Args:
        their_public_did (str):
        alias (Union[Unset, None, str]):
        mediation_id (Union[Unset, None, str]):
        my_endpoint (Union[Unset, None, str]):
        my_label (Union[Unset, None, str]):
        use_public_did (Union[Unset, None, bool]):

    Returns:
        Response[ConnRecord]
    """

    return sync_detailed(
        client=client,
        their_public_did=their_public_did,
        alias=alias,
        mediation_id=mediation_id,
        my_endpoint=my_endpoint,
        my_label=my_label,
        use_public_did=use_public_did,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    their_public_did: str,
    alias: Union[Unset, None, str] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
    my_label: Union[Unset, None, str] = UNSET,
    use_public_did: Union[Unset, None, bool] = UNSET,
) -> Response[ConnRecord]:
    """Create and send a request against public DID's implicit invitation

    Args:
        their_public_did (str):
        alias (Union[Unset, None, str]):
        mediation_id (Union[Unset, None, str]):
        my_endpoint (Union[Unset, None, str]):
        my_label (Union[Unset, None, str]):
        use_public_did (Union[Unset, None, bool]):

    Returns:
        Response[ConnRecord]
    """

    kwargs = _get_kwargs(
        client=client,
        their_public_did=their_public_did,
        alias=alias,
        mediation_id=mediation_id,
        my_endpoint=my_endpoint,
        my_label=my_label,
        use_public_did=use_public_did,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    their_public_did: str,
    alias: Union[Unset, None, str] = UNSET,
    mediation_id: Union[Unset, None, str] = UNSET,
    my_endpoint: Union[Unset, None, str] = UNSET,
    my_label: Union[Unset, None, str] = UNSET,
    use_public_did: Union[Unset, None, bool] = UNSET,
) -> Optional[ConnRecord]:
    """Create and send a request against public DID's implicit invitation

    Args:
        their_public_did (str):
        alias (Union[Unset, None, str]):
        mediation_id (Union[Unset, None, str]):
        my_endpoint (Union[Unset, None, str]):
        my_label (Union[Unset, None, str]):
        use_public_did (Union[Unset, None, bool]):

    Returns:
        Response[ConnRecord]
    """

    return (
        await asyncio_detailed(
            client=client,
            their_public_did=their_public_did,
            alias=alias,
            mediation_id=mediation_id,
            my_endpoint=my_endpoint,
            my_label=my_label,
            use_public_did=use_public_did,
        )
    ).parsed
