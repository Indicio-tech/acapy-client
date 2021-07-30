from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.indy_requested_creds_requested_pred import IndyRequestedCredsRequestedPred

T = TypeVar("T", bound="IndyPresSpecRequestedPredicates")


@attr.s(auto_attribs=True)
class IndyPresSpecRequestedPredicates:
    """Nested object mapping proof request predicate referents to requested-predicate specifiers"""

    additional_properties: Dict[str, IndyRequestedCredsRequestedPred] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        indy_pres_spec_requested_predicates = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = IndyRequestedCredsRequestedPred.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        indy_pres_spec_requested_predicates.additional_properties = additional_properties
        return indy_pres_spec_requested_predicates

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> IndyRequestedCredsRequestedPred:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: IndyRequestedCredsRequestedPred) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
