from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.admin_mediation_deny import AdminMediationDeny
from ...models.mediation_deny import MediationDeny
from ...types import Response


def _get_kwargs(
    mediation_id: str,
    *,
    client: Client,
    json_body: AdminMediationDeny,
) -> Dict[str, Any]:
    url = "{}/mediation/requests/{mediation_id}/deny".format(client.base_url, mediation_id=mediation_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[MediationDeny]:
    if response.status_code == 201:
        response_201 = MediationDeny.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[MediationDeny]:
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
    json_body: AdminMediationDeny,
) -> Response[MediationDeny]:
    """Deny a stored mediation request

    Args:
        mediation_id (str):
        json_body (AdminMediationDeny):

    Returns:
        Response[MediationDeny]
    """

    kwargs = _get_kwargs(
        mediation_id=mediation_id,
        client=client,
        json_body=json_body,
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
    json_body: AdminMediationDeny,
) -> Optional[MediationDeny]:
    """Deny a stored mediation request

    Args:
        mediation_id (str):
        json_body (AdminMediationDeny):

    Returns:
        Response[MediationDeny]
    """

    return sync_detailed(
        mediation_id=mediation_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    mediation_id: str,
    *,
    client: Client,
    json_body: AdminMediationDeny,
) -> Response[MediationDeny]:
    """Deny a stored mediation request

    Args:
        mediation_id (str):
        json_body (AdminMediationDeny):

    Returns:
        Response[MediationDeny]
    """

    kwargs = _get_kwargs(
        mediation_id=mediation_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    mediation_id: str,
    *,
    client: Client,
    json_body: AdminMediationDeny,
) -> Optional[MediationDeny]:
    """Deny a stored mediation request

    Args:
        mediation_id (str):
        json_body (AdminMediationDeny):

    Returns:
        Response[MediationDeny]
    """

    return (
        await asyncio_detailed(
            mediation_id=mediation_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
