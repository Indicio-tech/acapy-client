from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.raw_encoded import RawEncoded

T = TypeVar("T", bound="IndyProofRequestedProofRevealedAttrGroupValues")


@attr.s(auto_attribs=True)
class IndyProofRequestedProofRevealedAttrGroupValues:
    """Indy proof requested proof revealed attr groups group value"""

    additional_properties: Dict[str, RawEncoded] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        indy_proof_requested_proof_revealed_attr_group_values = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RawEncoded.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        indy_proof_requested_proof_revealed_attr_group_values.additional_properties = additional_properties
        return indy_proof_requested_proof_revealed_attr_group_values

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RawEncoded:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RawEncoded) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
