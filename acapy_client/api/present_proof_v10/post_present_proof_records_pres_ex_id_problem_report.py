from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v10_present_proof_module_response import V10PresentProofModuleResponse
from ...models.v10_presentation_problem_report_request import V10PresentationProblemReportRequest
from ...types import Response


def _get_kwargs(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: V10PresentationProblemReportRequest,
) -> Dict[str, Any]:
    url = "{}/present-proof/records/{pres_ex_id}/problem-report".format(client.base_url, pres_ex_id=pres_ex_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[V10PresentProofModuleResponse]:
    if response.status_code == 200:
        response_200 = V10PresentProofModuleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V10PresentProofModuleResponse]:
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
    json_body: V10PresentationProblemReportRequest,
) -> Response[V10PresentProofModuleResponse]:
    kwargs = _get_kwargs(
        pres_ex_id=pres_ex_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: V10PresentationProblemReportRequest,
) -> Optional[V10PresentProofModuleResponse]:
    """ """

    return sync_detailed(
        pres_ex_id=pres_ex_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: V10PresentationProblemReportRequest,
) -> Response[V10PresentProofModuleResponse]:
    kwargs = _get_kwargs(
        pres_ex_id=pres_ex_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    pres_ex_id: str,
    *,
    client: Client,
    json_body: V10PresentationProblemReportRequest,
) -> Optional[V10PresentProofModuleResponse]:
    """ """

    return (
        await asyncio_detailed(
            pres_ex_id=pres_ex_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
