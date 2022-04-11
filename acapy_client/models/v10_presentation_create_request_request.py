from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_proof_request import IndyProofRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="V10PresentationCreateRequestRequest")


@attr.s(auto_attribs=True)
class V10PresentationCreateRequestRequest:
    """
    Attributes:
        proof_request (IndyProofRequest):
        comment (Union[Unset, None, str]):
        trace (Union[Unset, bool]): Whether to trace event (default false)
    """

    proof_request: IndyProofRequest
    comment: Union[Unset, None, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proof_request = self.proof_request.to_dict()

        comment = self.comment
        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proof_request": proof_request,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        proof_request = IndyProofRequest.from_dict(d.pop("proof_request"))

        comment = d.pop("comment", UNSET)

        trace = d.pop("trace", UNSET)

        v10_presentation_create_request_request = cls(
            proof_request=proof_request,
            comment=comment,
            trace=trace,
        )

        v10_presentation_create_request_request.additional_properties = d
        return v10_presentation_create_request_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
