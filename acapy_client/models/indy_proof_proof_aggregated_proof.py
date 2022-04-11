from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofProofAggregatedProof")


@attr.s(auto_attribs=True)
class IndyProofProofAggregatedProof:
    """
    Attributes:
        c_hash (Union[Unset, str]): c_hash value
        c_list (Union[Unset, List[List[int]]]): c_list value
    """

    c_hash: Union[Unset, str] = UNSET
    c_list: Union[Unset, List[List[int]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        c_hash = self.c_hash
        c_list: Union[Unset, List[List[int]]] = UNSET
        if not isinstance(self.c_list, Unset):
            c_list = []
            for c_list_item_data in self.c_list:
                c_list_item = c_list_item_data

                c_list.append(c_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if c_hash is not UNSET:
            field_dict["c_hash"] = c_hash
        if c_list is not UNSET:
            field_dict["c_list"] = c_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        c_hash = d.pop("c_hash", UNSET)

        c_list = []
        _c_list = d.pop("c_list", UNSET)
        for c_list_item_data in _c_list or []:
            c_list_item = cast(List[int], c_list_item_data)

            c_list.append(c_list_item)

        indy_proof_proof_aggregated_proof = cls(
            c_hash=c_hash,
            c_list=c_list,
        )

        indy_proof_proof_aggregated_proof.additional_properties = d
        return indy_proof_proof_aggregated_proof

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
