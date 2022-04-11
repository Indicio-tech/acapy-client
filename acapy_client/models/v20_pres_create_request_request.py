from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_pres_request_by_format import V20PresRequestByFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20PresCreateRequestRequest")


@attr.s(auto_attribs=True)
class V20PresCreateRequestRequest:
    """
    Attributes:
        presentation_request (V20PresRequestByFormat):
        comment (Union[Unset, None, str]):
        trace (Union[Unset, bool]): Whether to trace event (default false)
    """

    presentation_request: V20PresRequestByFormat
    comment: Union[Unset, None, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        presentation_request = self.presentation_request.to_dict()

        comment = self.comment
        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "presentation_request": presentation_request,
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
        presentation_request = V20PresRequestByFormat.from_dict(d.pop("presentation_request"))

        comment = d.pop("comment", UNSET)

        trace = d.pop("trace", UNSET)

        v20_pres_create_request_request = cls(
            presentation_request=presentation_request,
            comment=comment,
            trace=trace,
        )

        v20_pres_create_request_request.additional_properties = d
        return v20_pres_create_request_request

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
