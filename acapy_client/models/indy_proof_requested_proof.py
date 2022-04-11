from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_proof_requested_proof_predicates import IndyProofRequestedProofPredicates
from ..models.indy_proof_requested_proof_revealed_attr_groups import IndyProofRequestedProofRevealedAttrGroups
from ..models.indy_proof_requested_proof_revealed_attrs import IndyProofRequestedProofRevealedAttrs
from ..models.indy_proof_requested_proof_self_attested_attrs import IndyProofRequestedProofSelfAttestedAttrs
from ..models.indy_proof_requested_proof_unrevealed_attrs import IndyProofRequestedProofUnrevealedAttrs
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofRequestedProof")


@attr.s(auto_attribs=True)
class IndyProofRequestedProof:
    """
    Attributes:
        predicates (Union[Unset, IndyProofRequestedProofPredicates]): Proof requested proof predicates.
        revealed_attr_groups (Union[Unset, None, IndyProofRequestedProofRevealedAttrGroups]): Proof requested proof
            revealed attribute groups
        revealed_attrs (Union[Unset, None, IndyProofRequestedProofRevealedAttrs]): Proof requested proof revealed
            attributes
        self_attested_attrs (Union[Unset, IndyProofRequestedProofSelfAttestedAttrs]): Proof requested proof self-
            attested attributes
        unrevealed_attrs (Union[Unset, IndyProofRequestedProofUnrevealedAttrs]): Unrevealed attributes
    """

    predicates: Union[Unset, IndyProofRequestedProofPredicates] = UNSET
    revealed_attr_groups: Union[Unset, None, IndyProofRequestedProofRevealedAttrGroups] = UNSET
    revealed_attrs: Union[Unset, None, IndyProofRequestedProofRevealedAttrs] = UNSET
    self_attested_attrs: Union[Unset, IndyProofRequestedProofSelfAttestedAttrs] = UNSET
    unrevealed_attrs: Union[Unset, IndyProofRequestedProofUnrevealedAttrs] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        predicates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.predicates, Unset):
            predicates = self.predicates.to_dict()

        revealed_attr_groups: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.revealed_attr_groups, Unset):
            revealed_attr_groups = self.revealed_attr_groups.to_dict() if self.revealed_attr_groups else None

        revealed_attrs: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.revealed_attrs, Unset):
            revealed_attrs = self.revealed_attrs.to_dict() if self.revealed_attrs else None

        self_attested_attrs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_attested_attrs, Unset):
            self_attested_attrs = self.self_attested_attrs.to_dict()

        unrevealed_attrs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unrevealed_attrs, Unset):
            unrevealed_attrs = self.unrevealed_attrs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if predicates is not UNSET:
            field_dict["predicates"] = predicates
        if revealed_attr_groups is not UNSET:
            field_dict["revealed_attr_groups"] = revealed_attr_groups
        if revealed_attrs is not UNSET:
            field_dict["revealed_attrs"] = revealed_attrs
        if self_attested_attrs is not UNSET:
            field_dict["self_attested_attrs"] = self_attested_attrs
        if unrevealed_attrs is not UNSET:
            field_dict["unrevealed_attrs"] = unrevealed_attrs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _predicates = d.pop("predicates", UNSET)
        predicates: Union[Unset, IndyProofRequestedProofPredicates]
        if isinstance(_predicates, Unset):
            predicates = UNSET
        else:
            predicates = IndyProofRequestedProofPredicates.from_dict(_predicates)

        _revealed_attr_groups = d.pop("revealed_attr_groups", UNSET)
        revealed_attr_groups: Union[Unset, None, IndyProofRequestedProofRevealedAttrGroups]
        if _revealed_attr_groups is None:
            revealed_attr_groups = None
        elif isinstance(_revealed_attr_groups, Unset):
            revealed_attr_groups = UNSET
        else:
            revealed_attr_groups = IndyProofRequestedProofRevealedAttrGroups.from_dict(_revealed_attr_groups)

        _revealed_attrs = d.pop("revealed_attrs", UNSET)
        revealed_attrs: Union[Unset, None, IndyProofRequestedProofRevealedAttrs]
        if _revealed_attrs is None:
            revealed_attrs = None
        elif isinstance(_revealed_attrs, Unset):
            revealed_attrs = UNSET
        else:
            revealed_attrs = IndyProofRequestedProofRevealedAttrs.from_dict(_revealed_attrs)

        _self_attested_attrs = d.pop("self_attested_attrs", UNSET)
        self_attested_attrs: Union[Unset, IndyProofRequestedProofSelfAttestedAttrs]
        if isinstance(_self_attested_attrs, Unset):
            self_attested_attrs = UNSET
        else:
            self_attested_attrs = IndyProofRequestedProofSelfAttestedAttrs.from_dict(_self_attested_attrs)

        _unrevealed_attrs = d.pop("unrevealed_attrs", UNSET)
        unrevealed_attrs: Union[Unset, IndyProofRequestedProofUnrevealedAttrs]
        if isinstance(_unrevealed_attrs, Unset):
            unrevealed_attrs = UNSET
        else:
            unrevealed_attrs = IndyProofRequestedProofUnrevealedAttrs.from_dict(_unrevealed_attrs)

        indy_proof_requested_proof = cls(
            predicates=predicates,
            revealed_attr_groups=revealed_attr_groups,
            revealed_attrs=revealed_attrs,
            self_attested_attrs=self_attested_attrs,
            unrevealed_attrs=unrevealed_attrs,
        )

        indy_proof_requested_proof.additional_properties = d
        return indy_proof_requested_proof

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
