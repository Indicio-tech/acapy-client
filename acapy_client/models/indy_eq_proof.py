from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_eq_proof_m import IndyEQProofM
from ..models.indy_eq_proof_revealed_attrs import IndyEQProofRevealedAttrs
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyEQProof")


@attr.s(auto_attribs=True)
class IndyEQProof:
    """
    Attributes:
        a_prime (Union[Unset, str]):  Example: 0.
        e (Union[Unset, str]):  Example: 0.
        m (Union[Unset, IndyEQProofM]):
        m2 (Union[Unset, str]):  Example: 0.
        revealed_attrs (Union[Unset, IndyEQProofRevealedAttrs]):
        v (Union[Unset, str]):  Example: 0.
    """

    a_prime: Union[Unset, str] = UNSET
    e: Union[Unset, str] = UNSET
    m: Union[Unset, IndyEQProofM] = UNSET
    m2: Union[Unset, str] = UNSET
    revealed_attrs: Union[Unset, IndyEQProofRevealedAttrs] = UNSET
    v: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        a_prime = self.a_prime
        e = self.e
        m: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.m, Unset):
            m = self.m.to_dict()

        m2 = self.m2
        revealed_attrs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revealed_attrs, Unset):
            revealed_attrs = self.revealed_attrs.to_dict()

        v = self.v

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a_prime is not UNSET:
            field_dict["a_prime"] = a_prime
        if e is not UNSET:
            field_dict["e"] = e
        if m is not UNSET:
            field_dict["m"] = m
        if m2 is not UNSET:
            field_dict["m2"] = m2
        if revealed_attrs is not UNSET:
            field_dict["revealed_attrs"] = revealed_attrs
        if v is not UNSET:
            field_dict["v"] = v

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        a_prime = d.pop("a_prime", UNSET)

        e = d.pop("e", UNSET)

        _m = d.pop("m", UNSET)
        m: Union[Unset, IndyEQProofM]
        if isinstance(_m, Unset):
            m = UNSET
        else:
            m = IndyEQProofM.from_dict(_m)

        m2 = d.pop("m2", UNSET)

        _revealed_attrs = d.pop("revealed_attrs", UNSET)
        revealed_attrs: Union[Unset, IndyEQProofRevealedAttrs]
        if isinstance(_revealed_attrs, Unset):
            revealed_attrs = UNSET
        else:
            revealed_attrs = IndyEQProofRevealedAttrs.from_dict(_revealed_attrs)

        v = d.pop("v", UNSET)

        indy_eq_proof = cls(
            a_prime=a_prime,
            e=e,
            m=m,
            m2=m2,
            revealed_attrs=revealed_attrs,
            v=v,
        )

        indy_eq_proof.additional_properties = d
        return indy_eq_proof

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
