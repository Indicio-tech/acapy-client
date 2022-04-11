from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_proof_proof_aggregated_proof import IndyProofProofAggregatedProof
from ..models.indy_proof_proof_proofs_proof import IndyProofProofProofsProof
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofProof")


@attr.s(auto_attribs=True)
class IndyProofProof:
    """
    Attributes:
        aggregated_proof (Union[Unset, IndyProofProofAggregatedProof]):
        proofs (Union[Unset, List[IndyProofProofProofsProof]]): Indy proof proofs
    """

    aggregated_proof: Union[Unset, IndyProofProofAggregatedProof] = UNSET
    proofs: Union[Unset, List[IndyProofProofProofsProof]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aggregated_proof: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregated_proof, Unset):
            aggregated_proof = self.aggregated_proof.to_dict()

        proofs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.proofs, Unset):
            proofs = []
            for proofs_item_data in self.proofs:
                proofs_item = proofs_item_data.to_dict()

                proofs.append(proofs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregated_proof is not UNSET:
            field_dict["aggregated_proof"] = aggregated_proof
        if proofs is not UNSET:
            field_dict["proofs"] = proofs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _aggregated_proof = d.pop("aggregated_proof", UNSET)
        aggregated_proof: Union[Unset, IndyProofProofAggregatedProof]
        if isinstance(_aggregated_proof, Unset):
            aggregated_proof = UNSET
        else:
            aggregated_proof = IndyProofProofAggregatedProof.from_dict(_aggregated_proof)

        proofs = []
        _proofs = d.pop("proofs", UNSET)
        for proofs_item_data in _proofs or []:
            proofs_item = IndyProofProofProofsProof.from_dict(proofs_item_data)

            proofs.append(proofs_item)

        indy_proof_proof = cls(
            aggregated_proof=aggregated_proof,
            proofs=proofs,
        )

        indy_proof_proof.additional_properties = d
        return indy_proof_proof

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
