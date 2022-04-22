from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_pres_request_by_format import V20PresRequestByFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20PresSendRequestRequest")


@attr.s(auto_attribs=True)
class V20PresSendRequestRequest:
    """
    Attributes:
        connection_id (str): Connection identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        presentation_request (V20PresRequestByFormat):
        auto_verify (Union[Unset, bool]): Verifier choice to auto-verify proof presentation
        comment (Union[Unset, None, str]):
        trace (Union[Unset, bool]): Whether to trace event (default false)
    """

    connection_id: str
    presentation_request: V20PresRequestByFormat
    auto_verify: Union[Unset, bool] = UNSET
    comment: Union[Unset, None, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        presentation_request = self.presentation_request.to_dict()

        auto_verify = self.auto_verify
        comment = self.comment
        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
                "presentation_request": presentation_request,
            }
        )
        if auto_verify is not UNSET:
            field_dict["auto_verify"] = auto_verify
        if comment is not UNSET:
            field_dict["comment"] = comment
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connection_id")

        presentation_request = V20PresRequestByFormat.from_dict(d.pop("presentation_request"))

        auto_verify = d.pop("auto_verify", UNSET)

        comment = d.pop("comment", UNSET)

        trace = d.pop("trace", UNSET)

        v20_pres_send_request_request = cls(
            connection_id=connection_id,
            presentation_request=presentation_request,
            auto_verify=auto_verify,
            comment=comment,
            trace=trace,
        )

        v20_pres_send_request_request.additional_properties = d
        return v20_pres_send_request_request

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
