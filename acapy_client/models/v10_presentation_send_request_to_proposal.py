from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="V10PresentationSendRequestToProposal")


@attr.s(auto_attribs=True)
class V10PresentationSendRequestToProposal:
    """
    Attributes:
        auto_verify (Union[Unset, bool]): Verifier choice to auto-verify proof presentation
        trace (Union[Unset, bool]): Whether to trace event (default false)
    """

    auto_verify: Union[Unset, bool] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_verify = self.auto_verify
        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_verify is not UNSET:
            field_dict["auto_verify"] = auto_verify
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_verify = d.pop("auto_verify", UNSET)

        trace = d.pop("trace", UNSET)

        v10_presentation_send_request_to_proposal = cls(
            auto_verify=auto_verify,
            trace=trace,
        )

        v10_presentation_send_request_to_proposal.additional_properties = d
        return v10_presentation_send_request_to_proposal

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
