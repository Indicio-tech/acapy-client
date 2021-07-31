from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.vc_record import VCRecord
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    credential_id: str,
) -> Dict[str, Any]:
    url = "{}/credential/w3c/{credential_id}".format(client.base_url, credential_id=credential_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[VCRecord]:
    if response.status_code == 200:
        response_200 = VCRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[VCRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    credential_id: str,
) -> Response[VCRecord]:
    kwargs = _get_kwargs(
        client=client,
        credential_id=credential_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    credential_id: str,
) -> Optional[VCRecord]:
    """ """

    return sync_detailed(
        client=client,
        credential_id=credential_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    credential_id: str,
) -> Response[VCRecord]:
    kwargs = _get_kwargs(
        client=client,
        credential_id=credential_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    credential_id: str,
) -> Optional[VCRecord]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            credential_id=credential_id,
        )
    ).parsed
