from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.indy_proof_req_attr_spec_non_revoked import IndyProofReqAttrSpecNonRevoked
from ..models.indy_proof_req_attr_spec_restrictions_item import IndyProofReqAttrSpecRestrictionsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofReqAttrSpec")


@attr.s(auto_attribs=True)
class IndyProofReqAttrSpec:
    """
    Attributes:
        name (Union[Unset, str]): Attribute name Example: favouriteDrink.
        names (Union[Unset, List[str]]): Attribute name group
        non_revoked (Union[Unset, None, IndyProofReqAttrSpecNonRevoked]):
        restrictions (Union[Unset, List[IndyProofReqAttrSpecRestrictionsItem]]): If present, credential must satisfy one
            of given restrictions: specify schema_id, schema_issuer_did, schema_name, schema_version, issuer_did,
            cred_def_id, and/or attr::<attribute-name>::value where <attribute-name> represents a credential attribute name
    """

    name: Union[Unset, str] = UNSET
    names: Union[Unset, List[str]] = UNSET
    non_revoked: Union[Unset, None, IndyProofReqAttrSpecNonRevoked] = UNSET
    restrictions: Union[Unset, List[IndyProofReqAttrSpecRestrictionsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        non_revoked: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.non_revoked, Unset):
            non_revoked = self.non_revoked.to_dict() if self.non_revoked else None

        restrictions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = []
            for restrictions_item_data in self.restrictions:
                restrictions_item = restrictions_item_data.to_dict()

                restrictions.append(restrictions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if names is not UNSET:
            field_dict["names"] = names
        if non_revoked is not UNSET:
            field_dict["non_revoked"] = non_revoked
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        names = cast(List[str], d.pop("names", UNSET))

        _non_revoked = d.pop("non_revoked", UNSET)
        non_revoked: Union[Unset, None, IndyProofReqAttrSpecNonRevoked]
        if _non_revoked is None:
            non_revoked = None
        elif isinstance(_non_revoked, Unset):
            non_revoked = UNSET
        else:
            non_revoked = IndyProofReqAttrSpecNonRevoked.from_dict(_non_revoked)

        restrictions = []
        _restrictions = d.pop("restrictions", UNSET)
        for restrictions_item_data in _restrictions or []:
            restrictions_item = IndyProofReqAttrSpecRestrictionsItem.from_dict(restrictions_item_data)

            restrictions.append(restrictions_item)

        indy_proof_req_attr_spec = cls(
            name=name,
            names=names,
            non_revoked=non_revoked,
            restrictions=restrictions,
        )

        indy_proof_req_attr_spec.additional_properties = d
        return indy_proof_req_attr_spec

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
