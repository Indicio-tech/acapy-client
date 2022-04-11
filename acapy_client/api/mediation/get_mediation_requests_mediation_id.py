from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.mediation_record import MediationRecord
from ...types import Response


def _get_kwargs(
    mediation_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/mediation/requests/{mediation_id}".format(client.base_url, mediation_id=mediation_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[MediationRecord]:
    if response.status_code == 200:
        response_200 = MediationRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[MediationRecord]:
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
) -> Response[MediationRecord]:
    """Retrieve mediation request record

    Args:
        mediation_id (str):

    Returns:
        Response[MediationRecord]
    """

    kwargs = _get_kwargs(
        mediation_id=mediation_id,
        client=client,
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
) -> Optional[MediationRecord]:
    """Retrieve mediation request record

    Args:
        mediation_id (str):

    Returns:
        Response[MediationRecord]
    """

    return sync_detailed(
        mediation_id=mediation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    mediation_id: str,
    *,
    client: Client,
) -> Response[MediationRecord]:
    """Retrieve mediation request record

    Args:
        mediation_id (str):

    Returns:
        Response[MediationRecord]
    """

    kwargs = _get_kwargs(
        mediation_id=mediation_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    mediation_id: str,
    *,
    client: Client,
) -> Optional[MediationRecord]:
    """Retrieve mediation request record

    Args:
        mediation_id (str):

    Returns:
        Response[MediationRecord]
    """

    return (
        await asyncio_detailed(
            mediation_id=mediation_id,
            client=client,
        )
    ).parsed
