from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.rev_reg_result import RevRegResult
from ...models.rev_reg_update_tails_file_uri import RevRegUpdateTailsFileUri
from ...types import Response


def _get_kwargs(
    rev_reg_id: str,
    *,
    client: Client,
    json_body: RevRegUpdateTailsFileUri,
) -> Dict[str, Any]:
    url = "{}/revocation/registry/{rev_reg_id}".format(client.base_url, rev_reg_id=rev_reg_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[RevRegResult]:
    if response.status_code == 200:
        response_200 = RevRegResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RevRegResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    rev_reg_id: str,
    *,
    client: Client,
    json_body: RevRegUpdateTailsFileUri,
) -> Response[RevRegResult]:
    """Update revocation registry with new public URI to its tails file

    Args:
        rev_reg_id (str):
        json_body (RevRegUpdateTailsFileUri):

    Returns:
        Response[RevRegResult]
    """

    kwargs = _get_kwargs(
        rev_reg_id=rev_reg_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    rev_reg_id: str,
    *,
    client: Client,
    json_body: RevRegUpdateTailsFileUri,
) -> Optional[RevRegResult]:
    """Update revocation registry with new public URI to its tails file

    Args:
        rev_reg_id (str):
        json_body (RevRegUpdateTailsFileUri):

    Returns:
        Response[RevRegResult]
    """

    return sync_detailed(
        rev_reg_id=rev_reg_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    rev_reg_id: str,
    *,
    client: Client,
    json_body: RevRegUpdateTailsFileUri,
) -> Response[RevRegResult]:
    """Update revocation registry with new public URI to its tails file

    Args:
        rev_reg_id (str):
        json_body (RevRegUpdateTailsFileUri):

    Returns:
        Response[RevRegResult]
    """

    kwargs = _get_kwargs(
        rev_reg_id=rev_reg_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    rev_reg_id: str,
    *,
    client: Client,
    json_body: RevRegUpdateTailsFileUri,
) -> Optional[RevRegResult]:
    """Update revocation registry with new public URI to its tails file

    Args:
        rev_reg_id (str):
        json_body (RevRegUpdateTailsFileUri):

    Returns:
        Response[RevRegResult]
    """

    return (
        await asyncio_detailed(
            rev_reg_id=rev_reg_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
