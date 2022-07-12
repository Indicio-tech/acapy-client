from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cred_rev_indy_records_result_rev_reg_delta import CredRevIndyRecordsResultRevRegDelta
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredRevIndyRecordsResult")


@attr.s(auto_attribs=True)
class CredRevIndyRecordsResult:
    """
    Attributes:
        rev_reg_delta (Union[Unset, CredRevIndyRecordsResultRevRegDelta]): Indy revocation registry delta
    """

    rev_reg_delta: Union[Unset, CredRevIndyRecordsResultRevRegDelta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rev_reg_delta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rev_reg_delta, Unset):
            rev_reg_delta = self.rev_reg_delta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rev_reg_delta is not UNSET:
            field_dict["rev_reg_delta"] = rev_reg_delta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _rev_reg_delta = d.pop("rev_reg_delta", UNSET)
        rev_reg_delta: Union[Unset, CredRevIndyRecordsResultRevRegDelta]
        if isinstance(_rev_reg_delta, Unset):
            rev_reg_delta = UNSET
        else:
            rev_reg_delta = CredRevIndyRecordsResultRevRegDelta.from_dict(_rev_reg_delta)

        cred_rev_indy_records_result = cls(
            rev_reg_delta=rev_reg_delta,
        )

        cred_rev_indy_records_result.additional_properties = d
        return cred_rev_indy_records_result

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
