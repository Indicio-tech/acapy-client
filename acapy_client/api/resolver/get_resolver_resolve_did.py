from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.resolution_result import ResolutionResult
from ...types import Response


def _get_kwargs(
    did: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/resolver/resolve/{did}".format(client.base_url, did=did)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ResolutionResult]:
    if response.status_code == 200:
        response_200 = ResolutionResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ResolutionResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    did: str,
    *,
    client: Client,
) -> Response[ResolutionResult]:
    """Retrieve doc for requested did

    Args:
        did (str):

    Returns:
        Response[ResolutionResult]
    """

    kwargs = _get_kwargs(
        did=did,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    did: str,
    *,
    client: Client,
) -> Optional[ResolutionResult]:
    """Retrieve doc for requested did

    Args:
        did (str):

    Returns:
        Response[ResolutionResult]
    """

    return sync_detailed(
        did=did,
        client=client,
    ).parsed


async def asyncio_detailed(
    did: str,
    *,
    client: Client,
) -> Response[ResolutionResult]:
    """Retrieve doc for requested did

    Args:
        did (str):

    Returns:
        Response[ResolutionResult]
    """

    kwargs = _get_kwargs(
        did=did,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    did: str,
    *,
    client: Client,
) -> Optional[ResolutionResult]:
    """Retrieve doc for requested did

    Args:
        did (str):

    Returns:
        Response[ResolutionResult]
    """

    return (
        await asyncio_detailed(
            did=did,
            client=client,
        )
    ).parsed
