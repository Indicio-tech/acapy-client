from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credential_proposal import CredentialProposal
from ..types import UNSET, Unset

T = TypeVar("T", bound="V10CredentialBoundOfferRequest")


@attr.s(auto_attribs=True)
class V10CredentialBoundOfferRequest:
    """
    Attributes:
        counter_proposal (Union[Unset, CredentialProposal]):
    """

    counter_proposal: Union[Unset, CredentialProposal] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        counter_proposal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.counter_proposal, Unset):
            counter_proposal = self.counter_proposal.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counter_proposal is not UNSET:
            field_dict["counter_proposal"] = counter_proposal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _counter_proposal = d.pop("counter_proposal", UNSET)
        counter_proposal: Union[Unset, CredentialProposal]
        if isinstance(_counter_proposal, Unset):
            counter_proposal = UNSET
        else:
            counter_proposal = CredentialProposal.from_dict(_counter_proposal)

        v10_credential_bound_offer_request = cls(
            counter_proposal=counter_proposal,
        )

        v10_credential_bound_offer_request.additional_properties = d
        return v10_credential_bound_offer_request

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
