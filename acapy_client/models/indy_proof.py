from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_proof_identifier import IndyProofIdentifier
from ..models.indy_proof_proof import IndyProofProof
from ..models.indy_proof_requested_proof import IndyProofRequestedProof
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProof")


@attr.s(auto_attribs=True)
class IndyProof:
    """
    Attributes:
        identifiers (Union[Unset, List[IndyProofIdentifier]]): Indy proof.identifiers content
        proof (Union[Unset, IndyProofProof]):
        requested_proof (Union[Unset, IndyProofRequestedProof]):
    """

    identifiers: Union[Unset, List[IndyProofIdentifier]] = UNSET
    proof: Union[Unset, IndyProofProof] = UNSET
    requested_proof: Union[Unset, IndyProofRequestedProof] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()

                identifiers.append(identifiers_item)

        proof: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proof, Unset):
            proof = self.proof.to_dict()

        requested_proof: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.requested_proof, Unset):
            requested_proof = self.requested_proof.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if proof is not UNSET:
            field_dict["proof"] = proof
        if requested_proof is not UNSET:
            field_dict["requested_proof"] = requested_proof

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifiers = []
        _identifiers = d.pop("identifiers", UNSET)
        for identifiers_item_data in _identifiers or []:
            identifiers_item = IndyProofIdentifier.from_dict(identifiers_item_data)

            identifiers.append(identifiers_item)

        _proof = d.pop("proof", UNSET)
        proof: Union[Unset, IndyProofProof]
        if isinstance(_proof, Unset):
            proof = UNSET
        else:
            proof = IndyProofProof.from_dict(_proof)

        _requested_proof = d.pop("requested_proof", UNSET)
        requested_proof: Union[Unset, IndyProofRequestedProof]
        if isinstance(_requested_proof, Unset):
            requested_proof = UNSET
        else:
            requested_proof = IndyProofRequestedProof.from_dict(_requested_proof)

        indy_proof = cls(
            identifiers=identifiers,
            proof=proof,
            requested_proof=requested_proof,
        )

        indy_proof.additional_properties = d
        return indy_proof

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
