from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofRequestedProofPredicate")


@attr.s(auto_attribs=True)
class IndyProofRequestedProofPredicate:
    """
    Attributes:
        sub_proof_index (Union[Unset, int]): Sub-proof index
    """

    sub_proof_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_proof_index = self.sub_proof_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_proof_index is not UNSET:
            field_dict["sub_proof_index"] = sub_proof_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sub_proof_index = d.pop("sub_proof_index", UNSET)

        indy_proof_requested_proof_predicate = cls(
            sub_proof_index=sub_proof_index,
        )

        indy_proof_requested_proof_predicate.additional_properties = d
        return indy_proof_requested_proof_predicate

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
