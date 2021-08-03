from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v20_pres_ex_record import V20PresExRecord
from ...models.v20_pres_spec_by_format_request import V20PresSpecByFormatRequest
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    pres_ex_id: str,
    json_body: V20PresSpecByFormatRequest,
) -> Dict[str, Any]:
    url = "{}/present-proof-2.0/records/{pres_ex_id}/send-presentation".format(client.base_url, pres_ex_id=pres_ex_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[V20PresExRecord]:
    if response.status_code == 200:
        response_200 = V20PresExRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V20PresExRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    pres_ex_id: str,
    json_body: V20PresSpecByFormatRequest,
) -> Response[V20PresExRecord]:
    kwargs = _get_kwargs(
        client=client,
        pres_ex_id=pres_ex_id,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    pres_ex_id: str,
    json_body: V20PresSpecByFormatRequest,
) -> Optional[V20PresExRecord]:
    """ """

    return sync_detailed(
        client=client,
        pres_ex_id=pres_ex_id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pres_ex_id: str,
    json_body: V20PresSpecByFormatRequest,
) -> Response[V20PresExRecord]:
    kwargs = _get_kwargs(
        client=client,
        pres_ex_id=pres_ex_id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    pres_ex_id: str,
    json_body: V20PresSpecByFormatRequest,
) -> Optional[V20PresExRecord]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            pres_ex_id=pres_ex_id,
            json_body=json_body,
        )
    ).parsed
