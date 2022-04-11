from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_non_revoc_proof import IndyNonRevocProof
from ..models.indy_primary_proof import IndyPrimaryProof
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofProofProofsProof")


@attr.s(auto_attribs=True)
class IndyProofProofProofsProof:
    """
    Attributes:
        non_revoc_proof (Union[Unset, None, IndyNonRevocProof]):
        primary_proof (Union[Unset, IndyPrimaryProof]):
    """

    non_revoc_proof: Union[Unset, None, IndyNonRevocProof] = UNSET
    primary_proof: Union[Unset, IndyPrimaryProof] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        non_revoc_proof: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.non_revoc_proof, Unset):
            non_revoc_proof = self.non_revoc_proof.to_dict() if self.non_revoc_proof else None

        primary_proof: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.primary_proof, Unset):
            primary_proof = self.primary_proof.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if non_revoc_proof is not UNSET:
            field_dict["non_revoc_proof"] = non_revoc_proof
        if primary_proof is not UNSET:
            field_dict["primary_proof"] = primary_proof

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _non_revoc_proof = d.pop("non_revoc_proof", UNSET)
        non_revoc_proof: Union[Unset, None, IndyNonRevocProof]
        if _non_revoc_proof is None:
            non_revoc_proof = None
        elif isinstance(_non_revoc_proof, Unset):
            non_revoc_proof = UNSET
        else:
            non_revoc_proof = IndyNonRevocProof.from_dict(_non_revoc_proof)

        _primary_proof = d.pop("primary_proof", UNSET)
        primary_proof: Union[Unset, IndyPrimaryProof]
        if isinstance(_primary_proof, Unset):
            primary_proof = UNSET
        else:
            primary_proof = IndyPrimaryProof.from_dict(_primary_proof)

        indy_proof_proof_proofs_proof = cls(
            non_revoc_proof=non_revoc_proof,
            primary_proof=primary_proof,
        )

        indy_proof_proof_proofs_proof.additional_properties = d
        return indy_proof_proof_proofs_proof

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
