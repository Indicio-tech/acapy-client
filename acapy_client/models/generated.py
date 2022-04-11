from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Generated")


@attr.s(auto_attribs=True)
class Generated:
    """
    Attributes:
        master_secret (Union[Unset, str]):  Example: 0.
        number (Union[Unset, str]):  Example: 0.
        remainder (Union[Unset, str]):  Example: 0.
    """

    master_secret: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    remainder: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        master_secret = self.master_secret
        number = self.number
        remainder = self.remainder

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if master_secret is not UNSET:
            field_dict["master_secret"] = master_secret
        if number is not UNSET:
            field_dict["number"] = number
        if remainder is not UNSET:
            field_dict["remainder"] = remainder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        master_secret = d.pop("master_secret", UNSET)

        number = d.pop("number", UNSET)

        remainder = d.pop("remainder", UNSET)

        generated = cls(
            master_secret=master_secret,
            number=number,
            remainder=remainder,
        )

        generated.additional_properties = d
        return generated

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
