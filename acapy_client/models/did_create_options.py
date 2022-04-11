from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.did_create_options_key_type import DIDCreateOptionsKeyType

T = TypeVar("T", bound="DIDCreateOptions")


@attr.s(auto_attribs=True)
class DIDCreateOptions:
    """
    Attributes:
        key_type (DIDCreateOptionsKeyType):  Example: ed25519.
    """

    key_type: DIDCreateOptionsKeyType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_type = self.key_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_type": key_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_type = DIDCreateOptionsKeyType(d.pop("key_type"))

        did_create_options = cls(
            key_type=key_type,
        )

        did_create_options.additional_properties = d
        return did_create_options

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
