from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_pres_spec_requested_attributes import IndyPresSpecRequestedAttributes
from ..models.indy_pres_spec_requested_predicates import IndyPresSpecRequestedPredicates
from ..models.indy_pres_spec_self_attested_attributes import IndyPresSpecSelfAttestedAttributes
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyPresSpec")


@attr.s(auto_attribs=True)
class IndyPresSpec:
    """
    Attributes:
        requested_attributes (IndyPresSpecRequestedAttributes): Nested object mapping proof request attribute referents
            to requested-attribute specifiers
        requested_predicates (IndyPresSpecRequestedPredicates): Nested object mapping proof request predicate referents
            to requested-predicate specifiers
        self_attested_attributes (IndyPresSpecSelfAttestedAttributes): Self-attested attributes to build into proof
        trace (Union[Unset, bool]): Whether to trace event (default false)
    """

    requested_attributes: IndyPresSpecRequestedAttributes
    requested_predicates: IndyPresSpecRequestedPredicates
    self_attested_attributes: IndyPresSpecSelfAttestedAttributes
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requested_attributes = self.requested_attributes.to_dict()

        requested_predicates = self.requested_predicates.to_dict()

        self_attested_attributes = self.self_attested_attributes.to_dict()

        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requested_attributes": requested_attributes,
                "requested_predicates": requested_predicates,
                "self_attested_attributes": self_attested_attributes,
            }
        )
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        requested_attributes = IndyPresSpecRequestedAttributes.from_dict(d.pop("requested_attributes"))

        requested_predicates = IndyPresSpecRequestedPredicates.from_dict(d.pop("requested_predicates"))

        self_attested_attributes = IndyPresSpecSelfAttestedAttributes.from_dict(d.pop("self_attested_attributes"))

        trace = d.pop("trace", UNSET)

        indy_pres_spec = cls(
            requested_attributes=requested_attributes,
            requested_predicates=requested_predicates,
            self_attested_attributes=self_attested_attributes,
            trace=trace,
        )

        indy_pres_spec.additional_properties = d
        return indy_pres_spec

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
