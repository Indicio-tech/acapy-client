from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.keylist_query import KeylistQuery
from ...models.keylist_query_filter_request import KeylistQueryFilterRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    mediation_id: str,
    *,
    client: Client,
    json_body: KeylistQueryFilterRequest,
    paginate_limit: Union[Unset, None, int] = -1,
    paginate_offset: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/mediation/keylists/{mediation_id}/send-keylist-query".format(client.base_url, mediation_id=mediation_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["paginate_limit"] = paginate_limit

    params["paginate_offset"] = paginate_offset

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


def _parse_response(*, response: httpx.Response) -> Optional[KeylistQuery]:
    if response.status_code == 201:
        response_201 = KeylistQuery.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[KeylistQuery]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    mediation_id: str,
    *,
    client: Client,
    json_body: KeylistQueryFilterRequest,
    paginate_limit: Union[Unset, None, int] = -1,
    paginate_offset: Union[Unset, None, int] = 0,
) -> Response[KeylistQuery]:
    """Send keylist query to mediator

    Args:
        mediation_id (str):
        paginate_limit (Union[Unset, None, int]):  Default: -1.
        paginate_offset (Union[Unset, None, int]):
        json_body (KeylistQueryFilterRequest):

    Returns:
        Response[KeylistQuery]
    """

    kwargs = _get_kwargs(
        mediation_id=mediation_id,
        client=client,
        json_body=json_body,
        paginate_limit=paginate_limit,
        paginate_offset=paginate_offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    mediation_id: str,
    *,
    client: Client,
    json_body: KeylistQueryFilterRequest,
    paginate_limit: Union[Unset, None, int] = -1,
    paginate_offset: Union[Unset, None, int] = 0,
) -> Optional[KeylistQuery]:
    """Send keylist query to mediator

    Args:
        mediation_id (str):
        paginate_limit (Union[Unset, None, int]):  Default: -1.
        paginate_offset (Union[Unset, None, int]):
        json_body (KeylistQueryFilterRequest):

    Returns:
        Response[KeylistQuery]
    """

    return sync_detailed(
        mediation_id=mediation_id,
        client=client,
        json_body=json_body,
        paginate_limit=paginate_limit,
        paginate_offset=paginate_offset,
    ).parsed


async def asyncio_detailed(
    mediation_id: str,
    *,
    client: Client,
    json_body: KeylistQueryFilterRequest,
    paginate_limit: Union[Unset, None, int] = -1,
    paginate_offset: Union[Unset, None, int] = 0,
) -> Response[KeylistQuery]:
    """Send keylist query to mediator

    Args:
        mediation_id (str):
        paginate_limit (Union[Unset, None, int]):  Default: -1.
        paginate_offset (Union[Unset, None, int]):
        json_body (KeylistQueryFilterRequest):

    Returns:
        Response[KeylistQuery]
    """

    kwargs = _get_kwargs(
        mediation_id=mediation_id,
        client=client,
        json_body=json_body,
        paginate_limit=paginate_limit,
        paginate_offset=paginate_offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    mediation_id: str,
    *,
    client: Client,
    json_body: KeylistQueryFilterRequest,
    paginate_limit: Union[Unset, None, int] = -1,
    paginate_offset: Union[Unset, None, int] = 0,
) -> Optional[KeylistQuery]:
    """Send keylist query to mediator

    Args:
        mediation_id (str):
        paginate_limit (Union[Unset, None, int]):  Default: -1.
        paginate_offset (Union[Unset, None, int]):
        json_body (KeylistQueryFilterRequest):

    Returns:
        Response[KeylistQuery]
    """

    return (
        await asyncio_detailed(
            mediation_id=mediation_id,
            client=client,
            json_body=json_body,
            paginate_limit=paginate_limit,
            paginate_offset=paginate_offset,
        )
    ).parsed
