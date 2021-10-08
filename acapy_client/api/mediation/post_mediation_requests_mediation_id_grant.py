from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.mediation_grant import MediationGrant
from ...types import Response


def _get_kwargs(
    mediation_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/mediation/requests/{mediation_id}/grant".format(client.base_url, mediation_id=mediation_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[MediationGrant]:
    if response.status_code == 201:
        response_201 = MediationGrant.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[MediationGrant]:
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
) -> Response[MediationGrant]:
    kwargs = _get_kwargs(
        mediation_id=mediation_id,
        client=client,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    mediation_id: str,
    *,
    client: Client,
) -> Optional[MediationGrant]:
    """ """

    return sync_detailed(
        mediation_id=mediation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    mediation_id: str,
    *,
    client: Client,
) -> Response[MediationGrant]:
    kwargs = _get_kwargs(
        mediation_id=mediation_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    mediation_id: str,
    *,
    client: Client,
) -> Optional[MediationGrant]:
    """ """

    return (
        await asyncio_detailed(
            mediation_id=mediation_id,
            client=client,
        )
    ).parsed
