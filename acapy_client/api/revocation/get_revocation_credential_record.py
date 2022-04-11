from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.cred_rev_record_result import CredRevRecordResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    cred_ex_id: Union[Unset, None, str] = UNSET,
    cred_rev_id: Union[Unset, None, str] = UNSET,
    rev_reg_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/revocation/credential-record".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cred_ex_id"] = cred_ex_id

    params["cred_rev_id"] = cred_rev_id

    params["rev_reg_id"] = rev_reg_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CredRevRecordResult]:
    if response.status_code == 200:
        response_200 = CredRevRecordResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CredRevRecordResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    cred_ex_id: Union[Unset, None, str] = UNSET,
    cred_rev_id: Union[Unset, None, str] = UNSET,
    rev_reg_id: Union[Unset, None, str] = UNSET,
) -> Response[CredRevRecordResult]:
    """Get credential revocation status

    Args:
        cred_ex_id (Union[Unset, None, str]):
        cred_rev_id (Union[Unset, None, str]):
        rev_reg_id (Union[Unset, None, str]):

    Returns:
        Response[CredRevRecordResult]
    """

    kwargs = _get_kwargs(
        client=client,
        cred_ex_id=cred_ex_id,
        cred_rev_id=cred_rev_id,
        rev_reg_id=rev_reg_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    cred_ex_id: Union[Unset, None, str] = UNSET,
    cred_rev_id: Union[Unset, None, str] = UNSET,
    rev_reg_id: Union[Unset, None, str] = UNSET,
) -> Optional[CredRevRecordResult]:
    """Get credential revocation status

    Args:
        cred_ex_id (Union[Unset, None, str]):
        cred_rev_id (Union[Unset, None, str]):
        rev_reg_id (Union[Unset, None, str]):

    Returns:
        Response[CredRevRecordResult]
    """

    return sync_detailed(
        client=client,
        cred_ex_id=cred_ex_id,
        cred_rev_id=cred_rev_id,
        rev_reg_id=rev_reg_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    cred_ex_id: Union[Unset, None, str] = UNSET,
    cred_rev_id: Union[Unset, None, str] = UNSET,
    rev_reg_id: Union[Unset, None, str] = UNSET,
) -> Response[CredRevRecordResult]:
    """Get credential revocation status

    Args:
        cred_ex_id (Union[Unset, None, str]):
        cred_rev_id (Union[Unset, None, str]):
        rev_reg_id (Union[Unset, None, str]):

    Returns:
        Response[CredRevRecordResult]
    """

    kwargs = _get_kwargs(
        client=client,
        cred_ex_id=cred_ex_id,
        cred_rev_id=cred_rev_id,
        rev_reg_id=rev_reg_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    cred_ex_id: Union[Unset, None, str] = UNSET,
    cred_rev_id: Union[Unset, None, str] = UNSET,
    rev_reg_id: Union[Unset, None, str] = UNSET,
) -> Optional[CredRevRecordResult]:
    """Get credential revocation status

    Args:
        cred_ex_id (Union[Unset, None, str]):
        cred_rev_id (Union[Unset, None, str]):
        rev_reg_id (Union[Unset, None, str]):

    Returns:
        Response[CredRevRecordResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            cred_ex_id=cred_ex_id,
            cred_rev_id=cred_rev_id,
            rev_reg_id=rev_reg_id,
        )
    ).parsed
