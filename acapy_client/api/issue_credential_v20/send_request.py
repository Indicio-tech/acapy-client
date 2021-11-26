from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v20_cred_ex_record import V20CredExRecord
from ...models.v20_cred_request_request import V20CredRequestRequest
from ...types import Response


def _get_kwargs(
    cred_ex_id: str,
    *,
    client: Client,
    json_body: V20CredRequestRequest,
) -> Dict[str, Any]:
    url = "{}/issue-credential-2.0/records/{cred_ex_id}/send-request".format(client.base_url, cred_ex_id=cred_ex_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[V20CredExRecord]:
    if response.status_code == 200:
        response_200 = V20CredExRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V20CredExRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cred_ex_id: str,
    *,
    client: Client,
    json_body: V20CredRequestRequest,
) -> Response[V20CredExRecord]:
    kwargs = _get_kwargs(
        cred_ex_id=cred_ex_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cred_ex_id: str,
    *,
    client: Client,
    json_body: V20CredRequestRequest,
) -> Optional[V20CredExRecord]:
    """ """

    return sync_detailed(
        cred_ex_id=cred_ex_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cred_ex_id: str,
    *,
    client: Client,
    json_body: V20CredRequestRequest,
) -> Response[V20CredExRecord]:
    kwargs = _get_kwargs(
        cred_ex_id=cred_ex_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cred_ex_id: str,
    *,
    client: Client,
    json_body: V20CredRequestRequest,
) -> Optional[V20CredExRecord]:
    """ """

    return (
        await asyncio_detailed(
            cred_ex_id=cred_ex_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
