from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.attribute_mime_types_result import AttributeMimeTypesResult
from ...types import Response


def _get_kwargs(
    credential_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/credential/mime-types/{credential_id}".format(client.base_url, credential_id=credential_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[AttributeMimeTypesResult]:
    if response.status_code == 200:
        response_200 = AttributeMimeTypesResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AttributeMimeTypesResult]:
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
) -> Response[AttributeMimeTypesResult]:
    """Get attribute MIME types from wallet

    Args:
        credential_id (str):

    Returns:
        Response[AttributeMimeTypesResult]
    """

    kwargs = _get_kwargs(
        credential_id=credential_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    credential_id: str,
    *,
    client: Client,
) -> Optional[AttributeMimeTypesResult]:
    """Get attribute MIME types from wallet

    Args:
        credential_id (str):

    Returns:
        Response[AttributeMimeTypesResult]
    """

    return sync_detailed(
        credential_id=credential_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    credential_id: str,
    *,
    client: Client,
) -> Response[AttributeMimeTypesResult]:
    """Get attribute MIME types from wallet

    Args:
        credential_id (str):

    Returns:
        Response[AttributeMimeTypesResult]
    """

    kwargs = _get_kwargs(
        credential_id=credential_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    credential_id: str,
    *,
    client: Client,
) -> Optional[AttributeMimeTypesResult]:
    """Get attribute MIME types from wallet

    Args:
        credential_id (str):

    Returns:
        Response[AttributeMimeTypesResult]
    """

    return (
        await asyncio_detailed(
            credential_id=credential_id,
            client=client,
        )
    ).parsed
