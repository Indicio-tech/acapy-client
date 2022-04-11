from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_ge_proof_pred_p_type import IndyGEProofPredPType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyGEProofPred")


@attr.s(auto_attribs=True)
class IndyGEProofPred:
    """
    Attributes:
        attr_name (Union[Unset, str]): Attribute name, indy-canonicalized
        p_type (Union[Unset, IndyGEProofPredPType]): Predicate type
        value (Union[Unset, int]): Predicate threshold value
    """

    attr_name: Union[Unset, str] = UNSET
    p_type: Union[Unset, IndyGEProofPredPType] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attr_name = self.attr_name
        p_type: Union[Unset, str] = UNSET
        if not isinstance(self.p_type, Unset):
            p_type = self.p_type.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attr_name is not UNSET:
            field_dict["attr_name"] = attr_name
        if p_type is not UNSET:
            field_dict["p_type"] = p_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attr_name = d.pop("attr_name", UNSET)

        _p_type = d.pop("p_type", UNSET)
        p_type: Union[Unset, IndyGEProofPredPType]
        if isinstance(_p_type, Unset):
            p_type = UNSET
        else:
            p_type = IndyGEProofPredPType(_p_type)

        value = d.pop("value", UNSET)

        indy_ge_proof_pred = cls(
            attr_name=attr_name,
            p_type=p_type,
            value=value,
        )

        indy_ge_proof_pred.additional_properties = d
        return indy_ge_proof_pred

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
