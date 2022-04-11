from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_eq_proof import IndyEQProof
from ..models.indy_ge_proof import IndyGEProof
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyPrimaryProof")


@attr.s(auto_attribs=True)
class IndyPrimaryProof:
    """
    Attributes:
        eq_proof (Union[Unset, None, IndyEQProof]):
        ge_proofs (Union[Unset, None, List[IndyGEProof]]): Indy GE proofs
    """

    eq_proof: Union[Unset, None, IndyEQProof] = UNSET
    ge_proofs: Union[Unset, None, List[IndyGEProof]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eq_proof: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.eq_proof, Unset):
            eq_proof = self.eq_proof.to_dict() if self.eq_proof else None

        ge_proofs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ge_proofs, Unset):
            if self.ge_proofs is None:
                ge_proofs = None
            else:
                ge_proofs = []
                for ge_proofs_item_data in self.ge_proofs:
                    ge_proofs_item = ge_proofs_item_data.to_dict()

                    ge_proofs.append(ge_proofs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eq_proof is not UNSET:
            field_dict["eq_proof"] = eq_proof
        if ge_proofs is not UNSET:
            field_dict["ge_proofs"] = ge_proofs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _eq_proof = d.pop("eq_proof", UNSET)
        eq_proof: Union[Unset, None, IndyEQProof]
        if _eq_proof is None:
            eq_proof = None
        elif isinstance(_eq_proof, Unset):
            eq_proof = UNSET
        else:
            eq_proof = IndyEQProof.from_dict(_eq_proof)

        ge_proofs = []
        _ge_proofs = d.pop("ge_proofs", UNSET)
        for ge_proofs_item_data in _ge_proofs or []:
            ge_proofs_item = IndyGEProof.from_dict(ge_proofs_item_data)

            ge_proofs.append(ge_proofs_item)

        indy_primary_proof = cls(
            eq_proof=eq_proof,
            ge_proofs=ge_proofs,
        )

        indy_primary_proof.additional_properties = d
        return indy_primary_proof

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
