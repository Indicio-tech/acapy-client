from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_proof_requested_proof_revealed_attr_group_values import (
    IndyProofRequestedProofRevealedAttrGroupValues,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofRequestedProofRevealedAttrGroup")


@attr.s(auto_attribs=True)
class IndyProofRequestedProofRevealedAttrGroup:
    """
    Attributes:
        sub_proof_index (Union[Unset, int]): Sub-proof index
        values (Union[Unset, IndyProofRequestedProofRevealedAttrGroupValues]): Indy proof requested proof revealed attr
            groups group value
    """

    sub_proof_index: Union[Unset, int] = UNSET
    values: Union[Unset, IndyProofRequestedProofRevealedAttrGroupValues] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_proof_index = self.sub_proof_index
        values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_proof_index is not UNSET:
            field_dict["sub_proof_index"] = sub_proof_index
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sub_proof_index = d.pop("sub_proof_index", UNSET)

        _values = d.pop("values", UNSET)
        values: Union[Unset, IndyProofRequestedProofRevealedAttrGroupValues]
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = IndyProofRequestedProofRevealedAttrGroupValues.from_dict(_values)

        indy_proof_requested_proof_revealed_attr_group = cls(
            sub_proof_index=sub_proof_index,
            values=values,
        )

        indy_proof_requested_proof_revealed_attr_group.additional_properties = d
        return indy_proof_requested_proof_revealed_attr_group

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
