from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v20_pres_problem_report_request import V20PresProblemReportRequest
from ...models.v20_present_proof_module_response import V20PresentProofModuleResponse
from ...types import Response


def _get_kwargs(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: V20PresProblemReportRequest,
) -> Dict[str, Any]:
    url = "{}/present-proof-2.0/records/{pres_ex_id}/problem-report".format(client.base_url, pres_ex_id=pres_ex_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[V20PresentProofModuleResponse]:
    if response.status_code == 200:
        response_200 = V20PresentProofModuleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V20PresentProofModuleResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: V20PresProblemReportRequest,
) -> Response[V20PresentProofModuleResponse]:
    """Send a problem report for presentation exchange

    Args:
        pres_ex_id (str):
        json_body (V20PresProblemReportRequest):

    Returns:
        Response[V20PresentProofModuleResponse]
    """

    kwargs = _get_kwargs(
        pres_ex_id=pres_ex_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: V20PresProblemReportRequest,
) -> Optional[V20PresentProofModuleResponse]:
    """Send a problem report for presentation exchange

    Args:
        pres_ex_id (str):
        json_body (V20PresProblemReportRequest):

    Returns:
        Response[V20PresentProofModuleResponse]
    """

    return sync_detailed(
        pres_ex_id=pres_ex_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: V20PresProblemReportRequest,
) -> Response[V20PresentProofModuleResponse]:
    """Send a problem report for presentation exchange

    Args:
        pres_ex_id (str):
        json_body (V20PresProblemReportRequest):

    Returns:
        Response[V20PresentProofModuleResponse]
    """

    kwargs = _get_kwargs(
        pres_ex_id=pres_ex_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: V20PresProblemReportRequest,
) -> Optional[V20PresentProofModuleResponse]:
    """Send a problem report for presentation exchange

    Args:
        pres_ex_id (str):
        json_body (V20PresProblemReportRequest):

    Returns:
        Response[V20PresentProofModuleResponse]
    """

    return (
        await asyncio_detailed(
            pres_ex_id=pres_ex_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
