from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.publish_revocations import PublishRevocations
from ...models.txn_or_publish_revocations_result import TxnOrPublishRevocationsResult
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PublishRevocations,
) -> Dict[str, Any]:
    url = "{}/revocation/publish-revocations".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "verify": client.verify_ssl,
    }


def _parse_response(*, response: httpx.Response) -> Optional[TxnOrPublishRevocationsResult]:
    if response.status_code == 200:
        response_200 = TxnOrPublishRevocationsResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TxnOrPublishRevocationsResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PublishRevocations,
) -> Response[TxnOrPublishRevocationsResult]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: PublishRevocations,
) -> Optional[TxnOrPublishRevocationsResult]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PublishRevocations,
) -> Response[TxnOrPublishRevocationsResult]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PublishRevocations,
) -> Optional[TxnOrPublishRevocationsResult]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
