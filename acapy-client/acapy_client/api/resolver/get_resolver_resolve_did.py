from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.resolution_result import ResolutionResult
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    did: str,
) -> Dict[str, Any]:
    url = "{}/resolver/resolve/{did}".format(client.base_url, did=did)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
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
    *,
    client: Client,
    did: str,
) -> Response[ResolutionResult]:
    kwargs = _get_kwargs(
        client=client,
        did=did,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    did: str,
) -> Optional[ResolutionResult]:
    """ """

    return sync_detailed(
        client=client,
        did=did,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    did: str,
) -> Response[ResolutionResult]:
    kwargs = _get_kwargs(
        client=client,
        did=did,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    did: str,
) -> Optional[ResolutionResult]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            did=did,
        )
    ).parsed
