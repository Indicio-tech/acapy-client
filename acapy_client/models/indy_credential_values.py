from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.indy_attr_value import IndyAttrValue

T = TypeVar("T", bound="IndyCredentialValues")


@attr.s(auto_attribs=True)
class IndyCredentialValues:
    """Credential attributes"""

    additional_properties: Dict[str, IndyAttrValue] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        indy_credential_values = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = IndyAttrValue.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        indy_credential_values.additional_properties = additional_properties
        return indy_credential_values

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> IndyAttrValue:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: IndyAttrValue) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
