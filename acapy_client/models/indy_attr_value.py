from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="IndyAttrValue")


@attr.s(auto_attribs=True)
class IndyAttrValue:
    """
    Attributes:
        encoded (str): Attribute encoded value Example: -1.
        raw (str): Attribute raw value
    """

    encoded: str
    raw: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encoded = self.encoded
        raw = self.raw

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encoded": encoded,
                "raw": raw,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encoded = d.pop("encoded")

        raw = d.pop("raw")

        indy_attr_value = cls(
            encoded=encoded,
            raw=raw,
        )

        indy_attr_value.additional_properties = d
        return indy_attr_value

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
