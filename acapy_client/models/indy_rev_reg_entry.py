from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_rev_reg_entry_value import IndyRevRegEntryValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyRevRegEntry")


@attr.s(auto_attribs=True)
class IndyRevRegEntry:
    """
    Attributes:
        value (Union[Unset, IndyRevRegEntryValue]):
        ver (Union[Unset, str]): Version of revocation registry entry Example: 1.0.
    """

    value: Union[Unset, IndyRevRegEntryValue] = UNSET
    ver: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        ver = self.ver

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if ver is not UNSET:
            field_dict["ver"] = ver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _value = d.pop("value", UNSET)
        value: Union[Unset, IndyRevRegEntryValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IndyRevRegEntryValue.from_dict(_value)

        ver = d.pop("ver", UNSET)

        indy_rev_reg_entry = cls(
            value=value,
            ver=ver,
        )

        indy_rev_reg_entry.additional_properties = d
        return indy_rev_reg_entry

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
