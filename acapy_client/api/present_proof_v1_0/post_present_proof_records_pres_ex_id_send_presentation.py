from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.indy_pres_spec import IndyPresSpec
from ...models.v10_presentation_exchange import V10PresentationExchange
from ...types import Response


def _get_kwargs(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: IndyPresSpec,
) -> Dict[str, Any]:
    url = "{}/present-proof/records/{pres_ex_id}/send-presentation".format(client.base_url, pres_ex_id=pres_ex_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[V10PresentationExchange]:
    if response.status_code == 200:
        response_200 = V10PresentationExchange.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V10PresentationExchange]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: IndyPresSpec,
) -> Response[V10PresentationExchange]:
    """Sends a proof presentation

    Args:
        pres_ex_id (str):
        json_body (IndyPresSpec):

    Returns:
        Response[V10PresentationExchange]
    """

    kwargs = _get_kwargs(
        pres_ex_id=pres_ex_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: IndyPresSpec,
) -> Optional[V10PresentationExchange]:
    """Sends a proof presentation

    Args:
        pres_ex_id (str):
        json_body (IndyPresSpec):

    Returns:
        Response[V10PresentationExchange]
    """

    return sync_detailed(
        pres_ex_id=pres_ex_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: IndyPresSpec,
) -> Response[V10PresentationExchange]:
    """Sends a proof presentation

    Args:
        pres_ex_id (str):
        json_body (IndyPresSpec):

    Returns:
        Response[V10PresentationExchange]
    """

    kwargs = _get_kwargs(
        pres_ex_id=pres_ex_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: IndyPresSpec,
) -> Optional[V10PresentationExchange]:
    """Sends a proof presentation

    Args:
        pres_ex_id (str):
        json_body (IndyPresSpec):

    Returns:
        Response[V10PresentationExchange]
    """

    return (
        await asyncio_detailed(
            pres_ex_id=pres_ex_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
