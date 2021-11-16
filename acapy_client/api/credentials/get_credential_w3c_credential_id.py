from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.vc_record import VCRecord
from ...types import Response


def _get_kwargs(
    credential_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/credential/w3c/{credential_id}".format(client.base_url, credential_id=credential_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "verify": client.verify_ssl,
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
    credential_id: str,
    *,
    client: Client,
) -> Response[VCRecord]:
    kwargs = _get_kwargs(
        credential_id=credential_id,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    credential_id: str,
    *,
    client: Client,
) -> Optional[VCRecord]:
    """ """

    return sync_detailed(
        credential_id=credential_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    credential_id: str,
    *,
    client: Client,
) -> Response[VCRecord]:
    kwargs = _get_kwargs(
        credential_id=credential_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    credential_id: str,
    *,
    client: Client,
) -> Optional[VCRecord]:
    """ """

    return (
        await asyncio_detailed(
            credential_id=credential_id,
            client=client,
        )
    ).parsed