from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_proof_request_non_revoked import IndyProofRequestNonRevoked
from ..models.indy_proof_request_requested_attributes import IndyProofRequestRequestedAttributes
from ..models.indy_proof_request_requested_predicates import IndyProofRequestRequestedPredicates
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofRequest")


@attr.s(auto_attribs=True)
class IndyProofRequest:
    """ """

    name: Union[Unset, str] = UNSET
    non_revoked: Union[Unset, None, IndyProofRequestNonRevoked] = UNSET
    nonce: Union[Unset, str] = UNSET
    requested_attributes: Union[Unset, IndyProofRequestRequestedAttributes] = UNSET
    requested_predicates: Union[Unset, IndyProofRequestRequestedPredicates] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        non_revoked: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.non_revoked, Unset):
            non_revoked = self.non_revoked.to_dict() if self.non_revoked else None

        nonce = self.nonce
        requested_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.requested_attributes, Unset):
            requested_attributes = self.requested_attributes.to_dict()

        requested_predicates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.requested_predicates, Unset):
            requested_predicates = self.requested_predicates.to_dict()

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if non_revoked is not UNSET:
            field_dict["non_revoked"] = non_revoked
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if requested_attributes is not UNSET:
            field_dict["requested_attributes"] = requested_attributes
        if requested_predicates is not UNSET:
            field_dict["requested_predicates"] = requested_predicates
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _non_revoked = d.pop("non_revoked", UNSET)
        non_revoked: Union[Unset, None, IndyProofRequestNonRevoked]
        if _non_revoked is None:
            non_revoked = None
        elif isinstance(_non_revoked, Unset):
            non_revoked = UNSET
        else:
            non_revoked = IndyProofRequestNonRevoked.from_dict(_non_revoked)

        nonce = d.pop("nonce", UNSET)

        _requested_attributes = d.pop("requested_attributes", UNSET)
        requested_attributes: Union[Unset, IndyProofRequestRequestedAttributes]
        if isinstance(_requested_attributes, Unset):
            requested_attributes = UNSET
        else:
            requested_attributes = IndyProofRequestRequestedAttributes.from_dict(_requested_attributes)

        _requested_predicates = d.pop("requested_predicates", UNSET)
        requested_predicates: Union[Unset, IndyProofRequestRequestedPredicates]
        if isinstance(_requested_predicates, Unset):
            requested_predicates = UNSET
        else:
            requested_predicates = IndyProofRequestRequestedPredicates.from_dict(_requested_predicates)

        version = d.pop("version", UNSET)

        indy_proof_request = cls(
            name=name,
            non_revoked=non_revoked,
            nonce=nonce,
            requested_attributes=requested_attributes,
            requested_predicates=requested_predicates,
            version=version,
        )

        indy_proof_request.additional_properties = d
        return indy_proof_request

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
