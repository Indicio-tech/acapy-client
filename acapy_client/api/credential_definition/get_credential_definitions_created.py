from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.credential_definitions_created_result import CredentialDefinitionsCreatedResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    cred_def_id: Union[Unset, None, str] = UNSET,
    issuer_did: Union[Unset, None, str] = UNSET,
    schema_id: Union[Unset, None, str] = UNSET,
    schema_issuer_did: Union[Unset, None, str] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
    schema_version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/credential-definitions/created".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cred_def_id"] = cred_def_id

    params["issuer_did"] = issuer_did

    params["schema_id"] = schema_id

    params["schema_issuer_did"] = schema_issuer_did

    params["schema_name"] = schema_name

    params["schema_version"] = schema_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CredentialDefinitionsCreatedResult]:
    if response.status_code == 200:
        response_200 = CredentialDefinitionsCreatedResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CredentialDefinitionsCreatedResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    cred_def_id: Union[Unset, None, str] = UNSET,
    issuer_did: Union[Unset, None, str] = UNSET,
    schema_id: Union[Unset, None, str] = UNSET,
    schema_issuer_did: Union[Unset, None, str] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
    schema_version: Union[Unset, None, str] = UNSET,
) -> Response[CredentialDefinitionsCreatedResult]:
    """Search for matching credential definitions that agent originated

    Args:
        cred_def_id (Union[Unset, None, str]):
        issuer_did (Union[Unset, None, str]):
        schema_id (Union[Unset, None, str]):
        schema_issuer_did (Union[Unset, None, str]):
        schema_name (Union[Unset, None, str]):
        schema_version (Union[Unset, None, str]):

    Returns:
        Response[CredentialDefinitionsCreatedResult]
    """

    kwargs = _get_kwargs(
        client=client,
        cred_def_id=cred_def_id,
        issuer_did=issuer_did,
        schema_id=schema_id,
        schema_issuer_did=schema_issuer_did,
        schema_name=schema_name,
        schema_version=schema_version,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    cred_def_id: Union[Unset, None, str] = UNSET,
    issuer_did: Union[Unset, None, str] = UNSET,
    schema_id: Union[Unset, None, str] = UNSET,
    schema_issuer_did: Union[Unset, None, str] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
    schema_version: Union[Unset, None, str] = UNSET,
) -> Optional[CredentialDefinitionsCreatedResult]:
    """Search for matching credential definitions that agent originated

    Args:
        cred_def_id (Union[Unset, None, str]):
        issuer_did (Union[Unset, None, str]):
        schema_id (Union[Unset, None, str]):
        schema_issuer_did (Union[Unset, None, str]):
        schema_name (Union[Unset, None, str]):
        schema_version (Union[Unset, None, str]):

    Returns:
        Response[CredentialDefinitionsCreatedResult]
    """

    return sync_detailed(
        client=client,
        cred_def_id=cred_def_id,
        issuer_did=issuer_did,
        schema_id=schema_id,
        schema_issuer_did=schema_issuer_did,
        schema_name=schema_name,
        schema_version=schema_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    cred_def_id: Union[Unset, None, str] = UNSET,
    issuer_did: Union[Unset, None, str] = UNSET,
    schema_id: Union[Unset, None, str] = UNSET,
    schema_issuer_did: Union[Unset, None, str] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
    schema_version: Union[Unset, None, str] = UNSET,
) -> Response[CredentialDefinitionsCreatedResult]:
    """Search for matching credential definitions that agent originated

    Args:
        cred_def_id (Union[Unset, None, str]):
        issuer_did (Union[Unset, None, str]):
        schema_id (Union[Unset, None, str]):
        schema_issuer_did (Union[Unset, None, str]):
        schema_name (Union[Unset, None, str]):
        schema_version (Union[Unset, None, str]):

    Returns:
        Response[CredentialDefinitionsCreatedResult]
    """

    kwargs = _get_kwargs(
        client=client,
        cred_def_id=cred_def_id,
        issuer_did=issuer_did,
        schema_id=schema_id,
        schema_issuer_did=schema_issuer_did,
        schema_name=schema_name,
        schema_version=schema_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    cred_def_id: Union[Unset, None, str] = UNSET,
    issuer_did: Union[Unset, None, str] = UNSET,
    schema_id: Union[Unset, None, str] = UNSET,
    schema_issuer_did: Union[Unset, None, str] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
    schema_version: Union[Unset, None, str] = UNSET,
) -> Optional[CredentialDefinitionsCreatedResult]:
    """Search for matching credential definitions that agent originated

    Args:
        cred_def_id (Union[Unset, None, str]):
        issuer_did (Union[Unset, None, str]):
        schema_id (Union[Unset, None, str]):
        schema_issuer_did (Union[Unset, None, str]):
        schema_name (Union[Unset, None, str]):
        schema_version (Union[Unset, None, str]):

    Returns:
        Response[CredentialDefinitionsCreatedResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            cred_def_id=cred_def_id,
            issuer_did=issuer_did,
            schema_id=schema_id,
            schema_issuer_did=schema_issuer_did,
            schema_name=schema_name,
            schema_version=schema_version,
        )
    ).parsed
