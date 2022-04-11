from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_non_revoc_proof_c_list import IndyNonRevocProofCList
from ..models.indy_non_revoc_proof_x_list import IndyNonRevocProofXList
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyNonRevocProof")


@attr.s(auto_attribs=True)
class IndyNonRevocProof:
    """
    Attributes:
        c_list (Union[Unset, IndyNonRevocProofCList]):
        x_list (Union[Unset, IndyNonRevocProofXList]):
    """

    c_list: Union[Unset, IndyNonRevocProofCList] = UNSET
    x_list: Union[Unset, IndyNonRevocProofXList] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        c_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.c_list, Unset):
            c_list = self.c_list.to_dict()

        x_list: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.x_list, Unset):
            x_list = self.x_list.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if c_list is not UNSET:
            field_dict["c_list"] = c_list
        if x_list is not UNSET:
            field_dict["x_list"] = x_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _c_list = d.pop("c_list", UNSET)
        c_list: Union[Unset, IndyNonRevocProofCList]
        if isinstance(_c_list, Unset):
            c_list = UNSET
        else:
            c_list = IndyNonRevocProofCList.from_dict(_c_list)

        _x_list = d.pop("x_list", UNSET)
        x_list: Union[Unset, IndyNonRevocProofXList]
        if isinstance(_x_list, Unset):
            x_list = UNSET
        else:
            x_list = IndyNonRevocProofXList.from_dict(_x_list)

        indy_non_revoc_proof = cls(
            c_list=c_list,
            x_list=x_list,
        )

        indy_non_revoc_proof.additional_properties = d
        return indy_non_revoc_proof

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
