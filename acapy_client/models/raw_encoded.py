from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawEncoded")


@attr.s(auto_attribs=True)
class RawEncoded:
    """
    Attributes:
        encoded (Union[Unset, str]): Encoded value Example: -1.
        raw (Union[Unset, str]): Raw value
    """

    encoded: Union[Unset, str] = UNSET
    raw: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encoded = self.encoded
        raw = self.raw

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encoded is not UNSET:
            field_dict["encoded"] = encoded
        if raw is not UNSET:
            field_dict["raw"] = raw

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encoded = d.pop("encoded", UNSET)

        raw = d.pop("raw", UNSET)

        raw_encoded = cls(
            encoded=encoded,
            raw=raw,
        )

        raw_encoded.additional_properties = d
        return raw_encoded

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
