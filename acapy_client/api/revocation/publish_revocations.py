from typing import Any, Dict, Optional, Union

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[PublishRevocations, TxnOrPublishRevocationsResult]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union[PublishRevocations, TxnOrPublishRevocationsResult]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = PublishRevocations.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = TxnOrPublishRevocationsResult.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PublishRevocations, TxnOrPublishRevocationsResult]]:
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
) -> Response[Union[PublishRevocations, TxnOrPublishRevocationsResult]]:
    """Publish pending revocations to ledger

    Args:
        json_body (PublishRevocations):

    Returns:
        Response[Union[PublishRevocations, TxnOrPublishRevocationsResult]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: PublishRevocations,
) -> Optional[Union[PublishRevocations, TxnOrPublishRevocationsResult]]:
    """Publish pending revocations to ledger

    Args:
        json_body (PublishRevocations):

    Returns:
        Response[Union[PublishRevocations, TxnOrPublishRevocationsResult]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PublishRevocations,
) -> Response[Union[PublishRevocations, TxnOrPublishRevocationsResult]]:
    """Publish pending revocations to ledger

    Args:
        json_body (PublishRevocations):

    Returns:
        Response[Union[PublishRevocations, TxnOrPublishRevocationsResult]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PublishRevocations,
) -> Optional[Union[PublishRevocations, TxnOrPublishRevocationsResult]]:
    """Publish pending revocations to ledger

    Args:
        json_body (PublishRevocations):

    Returns:
        Response[Union[PublishRevocations, TxnOrPublishRevocationsResult]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
